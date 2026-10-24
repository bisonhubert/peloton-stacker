# peloton-stacker

Stacks my Peloton classes for the week so I don't have to click through the app.

## Story

A block is 1-6 weeks of one or more programs, starting on a Monday. Each week runs Monday - Sunday, and any day can have more than one workout.

A program is either the same classes every week, like Tunde's Bike Bootcamp, or a list I rotate through, like Emma's Crush Your Core. A program can have supplements, like a 5 min cool down after every bootcamp class. Supplements come from a Peloton filter URL and prefer classes I haven't taken.

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

Peloton's stack holds 10 classes, and a week can have more than that. So instead of stacking a whole week at once, the script stacks from today forward. It empties the stack, then adds today's classes and each day after that until the next day won't fit in 10. It never splits a day, and it rolls into next week and stops at the end of the block. Running it every morning keeps the stack full of what's coming up. A class I skip drops off the next morning.

The script figures out which block and week each day is in from the block's `start`.

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

A block ends the Sunday after its last week. Near the end, the stack stops at that Sunday unless the next block is already in `blocks/`, then it rolls right into it. Once no block covers today, `./run.sh stack` stops with `No block covers the week of ...` and leaves my stack alone, so I add the next block before then. Keep blocks from overlapping.

Rotations restart at the first class in every new block. To pick up where the last block left off, reorder `rotation` in the program.

## Credit

Started from [geudrik/peloton-client-library](https://github.com/geudrik/peloton-client-library).
