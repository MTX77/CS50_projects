import csv
import requests


def main():
    # Read NYTimes Covid Database
    download = requests.get(
        "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
    )
    decoded_content = download.content.decode("utf-8")
    file = decoded_content.splitlines()
    reader = csv.DictReader(file)

    # Construct 14 day lists of new cases for each states
    new_cases = calculate(reader)

    # Create a list to store selected states
    states = []
    print("Choose one or more states to view average COVID cases.")
    print("Press enter when done.\n")

    while True:
        state = input("State: ")
        if state in new_cases:
            states.append(state)
        if len(state) == 0:
            break

    print(f"\nSeven-Day Averages")

    # Print out 7-day averages for this week vs last week
    comparative_averages(new_cases, states)


def calculate(reader):
    new_cases = dict()
    prev_cases = dict()

    for line in reader:
        state = line["state"]
        cases = int(line["cases"])

        if state not in prev_cases:
            prev_cases[state] = cases
            new_cases[state] = []
        else:
            new_case = cases - prev_cases[state]
            prev_cases[state] = cases

            if len(new_cases[state]) >= 14:
                new_cases[state].pop(0)

            new_cases[state].append(new_case)

    return new_cases


def comparative_averages(new_cases, states):
    for state in states:
        suma1 = sum(new_cases[state][:7])
        suma2 = sum(new_cases[state][7:])
        avg1 = suma1 / 7
        avg2 = suma2 / 7

        try:
            prc = (avg1 - avg2) / avg2 * 100
        except ZeroDivisionError:
            print("Division by 0")

        if prc > 0:
            print(f"{state} had a 7-day average of {avg2:.0f} and an increase of {prc:.2f}%")
        elif prc < 0:
            print(f"{state} had a 7-day average of {avg2:.0f} and an decrease of {abs(prc):.2f}%")
        else:
             print(f"{state} had a 7-day average of {avg2:.0f} and the same number of cases like last week")


main()
