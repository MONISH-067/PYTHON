"""
analytics.py
-------------
Performance analysis: scarcity, reliability score, monthly donation trends.

Author: Monish L (Module Owner - Analytics)
"""

import statistics
from collections import Counter
from datetime import datetime


def blood_group_scarcity_by_locality(donors):
    """
    Return {locality: {blood_group: count}} to highlight which localities
    are short on which blood groups.
    """
    scarcity = {}
    for details in donors.values():
        locality = details["location"]
        group = f"{details['blood_group']}{details['rh']}"
        scarcity.setdefault(locality, Counter())
        scarcity[locality][group] += 1
    return scarcity


def donor_reliability_score(donor_id, history, no_show_log=None):
    """
    Reliability score = donations completed / (donations completed + no-shows).
    no_show_log: optional dict {donor_id: no_show_count}.
    Returns a float between 0 and 1 (1.0 = perfectly reliable).
    """
    donations = sum(1 for entry in history if entry["donor_id"] == donor_id)
    no_shows = (no_show_log or {}).get(donor_id, 0)
    total = donations + no_shows
    if total == 0:
        return None  # insufficient data
    return round(donations / total, 2)


def monthly_donation_trend(history):
    """Return {'YYYY-MM': donation_count} sorted chronologically."""
    counts = Counter()
    for entry in history:
        month_key = entry["date"][:7]  # YYYY-MM
        counts[month_key] += 1
    return dict(sorted(counts.items()))


def average_donations_per_donor(history):
    """Statistics module usage: mean donations per donor across history."""
    if not history:
        return 0
    per_donor = Counter(entry["donor_id"] for entry in history)
    return round(statistics.mean(per_donor.values()), 2)
