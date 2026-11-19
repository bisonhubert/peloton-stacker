import datetime as dt
import re

from stack.client import search_params_from
from stack.plan import pick

ARMS = re.compile(r"\barms?\b", re.IGNORECASE)


def resolve(slots, search, ride):
    used = set()
    resolved = []
    for slot in slots:
        if slot.class_ref:
            found = ride(slot.class_ref)
        elif slot.shuffle:
            found = _draw(search, search_params_from(slot.search_url), *slot.shuffle)
        else:
            urls = filter(None, (slot.arms_search_url, slot.search_url))
            found = _pick(search, [search_params_from(url) for url in urls], used)
        used.add(found["id"])
        resolved.append((slot, found["id"], slot.title or found["title"], found["instructor_id"]))
    return resolved


def first_name(name):
    return name.split()[0]


def _pick(search, searches, used):
    for params in searches:
        for attempt in (params, {k: v for k, v in params.items() if k != "has_workout"}):
            for ride in search(attempt):
                if ride["id"] not in used and not _unwanted_arms(params, ride):
                    return ride
    raise LookupError(f"No class left for search {searches}")


def _unwanted_arms(params, ride):
    return params.get("has_cycling_arms") == "false" and ARMS.search(ride["title"])


def _draw(search, params, seed, week, aired_before):
    cutoff = dt.datetime.combine(aired_before, dt.time(), dt.timezone.utc).timestamp()
    params = {**params, "sort_by": "original_air_time", "desc": "false"}
    rides = {r["id"]: r for r in search(params) if r["original_air_time"] < cutoff}
    if not rides:
        raise LookupError(f"No class aired before {aired_before} for search {params}")
    return rides[pick(list(rides), seed, week)]
