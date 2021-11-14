# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 17:47:15 2021

"""

from pymongo import MongoClient

client= MongoClient("localhost")


db= client["DiccionarioSlang"]

col = db['Diccionario']

#Creamos las funciones que manipularan las bases de datos

def insertar(a,b):
    diccionario_agg = ({'Palabra_Español':a,
                        'Palabra_Slang':b})
    col.insert_one(diccionario_agg)

def mostrarDatos():
    for documentos in col.find({}):
        print(documentos)

def editarSignificado(PalabraV,SignificadoN):
    col.update_many({'Palabra_Español': PalabraV},{"$set": {"Palabra_Slang":SignificadoN}})

def eliminar(PalabraE):
    col.delete_one({'Palabra_Español': PalabraE})

def significadopalabra(palabrasig):
    for x in col.find({'Palabra_Español':palabrasig}):
        print (x)

#Una vez definidas todas las funciones le damos inicio al programa con un bucle While


print("Inicio del Programa Diccionario Slang Panameño")

while True:
    Respuesta1 = input("Si desea agregar una Palabra al Diccionario presione 1, de lo contrario presione otro valor : ")
    if Respuesta1 == "1":
        Respuesta11 = "1"
        while Respuesta11 == "1":
            a=input("Introduzca la Palabra : ")
            b = input ("Introduzca su significado : ")
            insertar(a,b)
            Respuesta11= input("Deseas agregar otra palabra?, Si (1), No (2): : ")
            
    Respuesta2 = input("\nSi desea editar el significado de una palabra del Diccionario presione 1, de lo contrario presione otro valor : ")
    if Respuesta2 == "1":
        PalabraV = input("Introduzca la palabra que desee cambiarle el significado : ")
        SignificadoN = input("Introduzca el nuevo significado de la palabra anterior : ")
        editarSignificado(PalabraV,SignificadoN)

    Respuesta3 = input("\nSi desea ver todas los datos del diccionario presione 1, de lo contrario presione otro valor : ")
    if Respuesta3 == "1":
        mostrarDatos()
              
    Respuesta4 = input("\nSi desea ver algun significado de una palabra del diccionario presione 1, de lo contrario presione otro valor : ")
    if Respuesta4 == "1":
        palabrasig= input("\nIntroduzca la palabra que quiere saber su significado : ")
        significadopalabra(palabrasig)
        
    Respuesta5 = input("\nSi desea eliminar alguna palabra del diccionario presione 1, de lo contrario presione otro valor : ")
    if Respuesta5 == "1":
        PalabraE = input("\nIntroduzca la palabra que desea eliminar : ")
        eliminar(PalabraE)
    
    Respuesta6 = input("\nSi desea salir del programa presione 1, de lo contrario presione otro valor : ")
    if Respuesta6 == "1":
        break
    
print("Fin del Programa")





