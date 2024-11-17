

base64Chars = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
               'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
               '0','1','2','3','4','5','6','7','8','9','+','/']

def base64ToBinary(base64):
    return decimalToBinary(base64Chars.index(base64))

def decimalToBinary(decimal):
    int = decimal
    result = ''
    if int >= 32:
        result += '1'
        int -= 32
    else:
        result += '0'
    if int >= 16:
        result += '1'
        int -= 16
    else:
        result += '0'
    if int >= 8:
        result += '1'
        int -= 8
    else:
        result += '0'
    if int >= 4:
        result += '1'
        int -= 4
    else:
        result += '0'
    if int >= 2:
        result += '1'
        int -= 2
    else:
        result += '0'
    if int >= 1:
        result += '1'
        int -= 1
    else:
        result += '0'
    return result

binary = '101101'

def binaryToDecimal(binary):
    total = 0
    for i in range(6):
        if binary[-i-1] == '1':
            total += 2**i
    return total

def binaryToBase64(binary):
    return base64Chars[binaryToDecimal(binary)]


print(binaryToBase64(binary))
print(base64ToBinary('t'))
print(base64Chars[45])

