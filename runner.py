import argparse
import datetime as dt
from pathlib import Path

from stack.client import Client, class_id_from
from stack.plan import active_block, load_block, load_off, rest_of_week, week_monday, week_slots
from stack.resolve import resolve, first_name

ROOT = Path(__file__).parent
PST = dt.timezone(dt.timedelta(hours=-8))


def print_stack(stack):
    print(f"Stack has {stack['numClasses']} classes:")
    for item in stack["userStack"]["stackedClassList"]:
        pelo = item["pelotonClass"]
        print(f"  {item['playOrder'] + 1}. {pelo['title']} ({pelo['classId']})")


def load_schedule():
    blocks = [load_block(p, ROOT / "programs") for p in sorted((ROOT / "blocks").glob("*.toml"))]
    return blocks, load_off(ROOT / "off.toml", ROOT / "programs")


def resolve_classes(client, slots):
    return resolve(slots, lambda params: client.search_classes(params, limit=50), client.ride)


def print_class(label, title, instructor, class_id):
    print(f"  {label:<10} {title} with {first_name(instructor)} ({class_id})")


def today():
    return dt.datetime.now(PST).date()


def week(week_number):
    schedule = load_schedule()
    monday = week_monday(today())
    block = active_block(*schedule, monday)
    if week_number:
        if week_number < 1 or (block.weeks and week_number > block.weeks):
            raise SystemExit(f"--week {week_number} is out of range for {block.name}")
        monday = block.monday_of(week_number)
        block = active_block(*schedule, monday)
    week_number = block.week_of(monday)
    client = Client()
    plan = resolve_classes(client, week_slots(block, week_number))
    names = client.instructor_names()
    print(f"{block.heading(week_number)} (starting {monday}):")
    for slot, class_id, title, instructor_id in plan:
        print_class(slot.day.title(), title, names[instructor_id], class_id)


def stack(dry_run, date):
    classes = rest_of_week(*load_schedule(), date)
    client = Client()
    plan = resolve_classes(client, [slot for _, _, slot in classes])
    names = client.instructor_names()
    heading = None
    for (date, block, _), (_, class_id, title, instructor_id) in zip(classes, plan):
        label = block.heading(block.week_of(week_monday(date)))
        if heading != label:
            heading = label
            print(f"{label}:")
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
