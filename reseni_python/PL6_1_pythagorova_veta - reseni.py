#Start code here
import math
def vypocitej_preponu(a, b):
  prepona = math.sqrt(a ** 2 + b ** 2)
  print(f"Pro odvěsny dlouhé {a} a {b} je přepona dlouhá {prepona}")
odvesna_a = float(input("Zadej odvěsnu a: "))
odvesna_b = float(input("Zadej odvěsnu b: "))
vypocitej_preponu(odvesna_a, odvesna_b)
