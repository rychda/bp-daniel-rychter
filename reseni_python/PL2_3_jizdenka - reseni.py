#Start code here
vek = int(input("Zadej svůj věk: "))
vzdalenost = int(input("Zadej vzdálenost tvé cesty: "))
zakladni_cena = vzdalenost * 2
kategorie = 0
cena_se_slevou = zakladni_cena * 0.5
if vek <= 14:
  kategorie = "dítě"
  vysledna_cena = "zdarma"
elif vek <= 25:
  kategorie = "student"
  vysledna_cena = cena_se_slevou
elif vek >= 65:
  kategorie = "senior"
  vysledna_cena = cena_se_slevou
else:
  kategorie = "dospělý"
  vysledna_cena = zakladni_cena
if vzdalenost < 10 and kategorie != "dítě":
  vysledna_cena = vysledna_cena + 15
print(f"Kategorie cestujícího: {kategorie}")
print(f"Základní cena: {zakladni_cena}")
print(f"Výsledná cena: {vysledna_cena}")
