# -*- coding: utf-8 -*-

import time
from datetime import datetime

from parsedatetime import parsedatetime
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardHide
from telegram.ext import CommandHandler, MessageHandler, Filters
from validators import url, ValidationFailure

from store import TinyDBStore

from config import params, allowed_users, other_users

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
        'message': '\U0001F570 I per acabar, seleccioneu el *minut* d\'entre els quatre quarts o escriviu qualsevol nombre entre 0 i 59:',
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
        'name': 'parking',
        'message': '\u0035\u20E3 Si per l\'excursió cal agafar el cotxe, envieu-me el *lloc d\'aparcament*, punt de sortida de l\'excursió.\n\nPodeu enviar /skip per a deixar el camp en blanc o /cancel per a cancel·lar la creació de l\'excursió.',
        'required': False
    },
    {
        'name': 'route',
        'message': '\u0036\u20E3 Envieu-me l\'*URL del mapa amb el GPX de la ruta*. Aquí també podeu enviar l\'URL d\'una pàgina de _Wikiloc_, per exemple.\n\nPodeu enviar /skip per a deixar el camp en blanc o /cancel per a cancel·lar el procés de creació de l\'excursió.',
        'required': False
    },
]


def parse_fields(field, value):
    if field == 'month':
        if value == 'Gener' or value == 'Febrer' or value == 'Març' or value == 'Abril' or value == 'Maig' or value == 'Juny' or value == 'Juliol' or value == 'Agost' or value == 'Setembre' or value == 'Octubre' or value == 'Novembre' or value == 'Desembre':  
             return value
        elif value == 'gener' or value == 'febrer' or value == 'març' or value == 'abril' or value == 'maig' or value == 'juny' or value == 'juliol' or value == 'agost' or value == 'setembre' or value == 'octubre' or value == 'novembre' or value == 'desembre':
             valuecap = value.capitalize()  
             return valuecap
        else:
             error = 'error'
             return error
    if field == 'day':
        try:
             value2 = int(value)
        except:
             error = 'error'
             return error
        if value2 >= 1 and value2 <= 31:
             return value
        else:
             error = 'error'
             return error
    if field == 'year':
        actualdate = datetime.now()
        actualyear = int(actualdate.year)
        try:
             value2 = int(value)
        except:
             error = 'error'
             return error
        if value2 >= actualyear and value2 <= actualyear + 3:
             return value
        else:
             error = 'error'
             return error
    if field == 'hour':
        try:
             value2 = int(value)
        except:
             error = 'error'
             return error
        if value2 >= 0 and value2 <= 23:
             return value
        else:
             error = 'error'
             return error
    if field == 'minute':
        try:
             value2 = int(value)
        except:
             error = 'error'
             return error
        if value2 >= 0 and value2 <= 59:
             return value
        else:
             error = 'error'
             return error
    if field == 'date':
        cal = parsedatetime.Calendar()
        time_struct, parse_status = cal.parse(value)
        timestamp = time.mktime(datetime(*time_struct[:6]).timetuple())
        return str(int(timestamp))
    if field == 'route':
        try:
             assert url(value)
             return value
        except:
             error = 'error'
             return error
    return value


def help_command(bot, update):
    bot.sendMessage(update.message.chat_id, text='Aquest bot és privat i només alguns usuaris poden crear esdeveniments per a excursions. Si quan envieu /start rebeu un missatge amb el vostre \U0001F194 vol dir que no teniu permisos.\n\nDe totes maneres un enviaré un enllaç amb les instruccions d\'ús del bot per a usuaris sense permisos que interactuen amb el bot a partir de missatges generats pel bot:')
    bot.sendMessage(update.message.chat_id, text='http://telegra.ph/Instruccions-d%c3%bas-CELP-familiar-11-28')
    bot.sendMessage(update.message.chat_id, text='Us pot ser útil també si genereu excursions i voleu explicar-ne el funcionament \U0001F609')

class CommandsModule(object):
    def __init__(self):
        self.handlers = [
            CommandHandler('start', self.start_command, pass_args=True),
            CommandHandler('skip', self.skip_command),
	    CommandHandler('cancel', self.cancel_command),
            CommandHandler('invite', self.invite_channel),
            CommandHandler('raw', self.get_raw),
            CommandHandler('help', help_command),
            MessageHandler((Filters.text), self.message)
        ]
        self.store = TinyDBStore()

    def start_command(self, bot, update, args):
        user_id = update.message.from_user.id
        if len(args) == 0:
            if str(user_id) in allowed_users.values():
                self.store.new_draft(user_id)
                bot.sendMessage(update.message.chat_id,parse_mode='Markdown',
                            text="Crearem un esdeveniment per a una excursió.\n\n\u0031\u20E3 El primer que heu de fer és enviar-me el *nom de l\'excursió*.\n\nSi no voleu continuar amb el procés, envieu /cancel.",
                            reply_markup=ReplyKeyboardHide())
            else:
                f_name = update.message.from_user.first_name
                bot.sendMessage(update.message.chat_id,
                            text= str(f_name) + ", no teniu permisos per crear excursions \U0001F622.\nSi necessiteu permisos, us caldrà el vostre identificador d'usuari.\n\U0001F194 = " + str(user_id) + ".")
        elif len(args) == 1 and args[0] == 'convida-al-canal':
            self.invite_channel(bot, update)

    def message(self, bot, update):
        user_id = update.message.from_user.id
        text = update.message.text
        draft = self.store.get_draft(user_id)

        if draft:
            event = draft['event']
            current_field = draft['current_field']
            field = FIELDS[current_field]

            event[field['name']] = parse_fields(field['name'], text)
            if field['name'] == 'day' and event['day'] == 'error':
                  bot.sendMessage(
                  update.message.chat_id,
                  text="\u26A0\uFE0F No és un dia vàlid, assegureu-vos què és un nombre entre 1 i 31 i torneu-ho a provar."
                  )
                  current_field += 0
                  self.update_draft(bot, event, user_id, update, current_field)

            elif field['name'] == 'month' and event['month'] == 'error':
                  bot.sendMessage(
                  update.message.chat_id,
                  text="\u26A0\uFE0F No és un mes vàlid, escriviu-lo amb lletres i en català i torneu-ho a provar."
                  )
                  current_field += 0
                  self.update_draft(bot, event, user_id, update, current_field)

            elif field['name'] == 'year' and event['year'] == 'error':
                  actualdate = datetime.now()
                  actualyear = int(actualdate.year)
                  bot.sendMessage(
                  update.message.chat_id,
                  text="\u26A0\uFE0F No és un any vàlid, heu d'escriure " + str(actualyear) + ", " + str(actualyear + 1) + ", " + str(actualyear + 2) + " o " + str(actualyear + 3) + " i torneu-ho a provar."
                  )
                  current_field += 0
                  self.update_draft(bot, event, user_id, update, current_field)

            elif field['name'] == 'hour' and event['hour'] == 'error':
                  bot.sendMessage(
                  update.message.chat_id,
                  text="\u26A0\uFE0F No és una hora vàlida, assegureu-vos que és un nombre entre 0 i 23 i torneu-ho a provar."
                  )
                  current_field += 0
                  self.update_draft(bot, event, user_id, update, current_field)

            elif field['name'] == 'minute' and event['minute'] == 'error':
                  bot.sendMessage(
                  update.message.chat_id,
                  text="\u26A0\uFE0F No és un minut vàlid, assegureu-vos què és un nombre entre 0 i 59 i torneu-ho a provar."
                  )
                  current_field += 0
                  self.update_draft(bot, event, user_id, update, current_field)

            elif field['name'] == 'route' and event['route'] == 'error':
                  bot.sendMessage(
                  update.message.chat_id,
                  text="\u26A0\uFE0F Sembla que l'URL que heu enviat no és vàlid, comproveu-lo i torneu-lo a enviar."
                  )
                  current_field += 0
                  self.update_draft(bot, event, user_id, update, current_field)

            else:
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
                now = datetime.now()
                now2 = int(now.year)
                now3 = str(now2)
                next1 = str(now2 + 1)
                next2 = str(now2 + 2)
                next3 = str(now2 + 3)
                bot.sendMessage(
                    update.message.chat_id,
                    parse_mode='Markdown',
                    text=FIELDS[current_field]['message'],
                    reply_markup=ReplyKeyboardMarkup(
                         keyboard=[
                              [now3],[next1],[next2],[next3]
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

    def invite_channel(self, bot, update):
        user_id = update.message.from_user.id
        user_f = update.message.from_user.first_name
        user_ln = update.message.from_user.last_name
        user_u = update.message.from_user.username
        if user_ln != "" and user_u != "":
           user_d= user_f + " " + user_ln + "* (podeu contactar-hi amb @" + user_u + ")"
        elif user_ln == "" and user_u != "":
           user_d= user_f + "* (podeu contactar-hi amb @" + user_u + ")" 
        elif user_ln != "" and user_u == "":
           user_d= user_f + " " + user_ln + "*"
        elif user_ln == "" and user_u == "":
           user_d= user_f + "*"
        if str(user_id) in other_users.values():
            keyboard = [[InlineKeyboardButton(text="\u2709\uFE0F Convida al canal", switch_inline_query="Convideu al canal")], []]
            bot.sendMessage(
                update.message.chat_id,
                text="Visca! Teniu permisos per a convidar gent al canal privat *CELP familiar*.\n\nPer convidar a algú al canal primer premeu el botó _Convida al canal_, i a continuació seleccioneu l'usuari a qui voleu convidar. Llavors haureu de prémer la capseta amb el rètol *«Convideu al canal»*",
                parse_mode='Markdown',
                reply_markup=InlineKeyboardMarkup(inline_keyboard=keyboard)
            )
            bot.sendMessage(
                chat_id= allowed_users['admin'],
                text="\U0001F6A6 L'usuari *" +user_d+ " ha volgut convidar a algú al canal, i té permisos.",
                parse_mode='Markdown'
            )
        else:
            bot.sendMessage(
                update.message.chat_id,
                text="No teniu permisos per convidar gent al canal privat *CELP familiar*.",
                parse_mode='Markdown'
            )
            bot.sendMessage(
                chat_id= allowed_users['admin'],
                text="\u26A0\uFE0F\n\U0001F6A6 L'usuari *" +user_d+ " ha volgut convidar a algú al canal i no té permisos.\nPer donar-li permisos, el seu \U0001F194: " + user_id + ".",
                parse_mode='Markdown'
            )

    def get_raw(self, bot, update):
        user_id = update.message.from_user.id
        if str(user_id) == allowed_users['admin']:
            bot.sendMessage(
                update.message.chat_id,
                text="Us envio els fitxers amb les *dades en cru*:",
                parse_mode='Markdown'
            )
            events_file= open('events.json', 'rb')
            bot.sendDocument(update.message.chat_id,
                             document=events_file)
            drafts_file= open('event_drafts.json', 'rb')
            bot.sendDocument(update.message.chat_id,
                             document=drafts_file)
            invites_file= open('invites.csv', 'rb')
            bot.sendDocument(update.message.chat_id,
                             document=invites_file)
        else:
            bot.sendMessage(
                update.message.chat_id,
                text="No teniu permisos per realitzar aquesta acció.",
                parse_mode='Markdown'
            )

    def get_handlers(self):
        return self.handlers
