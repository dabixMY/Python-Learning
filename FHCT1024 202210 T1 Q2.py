price = float(input("Enter price of the vehicle >> "))
downpay = float(input("Enter down payment amount  >> "))
interestRate = float(input("Enter loan interest rate   >> "))
tenure = float(input("Enter loan tenure (years)  >> "))
print()

loanamount = price - downpay
totInterest = loanamount * (interestRate / 100) * tenure
monthIns = (loanamount + totInterest) / (tenure * 12)
repay = round(monthIns)
lastPay = loanamount + totInterest - repay * (tenure * 12 - 1)

print(f"Computed amount            : {monthIns:.2f}")
print(f"Monthly repayment amount   : {repay:.2f}")
print(f"Last repayment amount      : {lastPay:.2f}")
print()

rm100 = repay % 100
rm50 = rm100 % 50
rm20 = rm50 % 20
rm10 = rm20 % 10
rm5 = rm10 % 5
rm1 = rm5 % 1

print(f"RM100 x {repay // 100:2d}  = {100 * (repay // 100):5d}")
print(f"RM 50 x {rm100 // 50:2d}  = {50 * (rm100 // 50):5d} ")
print(f"RM 20 x {rm50 // 20:2d}  = {20 * (rm50 // 20):5d}")
print(f"RM 10 x {rm20 // 10:2d}  = {10 * (rm20 // 10):5d}")
print(f"RM  5 x {rm10 // 5:2d}  = {5 * (rm10 // 5):5d}")
print(f"RM  1 x {rm5 // 1:2d}  = {rm5 // 1:5d}")
print()

intRate, percent = input("Enter loan interest rate   >> ").split("%")
intRate = float(intRate)
print()

print(f"Percentage in floating point number is {intRate:.2f}")