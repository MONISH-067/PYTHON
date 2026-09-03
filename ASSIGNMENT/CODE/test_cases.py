"""
test_cases.py
--------------
Automated execution of the minimum required test scenarios (TC1-TC7).
Run: python test_cases.py
"""

from datetime import date, timedelta

from donor_manager import InvalidBloodGroupError, register_donor
from eligibility_checker import InvalidDonorError, check_eligibility
from matching_engine import find_compatible_donors
from file_handler import load_donors

TODAY = date(2026, 9, 3)


def line(title):
    print("\n" + "-" * 60)
    print(title)
    print("-" * 60)


donors = {}

# TC1: Register a new donor with valid details
line("TC1: Register a new donor with valid details")
register_donor(donors, "D001", "asha rao", "O", "-", "chennai", "9000000001",
                (TODAY - timedelta(days=100)).isoformat())
print("PASS -> Donor D001 registered:", donors["D001"])

# TC2: Eligibility check - last donation 100 days ago -> ELIGIBLE
line("TC2: Eligibility check, last donation 100 days ago")
eligible, info = check_eligibility(donors, "D001", today=TODAY)
print(f"PASS -> eligible={eligible}, date={info}" if eligible else "FAIL")

# TC3: Eligibility check - last donation 30 days ago -> NOT ELIGIBLE, correct next date
line("TC3: Eligibility check, last donation 30 days ago")
register_donor(donors, "D002", "bala krishnan", "A", "+", "coimbatore", "9000000002",
                (TODAY - timedelta(days=30)).isoformat())
eligible, next_date = check_eligibility(donors, "D002", today=TODAY)
expected_next = TODAY - timedelta(days=30) + timedelta(days=90)
status = "PASS" if (not eligible and next_date == expected_next) else "FAIL"
print(f"{status} -> eligible={eligible}, next_eligible_date={next_date} (expected {expected_next})")

# TC4: Search for compatible donors for an O-negative emergency request
line("TC4: Compatible donors for O-negative request")
register_donor(donors, "D003", "chitra devi", "O", "-", "chennai", "9000000003",
                (TODAY - timedelta(days=120)).isoformat())
register_donor(donors, "D004", "dinesh kumar", "A", "+", "chennai", "9000000004",
                (TODAY - timedelta(days=120)).isoformat())
matches = find_compatible_donors(donors, "O-", "Chennai", today=TODAY)
match_ids = [m[0] for m in matches]
status = "PASS" if match_ids == ["D001", "D003"] or set(match_ids) == {"D001", "D003"} else "FAIL"
print(f"{status} -> only O- eligible donors returned: {match_ids}")

# TC5: Search for a donor by location
line("TC5: Search for a donor by location")
from donor_manager import search_by_location
results = search_by_location(donors, "Chennai")
status = "PASS" if set(results) == {"D001", "D003", "D004"} else "FAIL"
print(f"{status} -> donors in Chennai: {results}")

# TC6: Register a donor with an invalid blood group -> InvalidBloodGroupError
line("TC6: Register donor with invalid blood group 'X+'")
try:
    register_donor(donors, "D005", "eshwar", "X", "+", "madurai", "9000000005", "")
    print("FAIL -> no exception raised")
except InvalidBloodGroupError as exc:
    print(f"PASS -> InvalidBloodGroupError raised and handled: {exc}")

# TC7: Load a missing CSV file -> handled gracefully
line("TC7: Load a missing CSV file")
result = load_donors("data/does_not_exist.csv")
status = "PASS" if result == {} else "FAIL"
print(f"{status} -> missing file handled gracefully, returned: {result}")

line("ALL TEST SCENARIOS COMPLETE")
