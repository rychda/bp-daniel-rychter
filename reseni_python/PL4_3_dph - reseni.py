#Start code here
ceny = [47, 35, 91, 100, 220]
ceny_s_dph = []
for i in ceny:
  ceny_s_dph.append(i * 1.21)
print(ceny_s_dph)
for i in range(len(ceny)):
  rozdil_cen = ceny_s_dph[i] - ceny[i]
  print(f"Rozdíl mezi cenou bez DPH:{ceny[i]} a cenou s DPH: {ceny_s_dph[i]} je {rozdil_cen}")
