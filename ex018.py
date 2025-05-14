import math
n1 = int(input(' digite um angulo:'))
rad = math.radians(n1)
s = math.sin(rad)
c = math.cos(rad)
t = math.tan(rad)
print(f' o angulo {n1} tem {rad:.2f} radianos tem {s:.2f} de seno e {c:.2f} de cosseno e {t:.2f} de tangente ')
