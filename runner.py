import argparse
import datetime as dt
from pathlib import Path

from stack.client import Client, class_id_from
from stack.plan import STACK_LIMIT, active_block, load_block, week_monday, week_slots, window
from stack.resolve import resolve, first_name

ROOT = Path(__file__).parent
PST = dt.timezone(dt.timedelta(hours=-8))


def print_stack(stack):
    print(f"Stack has {stack['numClasses']} classes:")
    for item in stack["userStack"]["stackedClassList"]:
        pelo = item["pelotonClass"]
        print(f"  {item['playOrder'] + 1}. {pelo['title']} ({pelo['classId']})")


def load_blocks():
    return [load_block(p, ROOT / "programs") for p in sorted((ROOT / "blocks").glob("*.toml"))]


def resolve_classes(client, slots):
    return resolve(slots, lambda params: client.search_classes(params, limit=50), client.ride)


def print_class(label, title, instructor, class_id):
    print(f"  {label:<10} {title} with {first_name(instructor)} ({class_id})")


def today():
    return dt.datetime.now(PST).date()


def week(week_number):
    monday = week_monday(today())
    block = active_block(load_blocks(), monday)
    if week_number:
        if not 1 <= week_number <= block.weeks:
            raise SystemExit(f"--week must be 1-{block.weeks} for {block.name}")
        monday = block.start + dt.timedelta(weeks=week_number - 1)
    week_number = block.week_of(monday)
    client = Client()
    plan = resolve_classes(client, week_slots(block, week_number))
    names = client.instructor_names()
    print(f"{block.name}, week {week_number} of {block.weeks} (starting {monday}):")
    for slot, class_id, title, instructor_id in plan:
        print_class(slot.day.title(), title, names[instructor_id], class_id)


def stack(dry_run, date):
    classes = window(load_blocks(), date, STACK_LIMIT)
    client = Client()
    plan = resolve_classes(client, [slot for _, _, slot in classes])
    names = client.instructor_names()
    heading = None
    for (date, block, _), (_, class_id, title, instructor_id) in zip(classes, plan):
        week_number = block.week_of(week_monday(date))
        if heading != (block.name, week_number):
            heading = (block.name, week_number)
            print(f"{block.name}, week {week_number} of {block.weeks}:")
        print_class(f"{date:%a %b} {date.day}", title, names[instructor_id], class_id)
    if dry_run:
        return
    result = client.empty_stack()
    for _, class_id, _, _ in plan:
        result = client.add_class(class_id)
    print_stack(result)


def main():
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(dest="command", required=True)
    week_parser = commands.add_parser("week")
    week_parser.add_argument("--week", type=int)
    stack_parser = commands.add_parser("stack")
    stack_parser.add_argument("--dry-run", action="store_true")
    stack_parser.add_argument("--date", type=dt.date.fromisoformat, default=today())
    add_parser = commands.add_parser("add")
    add_parser.add_argument("class_url_or_id")
    commands.add_parser("empty")
    args = parser.parse_args()

    if args.command == "week":
        week(args.week)
    elif args.command == "stack":
        stack(args.dry_run, args.date)
    elif args.command == "add":
        print_stack(Client().add_class(class_id_from(args.class_url_or_id)))
    elif args.command == "empty":
        Client().empty_stack()


if __name__ == "__main__":
    main()
