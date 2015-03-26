import random
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

def cabeça():
    tartaruga.goto(-40, 60)  
    tartaruga.goto(-20, 60)
    tartaruga.goto(-20, 20)
    tartaruga.goto(-60, 20)
    tartaruga.goto(-60, 60)
    tartaruga.goto(-40, 60)
    
def corpo():
    tartaruga.penup()   
    tartaruga.goto(-40, 20)
    tartaruga.pendown()
    tartaruga.goto(-40, -80)
    
def braçoesquerdo():
    tartaruga.penup()
    tartaruga.goto(-40, 0)
    tartaruga.pendown()
    tartaruga.goto(-60, -40)
    
def braçodireito():
    tartaruga.penup()
    tartaruga.goto(-40, 0)
    tartaruga.pendown()
    tartaruga.goto(-20, -40)
    
def pernaesquerda():
    tartaruga.penup()
    tartaruga.goto(-40, -80)
    tartaruga.pendown()
    tartaruga.goto(-60, -120)
    
def pernadireita():    
    tartaruga.penup()
    tartaruga.goto(-40, -80)
    tartaruga.pendown()
    tartaruga.goto(-20, -120)
 
digitadas = []
acertos = []
erros = 0
lista1 = []
lista = open("palavras.csv","r+")
leitura = lista.readlines()
palavra = random.choice(leitura).lower()

letra =  window.textinput('','coloque uma letra') 
letra = digitadas

if letra in palavra:
   acertos =+ letra
elif letra in digitadas:
    print("voce já tentou esta letra")
else:
    erros =+ erros + 1
    if erros == 1:
        cabeça()
    if erros == 2:
        corpo()
    if erros == 3:
        braçoesquerdo()
    if erros == 4:
        braçodireito()
    if erros == 5:
        pernaesquerda()
    if erros == 6:
       pernadireita() 
    
cabeça()
corpo()
braçoesquerdo()
braçodireito()
pernaesquerda()
pernadireita()
window.exitonclick()