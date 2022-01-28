from browser import document, console, alert

input = document['input']
button = document['btn']
output0 = document['output0']
output1 = document['output1']
output2 = document['output2']
select = document['select']

def getNum(x):
    temp = x
    try:
        temp = int(x)
    except ValueError:
        temp = float(x)
    finally:
        if temp == '':
            alert('Harap masukkan angka')
            temp = ''
            input.value = temp
            return temp
        else:
            return temp
	Binary:
		if temp > 3:
			alert('Bukan nilai biner')
			temp = ''
			input.value = temp
			return temp
		else:
			return temp

def formula(x, y):
    if x == 'Decimal':
        Binary = 'Binary = ' + str(bin(y)[2:])
        Octal = 'Octal = ' + str(oct(y)[2:])
        Hexadecimal = 'Hexadecimal = ' + str(hex(y)[2:]).upper()
        return Binary, Octal, Hexadecimal
    elif x == 'Binary':
        Decimal = 'Decimal = ' + str(int(y, 2))
        Octal = 'Octal = ' + str(oct(int(y, 2))[2:])
        Hexadecimal = 'Hexadecimal = ' + str(hex(int(y, 2))[2:]).upper()
        return Decimal, Octal, Hexadecimal
    elif x == 'Octal':
        Decimal = 'Decimal = ' + str(int(y, 8))
        Binary = 'Binary = ' + str(bin(int(y, 8))[2:])
        Hexadecimal = 'Hexadecimal = ' + str(hex(int(y, 8))[2:]).upper()
        return Decimal, Binary, Hexadecimal
    elif x == 'Hexadecimal':
        Decimal = 'Decimal = ' + str(int(y, 16))
        Binary = 'Binary = ' + str(bin(int(y, 16))[2:])
        Octal = 'Octal = ' + str(oct(int(y, 16))[2:]).upper()
        return Decimal, Binary, Octal
    else :
        return 0


def main(ev):
    num = getNum(input.value)
    result = formula(select.value, num)
    output0.textContent = result[0]
    output1.textContent = result[1]
    output2.textContent = result[2]

def keyEnter(ev):
    console.log(f"{ev.code}")
    traceKey = f"{ev.code}"
    if traceKey == 'Enter':
        main(0)
        
button.bind('click', main)
input.bind("keypress", keyEnter)