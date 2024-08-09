# write a program that will calculate simple interest I = PRT/100
print("This program calculates simple interest")
principal = float(input("Type the principal: "))
rate = float(input("Type the rate e.g 5 for 5%, 20 for 20% etc.: "))
time = int(input("Type the numbers year for the loan: "))

simple_interest = (principal * rate * time) / 100
print("The simple interest is " + str(simple_interest))
paying = simple_interest + principal
print("This means you are paying " + str(paying) + " after " + str(time) + " years." )