import csv

with open("employees.csv", "r") as f:
    employees = csv.reader(f)

    with open("wages.csv", "w") as w:
        wages = csv.writer(w)
        current_row = 1

        for row in employees:
            if current_row == 1:
                wages.writerow(["employee_name", "pay_rate"])
            elif current_row > 1:
                name = row[0]
                hours = int(row[1])
                wages.writerow([name, hours*15])
            current_row += 1
