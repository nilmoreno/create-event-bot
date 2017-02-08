# -*- coding: utf-8 -*-

import time
from datetime import datetime

from parsedatetime import parsedatetime
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, Filters

from store import TinyDBStore

FIELDS = [
    {
        'name': 'name',
        'message': 'Envieu-me el nom de l\'excursió'
    },
    {
        'name': 'description',
        'message': 'Envieu-me una breu descripció de l\'excursió (o /skip per deixar el camp en blanc)',
        'required': False
    },
    {
        'name': 'date',
        'message': 'Envieu-me la data i hora de sortida de l\'excursió (ex.: 10/25/16 12:20)',
    },
    {
        'name': 'place',
        'message': 'Envieu-me el punt de trobada per iniciar l\'excursió (o /skip per deixar el camp en blanc)',
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
            CommandHandler('help', help_command),
            MessageHandler([Filters.text], self.message)
        ]
        self.store = TinyDBStore()

    def start_command(self, bot, update, args):
        user_id = update.message.from_user.id
        self.store.new_draft(user_id)
        bot.sendMessage(update.message.chat_id,
                        text="Crearem un esdeveniment per a una excursió. El primer que heu de fer és enviar-me el nom de l\'excursió.")

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

    def skip_command(self, bot, update):
        user_id = update.message.from_user.id
        draft = self.store.get_draft(user_id)

        if draft:
            current_field = draft['current_field']
            field = FIELDS[current_field]

            if field['required']:
                bot.sendMessage(update.message.chat_id,
                                text="Aquest camp és necessari. " + field['message'])
            else:
                event = draft['event']
                current_field += 1
                self.update_draft(bot, event, user_id, update, current_field)

    def update_draft(self, bot, event, user_id, update, current_field):
        self.store.update_draft(user_id, event, current_field)

        if current_field <= len(FIELDS) - 1:
            bot.sendMessage(
                update.message.chat_id,
                text=FIELDS[current_field]['message']
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
