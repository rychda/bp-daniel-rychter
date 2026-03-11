#Start code here
def dej_znamku(body):
    if body >= 90:
        znamka = 1
    elif body <= 89 and body >= 75:
        znamka = 2
    elif body <= 74 and body >= 60:
        znamka = 3
    elif body <= 59 and body >= 45:
        znamka = 4
    else:
        znamka = 5
    print(znamka)
tvoje_body = int(input("Zadej tvůj počet bodů: "))
print(f"Za počet bodů: {tvoje_body} dostáváš")
dej_znamku(tvoje_body)
