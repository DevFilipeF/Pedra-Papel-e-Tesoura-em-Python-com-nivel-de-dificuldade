import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random

co0 = "#FFFFFF"  # branco
co1 = "#333333"  # preto
co2 = "#fcc058"  # laranja
co3 = "#fff873"  # amarelo
co4 = "#34eb3d"   # verde
co5 = "#e85151"   # vermelho

fundo = "#3b3b3b"

janela = Tk()
janela.title("JokenPython")
janela.geometry("260x350")  
janela.resizable(False, False)
janela.configure(bg=fundo)

# dividindo a janela
frame_cima = Frame(janela, width=260, height=100, bg=co1, relief='raised')
frame_cima.grid(row=0, column=0, sticky=NW)

frame_baixo = Frame(janela, width=260, height=300, bg=co0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

# configuração frame de cima
app_1 = Label(frame_cima, text="Você", height=1, anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
app_1.place(x=25, y=70)
app_1_linha = Label(frame_cima, height=10, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
app_1_linha.place(x=0, y=0)
app_1_pontos = Label(frame_cima, text="0", height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_1_pontos.place(x=50, y=20)

app_ = Label(frame_cima, text=":", height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_.place(x=125, y=20)

app_2_pontos = Label(frame_cima, text="0", height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_2_pontos.place(x=170, y=20)
app_2 = Label(frame_cima, text="Máquina", height=1, anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
app_2.place(x=180, y=70)
app_2_linha = Label(frame_cima, height=10, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
app_2_linha.place(x=255, y=0)

app_linha = Label(frame_cima, width=255, anchor='center', font=('Ivy 1 bold'), bg=co0, fg=co0)
app_linha.place(x=0, y=95)

app_maquina = Label(frame_baixo, text="", height=1, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
app_maquina.place(x=190, y=10)

global jogador
global maquina
global rodadas
global pontos_jogador
global pontos_maquina
global dificuldade

pontos_jogador = 0
pontos_maquina = 0
rodadas = 5
dificuldade = "Justo" 

# Lógica do jogo
def jogar(i):
    global pontos_jogador
    global pontos_maquina
    global rodadas

    if rodadas > 0:
        print(rodadas)
        opcoes = ['pedra', 'papel', 'tesoura']
        maquina = random.choice(opcoes)
        jogador = i

        # Definindo a lógica da dificuldade
        if dificuldade == "Noob":
            
            if jogador == 'pedra':
                maquina = 'tesoura'
            elif jogador == 'papel':
                maquina = 'pedra'
            elif jogador == 'tesoura':
                maquina = 'papel'
                
        elif dificuldade == "Roubado":
            
            if jogador == 'pedra':
                maquina = 'papel'
            elif jogador == 'papel':
                maquina = 'tesoura'
            elif jogador == 'tesoura':
                maquina = 'pedra'

        app_maquina['text'] = maquina
        app_maquina['fg'] = co1

        # EMPATE
        if jogador == maquina:
            print('empate')
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co0
            app_linha['bg'] = co3
        else:
            if (jogador == 'pedra' and maquina == 'tesoura') or \
               (jogador == 'papel' and maquina == 'pedra') or \
               (jogador == 'tesoura' and maquina == 'papel'):
                print('Você Ganhou!')
                app_1_linha['bg'] = co4
                app_2_linha['bg'] = co0
                app_linha['bg'] = co0
                pontos_jogador += 10
            else:
                print('Máquina Ganhou!')
                app_1_linha['bg'] = co0
                app_2_linha['bg'] = co4
                app_linha['bg'] = co0
                pontos_maquina += 10

        # atualizando o placar
        app_1_pontos['text'] = pontos_jogador
        app_2_pontos['text'] = pontos_maquina

        rodadas -= 1
    else:
        app_1_pontos['text'] = pontos_jogador
        app_2_pontos['text'] = pontos_maquina
        fim_do_jogo()

# função Iniciar
def iniciar_jogo():
    global btn_icon_1
    global btn_icon_2
    global btn_icon_3
    
    
    btn_noob.destroy()
    btn_justo.destroy()
    btn_roubado.destroy()
    btn_jogar.destroy()
    label_dificuldade.destroy()

    icon_1 = Image.open('images/pedra.png')
    icon_1 = icon_1.resize((50, 50), Image.LANCZOS)
    icon_1 = ImageTk.PhotoImage(icon_1)
    btn_icon_1 = Button(frame_baixo, command=lambda: jogar('pedra'), width=50, image=icon_1, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    btn_icon_1.image = icon_1
    btn_icon_1.place(x=15, y=60)

    icon_2 = Image.open('images/papel.png')
    icon_2 = icon_2.resize((50, 50), Image.LANCZOS)
    icon_2 = ImageTk.PhotoImage(icon_2)
    btn_icon_2 = Button(frame_baixo, command=lambda: jogar('papel'), width=50, image=icon_2, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    btn_icon_2.image = icon_2
    btn_icon_2.place(x=95, y=60)

    icon_3 = Image.open('images/tesoura.png')
    icon_3 = icon_3.resize((50, 50), Image.LANCZOS)
    icon_3 = ImageTk.PhotoImage(icon_3)
    btn_icon_3 = Button(frame_baixo, command=lambda: jogar('tesoura'), width=50, image=icon_3, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    btn_icon_3.image = icon_3
    btn_icon_3.place(x=170, y=60)

# Função para acabar o jogo
def fim_do_jogo():
    global pontos_jogador
    global pontos_maquina
    global rodadas

    pontos_jogador = 0
    pontos_maquina = 0
    rodadas = 5
    
    
    btn_icon_1.destroy()
    btn_icon_2.destroy()
    btn_icon_3.destroy()
    
    # definindo o ganhador
    player_jogador = int(app_1_pontos['text'])
    player_maquina = int(app_2_pontos['text'])
    
    if player_jogador > player_maquina:
        app_ganhador = Label(frame_baixo, text="Você ganhou, fera!", height=1, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co1)
        app_ganhador.place(x=15, y=10)
    
    elif player_jogador < player_maquina:
        app_ganhador = Label(frame_baixo, text="Máquina ganhou! Tente de novo!", height=1, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co5)
        app_ganhador.place(x=15, y=10)
    
    else:
        app_ganhador = Label(frame_baixo, text="Empate! Que jogo!", height=1, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co3)
        app_ganhador.place(x=15, y=10)
    
    
    def jogar_novamente():
        app_1_pontos['text'] = 0
        app_2_pontos['text'] = 0
        app_ganhador.destroy()
        btn_jogar_novamente.destroy()
        label_dificuldade.destroy()
        
        btn_noob.destroy()
        btn_justo.destroy()
        btn_roubado.destroy()
       
        
        iniciar_jogo()
        
    btn_jogar_novamente = Button(frame_baixo,command=jogar_novamente, text='Jogar Novamente?' ,width=30,  bg=fundo, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=RAISED, overrelief=RIDGE)
    btn_jogar_novamente.place(x=5, y=151)
    
    btn_noob = Button(frame_baixo, command=lambda: selecionar_dificuldade("Noob"), text='Noob', bg=co2, fg=co0, font=('Ivy 10 bold'))
    btn_noob.place(x=15, y=110)

    btn_justo = Button(frame_baixo, command=lambda: selecionar_dificuldade("Justo"), text='Justo', bg=co2, fg=co0, font=('Ivy 10 bold'))
    btn_justo.place(x=90, y=110)

    btn_roubado = Button(frame_baixo, command=lambda: selecionar_dificuldade("Roubado"), text='Roubado', bg=co2, fg=co0, font=('Ivy 10 bold'))
    btn_roubado.place(x=165, y=110)
        

# Função para selecionar a dificuldade
def selecionar_dificuldade(nova_dificuldade):
    global dificuldade
    dificuldade = nova_dificuldade

# Selecionar Dificuldade
label_dificuldade = Label(frame_baixo, text="Escolha a Dificuldade:", bg=co0, fg=co1, font=('Ivy 10 bold'))
label_dificuldade.place(x=5, y=65)

btn_noob = Button(frame_baixo, command=lambda: selecionar_dificuldade("Noob"), text='Noob', bg=co2, fg=co0, font=('Ivy 10 bold'))
btn_noob.place(x=15, y=110)

btn_justo = Button(frame_baixo, command=lambda: selecionar_dificuldade("Justo"), text='Justo', bg=co2, fg=co0, font=('Ivy 10 bold'))
btn_justo.place(x=90, y=110)

btn_roubado = Button(frame_baixo, command=lambda: selecionar_dificuldade("Roubado"), text='Roubado', bg=co2, fg=co0, font=('Ivy 10 bold'))
btn_roubado.place(x=165, y=110)


btn_jogar = Button(frame_baixo,command=iniciar_jogo, text='Jogar' ,width=30,  bg=fundo, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=RAISED, overrelief=RIDGE)
btn_jogar.place(x=5, y=151)

janela.mainloop()
