from datetime import datetime as dt
from time import time, sleep
import math
import random

ecolha = random.choice([1, 2, 3])

numero_aleatorio = random.random()
print(numero_aleatorio)

potencia = math.pow(10, 10)
print(potencia)

num = math.ceil(10.1)
print(num)

print(math.pi)

print(time())

sleep(5)

print(dt.now())

print(dt.now().day)

print(dt.now().year)
