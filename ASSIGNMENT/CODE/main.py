"""
main.py
--------
Main Menu and program flow for the Community Blood Donation and
Emergency Matching System.

Flow: Main Menu -> Donor Registration -> Eligibility Check ->
      Emergency Matching -> Analysis & Reports -> File Operations

Author: Naresh Kumar V (Integration & Main Program Flow)
"""

import os

from donor_manager import (
    InvalidBloodGroupError, register_donor, search_by_name,
    search_by_location, search_by_blood_group, unique_localities,
    unique_blood_groups,
)
from eligibility_checker import InvalidDonorError, check_eligibility, record_donation
from matching_engine import find_compatible_donors, add_emergency_request
from analytics import blood_group_scarcity_by_locality, monthly_donation_trend
from reports import format_scarcity_report, format_trend_report, format_match_results
from file_handler import save_donors, load_donors, save_history, load_history, save_requests, load_requests

DATA_DIR = "data"
DONORS_CSV = os.path.join(DATA_DIR, "donors.csv")
HISTORY_CSV = os.path.join(DATA_DIR, "donation_history.csv")
REQUESTS_CSV = os.path.join(DATA_DIR, "emergency_requests.csv")


def gcd(a, b):
    """Illustrative CO1 program: Euclidean GCD (used for scheduling-slot math)."""
    while b:
        a, b = b, a % b
    return a


def main_menu():
    donors = load_donors(DONORS_CSV)
    history = load_history(HISTORY_CSV)
    requests_list = load_requests(REQUESTS_CSV)

    menu = """
========== COMMUNITY BLOOD DONATION & EMERGENCY MATCHING SYSTEM ==========
1. Register New Donor
2. Check Donor Eligibility
3. Record a Donation
4. Search Donors (name / location / blood group)
5. Raise Emergency Request & Find Compatible Donors
6. Generate Reports (scarcity / trend)
7. Save Data to CSV
0. Exit
============================================================================
"""
    while True:
        print(menu)
        choice = input("Enter choice: ").strip()
        try:
            if choice == "1":
                donor_id = input("Donor ID: ").strip()
                name = input("Name: ")
                bg = input("Blood group (A/B/AB/O): ")
                rh = input("Rh (+/-): ")
                location = input("Location: ")
                contact = input("Contact: ")
                last_donation = input("Last donation date (YYYY-MM-DD, blank if never): ").strip()
                register_donor(donors, donor_id, name, bg, rh, location, contact, last_donation)
                print(f"Donor {donor_id} registered successfully.")

            elif choice == "2":
                donor_id = input("Donor ID: ").strip()
                eligible, date_info = check_eligibility(donors, donor_id)
                print("ELIGIBLE" if eligible else f"NOT ELIGIBLE - next eligible on {date_info}")

            elif choice == "3":
                donor_id = input("Donor ID: ").strip()
                record_donation(donors, history, donor_id)
                print("Donation recorded.")

            elif choice == "4":
                mode = input("Search by (1) Name (2) Location (3) Blood group: ").strip()
                if mode == "1":
                    print(search_by_name(donors, input("Name keyword: ")))
                elif mode == "2":
                    print(search_by_location(donors, input("Location: ")))
                else:
                    print(search_by_blood_group(donors, input("Blood group (e.g. O): "),
                                                 input("Rh (+/-, optional): ") or None))

            elif choice == "5":
                req_id = input("Request ID: ").strip()
                bg_full = input("Requested blood group (e.g. O-): ").strip().upper()
                location = input("Emergency location: ").strip()
                add_emergency_request(requests_list, req_id, bg_full, location)
                matches = find_compatible_donors(donors, bg_full, location)
                print(format_match_results(matches, bg_full, location))

            elif choice == "6":
                print(format_scarcity_report(blood_group_scarcity_by_locality(donors)))
                print()
                print(format_trend_report(monthly_donation_trend(history)))

            elif choice == "7":
                save_donors(donors, DONORS_CSV)
                save_history(history, HISTORY_CSV)
                save_requests(requests_list, REQUESTS_CSV)
                print("Data saved.")

            elif choice == "0":
                save_donors(donors, DONORS_CSV)
                save_history(history, HISTORY_CSV)
                save_requests(requests_list, REQUESTS_CSV)
                print("Goodbye.")
                break

            else:
                print("Invalid choice, try again.")

        except InvalidBloodGroupError as exc:
            print(f"[INPUT ERROR] {exc}")
        except InvalidDonorError as exc:
            print(f"[INPUT ERROR] {exc}")
        except ValueError as exc:
            print(f"[INPUT ERROR] {exc}")
        except Exception as exc:  # final safety net so the app never crashes
            print(f"[UNEXPECTED ERROR] {exc}")
        finally:
            pass  # placeholder for cleanup / logging hooks


if __name__ == "__main__":
    main_menu()
