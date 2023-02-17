password =  input ('Введите пароль : ')
if len(password) < 7:
    print ("Пароль слишком короткий. ")
elif password[0:8] == "1234567":
    print('Пароль ненадёжный! ')
else:
    print("Пароль подходит. ")
