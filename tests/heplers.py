import random

Month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def generate_day():
    day = random.randint(1, 28)
    return str(day) if day >= 10 else '0' + str(day)

class GeneratedFormData():
    year = random.randint(1968, 2008)
    month = Month[random.randint(0, len(Month) - 1)]
    day = generate_day()


