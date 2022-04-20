from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

bot = ChatBot("Dante")

conversa = [
            "Oi",
            "Tudo bem?",
            "Sim, e com você?",
            "Que ótimo",
            "O que você gosta de fazer?",
            "Eu gosto de ouvir músicas. E você?"
            
]

trainer = ListTrainer(bot)
trainer.train(conversa)

while True:
    pergunta = input(str("Humano: "))
    resposta = bot.get_response(pergunta)
    print('Dante: ', resposta)