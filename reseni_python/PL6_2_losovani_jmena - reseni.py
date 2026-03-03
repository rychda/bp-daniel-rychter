#Start code here
import random
seznam_zaku = ["Honza", "Petr", "Pavel", "Anna", "Helena", "Martina"]
random.shuffle(seznam_zaku)
pocet_zaku = len(seznam_zaku)
nahodne_cislo = random.randint(0, pocet_zaku - 1)
vylosovany_zak = seznam_zaku[nahodne_cislo]
print(f"K tabuli dnes půjde: {vylosovany_zak}")
