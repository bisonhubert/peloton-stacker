import datetime as dt

from stack.client import search_params_from
from stack.plan import pick


def resolve(slots, search, ride):
    used = set()
    resolved = []
    for slot in slots:
        if slot.class_ref:
            found = ride(slot.class_ref)
        elif slot.shuffle:
            found = _draw(search, search_params_from(slot.search_url), *slot.shuffle)
        else:
            found = _pick(search, search_params_from(slot.search_url), used)
        used.add(found["id"])
        resolved.append((slot, found["id"], slot.title or found["title"], found["instructor_id"]))
    return resolved


def first_name(name):
    return name.split()[0]


def _pick(search, params, used):
    for attempt in (params, {k: v for k, v in params.items() if k != "has_workout"}):
        for ride in search(attempt):
            if ride["id"] not in used:
                return ride
    raise LookupError(f"No class left for search {params}")


def _draw(search, params, seed, week, aired_before):
    cutoff = dt.datetime.combine(aired_before, dt.time(), dt.timezone.utc).timestamp()
    params = {**params, "sort_by": "original_air_time", "desc": "false"}
    rides = {r["id"]: r for r in search(params) if r["original_air_time"] < cutoff}
    if not rides:
        raise LookupError(f"No class aired before {aired_before} for search {params}")
    return rides[pick(list(rides), seed, week)]
