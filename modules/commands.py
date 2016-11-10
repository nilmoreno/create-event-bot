# -*- coding: utf-8 -*-

import time
from datetime import datetime

from parsedatetime import parsedatetime
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardHide
from telegram.ext import CommandHandler, MessageHandler, Filters

from store import TinyDBStore

FIELDS = [
    {
        'name': 'name',
        'message': '\u0031\u20E3 Envieu-me el *nom de l\'excursió*.\n\nPer a cancel·lar el procés envieu /cancel.',
        'required': True
    },
    {
        'name': 'description',
        'message': '\u0032\u20E3 Envieu-me una *breu descripció* de l\'excursió.\n\nPodeu enviar /skip per a deixar el camp en blanc o /cancel per a cancel·lar la creació de l\'excursió.',
        'required': False
    },
    {
        'name': 'month',
        'message': '\u0033\u20E3 Ara m\'haureu d\'enviar la *data i hora* de sortida de l\'excursió.\n\n\U0001F5D3 En primer lloc seleccioneu el *mes*:',
        'required': True
    },
    {
        'name': 'day',
        'message': '\U0001F5D3 En segon lloc, haureu de seleccionar el *dia*:',
        'required': True
    },
    {
        'name': 'year',
        'message': '\U0001F5D3 Seleccioneu l\'*any*:',
        'required': True
    },
    {
        'name': 'hour',
        'message': '\U0001F570 Seleccioneu l\'*hora*:',
        'required': True
    },
    {
        'name': 'minute',
        'message': '\U0001F570 I per acabar, seleccioneu el *minut* d\'entre els quatre quarts:',
        'required': True
    },
    {
        'name': 'date',
        'message': 'Comproveu que la data és correcta (seguint l\'ordre *mes/dia/any hora:minut*) i si és així premeu el botó per a desar-la.\n\nPer a cancel·lar el procés envieu /cancel.',
        'required': True
    },
    {
        'name': 'place',
        'message': '\u0034\u20E3 Envieu-me el *punt de trobada* per iniciar l\'excursió.\n\nPodeu enviar /skip per a deixar el camp en blanc o /cancel per a cancel·lar la creació de l\'excursió.',
        'required': False
    },
    {
        'name': 'route',
        'message': '\u0035\u20E3 Envieu-me l\'*URL del mapa amb el GPX de la ruta*. Aquí també podeu enviar l\'URL d\'una pàgina de _Wikiloc_, per exemple.\n\nPodeu enviar /skip per a deixar el camp en blanc o /cancel per a cancel·lar el procés de creació de l\'excursió.',
        'required': False
    },
]


def parse_fields(field, value):
    if field == 'date':
        cal = parsedatetime.Calendar()
        time_struct, parse_status = cal.parse(value)
        timestamp = time.mktime(datetime(*time_struct[:6]).timetuple())
        return str(int(timestamp))
    return value


def help_command(bot, update):
    bot.sendMessage(update.message.chat_id, text='Aquest bot és privat i només alguns usuaris poden crear esdeveniments per a excursions.')


class CommandsModule(object):
    def __init__(self):
        self.handlers = [
            CommandHandler('start', self.start_command, pass_args=True),
            CommandHandler('skip', self.skip_command),
	    CommandHandler('cancel', self.cancel_command),
            CommandHandler('help', help_command),
            MessageHandler([Filters.text], self.message)
        ]
        self.store = TinyDBStore()

    def start_command(self, bot, update, args):
        user_id = update.message.from_user.id
        # Replace USER_ID with your user_id number:
        if user_id == USER_ID:
            self.store.new_draft(user_id)
            bot.sendMessage(update.message.chat_id,parse_mode='Markdown',
                        text="Crearem un esdeveniment per a una excursió.\n\n\u0031\u20E3 El primer que heu de fer és enviar-me el *nom de l\'excursió*.\n\nSi no voleu continuar amb el procés, envieu /cancel.",
                        reply_markup=ReplyKeyboardHide())
        else:
            f_name = update.message.from_user.first_name
            bot.sendMessage(update.message.chat_id,
                        text= str(f_name) + ", no teniu permisos per crear excursions \U0001F622.\nSi necessiteu permisos, us caldrà el vostre identificador d'usuari.\n\U0001F194 = " + str(user_id) + ".")

    def message(self, bot, update):
        user_id = update.message.from_user.id
        text = update.message.text
        draft = self.store.get_draft(user_id)

        if draft:
            event = draft['event']
            current_field = draft['current_field']
            field = FIELDS[current_field]

            event[field['name']] = parse_fields(field['name'], text)
            current_field += 1

            self.update_draft(bot, event, user_id, update, current_field)

        else:
            bot.sendMessage(
            update.message.chat_id,
            text="\U0001F914 No entenc el que em voleu dir, però sóc un robot \U0001F916 i funciono de manera molt senzilla:\n\n1. /start per començar a crear una excursió nova\n2. O per saber una mica més sobre mi, /help.",
            reply_markup=ReplyKeyboardHide()
            )

    def cancel_command(self, bot, update):
        user_id = update.message.from_user.id
        draft = self.store.get_draft(user_id)

        if draft:
            self.store.remove_draft(update.message.from_user.id)
            bot.sendMessage(
            update.message.chat_id,
            text="\U0001F5D1 S'ha cancel·lat la creació de l'excursió.",
            reply_markup=ReplyKeyboardHide()
            )
        else:
            bot.sendMessage(
            update.message.chat_id,
            text="\u26A0\uFE0F No hi ha res a cancel·lar.\nAquesta comanda només funciona quan s'ha iniciat la creació d'una excursió.",
            reply_markup=ReplyKeyboardHide()
        )

    def skip_command(self, bot, update):
        user_id = update.message.from_user.id
        draft = self.store.get_draft(user_id)

        if draft:
            current_field = draft['current_field']
            field = FIELDS[current_field]

            if field['required']:
                bot.sendMessage(update.message.chat_id,parse_mode='Markdown',
                                text="\u26A0\uFE0F Aquest camp és necessari.\n\n" + field['message'])
            else:
                event = draft['event']
                current_field += 1
                self.update_draft(bot, event, user_id, update, current_field)

        else:
            bot.sendMessage(update.message.chat_id,
                            text="\u26A0\uFE0F Aquesta ordre només té sentit si s'està creant una excursió i es vol deixar en blanc un camp que no és necessari.")

    def update_draft(self, bot, event, user_id, update, current_field):
        self.store.update_draft(user_id, event, current_field)

        if current_field <= len(FIELDS) - 1:

            if FIELDS[current_field]['name'] == 'month':
                bot.sendMessage(
                    update.message.chat_id,
                    parse_mode='Markdown',
                    text=FIELDS[current_field]['message'],
                    reply_markup=ReplyKeyboardMarkup(
                         keyboard=[
                              ['Gener','Febrer','Març'], ['Abril','Maig','Juny'],['Juliol','Agost','Setembre'],['Octubre','Novembre','Desembre']
                         ],
                         one_time_keyboard=True,
                         resize_keyboard=True
                ))

            elif FIELDS[current_field]['name'] == 'day' and event['month'] == 'Febrer':
                bot.sendMessage(
                    update.message.chat_id,
                    parse_mode='Markdown',
                    text=FIELDS[current_field]['message'],
                    reply_markup=ReplyKeyboardMarkup(
                         keyboard=[
                              ['1','2','3','4'],['5','6','7','8'],['9','10','11','12'],['13','14','15','16'],['17','18','19','20'],['21','22','23','24'],['25','26','27','28'],['29']
                         ],
                         one_time_keyboard=True,
                         resize_keyboard=True
                ))

            elif FIELDS[current_field]['name'] == 'day' and event['month'] == 'Abril':
                bot.sendMessage(
                    update.message.chat_id,
                    parse_mode='Markdown',
                    text=FIELDS[current_field]['message'],
                    reply_markup=ReplyKeyboardMarkup(
                         keyboard=[
                              ['1','2','3','4'],['5','6','7','8'],['9','10','11','12'],['13','14','15','16'],['17','18','19','20'],['21','22','23','24'],['25','26','27','28'],['29','30']
                         ],
                         one_time_keyboard=True,
                         resize_keyboard=True
                ))


            elif FIELDS[current_field]['name'] == 'day' and event['month'] == 'Juny':
                bot.sendMessage(
                    update.message.chat_id,
                    parse_mode='Markdown',
                    text=FIELDS[current_field]['message'],
                    reply_markup=ReplyKeyboardMarkup(
                         keyboard=[
                              ['1','2','3','4'],['5','6','7','8'],['9','10','11','12'],['13','14','15','16'],['17','18','19','20'],['21','22','23','24'],['25','26','27','28'],['29','30']
                         ],
                         one_time_keyboard=True,
                         resize_keyboard=True
                ))


            elif FIELDS[current_field]['name'] == 'day' and event['month'] == 'Setembre':
                bot.sendMessage(
                    update.message.chat_id,
                    parse_mode='Markdown',
                    text=FIELDS[current_field]['message'],
                    reply_markup=ReplyKeyboardMarkup(
                         keyboard=[
                              ['1','2','3','4'],['5','6','7','8'],['9','10','11','12'],['13','14','15','16'],['17','18','19','20'],['21','22','23','24'],['25','26','27','28'],['29','30']
                         ],
                         one_time_keyboard=True,
                         resize_keyboard=True
                ))


            elif FIELDS[current_field]['name'] == 'day' and event['month'] == 'Novembre':
                bot.sendMessage(
                    update.message.chat_id,
                    parse_mode='Markdown',
                    text=FIELDS[current_field]['message'],
                    reply_markup=ReplyKeyboardMarkup(
                         keyboard=[
                              ['1','2','3','4'],['5','6','7','8'],['9','10','11','12'],['13','14','15','16'],['17','18','19','20'],['21','22','23','24'],['25','26','27','28'],['29','30']
                         ],
                         one_time_keyboard=True,
                         resize_keyboard=True
                ))

            elif FIELDS[current_field]['name'] == 'day':
                bot.sendMessage(
                    update.message.chat_id,
                    parse_mode='Markdown',
                    text=FIELDS[current_field]['message'],
                    reply_markup=ReplyKeyboardMarkup(
                         keyboard=[
                              ['1','2','3','4'],['5','6','7','8'],['9','10','11','12'],['13','14','15','16'],['17','18','19','20'],['21','22','23','24'],['25','26','27','28'],['29','30','31']
                         ],
                         one_time_keyboard=True,
                         resize_keyboard=True
                ))

            elif FIELDS[current_field]['name'] == 'year':
                bot.sendMessage(
                    update.message.chat_id,
                    parse_mode='Markdown',
                    text=FIELDS[current_field]['message'],
                    reply_markup=ReplyKeyboardMarkup(
                         keyboard=[
                              ['2016','2017'],['2018','2019']
                         ],
                         one_time_keyboard=True,
                         resize_keyboard=True
                ))

            elif FIELDS[current_field]['name'] == 'hour':
                bot.sendMessage(
                    update.message.chat_id,
                    parse_mode='Markdown',
                    text=FIELDS[current_field]['message'],
                    reply_markup=ReplyKeyboardMarkup(
                         keyboard=[
                              ['6','7','8','9'],['10','11','12','13'],['14','15','16','17'],['18','19','20','21'],['22','23','0','1'],['2','3','4','5']
                         ],
                         one_time_keyboard=True,
                         resize_keyboard=True
                ))

            elif FIELDS[current_field]['name'] == 'minute':
                bot.sendMessage(
                    update.message.chat_id,
                    parse_mode='Markdown',
                    text=FIELDS[current_field]['message'],
                    reply_markup=ReplyKeyboardMarkup(
                         keyboard=[
                              ['00','15'],['30','45']
                         ],
                         one_time_keyboard=True,
                         resize_keyboard=True
                ))

            elif FIELDS[current_field]['name'] == 'date':
                 day = event['day']
                 year = event['year']
                 hour = event['hour']
                 minute = event['minute']
                 if event['month'] == 'Gener':
                      monthnum = '1'
                 elif event['month'] == 'Febrer':
                      monthnum = '2'
                 elif event['month'] == 'Març':
                      monthnum = '3'
                 elif event['month'] == 'Abril':
                      monthnum = '4'
                 elif event['month'] == 'Maig':
                      monthnum = '5'
                 elif event['month'] == 'Juny':
                      monthnum = '6'
                 elif event['month'] == 'Juliol':
                      monthnum = '7'
                 elif event['month'] == 'Agost':
                      monthnum = '8'
                 elif event['month'] == 'Setembre':
                      monthnum = '9'
                 elif event['month'] == 'Octubre':
                      monthnum = '10'
                 elif event['month'] == 'Novembre':
                      monthnum = '11'
                 else:
                      monthnum = '12'
                 newdate = monthnum + "/" + day + "/" + year + " " + hour + ":" + minute
                 bot.sendMessage(
                    update.message.chat_id,
                    parse_mode='Markdown',
                    text=FIELDS[current_field]['message'],
                    reply_markup=ReplyKeyboardMarkup(
                         keyboard=[
                              [newdate]
                         ],
                         one_time_keyboard=True,
                         resize_keyboard=True
                ))

            elif FIELDS[current_field]['name'] != 'month' or FIELDS[current_field]['name'] != 'day' or FIELDS[current_field]['name'] != 'year' or FIELDS[current_field]['name'] != 'hour' or FIELDS[current_field]['name'] != 'minute' or FIELDS[current_field]['name'] != 'date':
                bot.sendMessage(
                    update.message.chat_id,
                    parse_mode='Markdown',
                    text=FIELDS[current_field]['message'],
                    reply_markup=ReplyKeyboardHide()
                )
        else:
            event['user_id'] = user_id
            self.create_event(bot, update, event)

    def create_event(self, bot, update, event):
        self.store.insert_event(event)
        self.store.remove_draft(update.message.from_user.id)

        keyboard = [[InlineKeyboardButton(text="Envia l'excursió", switch_inline_query=event['name'])], []]
        bot.sendMessage(
            update.message.chat_id,
            text="S'ha creat l'excursió",
            reply_markup=InlineKeyboardMarkup(inline_keyboard=keyboard)
        )

    def get_handlers(self):
        return self.handlers
