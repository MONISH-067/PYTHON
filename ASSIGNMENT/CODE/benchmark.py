"""
benchmark.py
-------------
Measures execution time of compatible-donor search, eligibility calculation,
and donor lookup across increasing dataset sizes (100 / 500 / 1000 donors).
"""

import random
import time
from datetime import date, timedelta

from donor_manager import register_donor
from eligibility_checker import check_eligibility
from matching_engine import find_compatible_donors

TODAY = date(2026, 9, 3)
GROUPS = ["A", "B", "AB", "O"]
RH = ["+", "-"]
LOCATIONS = ["Chennai", "Coimbatore", "Madurai", "Trichy"]


def build_dataset(n):
    donors = {}
    for i in range(n):
        donor_id = f"D{i:05d}"
        last_donation = (TODAY - timedelta(days=random.randint(0, 200))).isoformat()
        register_donor(
            donors, donor_id, f"donor {i}",
            random.choice(GROUPS), random.choice(RH),
            random.choice(LOCATIONS), f"9{i:09d}", last_donation,
        )
    return donors


def time_it(func, *args, repeats=5):
    start = time.perf_counter()
    for _ in range(repeats):
        func(*args)
    elapsed_ms = (time.perf_counter() - start) / repeats * 1000
    return elapsed_ms


print(f"{'Metric':<28}{'100 donors':>14}{'500 donors':>14}{'1000 donors':>14}")
results = {}
for n in (100, 500, 1000):
    donors = build_dataset(n)
    sample_id = f"D{n // 2:05d}"

    lookup_time = time_it(lambda: donors.get(sample_id))
    eligibility_time = time_it(lambda: check_eligibility(donors, sample_id, TODAY))
    search_time = time_it(lambda: find_compatible_donors(donors, "AB+", "Chennai", TODAY), repeats=3)

    results[n] = (search_time, eligibility_time, lookup_time)

print(f"{'Compatible Donor Search':<28}" +
      "".join(f"{results[n][0]:>11.3f}ms" for n in (100, 500, 1000)))
print(f"{'Eligibility Calculation':<28}" +
      "".join(f"{results[n][1]:>11.4f}ms" for n in (100, 500, 1000)))
print(f"{'Donor Lookup Time':<28}" +
      "".join(f"{results[n][2]:>11.4f}ms" for n in (100, 500, 1000)))
