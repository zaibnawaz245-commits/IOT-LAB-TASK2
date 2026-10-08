hours = float(input("Enter number of hours worked: "))
rate = float(input("Enter hourly rate: "))

if hours <= 40:
    pay = hours * rate
else:
    normal_pay = 40 * rate
    overtime_hours = hours - 40
    overtime_pay = overtime_hours * (rate * 1.5)
    pay = normal_pay + overtime_pay

print("Total Pay is:", pay)