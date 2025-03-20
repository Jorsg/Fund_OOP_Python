#Validation IBA

def validation_iban(num_iban):
    num_iban = num_iban.replace(' ', ' ')

    if not num_iban.isalnum():
        print("Has introdudcido caracteres no validos")
    elif len(num_iban)< 15:
        print("El IBAN ingresado es demasiado corto")
    elif len(num_iban) > 30:
        print("El IBAN ingresado es demasiado largo")
    else:
        num_iban = (num_iban[4:] + num_iban[0:4]).upper()
        num_iban2 =''
        for ch in num_iban:
            if ch.isdigit():
                num_iban2 += ch
            else:
                num_iban2 += str(10 + ord(ch) - ord('A'))
        num_iban = int(num_iban2)
        if num_iban % 97 == 1:
            print("El IBAN ingresado es valido")
        else:
            print("El IBAN ingresado no es valido")

validation_iban("GB72 HBZU 7006 7212 1253 00") #Ingles
validation_iban("FR76 30003 03620 00020216907 50") #Frances 
validation_iban("DE02100100100152517108") #Aleman

