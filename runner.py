import argparse
import datetime as dt
from pathlib import Path

from stack.client import Client, class_id_from
from stack.plan import active_block, load_block, week_monday, week_slots
from stack.resolve import resolve, first_name

ROOT = Path(__file__).parent
PST = dt.timezone(dt.timedelta(hours=-8))


def print_stack(stack):
    print(f"Stack has {stack['numClasses']} classes:")
    for item in stack["userStack"]["stackedClassList"]:
        pelo = item["pelotonClass"]
        print(f"  {item['playOrder'] + 1}. {pelo['title']} ({pelo['classId']})")


def week(dry_run, week_number):
    monday = week_monday(dt.datetime.now(PST).date())
    blocks = [load_block(p, ROOT / "programs") for p in sorted((ROOT / "blocks").glob("*.toml"))]
    block = active_block(blocks, monday)
    if week_number:
        if not 1 <= week_number <= block.weeks:
            raise SystemExit(f"--week must be 1-{block.weeks} for {block.name}")
        monday = block.start + dt.timedelta(weeks=week_number - 1)
    week_number = block.week_of(monday)
    client = Client()
    plan = resolve(
        week_slots(block, week_number),
        lambda params: client.search_classes(params, limit=50),
        client.ride,
    )
    names = client.instructor_names()
    print(f"{block.name}, week {week_number} of {block.weeks} (starting {monday}):")
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
    week_parser.add_argument("--week", type=int)
    add_parser = commands.add_parser("add")
    add_parser.add_argument("class_url_or_id")
    commands.add_parser("empty")
    args = parser.parse_args()

    if args.command == "week":
        week(args.dry_run, args.week)
    elif args.command == "add":
        print_stack(Client().add_class(class_id_from(args.class_url_or_id)))
    elif args.command == "empty":
        Client().empty_stack()


if __name__ == "__main__":
    main()
