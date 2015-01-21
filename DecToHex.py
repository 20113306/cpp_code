__author__ = 'Sungsu'

def DecToHex():
	try:
		num = input("Enter the Decimal Number : ")
	except:
		print("Enter the Number not String or Character")
		DecToHex()
	else:
		temp  = str(hex(num))
		result = temp.split('x')
		print(result[1].upper())

DecToHex() 
