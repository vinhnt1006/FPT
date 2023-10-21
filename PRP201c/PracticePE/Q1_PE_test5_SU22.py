def computepay(hours, rate):
  if hours > 40:
    extra_hours = hours - 40
    extra_pay = extra_hours * rate * 1.5
    pay = 40 * rate + extra_pay
  else:
    pay = hours * rate
  return pay

hours = float(input("Enter hours: "))
rate = float(input("Enter rate: "))

pay = computepay(hours, rate)

print("Pay:", pay)