print("Welcome to the tip calculator!")
bill = float(input('What was the total bill? $'))
tip_values = (10,12,15)
x = 0
while x == 0:
    tip = int(input("How much would you like to tip: 10, 12, or 15 percent? "))
    if tip in tip_values:
        break
    else:
        continue
total = float(bill*(1+tip/100))
payers = int(input('"How many people to split the bill?"'))
final = round(total/payers,2)
print(f"Each person should pay ${final}")