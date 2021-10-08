username = 'munshikhush2@gmail.com'
password = 'ҌҩҶҴҩҁѱѳѱѴѱѵ'

decrypted = ''
for i in password:
            decrypted = decrypted + chr(ord(i)-(6*5+3)**2)

