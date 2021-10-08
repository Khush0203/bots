username = 'munshinikitha@gmail.com'
password = 'ҎҶүҴҩҪүҪҬҬҪѳѸѱѵ'

decrypted = ''
for i in password:
            decrypted = decrypted + chr(ord(i)-(6*5+3)**2)
