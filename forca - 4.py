import random
import turtle

lista = []
letras = []
acertos = []
erradas = []
leitura = []
digitadas = []
erros = 0
lista = open("entrada.txt","r+", encoding = "utf-8")
leitura = lista.readlines()
palavra = random.choice(leitura)
numletras = len(palavra) - 1
letras = palavra.split

window = turtle.Screen()
window.bgcolor("orange")
window.title("Forca")
window.setup(width=1400)
tartaruga   = turtle.Turtle()  
tartaruga.hideturtle()
tartaruga.speed(30)
tartaruga.pensize(4)  

tartaruga.penup()       
tartaruga.setpos(-100,-150)
tartaruga.pendown()
tartaruga.color("red")
tartaruga.goto(-180,-150)
tartaruga.goto(-140, -150)
tartaruga.goto(-140, 100)
tartaruga.goto(-40, 100)
tartaruga.penup

def cabeça():
    tartaruga.pendown
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




while erros<6:
    senha = ""    
    for letra in palavra:
         senha += letra if letra in acertos else "_ "
   
    forcaa = turtle.Turtle()
    forcaa.hideturtle()    
    forcaa.penup()    
    forcaa.setpos(-230,-200)       
    forcaa.write(senha, move=False, align="left", font=("Arial", 45, "normal"))
    
    if senha == palavra:
        break
    letras = window.textinput('','Digite uma letra ').lower().strip()
    if letras == ('exit'):
        break
    if letras in digitadas:
        print('voce ja digitou essa palavra')
        continue
    else:
        digitadas += letras
        forcaa.clear()
    if letras in palavra:
        acertos += letras
        forcaa.clear()
    else:
        erros = erros+1
        
    print(" letras:",letras)
    print(" palavra:", palavra )
    print(" type: " , type(palavra))
    
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