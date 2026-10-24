import datetime as dt
import tempfile
import unittest
from pathlib import Path

from stack.client import class_id_from, search_params_from, workout_id_from
from stack.plan import Block, active_block, load_block, load_program, week_monday, week_slots
from stack.resolve import first_name, resolve

ROOT = Path(__file__).parent.parent


def load():
    return load_block(ROOT / "blocks" / "2026_fall.toml", ROOT / "programs")


def bootcamp_only():
    program = load_program(ROOT / "programs" / "tunde_bike_bootcamp.toml")
    return Block("bootcamp", dt.date(2026, 10, 19), 1, [program])


def core_index(slot):
    workouts = load_program(ROOT / "programs" / "crush_your_core.toml").rotation
    return workouts.index(slot.class_ref) + 1


class TestPlan(unittest.TestCase):
    def test_week_monday(self):
        self.assertEqual(week_monday(dt.date(2026, 10, 19)), dt.date(2026, 10, 19))
        self.assertEqual(week_monday(dt.date(2026, 10, 25)), dt.date(2026, 10, 19))
        self.assertEqual(week_monday(dt.date(2026, 10, 26)), dt.date(2026, 10, 26))

    def test_active_block(self):
        block = Block("fall", dt.date(2026, 10, 19), 6, [])
        self.assertIs(active_block([block], dt.date(2026, 10, 19)), block)
        self.assertEqual(block.week_of(dt.date(2026, 11, 23)), 6)
        with self.assertRaises(LookupError):
            active_block([block], dt.date(2026, 11, 30))

    def test_week_slots(self):
        slots = week_slots(load(), 1)
        self.assertEqual(
            [(s.day, s.title or core_index(s)) for s in slots],
            [
                ("monday", "Lower Body + Climb Ride"),
                ("monday", "5 min cool down"),
                ("tuesday", 1),
                ("wednesday", "Upper Body + Progression Ride"),
                ("wednesday", "5 min cool down"),
                ("thursday", 2),
                ("friday", "Core + Conditioning Ride"),
                ("friday", "5 min cool down"),
                ("saturday", 3),
                ("sunday", 4),
            ],
        )

    def test_rotation_wraps_across_weeks(self):
        block = load()
        weeks = {
            week: [core_index(s) for s in week_slots(block, week) if not s.title]
            for week in range(1, 7)
        }
        self.assertEqual(
            weeks,
            {
                1: [1, 2, 3, 4],
                2: [5, 6, 7, 8],
                3: [9, 10, 11, 12],
                4: [13, 14, 1, 2],
                5: [3, 4, 5, 6],
                6: [7, 8, 9, 10],
            },
        )

    def test_combined_programs_merge_by_day(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            (tmp / "a.toml").write_text(
                'name = "A"\n'
                '[[workouts]]\nday = "monday"\ntitle = "A Mon"\nclass = "a1"\n'
                '[[workouts]]\nday = "sunday"\ntitle = "A Sun"\nclass = "a2"\n'
            )
            (tmp / "b.toml").write_text(
                'name = "B"\n'
                '[[workouts]]\nday = "tuesday"\ntitle = "B Tue"\nclass = "b1"\n'
                '[[workouts]]\nday = "sunday"\ntitle = "B Sun"\nclass = "b2"\n'
            )
            (tmp / "block.toml").write_text('start = 2026-10-19\nweeks = 2\nprograms = ["a", "b"]\n')
            slots = week_slots(load_block(tmp / "block.toml", tmp), 1)
        self.assertEqual([s.title for s in slots], ["A Mon", "B Tue", "A Sun", "B Sun"])


class TestClient(unittest.TestCase):
    def test_class_id_from(self):
        url = "https://members.onepeloton.com/x?modal=classDetailsModal&classId=abc123"
        self.assertEqual(class_id_from(url), "abc123")
        self.assertEqual(class_id_from("abc123"), "abc123")

    def test_workout_id_from(self):
        self.assertEqual(
            workout_id_from("https://members.onepeloton.com/profile/workouts/783d8829"), "783d8829"
        )
        self.assertIsNone(
            workout_id_from("https://members.onepeloton.com/profile/workouts/w1?classId=c1")
        )
        self.assertIsNone(workout_id_from("abc123"))

    def test_search_params_from(self):
        params = search_params_from(week_slots(load(), 1)[1].search_url)
        self.assertEqual(
            params,
            {
                "browse_category": "cycling",
                "duration": "300",
                "class_type_id": "a1fa617f3ba14c0a8c25468d5c88b3ea",
                "instructor_id": "2e57092bee334c8c8dcb9fe16ba5308c,c9bd86e59b9b4f96981848467838aa9c,"
                "561f95c405734d8488ed8dcc8980d599,f6f2d613dc344e4bbf6428cd34697820",
                "has_workout": "false",
                "sort_by": "original_air_time",
                "desc": "true",
            },
        )


def ride(class_ref):
    return {"id": class_id_from(class_ref), "title": "Ride", "instructor_id": "i"}


class TestResolve(unittest.TestCase):
    def test_first_name(self):
        self.assertEqual(first_name("Tunde Oyeneyin"), "Tunde")
        self.assertEqual(first_name("Emma"), "Emma")

    def test_picks_distinct_untaken_cool_downs(self):
        def search(params):
            return [{"id": f"cd{i}", "title": f"Cool Down {i}", "instructor_id": "i"} for i in range(5)]

        ids = [class_id for _, class_id, _, _ in resolve(week_slots(bootcamp_only(), 1), search, ride)]
        self.assertEqual(
            ids,
            [
                "5784b01e862b416390307db97aa05d57",
                "cd0",
                "dfa893187ca94f28b0fbb3b20e7cc2c2",
                "cd1",
                "d8f891498789414ea288764921b98538",
                "cd2",
            ],
        )

    def test_falls_back_to_taken_classes(self):
        def search(params):
            rides = [{"id": i, "title": i, "instructor_id": "i"} for i in ("new", "old1", "old2")]
            return rides[:1] if "has_workout" in params else rides

        ids = [class_id for _, class_id, _, _ in resolve(week_slots(bootcamp_only(), 1), search, ride)]
        self.assertEqual(ids[1::2], ["new", "old1", "old2"])

    def test_untitled_workouts_use_class_title(self):
        slots = [s for s in week_slots(load(), 1) if not s.title]
        titles = [title for _, _, title, _ in resolve(slots, None, ride)]
        self.assertEqual(titles, ["Ride"] * 4)


if __name__ == "__main__":
    unittest.main()
