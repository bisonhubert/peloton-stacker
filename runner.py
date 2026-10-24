import argparse
import datetime as dt
from pathlib import Path

from stack.client import Client, class_id_from
from stack.plan import active_cycle, load_cycle, week_monday, week_slots
from stack.resolve import resolve, first_name

ROOT = Path(__file__).parent
PST = dt.timezone(dt.timedelta(hours=-8))


def print_stack(stack):
    print(f"Stack has {stack['numClasses']} classes:")
    for item in stack["userStack"]["stackedClassList"]:
        pelo = item["pelotonClass"]
        print(f"  {item['playOrder']}. {pelo['title']} ({pelo['classId']})")


def week(dry_run):
    monday = week_monday(dt.datetime.now(PST).date())
    cycles = [load_cycle(p, ROOT / "programs") for p in sorted((ROOT / "cycles").glob("*.toml"))]
    cycle = active_cycle(cycles, monday)
    client = Client()
    week_number = cycle.week_of(monday)
    plan = resolve(
        week_slots(cycle, week_number),
        lambda params: client.search_classes(params, limit=50),
        client.ride,
    )
    names = client.instructor_names()
    print(f"{cycle.name}, week {week_number} of {cycle.weeks} (starting {monday}):")
    for slot, class_id, title, instructor_id in plan:
        instructor = first_name(names[instructor_id])
        print(f"  {slot.day.title():<10} {title} with {instructor} ({class_id})")
    if dry_run:
        return
    client.empty_stack()
    for _, class_id, _, _ in plan:
        stack = client.add_class(class_id)
    print_stack(stack)


def main():
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(dest="command", required=True)
    week_parser = commands.add_parser("week")
    week_parser.add_argument("--dry-run", action="store_true")
    add_parser = commands.add_parser("add")
    add_parser.add_argument("class_url_or_id")
    commands.add_parser("empty")
    args = parser.parse_args()

    if args.command == "week":
        week(args.dry_run)
    elif args.command == "add":
        print_stack(Client().add_class(class_id_from(args.class_url_or_id)))
    elif args.command == "empty":
        Client().empty_stack()


if __name__ == "__main__":
    main()
