"""
file_handler.py
----------------
Handles all CSV read/write (persistence) operations for the Community Blood
Donation and Emergency Matching System.

Author: Naresh Kumar V (Module Owner - File Handling & Main Program Flow)
"""

import csv
import os


DONOR_FIELDS = ["donor_id", "name", "blood_group", "rh", "location", "contact", "last_donation"]
HISTORY_FIELDS = ["donor_id", "date"]
REQUEST_FIELDS = ["request_id", "blood_group", "location", "status"]


def save_donors(donors, filepath):
    """Write the donors dictionary to a CSV file."""
    try:
        with open(filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=DONOR_FIELDS)
            writer.writeheader()
            for donor_id, details in donors.items():
                row = {
                    "donor_id": donor_id,
                    "name": details["name"],
                    "blood_group": details["blood_group"],
                    "rh": details["rh"],
                    "location": details["location"],
                    "contact": details["contact"],
                    "last_donation": details["last_donation"],
                }
                writer.writerow(row)
        return True
    except (OSError, IOError) as exc:
        print(f"[ERROR] Could not save donors to '{filepath}': {exc}")
        return False


def load_donors(filepath):
    """Load donors from a CSV file into a dictionary. Returns {} if missing."""
    donors = {}
    if not os.path.exists(filepath):
        print(f"[WARNING] File '{filepath}' not found. Starting with an empty donor list.")
        return donors
    try:
        with open(filepath, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                donors[row["donor_id"]] = {
                    "name": row["name"].strip().title(),
                    "blood_group": row["blood_group"].strip().upper(),
                    "rh": row["rh"].strip(),
                    "location": row["location"].strip().title(),
                    "contact": row["contact"].strip(),
                    "last_donation": row["last_donation"].strip(),
                }
    except (OSError, IOError, csv.Error) as exc:
        print(f"[ERROR] Could not read donors from '{filepath}': {exc}")
    return donors


def save_history(history, filepath):
    """Write donation history (list of dicts) to a CSV file."""
    try:
        with open(filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=HISTORY_FIELDS)
            writer.writeheader()
            writer.writerows(history)
        return True
    except (OSError, IOError) as exc:
        print(f"[ERROR] Could not save donation history: {exc}")
        return False


def load_history(filepath):
    """Load donation history from CSV into a list of dicts."""
    history = []
    if not os.path.exists(filepath):
        print(f"[WARNING] File '{filepath}' not found. Starting with empty donation history.")
        return history
    try:
        with open(filepath, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                history.append({"donor_id": row["donor_id"], "date": row["date"]})
    except (OSError, IOError, csv.Error) as exc:
        print(f"[ERROR] Could not read donation history: {exc}")
    return history


def save_requests(requests, filepath):
    """Write pending emergency requests (list of dicts) to a CSV file."""
    try:
        with open(filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=REQUEST_FIELDS)
            writer.writeheader()
            writer.writerows(requests)
        return True
    except (OSError, IOError) as exc:
        print(f"[ERROR] Could not save emergency requests: {exc}")
        return False


def load_requests(filepath):
    """Load pending emergency requests from CSV into a list of dicts."""
    requests = []
    if not os.path.exists(filepath):
        print(f"[WARNING] File '{filepath}' not found. Starting with no pending requests.")
        return requests
    try:
        with open(filepath, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                requests.append(row)
    except (OSError, IOError, csv.Error) as exc:
        print(f"[ERROR] Could not read emergency requests: {exc}")
    return requests
