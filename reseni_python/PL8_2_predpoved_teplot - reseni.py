#Start code here
import pygal
graf = pygal.Line()
graf.title = "Přepověd teplot od 28.2. do 6.3."
graf.add("Teplota v °C", [13, 11, 11, 13, 13, 12, 11])
graf.x_labels = "So", "Ne", "Po", "Út", "St", "Čt", "Pá"
graf.render()
