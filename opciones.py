from nombres import *
from apellidos import *
from listados import *

def opciones():
  while True:
    op = input('''
          [1] Solo un nombre.
          [2] Nombre y apellido.
          [3] Un nombre y dos apellidos.
          [x] Salir
          
          ''')
    
    if op == '1':
      nombre_todos()
      print('')
      
    elif op == '2':
      nombre_todos()
      paterno()
      print('')
      
    elif op == '3':
      nombre_todos()
      paterno()
      materno()
      print('')
      
    elif op == 'x':
      break
    
    else:
      print('Opción no válida.')