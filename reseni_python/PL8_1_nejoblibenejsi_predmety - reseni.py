#Start code here
import pygal
graf = pygal.Bar()
graf.title = "Oblíbenost předmětů ve třídě"
graf.add("Matematika", [2])
graf.add("Český jazyk", [3])
graf.add("Anglický jazyk", [7])
graf.add("Informatika", [8])
graf.render()
