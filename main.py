#Isaac Bissonette
#10/11/24

#Input block

length = float(input('Enter your room length in feet: '))
width = float(input('Enter your room width in feet: '))
price_per_sq_yard = float(input('Enter the price per square foot ($2.00 - $4.50): '))

#Variable block

SALES_TAX = float(6.00)
square_feet = length * width
square_yards = float(square_feet / 9)

#Total block

subtotal = square_yards * price_per_sq_yard
total = subtotal + SALES_TAX

#Finishing statement

print(f'you need {square_yards:.2f} of carpet')
print()
print(f'The order subtotal is ${subtotal:.2f}.')
print()
print(f'The state sales tax is ${SALES_TAX}.')
print()
print(f'The grand total is ${total:.2f}')
print()

#Cause why not

if total >=1000:
    print('How can you even afford this?')
