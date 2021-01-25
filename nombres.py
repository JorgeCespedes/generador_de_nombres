import random
from listados import *



def nombre_hombre():
  nom = nombres_hombres[random.randint(0,len(nombres_hombres) - 1)]
  print('Nombre : {}'. format(nom))

def nombre_mujer():
  nom = nombres_mujeres[random.randint(0,len(nombres_mujeres) - 1)]
  print('Nombre : {}'. format(nom))

def nombre_todos():
  nombre_todos = nombres_mujeres + nombres_hombres
  nombre = nombre_todos[ random.randint(0, len(nombre_todos) - 1) ]
  print('Nombre : {}'. format(nombre))
  
