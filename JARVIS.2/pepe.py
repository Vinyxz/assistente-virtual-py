import random
import pyttsx3
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import scrolledtext
from PIL import ImageTk, Image  


engine = pyttsx3.init()


def cumprimento():
    cumprimentos = ["Olá! Em que posso ajudar?", "Oi, tudo bem?", "Olá, como posso ser útil?"]
    return random.choice(cumprimentos)


def responder(pergunta):
    if "como você está" in pergunta.lower():
        resposta = "Estou bem, obrigado por perguntar!"
    elif "quem é você" in pergunta.lower():
        resposta = "Eu sou a Penelope, sua assistente virtual."
    elif "hora" in pergunta.lower():
        resposta = obter_hora()
    else:
        resposta = "Desculpe, não entendi. Poderia repetir?"

    
    engine.say(resposta)
    engine.runAndWait()

    return resposta

# Função para obter a hora atual no fuso horário de Brasília
def obter_hora():
    fuso_horario = timedelta(hours=-3)  
    hora_brasilia = datetime.utcnow() + fuso_horario
    return f"A hora atual em Brasília é {hora_brasilia.strftime('%H:%M')}."

def enviar_comando():
    entrada = entrada_usuario.get()
    if entrada.strip() == "":
        adicionar_mensagem("Você: (Digite algo para enviar)")
        return

    adicionar_mensagem(f"Você: {entrada}")
    resposta = responder(entrada)
    adicionar_mensagem(f"Penelope: {resposta}")

def adicionar_mensagem(mensagem):
    texto_saida.config(state=tk.NORMAL)
    texto_saida.insert(tk.END, mensagem + "\n")
    texto_saida.config(state=tk.DISABLED)
    texto_saida.see(tk.END)  


def configurar_interface():
    janela = tk.Tk()
    janela.title("Penelope - Assistente Virtual")
    janela.geometry("500x400")
    janela.config(bg="black")  

    label_instrucao = tk.Label(janela, text="Digite um comando:", fg="white", bg="black", font=("Arial", 12))
    label_instrucao.pack(pady=10)

    global entrada_usuario
    entrada_usuario = tk.Entry(janela, width=50)
    entrada_usuario.pack()

    botao_enviar = tk.Button(janela, text="Enviar", command=enviar_comando, bg="blue", fg="white")
    botao_enviar.pack(pady=10)

    global texto_saida
    texto_saida = scrolledtext.ScrolledText(janela, width=50, height=15, state=tk.DISABLED, bg="black", fg="white")
    texto_saida.pack(padx=10, pady=10)

    janela.mainloop()

if __name__ == "__main__":
    configurar_interface()