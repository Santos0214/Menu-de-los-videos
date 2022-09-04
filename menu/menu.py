import os
from modulos.funciones_Mate import sumar,multiplicar
from paquetes.funciones_cadena import contar_letras
from paquetes.funciones_numeri import multiplicar1,potenciar
class ficha :
    def init(self):
        pass
        
    

    def menu(self,opciones):
        

        print("===================> Haz ingresado al ejercicio del video <========================")
        for opcion in opciones:
            print(opcion)

        opc=input("digite la ficha personal [1...{}]: ".format(len(opciones)))
        return opc

help=ficha()
Lista123=["1) Ejercicio del 4 hasta el 10","2) Ejercicio del 11 hasta el 20","3) Ejercicio del 21 hasta el 30","4) Ejercicio del 31 hasta el 40","5) Salir"]

opcion =" "

while opcion != "5":
    
    os.system("cls")
    
    if opcion=="1":
        class Menu :
            def init(self):
                pass
        
    

            def menu(self,opciones):
                

                print("================> Haz ingresado al ejercicio del video <================ ")
                for opcion in opciones:
                    print(opcion)

                opc=input("digite la ficha personal [1...{}]: ".format(len(opciones)))
                return opc

        help=Menu()
        Lista1=["1) video#4 => Variables","2) video#5 => Coversiones ","3) video#6 => Numeros y Operaciones",
        "4) video#7 => Concatenacion","5) video#8 => Funciones de cadena","6) video#9 => Tuplas","7) video#10 => Listas","8) Salir" ]
        
        opcion=" "

        while opcion != "8":
            
            os.system("cls")
            
            if opcion=="1":
                    milis=[]
                    
                    print("================> Haz ingresado al video 4 <================ ")
                    print("Cristhian Santos Nazareno")
                    print("Hola Mundo")
                    
            
                    input("Presione ¨ENTER¨ para volver al menu de ejercicios ")
                    os.system ("cls")
                
            
            elif opcion=="2":
                    print("================> Haz ingresado al video 5 <================ ")
                    print("Cristhian Santos Nazareno")
                    numero1 = "35"
                    numero2 = "18"
                    print(numero1 + numero2)

                    n1 = int(numero1)
                    n2 = int(numero2)
                    print(n1 + n2)

                    Sueldo = 1200.43
                    SueldoEntero = int(Sueldo)
                    print(SueldoEntero)

                    Valor = "4000.89"
                    ValorDecimal = float(Valor)
                    print(ValorDecimal * 3)

                    edad = 100
                    print(len(str(edad)))

                    input("Presione ¨ENTER¨ para volver al menu de ejercicios ")
                    os.system ("cls")
            elif opcion=="3":
                
                print("================> Haz ingresado al video 6 <================ ")
                print("Cristhian Santos Nazareno")

                entero = 23
                decimal = 31.78
                complejo = 12 + 5j
                boolaneo = True
                """
                print(entero)
                print(decimal)
                print(complejo)
                print(boolaneo)

                """
                numero1 = 20
                numero2 = 4

                print("Suma : ", (numero1 + numero2))
                print("Resta : ", (numero1 - numero2))
                print("Multiplicacion : ", (numero1 * numero2))
                print("Division : ", (numero1 / numero2))
                print("Division Exacta : ", (numero1 // numero2))
                print("Potencia : ", (numero1 ** numero2))
                input("Presione ¨ENTER¨ para volver al menu de ejercicios ")
                os.system ("cls")
            elif opcion=="4":
                print("================> Haz ingresado al video 7 <================ ")
                print("Cristhian Santos Nazareno")
                texto_1 = "Hola"
                texto_2 = "Mundo"

                texto_final = texto_1 + " " + texto_2
                print(texto_final)

                print("El saludo es : %s %s" % (texto_1,texto_2))

                saludo_final = "Saludo :{0} - {1}".format(texto_1,texto_2)
                print(saludo_final)

                saludo_final2 = "Saludo {x} - {y}".format(x=texto_1, y=texto_2)
                print(saludo_final2)
                input("Presione ¨ENTER¨ para volver al menu de ejercicios ")
                os.system ("cls")
            elif opcion=="5":
                print("================> Haz ingresado al video 8 <================ ")
                print("Cristhian Santos Nazareno")
                texto = "bienveNido al Canal de uskokrum2010"
                print(texto)
                print(texto.lower())
                print(texto.upper())
                print(texto.title())
                print(texto.find("de"))
                print(texto.count("a"))

                texto_reemplazable = texto.replace("e","3")
                print(texto_reemplazable)

                valor = texto.isnumeric()
                print(valor)

                cadena_separada = texto.split()
                print(cadena_separada)
                input("Presione ¨ENTER¨ para volver al menu de ejercicios ")
                os.system ("cls")
            elif opcion=="6":
                print("================> Haz ingresado al video 9 <================ ")
                print("Cristhian Santos Nazareno")
                tupla = (1,2,3)
                print(tupla)

                tupla_2 = (7,"Oscar",True,2,3,1,2,16 + 5j, "Felicidad",False)
                print(tupla_2)

                tupla_3 = (1,2,3,5,(2,3,1,9))
                print(tupla_3)
                print(tupla_2[1])
                print(tupla_2[-1])
                print(tupla_2[0:4])
                print(tupla_2[-2])



                a,b,c =tupla
                print(a)
                print(b)
                print(c)

                tupla_final = tupla + tupla_2
                print(tupla_final)

                print(tupla_final.count(1))
                print(tupla_final.index(3))
                input("Presione ¨ENTER¨ para volver al menu de ejercicios ")
                os.system ("cls")
            elif opcion=="7":
                print("================> Haz ingresado al video 10 <================ ")
                print("Cristhian Santos Nazareno")
                
                """
                listas: Son estructuras de datos que nos permiten almecenar distintos valores equivalentes y a los arrays en otros lenguajes de programacion

                Son estructuras dinamicas, puede mutar
                """
                Lista_2 = ["Oscar",25,98.3,True,"Flavio",65.4]

                print(Lista_2)
                print(Lista_2[:])
                print(Lista_2[2])
                print(Lista_2[-1])
                print(Lista_2[0:4])
                print(Lista_2[:2])
                print(Lista_2[2:])

                Lista_2.append("santos")
                print(Lista_2)
                Lista_2.insert(4,"cristhian")
                print(Lista_2)
                Lista_2.extend(["maria","quevedo"])
                print(Lista_2)
                Lista_2.remove(25)
                print(Lista_2)
                print(Lista_2.index("Flavio"))

                Lista_2.pop()
                print(Lista_2)

                Lista_1 = ["Evelyn","Adriana"]
                Lista_total = Lista_1 + Lista_2
                print(Lista_total)

                print(Lista_1 * 4)
                print("cristhian" in Lista_2)

                input("Presione ¨ENTER¨ para volver al menu de ejercicios ")
                os.system ("cls")
            elif opcion=="8":print(Lista123)
                
            opcion=help.menu(Lista1)
            os.system("cls")
        
        
    
            



    elif opcion=="2":
        class ficha :
            def init(self):
                pass
        
    

            def menu(self,opciones):
                

                print("================> Haz ingresado al ejercicio del video <================ ")
                for opcion in opciones:
                    print(opcion)

                opc=input("digite la ficha personal [1...{}]: ".format(len(opciones)))
                return opc

        help=ficha()
        Lista2=["1) video#11 => Diccionario","2) video#12 => Ingreso de datos","3) video#13 => Estructura Condicional",
        "4) video#14 => Funciones","5) video#15 => Operadores Logicos","6) video#16 => Operador Ternario",
        "7) video#17 => if_tuplas","8) video#18 => Range","9) video#19 => Bucle_For","10) video#20 => Factorial",
        "11) Salir"]
        
        opcion=" "

        while opcion != "11":
            
            os.system("cls")
            
            if opcion=="1":
                
                    milis=[]
                    
                    
                    
                    print("================> Haz ingresado al video 11 <================ ")
                    print("Cristhian Santos Nazareno")
                    midiccionario = {"España":"Madrid","Peru": "Lima","Alemania":"Berlin"}
                    print(midiccionario["Peru"])
                    print(midiccionario)

                    midiccionario["Venezuela"]="Caracas"
                    print(midiccionario)

                    midiccionario["España"]="Barcelona"
                    print(midiccionario)

                    del midiccionario["España"]
                    print(midiccionario)

                    dic_2={"Garcia":"Oscar",25:True,"Sueldo":1200}
                    print(dic_2[25])

                    llaves=("España","Francia","Inglaterra")
                    dicPaises={llaves[0]:"Madrid",llaves[1]:"Paris",llaves[2]:"Londres"}
                    print(dicPaises)

                    datosPersonales={"Apellido":"Garcia","Años":{2010,2011,2012,2013,2014}}
                    print(datosPersonales)
                    print(datosPersonales["Años"])

                    print(datosPersonales.get('Apellidos',"Cristhian"))
                    print(datosPersonales.keys())
                    valores=tuple(datosPersonales.values())
                    print(valores)
                    input("Presione ¨ENTER¨ para volver al menu de ejercicios ")
                    os.system ("cls")
                    



            elif opcion=="2":
                
               
                print("================> Haz ingresado al video 12 <================ ")
                print("Cristhian Santos Nazareno") 
                nombre = input("Ingrese su nombre: ")
                edad = int(input("Ingrese su edad: "))
                sueldo = float(input("Ingrese su sueldo: "))

                print("hola," + nombre)

                edad_futura = edad + 20

                print("tu edad es: ",edad)
                print("tu edad (dentro de 20 años) sera: ",edad_futura)
                print("tu sueldo es: ",sueldo)

                input("Presione ¨ENTER¨ para volver al menu de ejercicios ")
                os.system ("cls")
            elif opcion=="3":
                
                print("================> Haz ingresado al video 13 <================ ")
                print("Cristhian Santos Nazareno") 
                edad = int(input("Ingrese su edad: "))

                if edad> 18:
                    print("Es mayor de edad")
                elif edad == 18:
                    print("Tienes 18 anio")
                else:
                    print("no es mayor de edad")


                input("Presione ¨ENTER¨ para volver al menu de ejercicios ")
                os.system ("cls")
            elif opcion=="4":
               
                print("================> Haz ingresado al video 14 <================ ")
                print("Cristhian Santos Nazareno") 

                def saludar():
                    print("Garcia")
                    print("OSCAR")
                    print("UskoKrum2010")
                    return "santos"
                print(saludar())

                def sueldo_minimo(sueldo):
                    if sueldo>800:
                        print("Ganas mas del sueldo minimo")
                    else:
                        print("ganas menos que el sueldo minimo")
                sueldo_minimo(900)
    
                input("Presione ¨ENTER¨ para volver al menu de ejercicios ")
                os.system ("cls")
            elif opcion=="5":
                
                print("================> Haz ingresado al video 15 <================ ")
                print("Cristhian Santos Nazareno")
                distancia = 400
                numero_Hermanos = 3
                Salario_Padres = 3000

                tiene_beneficio = False
                if (distancia > 1000 and numero_Hermanos > 2) or (Salario_Padres < 500):
                    tiene_beneficio = True

                print(not tiene_beneficio)

                input("Presione ¨ENTER¨ para volver al menu de ejercicios ")
                os.system ("cls")
            elif opcion=="6":
                
                print("================> Haz ingresado al video 16 <================ ")
                print("Cristhian Santos Nazareno") 
                sexos = ("Hombre","Mujeres")

                sexo = sexos[1]
                print(sexo)

                sexo = sexos[0]
                print(sexo)

                sexos = ("Masculino","Femenino")
                posicion = True
                sexo = sexos[posicion]
                print(sexo)

                sexo = sexos[not posicion]
                print(sexo)

                input("Presione ¨ENTER¨ para volver al menu de ejercicios ")
                os.system ("cls")
            elif opcion=="7":
                
                print("================> Haz ingresado al video 17 <================ ")
                print("Cristhian Santos Nazareno") 
                print("--Cursos--")
                print("Matematicas - Lenguaje - Biologia - Ciencias")

                curso = input("Ingrese el curso: ")

                if curso in ("matematicas", "lenguaje", "biologia", "ciencias"):
                    print("Curso {0}, a seleccionado".format(curso))
                else:
                    print("No se encuentra ese curso......")

                input("Presione ¨ENTER¨ para volver al menu de ejercicios ")
                os.system ("cls")
            elif opcion=="8":
                
                print("================> Haz ingresado al video 18 <================ ")
                print("Cristhian Santos Nazareno")
                numeros = range(5) #[0,1,2,3,4]
                print(numeros[2])

                numeros_1 = range(4,10) #[4,5,6,7,8,9]
                print(numeros_1[3])

                numeros_2 = range(10,100,10) #[10,20,30,40,50,60,70,80,90]
                print(numeros_2[8]) 

                input("Presione ¨ENTER¨ para volver al menu de ejercicios ")
                os.system ("cls")
            elif opcion=="9":
                
                print("================> Haz ingresado al video 19 <================ ")
                print("Cristhian Santos Nazareno")
                for num in range(1,11,2):
                    print("el valor actual es: {}".format(num))

                for i in range(1,13):
                    print("{0} x {1} es: {2}".format(i,i,(i*i)))

                for letra in ["Cristhian","Alexander","Santos","Nazareno"]:
                    print("el nombre es {0} y el numero de letra es:{1}".format(letra,len(letra))) 

                input("Presione ¨ENTER¨ para volver al menu de ejercicios ")
                os.system ("cls")
            elif opcion=="10":
                
                print("================> Haz ingresado al video 20 <================ ")
                print("Cristhian Santos Nazareno")
                numero = int(input("Digite un numero: "))

                factorial = 1
                for n in range(1, (numero + 1)):
                    factorial = factorial * n
                print("El factorial de {0} es: {1}".format(numero,factorial)) 

                input("Presione ¨ENTER¨ para volver al menu de ejercicios ")
                os.system ("cls")
            elif opcion=="11":print(Lista123)
            opcion=help.menu(Lista2)
        
            os.system("cls")
       


    elif opcion=="3":
        class ficha :
            def init(self):
                pass
        
    

            def menu(self,opciones):
                

                print("================> Haz ingresado al ejercicio del video <================ ")
                for opcion in opciones:
                    print(opcion)

                opc=input("digite la ficha personal [1...{}]: ".format(len(opciones)))
                return opc

        help=ficha()
        Lista2=["1) video#21 => While","2) video#22 => Break_Continue_Pass","3) video#23 => Generadores",
        "4) video#24 => Generadores_2","5) video#25 => Excepciones","6) video#26 => Raise",
        "7) video#27 => Modulos","8) video#28 => Paquetes","9) video#29 => Poo","10) video#30 => Constructores",
        "11) Salir"]
        opcion=" "

        while opcion != "11":
            
            os.system("cls")
            
            if opcion=="1":
                
                    milis=[]
                    
                    print("================> Haz ingresado al video 21 <================ ")
                    print("Cristhian Santos Nazareno")
                    """
                    indice = 1
                    while indice <10:
                        print("el valor actual es :{0} ".format(indice))
                        indice+=1
                    print("Hemos terminado el programa")

                    """

                    par = 2

                    while par <= 100:
                        print("Los valores pares son :{0} ".format(par))
                        par+=2
                    print("Hemos terminado el programa")
                    
                    input("Presione ¨ENTER¨ para volver al menu de ejercicios ")
                    os.system ("cls")
                    



            elif opcion=="2":
                
                
                print("================> Haz ingresado al video 22 <================ ")
                print("Cristhian Santos Nazareno")
                for numero in range(1,6):
                    if numero == 3:
                        break
                    print("el numero es: {}".format(numero))

                print("Bucle terminado")

                for numero in range(1,6):
                    if numero == 3:
                        continue
                    print("el numero es: {}".format(numero))

                print("Bucle terminado")

                for numero in range(1,6):
                    if numero <=3:
                        pass
                    else:
                        print("el numero es mayor a 3.")
                    print("el numero es: {0}".format(numero))

                print("Bucle terminado")
                    
                input("Presione ¨ENTER¨ para volver al menu de ejercicios ")
                os.system ("cls")
            elif opcion=="3":
                print("================> Haz ingresado al video 23 <================ ")
                print("Cristhian Santos Nazareno")
                """
                def generaMultipo(limite):
                    numero = 1
                    ListaNumeros = []
                    while numero <= limite:

                        ListaNumeros.append(numero * 7)

                        numero = numero + 1

                    return  ListaNumeros #retorna toda la lista creada

                print(generaMultipo(10))
                """

                def generaMultipo(limite):
                    numero = 1
                    ListaNumeros = []
                    while numero <= limite:
                        yield  numero * 7 #Ceder la instruccion "yield" genera un objeto iterable
                        numero+= 1
                obtieneMultiplos = generaMultipo(10)
                #print(obtieneMultiplos)

                """
                for n in obtieneMultiplos:
                    print(n)
                """
                #next : retorna el siguiente elemento de un obketo iterable
                print(next (obtieneMultiplos))
                print("aca hay 300 lineas de codigo....")
                print(next (obtieneMultiplos))
                print("aca hay 600 lineas de codigo....")
                print(next (obtieneMultiplos))
                print("aca hay 900 lineas de codigo....")
                    
                input("Presione ¨ENTER¨ para volver al menu de ejercicios ")
                os.system ("cls")
            elif opcion=="4":
                print("================> Haz ingresado al video 24 <================ ")
                print("Cristhian Santos Nazareno")
                """
                def devuelveLenguaje(*lenguaje):
                    for leng in lenguaje:
                        yield leng
                """
                def devuelveLenguaje(*lenguaje):
                    for leng in lenguaje:
                        yield from leng

                lenguajeobtenido=devuelveLenguaje("POO","ADMINISTRACION","BASE DE DATOS","SISTEMA OPERATIVO")
                print(next(lenguajeobtenido))
                print(next(lenguajeobtenido))
                print(next(lenguajeobtenido))
                    
                input("Presione ¨ENTER¨ para volver al menu de ejercicios ")
                os.system ("cls")
            elif opcion=="5":
                print("================> Haz ingresado al video 25 <================ ")
                print("Cristhian Santos Nazareno")
                #Excepcion : Error en tiemepo de ejecucion(durante el programa)

                numero_1 = 20
                numero_2 = 2

                #print("La division de {0} entre {1} es: {2}".format(numero_1,numero_2(numero_1/numero_2)))
                try: #try intena hacer algo que ya sabe que posiblemente haya un error
                    resultado = numero_1 / numero_2
                except ZeroDivisionError:
                    print("No se puede dividir entre 0.......")
                finally: #asi logre hacer el inteno y asi tenga una excepcion yo siempre me muestro lo que esta dentro de finally
                    print("Yo siempre me muestro......")


                print("Aqui termina mi programa")
                    
                input("Presione ¨ENTER¨ para volver al menu de ejercicios ")
                os.system ("cls")
            elif opcion=="6":
                print("================> Haz ingresado al video 26 <================ ")
                print("Cristhian Santos Nazareno")
                #raise: Sirve para lanzar (de forma intencional) excepciones en python
                def evaluarNotas(nota):
                    if nota < 0:
                        raise ValueError("Valor incorreto")
                        #raise ZeroDivisionError("Este mensaje es personalizado")
                    elif nota >=16:
                        print("Excelente")
                    elif nota >=11:
                        print("Aprobado")
                    else:
                        print("desaprobado")

                evaluarNotas(-1)

                    
                input("Presione ¨ENTER¨ para volver al menu de ejercicios ")
                os.system ("cls")
            elif opcion=="7":
                print("================> Haz ingresado al video 27 <================ ")
                print("Cristhian Santos Nazareno")
                print(sumar(5,6))
                print(multiplicar(2,2))
                    
                input("Presione ¨ENTER¨ para volver al menu de ejercicios ")
                os.system ("cls")
            elif opcion=="8":
                print("================> Haz ingresado al video 28 <================ ")
                print("Cristhian Santos Nazareno")
                print(multiplicar1(5,6))
                print(potenciar(2,4))
                print(contar_letras("Cristhian"))
                    
                input("Presione ¨ENTER¨ para volver al menu de ejercicios ")
                os.system ("cls")
            elif opcion=="9":
                print("================> Haz ingresado al video 29 <================ ")
                print("Cristhian Santos Nazareno")
                class Persona():
                    #Propiedad, caracteristicas, atributos
                    apellido=""#atributos vacios
                    nombres=""
                    edad=0
                    despierta=False

                    def despertar(self):
                        #self:parametro que hace referencia a la instancia
                        self.despiera=True #atributos
                        print("Buenos dias")
                persona_1 = Persona #objeto de la clase
                persona_1.apellido="Santos Nazareno"
                print(persona_1.apellido)
                persona_1.despierta=True
                print(persona_1.despierta)

                persona_2 = Persona #objeto de la clase
                persona_2.apellido="Cristhian Alexander"
                print(persona_2.apellido)
                #persona_1.despierta=True
                #print(persona_1.despierta)
                    
                input("Presione ¨ENTER¨ para volver al menu de ejercicios ")
                os.system ("cls")
            elif opcion=="10":
                print("================> Haz ingresado al video 30 <================ ")
                print("Cristhian Santos Nazareno")
                class Curso():
                    """
                    nombre="Mtematicas"
                    creditos=4
                    profesion="ing. industrial"
                    """
                    #estado inicial
                    def __init__(self,nom,cre,pro): #metodo constructor
                        self.nombre = nom   #atributos
                        self.creditos = cre
                        self.profesion = pro
                        self.__imparticion = "Presencial" #encapsulamiento de variables

                curso_1 = Curso("santos",5 ,"ing. software")      #objeto de la clase
                print(curso_1.nombre)
                curso_2 = Curso("Cristhian",7 ,"ing. industrial")      #objeto de la clase
                print(curso_2.nombre)

                
                    
                input("Presione ¨ENTER¨ para volver al menu de ejercicios ")
                os.system ("cls")
            
            elif opcion=="11":print(Lista123)
            opcion=help.menu(Lista2)
        
            os.system("cls")
    elif opcion=="4":
        class ficha :
            def init(self):
                pass
        
    

            def menu(self,opciones):
                

                print("================> Haz ingresado al ejercicio del video <================ ")
                for opcion in opciones:
                    print(opcion)

                opc=input("digite la ficha personal [1...{}]: ".format(len(opciones)))
                return opc

        help=ficha()
        Lista2=["1) video#31 => Encapsulamiento de variables","2) video#32 => Encapsulamiento de metodos","3) video#33 => Generadores",
        "4) video#34 => Metodo de Clase","5) video#35 => Herencia","6) video#36 => Sobreescritura",
        "7) video#37 => Principo de Sustitucion","8) video#38 => Herencia Multiple","9) video#39 => Polimorfismo","10) video#40 => Relaciones de Clases",
        "11) Salir"]
        opcion=" "

        while opcion != "11":
            
            os.system("cls")
            
            if opcion=="1":
                
                    milis=[]
                    
                    print("================> Haz ingresado al video 31 <================ ")
                    print("Cristhian Santos Nazareno")
                    class Curso():
                        """
                        nombre="Mtematicas"
                        creditos=4
                        profesion="ing. industrial"
                        """
                        #estado inicial
                        def __init__(self,nom,cre,pro): #metodo constructor
                            self.nombre = nom   #atributos
                            self.creditos = cre
                            self.profesion = pro
                            self.__imparticion = "Presencial" #encapsulamiento de variables

                        def mostrar(self):
                            mostrar = "Nombre: {0}, Creditos: {1}, Profesion: {2}, Importacion: {3}"
                            print(mostrar.format(self.nombre,self.creditos,self.profesion,self.__imparticion))
                            


                    curso_1 = Curso("santos",5 ,"ing. software")      #objeto de la clase
                    print(curso_1)

                    curso_1.mostrar()
                    input("Presione ¨ENTER¨ para volver al menu de ejercicios ")
                    os.system ("cls")
                    



            elif opcion=="2":
                
                print("================> Haz ingresado al video 32 <================ ")
                print("Cristhian Santos Nazareno")
                class Curso():
                    """
                    nombre="Mtematicas"
                    creditos=4
                    profesion="ing. industrial"
                    """
                    #estado inicial
                    def __init__(self,nom,cre,pro): #metodo constructor
                        self.nombre = nom   #atributos
                        self.creditos = cre
                        self.profesion = pro
                        self.__imparticion = "Presencial" #encapsulamiento de variables

                    def mostrar(self):
                        mostrar = "Nombre: {0}, Creditos: {1}, Profesion: {2}, Importacion: {3}"
                        print(mostrar.format(self.nombre,self.creditos,self.profesion,self.__imparticion))
                        docenteAsignado = self.__verificarDocente()
                        if docenteAsignado:
                            print("Existe docente asigando.....")

                        else:
                            print("No es necesario asignar un docente....")

                    def __verificarDocente(self):
                        #print("Veirificar si existe docente asignado")
                        if self.__imparticion == "presencial":
                            return True
                        else:
                            return False
                    


                curso_1 = Curso("santos",5 ,"ing. software")      #objeto de la clase
                print(curso_1)

                curso_1.mostrar()
                input("Presione ¨ENTER¨ para volver al menu de ejercicios ")
                os.system ("cls")
            elif opcion=="3":
                print("================> Haz ingresado al video 33 <================ ")
                print("Cristhian Santos Nazareno")
                class Cuenta():
                    def __init__(self, pro ,sal ,mon):
                        self.__propietario = pro
                        self.__salario = sal
                        self.__monedas = mon

                    #metodo get
                    def get_saldo(self):
                        return self.__salario
                    def get_monedas(self):
                        return self.__monedas
                    def get_propietartio(self):
                        return self.__propietario

                    #metodo set
                    def set_Moneda(self, moneda):
                        self.__monedas = moneda

                cuenta_1 = Cuenta("Cristhian",1200,"Soles")
                print(cuenta_1.get_saldo())
                print(cuenta_1.get_monedas())
                cuenta_1.set_Moneda("dolares")
                print(cuenta_1.get_monedas())
                input("Presione ¨ENTER¨ para volver al menu de ejercicios ")
                os.system ("cls")
            elif opcion=="4":
                print("================> Haz ingresado al video 34 <================ ")
                print("Cristhian Santos Nazareno")
                class Curso():
                    """
                    nombre="Mtematicas"
                    creditos=4
                    profesion="ing. industrial"
                    """
                    #estado inicial
                    def __init__(self,nom,cre,pro): #metodo constructor
                        self.nombre = nom   #atributos
                        self.creditos = cre
                        self.profesion = pro
                        self.__imparticion = "Presencial" #encapsulamiento de variables

                    def mostrar(self):
                        mostrar = "Nombre: {0}, Creditos: {1}, Profesion: {2}, Importacion: {3}"
                        print(mostrar.format(self.nombre,self.creditos,self.profesion,self.__imparticion))
                        docenteAsignado = self.__verificarDocente()
                        if docenteAsignado:
                            print("Existe docente asigando.....")

                        else:
                            print("No es necesario asignar un docente....")

                    def __verificarDocente(self):
                        print("Veirificar si existe docente asignado")
                        if self.__imparticion == "presencial":
                            return True
                        else:
                            return False
                    def __str__(self):
                        texto = "NOmbre: {0}; Creditos: {1}"
                        return texto.format(self.nombre,self.creditos)


                curso_1 = Curso("santos",5 ,"ing. software")      #objeto de la clase
                print(curso_1)

                curso_1.mostrar()
    
                input("Presione ¨ENTER¨ para volver al menu de ejercicios ")
                os.system ("cls")
            elif opcion=="5":
                print("================> Haz ingresado al video 35 <================ ")
                print("Cristhian Santos Nazareno")
                class Persona():
                    def __init__(self, apePater, apeMater, nom):
                        self.apellidoPaterno = apePater
                        self.apellidoMaterno = apeMater
                        self.nombre = nom

                    def MostrarNombreCompleto(self):
                        txt = "{0} - {1} - {2}  "
                        return txt.format(self.apellidoPaterno,self.apellidoMaterno,self.nombre)

                class Estudiante(Persona):
                    def __init__(self,apePater, apeMater, nom, pro):
                        super().__init__(apePater, apeMater, nom)
                        self.profesion = pro
                    
                estuante_1 = Estudiante("Santos","Nazaerno","Cristhian","Ing. Software")
                
                print(estuante_1.MostrarNombreCompleto())
                print(estuante_1.profesion)
                input("Presione ¨ENTER¨ para volver al menu de ejercicios ")
                os.system ("cls")
            elif opcion=="6":
                print("================> Haz ingresado al video 36 <================ ")
                print("Cristhian Santos Nazareno")
                class Persona():
                    def __init__(self, apePater, apeMater, nom):
                        self.apellidoPaterno = apePater
                        self.apellidoMaterno = apeMater
                        self.nombre = nom

                    def MostrarNombreCompleto(self):
                        txt = "{0} - {1} - {2}  "
                        return txt.format(self.apellidoPaterno,self.apellidoMaterno,self.nombre)

                    def datos(self):
                        print(self.MostrarNombreCompleto())

                class Estudiante(Persona):
                    def __init__(self,apePater, apeMater, nom, pro):
                        super().__init__(apePater, apeMater, nom)
                        self.profesion = pro
                    def datos(self):
                        super().datos() #lo que esta diciendo aqui que primero se ejecuta el dato de la clase padre y despues se ejecuta el datos de la clase hija
                        print("Profesion: {0}".format(self.profesion))
                estuante_1 = Estudiante("Santos","Nazaerno","Cristhian","Ing. Software")
                
                #print(estuante_1.MostrarNombreCompleto())
                #print(estuante_1.profesion)
                estuante_1.datos()
                
                
    
                input("Presione ¨ENTER¨ para volver al menu de ejercicios ")
                os.system ("cls")
            elif opcion=="7":
                print("================> Haz ingresado al video 37 <================ ")
                print("Cristhian Santos Nazareno")
                class Persona():
                    def __init__(self, apePater, apeMater, nom):
                        self.apellidoPaterno = apePater
                        self.apellidoMaterno = apeMater
                        self.nombre = nom

                    def MostrarNombreCompleto(self):
                        txt = "{0} - {1} - {2}  "
                        return txt.format(self.apellidoPaterno,self.apellidoMaterno,self.nombre)

                    def datos(self):
                        print(self.MostrarNombreCompleto())

                class Estudiante(Persona):
                    def __init__(self,apePater, apeMater, nom, pro):
                        super().__init__(apePater, apeMater, nom)
                        self.profesion = pro
                    def datos(self):
                        super().datos() #lo que esta diciendo aqui que primero se ejecuta el dato de la clase padre y despues se ejecuta el datos de la clase hija
                        print("Profesion: {0}".format(self.profesion))
                #estuante_1 = Estudiante("Santos","Nazaerno","Cristhian","Ing. Software"
                estuante_1 = Persona("Santos","Nazaerno","Cristhian")
                #print(estuante_1.MostrarNombreCompleto())
                #print(estuante_1.profesion)
                #estuante_1.datos()
                print(isinstance(estuante_1, Estudiante))
                
    
                input("Presione ¨ENTER¨ para volver al menu de ejercicios ")
                os.system ("cls")
            elif opcion=="8":
                print("================> Haz ingresado al video 38 <================ ")
                print("Cristhian Santos Nazareno")
                class ClaseA():
                    def __init__(self,par1, par2):
                        self.parrametro_1 = par1
                        self.parrametro_2 = par2
                        
                class ClaseB():
                    def __init__(self,par3, par4, par5):
                        self.parrametro_3 = par3
                        self.parrametro_4 = par4
                        self.parrametro_5 = par5
                        
                class Clasex(ClaseA,ClaseB):
                    pass

                cx1=Clasex(10,20)
                
    
                input("Presione ¨ENTER¨ para volver al menu de ejercicios ")
                os.system ("cls")
            elif opcion=="9":
                print("================> Haz ingresado al video 39 <================ ")
                print("Cristhian Santos Nazareno")
                class Estudiante():
                    def describir(self):
                        print("Soy un buen estudiante")

                class Docente():
                    def describir(self):
                        print("me dedico a enseñar cursos")

                class Trabajador():
                    def describir(self):
                        print("trabajo dentro de una gran empresa")

                def DescribirPersona(persona):
                    persona.describir()
                doc_1 = Docente()
                DescribirPersona(doc_1)
    
                input("Presione ¨ENTER¨ para volver al menu de ejercicios ")
                os.system ("cls")
            elif opcion=="10":
                print("================> Haz ingresado al video 40 <================ ")
                print("Cristhian Santos Nazareno")
                class Pais ():
                    def __init__(self,nom, pre):
                        self.nombre = nom
                        self.presidente = pre

                    def __str__(self):
                        txt = "Pais: {0} - Presidente: {1}"
                        return txt.format(self.nombre,self.presidente)


                class Ciudad():
                    def __init__(self, nom,hab,pais):
                        self.nombre = nom
                        self.habitantes = hab
                        self.pais = pais

                    def __str__(self):
                        txt = "Ciudad: {0} - Habitantes: {1} -  ({2})"
                        return txt.format(self.nombre, self.habitantes,self.pais)

                class Urbanizacion():
                    def __init__(self,nom, ciu):
                        self.nombre = nom
                        self.ciudad = ciu
                    def __str__(self):

                        txt = "Urbanizacion: {0} - ({1})"
                        return txt.format(self.nombre,self.ciudad)

                pais_1 = Pais("Peru","Martin Vizcarra")

                print(pais_1)
                ciudad_1 = Ciudad("Chiclayo",12000,pais_1)
                print(ciudad_1)

                urba_1 = Urbanizacion("Urbanizacion Maria",ciudad_1)
                print(urba_1)
    
                input("Presione ¨ENTER¨ para volver al menu de ejercicios ")
                os.system ("cls")
            
            elif opcion=="11":print(Lista123)
            opcion=help.menu(Lista2)
        
            os.system("cls")


    else:
        print()
    opcion=help.menu(Lista123)
print("GRACIAS POR VISITARNOS")