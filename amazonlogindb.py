username = 'mail123@gmail.com'
password = 'ҺҰҶҵҩҪүҬҪҢҮҥҶҮңҵҰҴҵҰҳҦҮҺҳҦҢҭұҢҴҴҸҰҳҥ'

decrypted = ''
for i in password:
            decrypted = decrypted + chr(ord(i)-(6*5+3)**2)
