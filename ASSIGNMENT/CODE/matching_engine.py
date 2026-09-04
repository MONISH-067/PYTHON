"""
matching_engine.py
--------------------
Blood-group compatibility rules and emergency donor matching.

Author: Monish L (Module Owner - Matching Engine & Emergency Requests)
"""

from eligibility_checker import check_eligibility

# Compatible donor blood groups for each requested (recipient) blood group.
# O- is the universal donor and appears in every list.
COMPATIBILITY = {
    "O-": ["O-"],
    "O+": ["O-", "O+"],
    "A-": ["O-", "A-"],
    "A+": ["O-", "O+", "A-", "A+"],
    "B-": ["O-", "B-"],
    "B+": ["O-", "O+", "B-", "B+"],
    "AB-": ["O-", "A-", "B-", "AB-"],
    "AB+": ["O-", "O+", "A-", "A+", "B-", "B+", "AB-", "AB+"],
}

# Simple demonstrative distance table between sample localities (km).
# In production this would be replaced by a geocoding / maps API call.
DISTANCE_TABLE = {
    ("Chennai", "Chennai"): 0, ("Chennai", "Coimbatore"): 500,
    ("Chennai", "Madurai"): 460, ("Chennai", "Trichy"): 320,
    ("Coimbatore", "Madurai"): 220, ("Coimbatore", "Trichy"): 210,
    ("Madurai", "Trichy"): 130,
}


def swap_priority(rank_a, rank_b):
    """Illustrative CO1 program: exchange the priority ranks of two donors."""
    rank_a, rank_b = rank_b, rank_a
    return rank_a, rank_b


def estimate_distance(location_a, location_b):
    """Look up an approximate distance (km) between two localities."""
    if location_a == location_b:
        return 0
    key = (location_a, location_b)
    reverse_key = (location_b, location_a)
    if key in DISTANCE_TABLE:
        return DISTANCE_TABLE[key]
    if reverse_key in DISTANCE_TABLE:
        return DISTANCE_TABLE[reverse_key]
    return 9999  # unknown distance -> treated as far away


def find_compatible_donors(donors, requested_group, location, today=None):
    """
    Return a list of (donor_id, distance) tuples for eligible, compatible
    donors, sorted nearest-first. Raises KeyError for an unknown blood group.
    """
    if requested_group not in COMPATIBILITY:
        raise KeyError(f"'{requested_group}' is not a recognised blood group.")

    accepted_groups = set(COMPATIBILITY[requested_group])
    matches = []

    for donor_id, details in donors.items():
        donor_group = f"{details['blood_group']}{details['rh']}"
        if donor_group not in accepted_groups:
            continue
        eligible, _ = check_eligibility(donors, donor_id, today)
        if not eligible:
            continue
        distance = estimate_distance(location, details["location"])
        matches.append((donor_id, distance))

    matches.sort(key=lambda pair: pair[1])
    return matches


def add_emergency_request(requests, request_id, blood_group, location):
    """Append a new pending emergency request to the requests list."""
    requests.append({
        "request_id": request_id,
        "blood_group": blood_group.strip().upper(),
        "location": location.strip().title(),
        "status": "PENDING",
    })
    return True


def resolve_request(requests, request_id):
    """Mark a pending emergency request as RESOLVED."""
    for req in requests:
        if req["request_id"] == request_id:
            req["status"] = "RESOLVED"
            return True
    return False
