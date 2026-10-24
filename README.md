# peloton-stacker

Keeps my Peloton stack loaded with the next few days of my training plan, so I don't have to click through the app.

## Story

I train in blocks of 1-6 weeks. A block starts on a Monday and combines one or more programs, and any day can have more than one workout.

A program is the same classes every week, like Tunde's Bike Bootcamp, a list I rotate through, like Emma's Crush Your Core, or a pool I shuffle, like my weekend yoga. A program can also have supplements, like a 5 min cool down after every bootcamp class. Supplements come from a Peloton filter URL and prefer classes I haven't taken.

Peloton's stack only holds 10 classes and my weeks have more than that, so every morning the script restacks from today forward.

```
programs/   one TOML per program
blocks/     one TOML per block, start date + weeks + programs
stack/      Peloton client, plan, class picking
runner.py   CLI
```

## Setup

```sh
export PELOTON_USERNAME=...
export PELOTON_PASSWORD=...
pip install requests
```

Python 3.11+.

## Stack classes

The script empties the stack, then adds today's classes and each day after until the next day won't fit in 10. It never splits a day, rolls into next week, and stops at the end of the block. A class I skip drops off the next morning. It picks every class before emptying the stack, so if anything fails my stack stays as it was.

```sh
./run.sh stack --dry-run   # print what would be stacked, don't touch the stack
./run.sh stack             # empty the stack, then stack from today
./run.sh stack --date 2026-10-26 --dry-run   # stack from another day
```

To see a whole week of the current block without touching the stack:

```sh
./run.sh week              # this week
./run.sh week --week 2     # week 2
```

## Other commands

```sh
./run.sh add <class url or id>   # add one class
./run.sh empty                   # empty the stack
./test.sh                        # run tests
```

## Run it on GitHub

`.github/workflows/stack.yml` runs the tests and then `stack` every day at midnight Pacific. It reads `PELOTON_USERNAME` and `PELOTON_PASSWORD` from the repo's Actions secrets, under Settings, Secrets and variables, Actions.

To run it by hand, open Actions, pick Stack classes, and Run workflow. I can fill in a date to stack from or check dry run there.

GitHub turns off scheduled workflows after 60 days without a commit, so if a block goes quiet that long I re-enable it from the Actions tab.

## Add a program

Fixed classes every week:

```toml
name = "Tunde Oyeneyin Bike Bootcamp"

[[workouts]]
day = "monday"
title = "Lower Body + Climb Ride"
class = "https://members.onepeloton.com/classes/...?classId=..."

[[supplements]]
title = "5 min cool down"
search = "https://members.onepeloton.com/classes/cycling?..."
```

A workout or supplement can use `search` with a Peloton filter URL instead of a fixed `class`. It picks the newest class I haven't taken, falls back to ones I have, and never picks the same class twice in one stack. Without a `title` it shows the class's own title.

```toml
name = "Weekday Rides"

[[workouts]]
day = "tuesday"
search = "https://members.onepeloton.com/classes/cycling/?..."
```

Programs stack in the order the block lists them, so on Tuesday Weekday Rides comes after Crush Your Core.

Rotating classes, picks up where last week left off and wraps around:

```toml
name = "Emma Lovewell Crush Your Core"
days = ["tuesday", "thursday", "saturday", "sunday"]
rotation = [
  "https://members.onepeloton.com/profile/workouts/...",
]
```

Shuffled classes, a random class each week from a pool. Each shuffle has its own pool and goes through every class in it before repeating, then reshuffles. The order is fixed per block, so a dry run and the real run pick the same class. A pool is either a list of classes or a search URL:

```toml
name = "Weekend"

[[shuffles]]
day = "saturday"
classes = [
  "https://members.onepeloton.com/classes/...?classId=...",
]

[[shuffles]]
day = "sunday"
search = "https://members.onepeloton.com/classes/yoga?..."
```

A search pool only uses classes that aired before the block started, so new releases don't reshuffle the block halfway through.

## Start a block

A block is a TOML file in `blocks/`. The file name is the block name the script prints, and `programs` lists file names from `programs/` without `.toml`.

```toml
start = 2026-11-09   # Monday of week 1
weeks = 6            # 1-6
programs = ["tunde_bike_bootcamp", "crush_your_core"]
```

The script counts weeks from `start`, so `start` is the only thing that sets which week I'm in. If I'm already partway into a block, I count back from this Monday. Week 4 this week means `start` is the Monday three weeks ago.

A block ends the Sunday after its last week. In a block's last days the stack stops at that Sunday, unless the next block is already in `blocks/`. Once no block covers today, `./run.sh stack` stops with `No block covers the week of ...` and leaves my stack alone, so I add the next block before then. Blocks shouldn't overlap, since the script uses the first one it finds.

Rotations restart at the first class in every new block. To pick up where the last block left off, reorder `rotation` in the program.

## Credit

Started from [geudrik/peloton-client-library](https://github.com/geudrik/peloton-client-library).
