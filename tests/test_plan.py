import datetime as dt
import tempfile
import unittest
from pathlib import Path

from stack.client import class_id_from, search_params_from, workout_id_from
from stack.plan import (
    Block,
    active_block,
    load_block,
    load_off,
    load_program,
    pick,
    rest_of_week,
    week_monday,
    week_slots,
)
from stack.resolve import first_name, resolve

ROOT = Path(__file__).parent.parent
DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]


def load():
    return load_block(ROOT / "blocks" / "2026_fall.toml", ROOT / "programs")


def off():
    return load_off(ROOT / "off.toml", ROOT / "programs")


def bootcamp_only():
    program = load_program(ROOT / "programs" / "tunde_bike_bootcamp.toml")
    return Block("bootcamp", dt.date(2026, 10, 19), 1, [program])


CORE = "Emma Lovewell Crush Your Core"


def core_index(slot):
    workouts = load_program(ROOT / "programs" / "crush_your_core.toml").rotation
    return workouts.index(slot.class_ref) + 1


def label(slot):
    if slot.program == CORE:
        return core_index(slot)
    return slot.title or slot.program


class TestPlan(unittest.TestCase):
    def test_week_monday(self):
        self.assertEqual(week_monday(dt.date(2026, 10, 19)), dt.date(2026, 10, 19))
        self.assertEqual(week_monday(dt.date(2026, 10, 25)), dt.date(2026, 10, 19))
        self.assertEqual(week_monday(dt.date(2026, 10, 26)), dt.date(2026, 10, 26))

    def test_active_block(self):
        block = Block("fall", dt.date(2026, 10, 19), 6, [])
        self.assertIs(active_block([block], off(), dt.date(2026, 10, 19)), block)
        self.assertEqual(block.week_of(dt.date(2026, 11, 23)), 6)
        with self.assertRaises(LookupError):
            active_block([block], off(), dt.date(2026, 10, 12))

    def test_week_slots(self):
        slots = week_slots(load(), 1)
        self.assertEqual(
            [(s.day, label(s)) for s in slots],
            [
                ("monday", "Lower Body + Climb Ride"),
                ("monday", "5 min cool down"),
                ("tuesday", 1),
                ("tuesday", "Weekday Rides"),
                ("wednesday", "Upper Body + Progression Ride"),
                ("wednesday", "5 min cool down"),
                ("thursday", 2),
                ("thursday", "Weekday Rides"),
                ("friday", "Core + Conditioning Ride"),
                ("friday", "5 min cool down"),
                ("saturday", 3),
                ("saturday", "Weekend"),
                ("sunday", 4),
                ("sunday", "Weekend"),
            ],
        )

    def test_rotation_wraps_across_weeks(self):
        block = load()
        weeks = {
            week: [core_index(s) for s in week_slots(block, week) if s.program == CORE]
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


class TestRestOfWeek(unittest.TestCase):
    def test_stacks_the_whole_week_from_monday(self):
        classes = rest_of_week([load()], off(), dt.date(2026, 10, 19))
        self.assertEqual(len(classes), 14)
        self.assertEqual(classes[0][0], dt.date(2026, 10, 19))
        self.assertEqual(classes[-1][0], dt.date(2026, 10, 25))
        self.assertEqual([date for date, _, _ in classes], sorted(date for date, _, _ in classes))

    def test_midweek_stacks_through_sunday(self):
        classes = rest_of_week([load()], off(), dt.date(2026, 10, 24))
        self.assertEqual({date for date, _, _ in classes}, {dt.date(2026, 10, 24), dt.date(2026, 10, 25)})

    def test_never_rolls_into_next_week(self):
        classes = rest_of_week([load()], off(), dt.date(2026, 11, 8))
        self.assertEqual({date for date, _, _ in classes}, {dt.date(2026, 11, 8)})
        self.assertEqual({block.name for _, block, _ in classes}, {"2026_fall"})

    def test_off_week(self):
        classes = rest_of_week([load()], off(), dt.date(2026, 11, 9))
        self.assertEqual(len(classes), 11)
        self.assertEqual({block.name for _, block, _ in classes}, {"off"})

    def test_before_first_block(self):
        with self.assertRaises(LookupError):
            rest_of_week([load()], off(), dt.date(2026, 9, 27))


class TestBreaks(unittest.TestCase):
    def winter(self):
        return Block(
            "winter", dt.date(2026, 11, 16), 3, [], [dt.date(2026, 11, 23), dt.date(2026, 11, 30)]
        )

    def test_breaks_extend_the_block_and_skip_week_numbers(self):
        block = self.winter()
        self.assertEqual(block.end, dt.date(2026, 12, 21))
        self.assertEqual(block.week_of(dt.date(2026, 12, 7)), 2)
        self.assertEqual(block.week_of(dt.date(2026, 12, 14)), 3)
        self.assertEqual(block.monday_of(2), dt.date(2026, 12, 7))

    def test_break_runs_the_off_schedule_from_its_first_week(self):
        block = active_block([self.winter()], off(), dt.date(2026, 11, 30))
        self.assertEqual(block.name, "winter break")
        self.assertEqual(block.week_of(dt.date(2026, 11, 30)), 2)
        slots = week_slots(block, 1)
        self.assertEqual([s.day for s in slots if s.program == CORE], DAYS)

    def test_rejects_break_outside_the_block(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "block.toml"
            path.write_text("start = 2026-11-16\nweeks = 2\nbreaks = [2026-11-16]\nprograms = []\n")
            with self.assertRaises(ValueError):
                load_block(path, ROOT / "programs")


class TestOff(unittest.TestCase):
    def test_starts_when_the_last_block_ends(self):
        block = active_block([load()], off(), dt.date(2026, 11, 16))
        self.assertEqual(block.start, dt.date(2026, 11, 9))
        self.assertEqual(block.heading(block.week_of(dt.date(2026, 11, 16))), "off, week 2")

    def test_next_block_takes_over_and_off_restarts_after_it(self):
        fall = load()
        winter = Block("winter", dt.date(2026, 12, 7), 1, [])
        self.assertIs(active_block([fall, winter], off(), dt.date(2026, 12, 7)), winter)
        block = active_block([fall, winter], off(), dt.date(2026, 12, 14))
        self.assertEqual(block.start, dt.date(2026, 12, 14))

    def test_core_runs_daily_and_rotates(self):
        block = active_block([load()], off(), dt.date(2026, 11, 9))
        weeks = {
            week: [(s.day, core_index(s)) for s in week_slots(block, week) if s.program == CORE]
            for week in (1, 2, 3)
        }
        self.assertEqual(weeks[1], list(zip(DAYS, range(1, 8))))
        self.assertEqual(weeks[2], list(zip(DAYS, range(8, 15))))
        self.assertEqual(weeks[3], weeks[1])

    def test_block_keeps_core_on_its_own_days(self):
        days = [s.day for s in week_slots(load(), 1) if s.program == CORE]
        self.assertEqual(days, ["tuesday", "thursday", "saturday", "sunday"])

    def test_week(self):
        block = active_block([load()], off(), dt.date(2026, 11, 9))
        self.assertEqual(
            [(s.day, s.program) for s in week_slots(block, 1) if s.program != CORE],
            [
                ("tuesday", "Weekday Rides"),
                ("thursday", "Weekday Rides"),
                ("saturday", "Weekend"),
                ("sunday", "Weekend"),
            ],
        )


class TestArmsRides(unittest.TestCase):
    def rides_slots(self, block):
        return [s for s in week_slots(block, 1) if s.program == "Weekday Rides"]

    def off_block(self):
        return active_block([load()], off(), dt.date(2026, 11, 9))

    def test_strength_block_never_searches_arms_rides(self):
        searches = []

        def search(params):
            searches.append(params)
            return [{"id": f"r{len(searches)}", "title": "Ride", "instructor_id": "i"}]

        resolve(self.rides_slots(load()), search, ride)
        self.assertEqual([s["has_cycling_arms"] for s in searches], ["false", "false"])

    def test_off_prioritizes_arms_rides(self):
        def search(params):
            arms = params["has_cycling_arms"] == "true"
            return [{"id": f"{arms}{params['duration']}", "title": "Ride", "instructor_id": "i"}]

        ids = [class_id for _, class_id, _, _ in resolve(self.rides_slots(self.off_block()), search, ride)]
        self.assertEqual(ids, ["True1200", "True1800"])

    def test_block_without_strength_prioritizes_arms_rides(self):
        program = load_program(ROOT / "programs" / "weekday_rides.toml")
        block = Block("rides", dt.date(2026, 10, 19), 1, [program])
        self.assertTrue(all(s.arms_search_url for s in self.rides_slots(block)))

    def test_off_falls_back_when_no_arms_rides(self):
        def search(params):
            if params["has_cycling_arms"] == "true":
                return []
            return [{"id": params["duration"], "title": "Ride", "instructor_id": "i"}]

        ids = [class_id for _, class_id, _, _ in resolve(self.rides_slots(self.off_block()), search, ride)]
        self.assertEqual(ids, ["1200", "1800"])


class TestShuffle(unittest.TestCase):
    def test_pick_uses_every_item_before_repeating(self):
        items = ["a", "b", "c", "d"]
        for start in range(0, 40, 4):
            picks = [pick(items, "seed", week) for week in range(start + 1, start + 5)]
            self.assertEqual(sorted(picks), items)

    def test_pick_never_repeats_back_to_back(self):
        for seed in range(200):
            picks = [pick(["a", "b", "c"], seed, week) for week in range(1, 31)]
            self.assertTrue(all(a != b for a, b in zip(picks, picks[1:])))

    def test_pick_is_stable(self):
        self.assertEqual(pick(list("abcdef"), "seed", 3), pick(list("fedcba"), "seed", 3))

    def test_saturday_does_not_repeat_in_weeks_1_to_4(self):
        block = load()
        picks = [
            s.class_ref
            for week in range(1, 5)
            for s in week_slots(block, week)
            if s.program == "Weekend" and s.day == "saturday"
        ]
        self.assertEqual(len(set(picks)), 4)

    def test_sunday_does_not_repeat_in_weeks_1_to_6(self):
        block = load()
        rides = [
            {"id": f"yin{i}", "title": "Yin", "instructor_id": "i", "original_air_time": 0}
            for i in range(10)
        ]
        picks = [
            class_id
            for week in range(1, 7)
            for _, class_id, _, _ in resolve(
                [s for s in week_slots(block, week) if s.program == "Weekend" and s.day == "sunday"],
                lambda params: rides,
                ride,
            )
        ]
        self.assertEqual(len(set(picks)), 6)

    def test_shuffle_search_ignores_classes_aired_during_block(self):
        block = load()
        aired_before = {"id": "old", "title": "Yin", "instructor_id": "i", "original_air_time": 0}
        aired_after = {**aired_before, "id": "new", "original_air_time": 4_000_000_000}
        searches = []

        def search(params):
            searches.append(params)
            return [aired_before, aired_after]

        slots = [s for s in week_slots(block, 1) if s.program == "Weekend" and s.day == "sunday"]
        self.assertEqual(resolve(slots, search, ride)[0][1], "old")
        self.assertEqual(searches[0]["desc"], "false")


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

    def test_searched_workouts_prefer_new_classes(self):
        searches = []

        def search(params):
            searches.append(params)
            if params.get("has_workout") == "false":
                return [{"id": "new", "title": "New", "instructor_id": "i"}]
            return [{"id": "taken", "title": "Taken", "instructor_id": "i"}]

        slots = [s for s in week_slots(load(), 1) if s.program == "Weekday Rides"]
        resolved = resolve(slots, search, ride)
        self.assertEqual(
            [(s.day, title) for s, _, title, _ in resolved],
            [("tuesday", "New"), ("thursday", "Taken")],
        )
        self.assertEqual(searches[0]["duration"], "1200")
        self.assertEqual(searches[1]["duration"], "1800")
        self.assertEqual(searches[0]["has_cycling_arms"], "false")
        self.assertEqual(searches[1]["has_cycling_arms"], "false")

    def test_untitled_workouts_use_class_title(self):
        slots = [s for s in week_slots(load(), 1) if s.program == CORE]
        titles = [title for _, _, title, _ in resolve(slots, None, ride)]
        self.assertEqual(titles, ["Ride"] * 4)


if __name__ == "__main__":
    unittest.main()
