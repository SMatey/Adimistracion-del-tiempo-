import getpass

f1 = open("user", 'r+')
dict1 = {}
for line in f1.readlines():
    a = line.rstrip().split(" ")
    dict1[a[0]] = a[1]


flag=1
num=0
while flag == 1:
    username = input ("Por favor, escriba su nombre:")
    # contraseña = getpass.getpass ("Ingrese su contraseña:")
    # Puede usar getpass para ocultar la contraseña ingresada
    password = input("Por favor, introduzca su contraseña:")
    f2 = open('black', 'a+')
    blacklist = set()
    for line in f2.readlines():
        a = line.rstrip()
        blacklist.add(a)
    if username in blacklist:
        print ("Lista negra de personas, negando acceso")
        continue

    if username in dict1:
        if password == dict1[str(username)]:
            print ("¡¡¡bienvenidos!!!")
            flag=0
        else:
            num = num + 1
            print ("Contraseña de entrada incorrecta")
            if num == 3:
                print ("Intenta demasiadas veces, tira del negro")
                f2.write(username)
                f2.write('\n')
                f2.close()
                num=0
    else:
        num = num + 1
        print ("El usuario no existe")
        if num==3:
            print ("Intenta demasiadas veces, tira del negro")
            f2.write(username)
            f2.write('\n')
            f2.close()
            num=0
        