#Start code here
import random
import math
nahodne_cislo = random.randint(1, 20)
def obvod_kruhu(polomer):
  obvod = round(2 * math.pi * polomer)
  print(f"Obvod kruhu při poloměru {polomer} je {obvod}")
def obsah_kruhu(polomer):
  obsah = round(math.pi * (polomer ** 2))
  print(f"Obsah kruhu při poloměru {polomer} je {obsah}")
obvod_kruhu(nahodne_cislo)
obsah_kruhu(nahodne_cislo)
