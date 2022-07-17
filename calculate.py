import sys
if len(sys.argv) != 4:
	print ("Syntax: calculate.py X +-*/ Y") #Або, якщо чесно ("Syntax: calculate.py X +,-,\*,/ Y")
	sys.exit(1)

# Замість функції float  можно використовувати int для отримання цілих чисел
if sys.argv[1].isnumeric() and sys.argv[3].isnumeric():
	if sys.argv[2] == "+":
		print (float(sys.argv[1])+float(sys.argv[3]))
	elif sys.argv[2] == "-":
		print (float(sys.argv[1])-float(sys.argv[3]))
	elif sys.argv[2] == "*": #Дуже цікаіий момент, так і не зміг зробити так, щоб у нас оброблялся символ * з командного рядка без символа екранування :(
#На stackoverflow кажуть що це неможливо:
# https://stackoverflow.com/questions/68935886/multiplication-on-the-command-line-using-argparse
# Дуже хотів би побачити Вашу еталону реалізацію програми calculate.py
		print (float(sys.argv[1])*float(sys.argv[3]))
	elif sys.argv[2] == "/":
		print (float(sys.argv[1])/float(sys.argv[3]))
	else: 
		print ("Use + or - or * or / operator") # ("... or \* or ...")
else:
	print ("Please enter number")
sys.exit(0)
