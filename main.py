import time
print("Welcome to the PizzaPuzza Virtual Order Terminal! Use Code \"20Chez\" for 20% off your order! \n \n")
time.sleep(1.2) # Program will wait 1.2 seconds before asking the user for an input.

#Asks user for their Pizza Type, then checks which it is, then adds it to the subtotal.
PizzaType = str(input("Do you want a Large pizza or Extra Large pizza? (LRG/EX.LRG) \n"))
if PizzaType==str('LRG'):
  SubT = 6
elif PizzaType==str('EX.LRG'):
  SubT = 10
else:
  quit('Unfortunately, we don\'t sell that size here.')
# checks for pizza type, changes SubT or crashes :thumbsup:

TopAMT = int(input('\n How many toppings do you want? (1/2/3/4) \n'))
if TopAMT == 4:
  SubT = SubT + 3.35
elif TopAMT in range(1,4,1):
  SubT = SubT + (TopAMT - 1) * 0.75 + 1
else:
  quit('You silly billy, that\'s not a valid amount!')
# checks topping amount, does math n' shit

Tax = SubT*0.13
# calculates the tax before doing the cupon math n stuff since cupons dont effect tax in pizzapuzza :quepro:

CuponYN = str(input('\n Will you be using a cupon? (Y/N) \n'))
if CuponYN == str('Y'):
  CuponCode = str(input('\n Please enter your Cupon Code. \n'))
  if CuponCode == str('20Chez'):
    SubT = SubT - (SubT * 0.20)
  else:
    print('\n You idiot, I just told you the code. You just missed out on an oppurtunity to save money, just to test the program. You could\'ve saved money on this pizza, but NOOOOOO, you HAD to test this out. Why? Were you curious? Another crappy programmer? I\'m inside your computer, loser. Start running. Now get back to ordering your disgusting pizza with cucumbers on it. You pathetic idiot. \n \n')
elif CuponYN == str('N'):
  print('Alrighty, then. \n')
  time.sleep(0.3)
else:
  print('Dunno what that means, but I guess you won\'t be using a cupon. \n')
  time.sleep(0.3)
# checks for cupons in a very sarcastic way

T = SubT + Tax

if TopAMT == 1:
  print('REVIEW: You ordered a', PizzaType, 'pizza with Cucumbers.')
elif TopAMT == 2:
  print('REVIEW: You ordered a', PizzaType, 'pizza with Cucumbers and Apple slices.')
elif TopAMT == 3:
  print('REVIEW: You ordered a', PizzaType, 'pizza with Cucumbers, Battery acid, and Mustard.')
elif TopAMT == 4:
  print('REVIEW: You ordered a', PizzaType, 'pizza with Cucumbers, Ghost pepper, Blueberry-flavored chapstick, and Garlic oil')
time.sleep(1)
# congratulations, you're on my personal hitlist now. your taste in pizza is repulsive, to say the least.

print('Your subtotal is: $', round(SubT, 2))
time.sleep(0.05)
print('Your tax is: $', round(Tax, 2))
time.sleep(0.05)
print('Your total is: $', round(T, 2))
time.sleep(0.05)
# yummy prices :drool: