#-*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os
import pyttsx3
speaker = pyttsx3
import speech_recognition as sr

bot = ChatBot('Jerry', read_only=True)

"""
bot.set_trainer(ListTrainer) # definir treinamento
for _file in os.listdir('chats'): # percorrer todos os arquivos em chats
    lines = open('chats/'+ _file, 'r').readlines()
    bot.train(lines)
"""

def speak(text):
    speaker.say(text)
    speaker.runAndWait()

r = sr.Recognizer()

with sr.Microphone() as S:
    r.adjust_for_ambient_noise(S)

    while True:
        try:
            audio = r.listen(S)
            speech = r.recognize_google(audio, language='pt')

            print('Você disse: ', speech)
            response = bot.get_response(speech)
            print('Bot: ', response)

        except:
            speak('Ocorreu um erro ao reconhecer a sua voz')