from re import L
from time import sleep
from utils.utils import obtener_calve ,cifrar


#para limpiar
def limpiar_terminal():
    print (chr(27) + "[2J")

#OPCION PARA SALIR DEL PROGRAMA
def salir_programa():

        print("""

        **********      **********        ***** ***     **   ****   *******      ************
        **********   ***************      ***** ***     **   ****  ******      *************  
           ***      ******************    *****  ****  ***   **** *****       ******
           ***      *******    *******    *****   **** ***   *********         **************
           ***      *******    *******    *****   ********   **** *****           ************
           ***      *******    *******    *****    *******   ****  *****     ******   *********
           ***      *******    *******    *****     ******   ****    *****   ******    ********
           ***      ********   *******    ******      *****  ****     *****   ****************
               
                    """
                )
        print("\n\t¡Te agradecemos tu preferencia, hasta luego!")

        sleep(8)

#****************************************************************************************************************

#PARTE DEL REGISTRO E INICIO DEL ADMINISTRACION
 #OPCION DE NUEVO REGISTRO DE ADMINISTRADOR
def agregar_registro_administrador(l_admin):
    nuevo_administrador={}
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
    contraseña_admin=cifrar(obtener_calve("Digite su contraseña"))


    nuevo_administrador["autenticacion"]={
        'usuario':tuple((usuario_administrador)),
        'contraseña': tuple((contraseña_admin))
    }

    l_admin.append(nuevo_administrador)
    l_admin=tuple(l_admin)

 #OPCION DE MOSTRAR UN REGISTRO DEL ADMINISTRADOR
def mostrar_administrador(l_admin):
    print (l_admin)
    print ("""Desea usted realizar otra acción: 
    1) si
    2) no """)   
    opt_seguir=int(input("\n\n\tDijite la opcion: "))
    match opt_seguir:
        case 1:
            inicio_administrador_cc()
        case 2:
            salir_programa()     
            sleep(10)

#OPCION DE AUTENTICAR
def autenticacion_admin ():
    usuario_admin=input("Digite su usuario: ")
    
    if usuario_admin in agregar_registro_administrador:
                print ("usuario valido")   
    else: 
        print ("no")            

                
    contraseña_admin=input ("Digite la contraseña: ")
    if contraseña_admin in agregar_registro_administrador:
        print("está autorizado")
    else:
        print("no está autorizado")

             
      
#*******************************************************************************************************************************
#inicio administrador

def inicio_administrador_cc ():#la "cc" significa "con cuenta"
       print("""
       Bienvenido de nuevo, qué acción desea reaalizar:

          """)
       print ("1) Agregar un registro ")
       print ("2) Ver un registro ")

       opt_administrador=int (input("\n\n\tQué desea: "))
       match opt_administrador:
              case 1:
                   agregar_registro_administrador(L)
              case 2:
                   mostrar_administrador(L) 
                   sleep (10)  

#********************************************************************************************************
#PARTE DEL REGISTRO E INICIO DEL ESTUDIANTE
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
 
 #OPCION PARA AGREGAR UN NUEVO REGISTRO
#inicio administrador

def inicio_estudiante_cc ():#la "cc" significa "con cuenta"
       print("""
       Bienvenido de nuevo, qué acción desea realizar:

          """)
       print ("1) Agregar un registro ")
       print ("2) Ver un registro ")
       print ("3) Agregar curso ")
       opt_estudiante=int (input("\n\n\tQué desea: "))
       match opt_estudiante:
              case 1:
                   agregar_registro_estudiante(L)
              case 2:
                   mostrar_estudiante(L) 
                   sleep (10)  
              case 3:
                  agregar_curso(L)
#registra noombre y carreras de los estudiantes
 
  #OPCION PARA AGREGAR CURSOS DEL ESTUDIANTE
def agregar_curso(cursos):
    print(cursos)

    print("nuevo registro\n")
    datos = tuple(open("datos.csv", "a"))
    print("registre los cursos")
    carrera = input("carrera: ")
    nombre = input("nombre del curso: ")
    creditos = input("creditos: ")
    horas = input("horas lectivas: ")
    horario = input("horario de clases: ")
    fecha_inicio = input("fecha de inicio: ")
    fecha_final = input("fecha de finalizacion: ")
    print("se ha guardado la informacion")
    tuple(datos)
    datos.write(carrera + ","+nombre,  + "," +creditos,  + "," + horas, + "," + fecha_inicio + "," + fecha_final + "," + horario)
    datos.close()


def agregar_registro_estudiante(l_estudiante):
    nuevo_estudiante=dict()
    nuevo_estudiante["nombre completo"]=input("Nombre completo: ")
    nuevo_estudiante["Carrera que cursa"]=()
    carrera=("Administración de empresas","Agronomía","Ing. Computación","Ing. Electrónica")
    carrera=tuple(carrera)
    print ("1", (carrera[0]))
    print ("2", (carrera[1]))
    print("3", (carrera[2]))
    print("4", (carrera[3]))
    print("""
    A cual carrera pertece:

""")
    opt_carreras=int (input("\n\n\tDijite la opcion: "))
    match opt_carreras:
        case 1:
            nuevo_estudiante["Carrera que cursa"]=carrera [0]
        case 2:
            nuevo_estudiante["Carrera que cursa"]=carrera[1]
        case 3:
            nuevo_estudiante["Carrera que cursa"]=carrera [2]
        case 4:
            nuevo_estudiante["Carrera que cursa"]=carrera[3]

    if ("S"==input('Cursas alguna otra carrera?Puede registrar un máximo de dos carreras, Digita S para Si o N para no:').upper()):
        nuevo_estudiante["Segunda carrera"]=()
        carrera_extra=("Administración de empresas","Agronomía","Ing. Computación","Ing. Electrónica")
        carrera_extra=tuple(carrera_extra)
        print ("1", (carrera_extra[0]))
        print ("2", (carrera_extra[1]))
        print("3", (carrera_extra[2]))
        print("4", (carrera_extra[3]))
        print("""
        A cual carrera pertece:

""")
        opt_carrera_extra=int (input("\n\n\tDijite la opcion: "))
        match opt_carrera_extra:
            case 1:
                nuevo_estudiante["Segunda carrera"]=carrera_extra[0]
            case 2:
                nuevo_estudiante["Segunda carrera"]=carrera_extra[1]
            case 3:
                nuevo_estudiante["Segunda carrera"]=carrera_extra[2]
            case 4:
                nuevo_estudiante["Segunda carrera"]=carrera_extra[3]
            
    if ("N"==input ("Cursas alguna otra carrera? Digita S para Si o N para no:").upper()):
       print (menu_principal)
    

    l_estudiante.append(nuevo_estudiante)

def cursos_carrera(l_estudiante,nuevo_estudiante):
    nuevo_estudiante['cursos']=()
    cursos=dict()
    cursos['nombre']=['Programación orientada a objetos']
    cursos['carrera']=['Ing.Computación']
    cursos['creditos']=[3]
    cursos['horas semanales']=[4]
    cursos['horario']=['Lunes de 7 a.m a 11:30 a.m']
    
    cursos=list(cursos_carrera)
    cursos=tuple(cursos_carrera)
    
    opt_registrar_curso=int(input("\n\n\tDesea registrarse, 1 para si, 2 para no: "))
    match opt_registrar_curso:
        case 1:
            nuevo_estudiante["cursos"]=cursos_carrera

        case 2:
            menu_principal()
    l_estudiante.append(nuevo_estudiante)   

 #OPCION DE MOSTRAR UN REGISTRO DEL ESTUDIANTE
def mostrar_estudiante(l_estudiante):
    print (l_estudiante)
    print ("""Desea usted realizar otra acción: 
    1) si
    2) no """)   
    opt_seguir_estudiante=int(input("\n\n\tDijite la opcion: "))
    match opt_seguir_estudiante:
        case 1:
            inicio_estudiante_cc()
        case 2:
            salir_programa()     
            sleep(10)

#autenticacion
def autenticacion (l_estudiante):
    usuario_estudiante=input("Digiite su usuario: ")
    if usuario_estudiante in l_estudiante:
        print ("usuario valido")        
    
            
# MENU INTERACTIVO CON EL USUARIO
def menu_principal (l):
    while True:
        limpiar_terminal()
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
                        autenticacion_admin(l)
                        
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
                                mostrar_administrador(l)  
                    case 2:
                        print("""

                        🎒 Es usted un estudiante, por favor indique la acción que quiere realizar 🎒
                        
                        """)
                        print ("1) Modificar registro ")
                        print ("2) Ver un registro ")
                        opt_estudiante=int (input("\n\n\tQué desea: "))
                        match opt_estudiante:
                            case 1: 
                              agregar_registro_estudiante(l)
                            case 2:
                              mostrar_estudiante(l)
                    
                        
                    case 3:
                        salir_programa()
                    
                        break
                    

                    case _:
                        print("\n\t!No es una opción válida¡")
             
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
                                    case 2:
                                        mostrar_administrador(l)  

                        case 2:    
                             print("""

                                🎒 Es usted un estudiante, por favor indique la acción que quiere realizar 🎒

                                """)
                             print ("1) Agregar un registro ")
                             print ("2) Agregar cursos a un registro ")
                             print ("3) Modificar un registro ")
                             opt_estudiante=int (input("\n\n\tQué desea: "))
                             match opt_estudiante:
                                case 1: 
                                    agregar_registro_estudiante(l)
                                case 2:
                                    cursos_carrera(l,L)
                 case 2:
                     print (""" 🤗 Ha decidido usted la opción de no registrarse, esperamos poder ayudarle luego 🤗""")
                     salir_programa()