#Start code here
from turtle import *
def n_uhelnik(n):
  uhel = 360 / n
  turtle = Turtle()
  for i in range(n):
    turtle.forward(50)
    turtle.left(uhel)
pocet_stran = int(input("Zadej požadovaný počet stran: "))
n_uhelnik(pocet_stran)
