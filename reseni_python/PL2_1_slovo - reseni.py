#Start code here
slovo = input("Zadej slovo: ")
pismeno = input("Zadej písmeno: ")
obracene = slovo[::-1]
pocet_vyskytu = slovo.count(pismeno)
print(f"{slovo.upper()} je pozpátku {obracene} a písmeno {pismeno} je ve větě {pocet_vyskytu}x.")
