"""
donor_manager.py
-----------------
Donor registration, profile management and search operations.

Author: Monika S (Module Owner - Donor Registration & Search)
"""


class InvalidBloodGroupError(Exception):
    """Custom exception raised when a donor is registered with an
    unrecognised blood group / Rh factor combination."""
    pass


VALID_BLOOD_GROUPS = {"A", "B", "AB", "O"}
VALID_RH = {"+", "-"}


def register_donor(donors, donor_id, name, blood_group, rh, location, contact, last_donation):
    """
    Register a new donor into the donors dictionary.

    donors: dict -> {donor_id: {name, blood_group, rh, location, contact, last_donation}}
    Raises InvalidBloodGroupError for an unrecognised blood group/Rh pair.
    Returns True on success.
    """
    name = name.strip().title()
    location = location.strip().title()
    blood_group = blood_group.strip().upper()
    rh = rh.strip()

    if blood_group not in VALID_BLOOD_GROUPS or rh not in VALID_RH:
        raise InvalidBloodGroupError(
            f"'{blood_group}{rh}' is not a valid blood group/Rh combination."
        )

    if donor_id in donors:
        raise ValueError(f"Donor ID '{donor_id}' already exists.")

    donors[donor_id] = {
        "name": name,
        "blood_group": blood_group,
        "rh": rh,
        "location": location,
        "contact": contact.strip(),
        "last_donation": last_donation,
    }
    return True


def get_blood_group_tuple(donor_id, donors):
    """Return the immutable (blood_group, rh) tuple identity for a donor."""
    details = donors.get(donor_id)
    if details is None:
        return None
    return (details["blood_group"], details["rh"])


def search_by_name(donors, keyword):
    """Case-insensitive substring search by donor name."""
    keyword = keyword.strip().lower()
    return [
        donor_id for donor_id, details in donors.items()
        if keyword in details["name"].lower()
    ]


def search_by_location(donors, location):
    """Return donor IDs located in the given locality."""
    location = location.strip().lower()
    return [
        donor_id for donor_id, details in donors.items()
        if details["location"].lower() == location
    ]


def search_by_blood_group(donors, blood_group, rh=None):
    """List comprehension based filter for donors of a given blood group (+ optional Rh)."""
    blood_group = blood_group.strip().upper()
    if rh:
        return [
            donor_id for donor_id, d in donors.items()
            if d["blood_group"] == blood_group and d["rh"] == rh
        ]
    return [donor_id for donor_id, d in donors.items() if d["blood_group"] == blood_group]


def unique_localities(donors):
    """Return the set of unique localities currently registered."""
    return {details["location"] for details in donors.values()}


def unique_blood_groups(donors):
    """Return the set of unique blood-group+Rh combinations registered."""
    return {f"{d['blood_group']}{d['rh']}" for d in donors.values()}
