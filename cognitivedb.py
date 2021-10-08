username = 'munshikhush234@gmail.com'
password = 'ҍҢҭҢңҢңҶҁѳ'

decrypted = ''
for i in password:
            decrypted = decrypted + chr(ord(i)-(6*5+3)**2)