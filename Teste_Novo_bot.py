from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, filters, MessageHandler, CallbackQueryHandler
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultPhoto
import logging
import telegram
import openpyxl
from datetime import datetime
from rich import print
import requests
import emoji, telegram
from telegram.ext import Updater

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def enviar_agendamento():
    workbook = openpyxl.load_workbook('./Basedata.xlsx')
    worksheet = workbook.active
    for row in worksheet.iter_rows(min_row=8, max_col=4, values_only=True):
        estabelecimento = row[1]
        profissional = row[1]
        data = row[1]
        horario = row[1]
        telegram = [1]
    bot = telegram.Bot(token='6114238245:AAEzplQA14_Sycw64C79uus4JJenFokQjyI')
    bot.send_message(text=f"Olá, o Sr(a) tem uma agendamento em nosso {estabelecimento} para o dia {data}, com o profissional {profissional} às {horario}.")
    if datetime.now == data:
        menu = [
            [
                InlineKeyboardButton('✅ Confirmar Agendamento', callback_data= 'Obrigado, aguardamos o Sr(a) na data e horário agendado. Até já!')
            ],
            [
                InlineKeyboardButton('❌ Cancelar Agendamento', callback_data= 'Lamentamos, mas está tudo bem. Favor acessar nossa plataforma ou telefonar para fazer um novo agendamento.')
            ]
        ]

async def iniciar(update:Update, context: ContextTypes.DEFAULT_TYPE):

    banner = [
        [
            
        ]
    ]
        
    keyboard = [
        [
            InlineKeyboardButton('📆 Agendar Serviço',callback_data= 'Calendario'),
            InlineKeyboardButton('💼 Nossos Serviços', url='https://drive.google.com/file/d/1WFiz9w_o8FZgzzPzdAHKCDDnvUuR_Ho0/view?usp=share_link')
            
        ],
        [
            InlineKeyboardButton('⏲ Nossos Horários', callback_data='De Seg a Sab: 09:00h às 19:00.'),
            InlineKeyboardButton('🏠 Nossa Morada', url= 'https://goo.gl/maps/jtkyXaMXWptsriAN6')
        ],
        [
            InlineKeyboardButton('🏃‍♂️ Sair',callback_data='Obrigado por nos visitar.')
        ]
    ]
    reply_keyboard = InlineKeyboardMarkup(banner)
    await update.message.reply_photo('./Binno.jpg')
    reply_keyboard = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Olá! Eu sou o Binno, assistente virtual do Super Barber e estou aqui para lhe ajudar. Escolha sua opção:',reply_markup=reply_keyboard)

##########################################################################################################

##########################################################################################################

############## TRABALHAR NO RETORNO DOS BOTÕES ##############################################

async def monitorador_de_respostas(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None: 
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=f'{query.data}')
#############################################################################################

async def ajuda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Para ver as opções digite /iniciar')

enviar_agendamento()

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
