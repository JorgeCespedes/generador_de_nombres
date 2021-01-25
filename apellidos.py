import random
from listados import *




def paterno():
  apellido_paterno = apellidos[random.randint(0,len(apellidos)-1)].capitalize()
  print('Apellido paterno: {} '.format(apellido_paterno) )

def materno():
  apellido_materno = apellidos[random.randint(0,len(apellidos)-1)].capitalize()
  print('Apellido materno: {} '. format(apellido_materno) )

