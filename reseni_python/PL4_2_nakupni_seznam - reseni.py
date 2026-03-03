#Start code here
seznam = []
vstup = ""
while vstup != "hotovo":
  vstup = input("Zadej položku do nákupního seznamu: ")
  seznam.append(vstup)
print(seznam)
for i in range(len(seznam)):
  if seznam[i] == "mléko":
    print("Mléko je v seznamu!")
