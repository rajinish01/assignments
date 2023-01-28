"""
In a university, your attendance determines whether you will be
allowed to attend your graduation ceremony.
You are not allowed to miss classes for four or more consecutive days.
Your graduation ceremony is on the last day of the academic year,
which is the Nth day.

Your task is to determine the following:

1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.

Represent the solution in the string format as "Answer of (2) / Answer
of (1)", don't actually divide or reduce the fraction to decimal

Test cases:

for 5 days: 14/29

for 10 days: 372/773
"""

from itertools import permutations


def graduation_ceremony(graduation_day, min_days_to_attend=4):

    if not min_days_to_attend >= 4:
        raise Exception("Graduation Day should be more than 4")

    total_ways_to_attend = 2**graduation_day
    total_ways_to_miss = 2 ** (graduation_day - 1)

    invalid_ways_to_attend = {("0",) * graduation_day: 1}

    possible_days = graduation_day - min_days_to_attend

    for present in range(1, possible_days + 1):
        absent = graduation_day - present
        choices = "1" * present + "0" * absent
        possible_choices = set(permutations(choices))

        for choice in possible_choices:
            attendence = possible_days - present + 1
            is_match = False

            for count in range(attendence):
                absent_days = graduation_day - present - count
                present_days = present + count + 1

                for i in range(present_days):
                    sub_string = choice[i : i + absent_days]
                    if sub_string.count("0") == absent_days:
                        invalid_ways_to_attend.update(
                            {choice: invalid_ways_to_attend.get(choice, 0) + 1}
                        )
                        is_match = True
                        break
                if is_match:
                    break

    possible_ways_to_attend = total_ways_to_attend - len(invalid_ways_to_attend)
    invalid_consecutive_days = sum(
        1 for ways in invalid_ways_to_attend if ways[-1] == "0"
    )
    probability = total_ways_to_miss - invalid_consecutive_days

    print("{}/{}".format(probability, possible_ways_to_attend))


if __name__ == "__main__":
    graduation_ceremony(10, 4)
