import csv
from datetime import datetime, timedelta

def analyze_file(input_file):
    with open(input_file, 'r') as file:
        reader = csv.DictReader(file)
        employees = {}

        for row in reader:
            name = row['Employee Name']
            start_time = datetime.strptime(row['Start Time'], '%H:%M')
            end_time = datetime.strptime(row['End Time'], '%H:%M')
            date = datetime.strptime(row['Date'], '%Y-%m-%d')

            if name not in employees:
                employees[name] = []

            employees[name].append({'date': date, 'start_time': start_time, 'end_time': end_time})

    print("Employees who worked for 7 consecutive days:")
    for name, shifts in employees.items():
        consecutive_days = 1
        shifts.sort(key=lambda x: x['date'])

        for i in range(1, len(shifts)):
            if (shifts[i]['date'] - shifts[i-1]['date']).days == 1:
                consecutive_days += 1
            else:
                consecutive_days = 1

            if consecutive_days == 7:
                print(f"{name} has worked for 7 consecutive days.")

    print("\nEmployees with less than 10 hours between shifts (but greater than 1 hour):")
    for name, shifts in employees.items():
        shifts.sort(key=lambda x: x['date'])
        for i in range(1, len(shifts)):
            hours_between = (shifts[i]['start_time'] - shifts[i-1]['end_time']).total_seconds() / 3600
            if 1 < hours_between < 10:
                print(f"{name} has less than 10 hours between shifts (but greater than 1 hour).")

    print("\nEmployees who worked for more than 14 hours in a single shift:")
    for name, shifts in employees.items():
        for shift in shifts:
            hours_worked = (shift['end_time'] - shift['start_time']).total_seconds() / 3600
            if hours_worked > 14:
                print(f"{name} has worked for more than 14 hours in a single shift.")

if __name__ == "__main__":
    input_file = "your_input_file.csv"
    analyze_file(input_file)



# Please replace "your_input_file.csv"
