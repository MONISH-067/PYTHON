"""
reports.py
-----------
Formats analytics output into human-readable reports (string manipulation).

Author: Naresh Kumar V (Module Owner - Reports & Formatting)
"""


def format_scarcity_report(scarcity_data):
    """Build a formatted, readable scarcity report string."""
    lines = ["BLOOD-GROUP SCARCITY BY LOCALITY", "=" * 40]
    for locality, counts in scarcity_data.items():
        lines.append(f"\nLocality: {locality.title()}")
        for group, count in sorted(counts.items()):
            flag = " <-- LOW STOCK" if count <= 2 else ""
            lines.append(f"  {group:<4}: {count} donor(s){flag}")
    return "\n".join(lines)


def format_trend_report(trend_data):
    """Build a formatted monthly donation trend report string."""
    lines = ["MONTHLY DONATION TREND", "=" * 40]
    for month, count in trend_data.items():
        bar = "#" * count
        lines.append(f"  {month} | {bar} ({count})")
    return "\n".join(lines)


def format_match_results(matches, requested_group, location):
    """Build a formatted nearest-compatible-donor report string."""
    header = f"COMPATIBLE DONORS FOR {requested_group} REQUEST @ {location.title()}"
    lines = [header, "=" * len(header)]
    if not matches:
        lines.append("No eligible compatible donors found.")
    for donor_id, distance in matches:
        lines.append(f"  {donor_id:<6} distance: {distance:>4} km")
    return "\n".join(lines)


def clean_text(raw_text):
    """
    Demonstrates required string methods: strip(), upper(), title(),
    find(), replace() used together to normalise free-text input.
    """
    text = raw_text.strip()
    text = text.replace("_", " ")
    text = text.title()
    if text.find("Unknown") != -1:
        text = text.replace("Unknown", "N/A")
    return text
