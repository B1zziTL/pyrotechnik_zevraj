#vlozenie modulov
import tkinter
import random

#nastavenie platna a jeho rozmerov
canvas = tkinter.Canvas(width=500, height=300) 
canvas.pack()

#zadeklarovanie premennych a zoznamov
cislo = 30
koniec_hry = 0
farbicky = ['green', 'red', 'grey', 'blue', 'orange']
umiestnenie = [100,110,120,130,140]
prekvapenie = int(random.choice(umiestnenie))

#vypisanie textu
canvas.create_text(250,30,text='Pyrotechnik',font='Arial 20',fill='blue')
canvas.create_text(250,60,text='označ správny káblik')

def tik_tak(): #funkcia na odpocitavanie casu
    #globalne premenne
    global cislo
    global nieco
    global koniec_hry
    
    if koniec_hry != 1: #za podmienky, ze este hrac nevyhral
        #vymazanie platna
        canvas.delete('all')
        
        #vykreslenie obdlznikov
        for i in range(5):
            canvas.create_rectangle(50,umiestnenie[i],350,umiestnenie[i]+10,fill=farbicky[i])

        #zacatie odpocitavania
        canvas.create_text(400,100,font='Arial 20',text=cislo)

        #podmienky na odpocitavanie a co nastane po dosiahnuti 0
        if cislo > 0:
            cislo -= 1
            canvas.after(100,tik_tak)
        else:
            canvas.delete('all')
            return

def klik_blik(suradnice): #funkcia na zistenie suradnic kliku
    #globalne premenne
    global cislo
    global koniec_hry
    x = suradnice.x
    y = suradnice.y

    #podmienky na vyhru a co sa stane po vyhre
    if x >= 50 and x <= 350:
        if cislo > 0:
            if y > prekvapenie and y < (prekvapenie+10):
                canvas.create_text(250,250,font='Arial 20',text="Vyhral si!")
                koniec_hry = 1

#nastavenie tlacidla mysky
canvas.bind('<Button-1>',klik_blik)
                     
#privolanie funkcie
tik_tak()
