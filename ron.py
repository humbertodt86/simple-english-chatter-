import streamlit as st
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
chatbot = ChatBot("Ron Obvious")


conversation = [
    'oi',
'olá',
'qual o seu nome ?',
'meu nome é Umba',
'legal',
'qual sua cor favorita ?',
'amarelo',
'verde ',
'o que você gosta de fazer?',
'eu gosto de comer pizza',
'Eu gosto de dormir ',
'Qual a sua idade ?',
'9 anos',
'Eu gosto de ver tv.',
]

trainer = ListTrainer(chatbot)

trainer.train(conversation)

request = 0



# Text Area
bot = st.empty()


# Receiving User Text Input
texto = st.text_input("Type here","Say hello..")
if st.button("Enviar"):
    request = texto
    response = chatbot.get_response(request)
    bot.text(response)



