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
    await update.message.reply_photo('https://i.ibb.co/TWbTXDz/Binno.jpg', 'Olá! Eu sou o Binno, assistente virtual do Super Barber e estou aqui para lhe ajudar. Escolha sua opção:',reply_markup=reply_keyboard)
 
async def monitorador_de_respostas(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=f'Você escolheu: {query.data}')

async def ajuda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Para ver as opções digite /iniciar')

if __name__ == '__main__':
    application = ApplicationBuilder().token('TOKEN').build()
    application.add_handler(CommandHandler('iniciar',iniciar))
    application.add_handler(CommandHandler('start',iniciar))
    application.add_handler(CommandHandler('ajuda',ajuda))
    application.add_handler(CallbackQueryHandler(monitorador_de_respostas))

    application.run_polling()