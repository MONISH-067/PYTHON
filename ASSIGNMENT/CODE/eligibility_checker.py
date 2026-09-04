"""
eligibility_checker.py
-----------------------
Donation eligibility tracking based on the mandatory 90-day gap rule.

Author: Monika S (Module Owner - Eligibility Tracking)
"""

from datetime import datetime, timedelta

DATE_FORMAT = "%Y-%m-%d"
ELIGIBILITY_GAP_DAYS = 90


class InvalidDonorError(Exception):
    """Raised when an operation references a donor_id that does not exist."""
    pass


def check_eligibility(donors, donor_id, today=None):
    """
    Determine whether a donor is currently eligible to donate.

    Returns a tuple: (is_eligible: bool, relevant_date: date)
      - If eligible, relevant_date is today's date.
      - If not eligible, relevant_date is the next-eligible date.
    """
    if donor_id not in donors:
        raise InvalidDonorError(f"Donor ID '{donor_id}' was not found.")

    today = today or datetime.today().date()
    last_str = donors[donor_id]["last_donation"]

    if not last_str:
        # Never donated before -> immediately eligible
        return True, today

    last_date = datetime.strptime(last_str, DATE_FORMAT).date()
    days_since = (today - last_date).days

    if days_since >= ELIGIBILITY_GAP_DAYS:
        return True, today

    next_eligible = last_date + timedelta(days=ELIGIBILITY_GAP_DAYS)
    return False, next_eligible


def calculate_next_eligible_date(last_donation_str):
    """Given a last-donation date string, return the next-eligible date."""
    last_date = datetime.strptime(last_donation_str, DATE_FORMAT).date()
    return last_date + timedelta(days=ELIGIBILITY_GAP_DAYS)


def record_donation(donors, history, donor_id, donation_date=None):
    """
    Record a new donation: updates the donor's last_donation field and
    appends an entry to the donation history list.
    """
    if donor_id not in donors:
        raise InvalidDonorError(f"Donor ID '{donor_id}' was not found.")

    donation_date = donation_date or datetime.today().strftime(DATE_FORMAT)
    donors[donor_id]["last_donation"] = donation_date
    history.append({"donor_id": donor_id, "date": donation_date})
    return True


def eligible_donor_ids(donors, today=None):
    """List comprehension: all donor IDs currently eligible to donate."""
    today = today or datetime.today().date()
    return [
        donor_id for donor_id in donors
        if check_eligibility(donors, donor_id, today)[0]
    ]
