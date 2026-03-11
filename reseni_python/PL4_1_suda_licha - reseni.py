#Start code here
cisla = [1, 2, 3, 72, 8, 11, 9]
suda = []
licha = []
for i in cisla:
    if i % 2 == 0:
        suda.append(i)
    else:
        licha.append(i)
print(suda)
print(licha)
if len(licha) > len(suda):
    print("Lichých čísel je více.")
elif len(licha) < len(suda):
    print("Sudých čísel je více.")
else:
    print("Počet sudých a lichých čísel je stejný!")
