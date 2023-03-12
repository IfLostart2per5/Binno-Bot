from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, filters, MessageHandler, CallbackQueryHandler
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultPhoto
import logging
from datetime import datetime
from rich import print
import requests
import emoji, telegram
from telegram.ext import Updater

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# FLuxo de criação para bot que responde a comandos:
#1- Registrar um handler de comandos(classe que observa se x comando foi digitado)
#2- criar uma função quando x comando for digitado
#3- Ligar o monitoramento de comandos

#==================================================

#2- criar uma função quando x comando for digitado

'''
buttonsMenu = [
    [telegram.InlineKeyboardButton("UP", callback_data="UpVote")],
    [telegram.InlineKeyboardButton("DOWN", callback_data="DownVote")],
    ]
    keyboard_markup = telegram.InlineKeyboardMarkup(buttonsMenu)
    context.bot.sendPhoto(chat_id=update.message.chat.id, photo=open('./imgpath.jpg'), 'rb'),caption='messageText', reply_markup=keyboard_markup)'''



async def iniciar(update:Update, context: ContextTypes.DEFAULT_TYPE):
        
    keyboard = [
        [
            InlineKeyboardButton('📆 Agendar Serviço',callback_data='Abre Calendário'),
            InlineKeyboardButton('💼 Nossos Serviços',callback_data='PDF Serviços'),
        ],
        [
            InlineKeyboardButton('⏲ Nossos Horários', callback_data='Horário de Funcionamento'),
            InlineKeyboardButton('🏠 Morada',callback_data='Morada do estebecimento')
        ],
        [
            InlineKeyboardButton('🏃‍♂️ Sair',callback_data='Fechar Bot')
        ]
    ]
    reply_keyboard = InlineKeyboardMarkup(keyboard)
    reply_keyboard = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Olá! Eu sou o Binno, assistente virtual do Super Barber e estou aqui para lhe ajudar. Escolha sua opção:',reply_markup=reply_keyboard)

#_photo('https://i.ibb.co/TWbTXDz/Binno.jpg', 
    #await context.bot.sendPhoto(chat_id=update.message.chat.id, photo=open('./Binno.jpg', 'rb'),caption='Olá! Eu sou o Binno, assistente virtual do Super Barber e estou aqui para lhe ajudar. Escolha sua opção:', reply_markup=reply_keyboard)
    #await update.message.reply_text('Olá! Eu sou o Binno, assistente virtual do Super Barber e estou aqui para lhe ajudar. Escolha sua opção:',reply_markup=reply_keyboard)


async def monitorador_de_respostas(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=f'Você escolheu: {query.data}')

async def ajuda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Para ver as opções digite /iniciar')

if __name__ == '__main__':
    application = ApplicationBuilder().token('6114238245:AAEzplQA14_Sycw64C79uus4JJenFokQjyI').build()
    #1- Registrar um handler de comandos(classe que observa se x comando foi digitado)
    application.add_handler(CommandHandler('iniciar',iniciar))
    application.add_handler(CommandHandler('start',iniciar))
    application.add_handler(CommandHandler('ajuda',ajuda))
    application.add_handler(CallbackQueryHandler(monitorador_de_respostas))
    #application.add_handler(CallbackQueryHandler(enviar_imagem))
    #3- Ligar o monitoramento de comandos
    application.run_polling()


# FUNÇÃO PARA ENVIAR MENSAGEM:
'''
def enviar_imagem(banner, caption):
    token = '6114238245:AAEzplQA14_Sycw64C79uus4JJenFokQjyI'
    for link in banner:
        requests.get(f'https://api.telegram.org/bot{token}/sendPhoto?&photo={link}&caption={caption}')
def enviar_imagem(banner, caption):
    token = '6114238245:AAEzplQA14_Sycw64C79uus4JJenFokQjyI'
    for link in banner:
        requests.get(f'https://api.telegram.org/bot{token}/sendPhoto?&photo={link}&caption={caption}')
  
imagem = ['https://i.ibb.co/TWbTXDz/Binno.jpg']
enviar_imagem(banner=imagem, caption='Olá! Eu sou o Binno, assistente virtual do Super Barber e estou aqui para lhe ajudar. Escolha sua opção:')
# Foto Binno https://i.ibb.co/TWbTXDz/Binno.jpg

token = "6114238245:AAEzplQA14_Sycw64C79uus4JJenFokQjyI"
bot = telegram.Bot(token=token)

pic = "https://i.ibb.co/TWbTXDz/Binno.jpg"
try:
    chat_id = bot.get_updates()[-1].message.chat_id
except IndexError:
    chat_id = 0

def start(bot, update):
    bot.send_photo(chat_id, open(pic,'rb'))
    update.message.reply_text(text="helo",reply_markup=())

'''