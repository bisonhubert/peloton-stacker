import datetime as dt
import tempfile
import unittest
from pathlib import Path

from stack.client import class_id_from, search_params_from
from stack.plan import active_cycle, load_cycle, week_monday, week_slots
from stack.resolve import resolve, first_name

ROOT = Path(__file__).parent.parent


def load():
    return load_cycle(ROOT / "cycles" / "tunde_bootcamp.toml", ROOT / "programs")


class TestPlan(unittest.TestCase):
    def test_week_monday(self):
        self.assertEqual(week_monday(dt.date(2026, 10, 19)), dt.date(2026, 10, 19))
        self.assertEqual(week_monday(dt.date(2026, 10, 25)), dt.date(2026, 10, 19))
        self.assertEqual(week_monday(dt.date(2026, 10, 26)), dt.date(2026, 10, 26))

    def test_active_cycle(self):
        cycle = load()
        self.assertIs(active_cycle([cycle], dt.date(2026, 10, 19)), cycle)
        self.assertEqual(cycle.week_of(dt.date(2026, 11, 23)), 6)
        with self.assertRaises(LookupError):
            active_cycle([cycle], dt.date(2026, 11, 30))

    def test_week_slots(self):
        slots = week_slots(load())
        self.assertEqual(
            [(s.day, s.title) for s in slots],
            [
                ("monday", "Lower Body + Climb Ride"),
                ("monday", "5 min cool down"),
                ("wednesday", "Upper Body + Progression Ride"),
                ("wednesday", "5 min cool down"),
                ("friday", "Core + Conditioning Ride"),
                ("friday", "5 min cool down"),
            ],
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
            (tmp / "cycle.toml").write_text('start = 2026-10-19\nweeks = 2\nprograms = ["a", "b"]\n')
            slots = week_slots(load_cycle(tmp / "cycle.toml", tmp))
        self.assertEqual([s.title for s in slots], ["A Mon", "B Tue", "A Sun", "B Sun"])


class TestClient(unittest.TestCase):
    def test_class_id_from(self):
        url = "https://members.onepeloton.com/x?modal=classDetailsModal&classId=abc123"
        self.assertEqual(class_id_from(url), "abc123")
        self.assertEqual(class_id_from("abc123"), "abc123")

    def test_search_params_from(self):
        params = search_params_from(week_slots(load())[1].search_url)
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


def ride(class_id):
    return {"id": class_id, "instructor_id": "i"}


class TestResolve(unittest.TestCase):
    def test_first_name(self):
        self.assertEqual(first_name("Tunde Oyeneyin"), "Tunde")
        self.assertEqual(first_name("Emma"), "Emma")

    def test_picks_distinct_untaken_cool_downs(self):
        def search(params):
            return [{"id": f"cd{i}", "title": f"Cool Down {i}", "instructor_id": "i"} for i in range(5)]

        ids = [class_id for _, class_id, _, _ in resolve(week_slots(load()), search, ride)]
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

        ids = [class_id for _, class_id, _, _ in resolve(week_slots(load()), search, ride)]
        self.assertEqual(ids[1::2], ["new", "old1", "old2"])


if __name__ == "__main__":
    unittest.main()
