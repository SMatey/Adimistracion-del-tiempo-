l_admin={
        "majo": {
            "nombre": "Maria José Solis",
            "numero": "83817491",
            "password": "123"
    },
        "asolisgo": {
            "nombre": "Allan Solis Gonzalez",
            "numero": "86453803",
            "password": "1095"
    }
 } 
usuario = input("Escriba su usuario: ")
contraseña = input("Escriba su contraseña: ")
if usuario in l_admin and contraseña == l_admin[usuario]['password']:
        print("usuario valido, bienvenido")
        print (l_admin[usuario])
else:
        print("usuario o contraseña invalida")

def agregar_registro_administrador(l_admin):
    nuevo_administrador=dict()
    nuevo_administrador['nombre completo']=input ("Nombre completo: ")
    if ("S"==input('Tienes algún número telefónico para registrar? Digita S para Si o N para No:').upper()):
        lista_telefono=[]
        while True:
            lista_telefono.append(input("Número de teléfono: "))
            if ("N"==input('Tienes algún otro número telefónico? Digita S para Si o N para No:').upper()):
                break
        nuevo_administrador['telefono']=lista_telefono
    
    print ("\nAutenticación: ")
    usuario_administrador=input ("\tNombre de usuario: ")
    contraseña_admin=int(input("Digite su contraseña en números"))


    nuevo_administrador["autenticacion"]={
        'usuario':tuple((usuario_administrador)),
        'contraseña': tuple((contraseña_admin))
    }

    l_admin.append(nuevo_administrador)  

    
def menu_principal (l):
    while True:
       
        print("""
                  *********************************************
                  ⏳Bienvenido a su administrador del tiempo⏳
                  *********************************************  
        
        Cuenta usted con algún registro?:

        """)
        print("1) Si")
        print("2) No")
        opt_si_tiene_cuenta=int (input("\n\n\tDijite la opcion: "))
        match opt_si_tiene_cuenta:
          case 1:
                print ("""

                 🕰  Hola, bienvenido de nuevo a tu sistema de administración del tiempo  🕰  
               
                Escoja su tipo de usuario:

                """ )
                print ("1) Administrador ")
                print ("2) Estudiante ")
                print ("3) Salir")

                opt=int (input("\n\n\tDijite el numero correspondiente:  "))

                match opt:
                    case 1:
                        #autenticacion_admin(l)
                        
                        print("""

                        💼 Es usted un administrador, por favor indique la acción que quiere realizar 💼
                        
                        """)
                        print ("1) Modificar un registro ")
                        print ("2) Ver un registro ")
                        opt_administrador=int (input("\n\n\tQué desea: "))
                        match opt_administrador:
                            case 1:
                                agregar_registro_administrador(l)
                           
                
                    
    
             
          case 2:
             print (""" Desea usted registrarse?🤔
             
             """)
             print("1) Si ")
             print("2) No")
             opt_decide_registrar=int (input("\n\n\tQué desea: "))
             match opt_decide_registrar:
                 case 1:
                     print("""Cuál es su tipo de usuario:

                       1) administrador 💼
                       2) estudiante 🎒
                       
                        """)
                     opt_que_es=int(input("\n\n\tDigite su respuesta:  "))
                     match opt_que_es:
                        
                        case 1:    
                             print("""

                                💼 Es usted un administrador, por favor indique la acción que quiere realizar 💼

                                """)  
                             print ("1) Agregar un registro ")
                             print ("2) Ver un registro ")
                             opt_administrador=int (input("\n\n\tQué desea: "))
                             match opt_administrador:
                                    case 1:
                                        agregar_registro_administrador(l)
                                      



      



       