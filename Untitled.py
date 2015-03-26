arquivo = open("palavras.csv", "r+")
leitura=arquivo.read(1000)
lista = leitura.split(',')
import random
palavra = random.choice(lista)

import turtle
window = turtle.Screen()
window.bgcolor("orange")
window.title("Forca")

tartaruga   = turtle.Turtle()  
tartaruga.hideturtle()
tartaruga.speed(30)  

tartaruga.penup()       
tartaruga.setpos(-100,-150)
tartaruga.pendown()
tartaruga.color("red")
tartaruga.goto(-180,-150)
tartaruga.goto(-140, -150)
tartaruga.goto(-140, 100)
tartaruga.goto(-40, 100)

def cabeca:
    tartaruga.goto(-40, 60)  
    tartaruga.goto(-20, 60)
    tartaruga.goto(-20, 20)
    tartaruga.goto(-60, 20)
    tartaruga.goto(-60, 60)
    tartaruga.goto(-40, 60)
    
def corpo
    tartaruga.penup()   
    tartaruga.goto(-40, 20)
    tartaruga.pendown()
    tartaruga.goto(-40, -80)
    
def bracoesquerdo
    tartaruga.penup()
    tartaruga.goto(-40, 0)
    tartaruga.pendown()
    tartaruga.goto(-60, -40)
    
def braçodireito
    tartaruga.penup()
    tartaruga.goto(-40, 0)
    tartaruga.pendown()
    tartaruga.goto(-20, -40)
    
def pernaesquerda
    tartaruga.penup()
    tartaruga.goto(-40, -80)
    tartaruga.pendown()
    tartaruga.goto(-60, -120)
    
def pernadireita    
    tartaruga.penup()
    tartaruga.goto(-40, -80)
    tartaruga.pendown()
    tartaruga.goto(-20, -120)

window.exitonclick()