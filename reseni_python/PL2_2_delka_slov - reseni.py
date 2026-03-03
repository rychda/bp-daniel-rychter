#Start code here
prvni_slovo = input("Zadej první slovo: ")
druhe_slovo = input("Zadej druhé slovo: ")
rozdil_znaku = len(prvni_slovo.strip()) - len(druhe_slovo.strip())
print(f"Počet znaků, okterý se liší slova {prvni_slovo} a {druhe_slovo} je {rozdil_znaku}")
