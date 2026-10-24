from stack.client import search_params_from


def resolve(slots, search, ride):
    used = set()
    resolved = []
    for slot in slots:
        if slot.class_ref:
            found = ride(slot.class_ref)
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
