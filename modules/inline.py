# -*- coding: utf-8 -*-

import base64
import datetime
import json
from six.moves import urllib

from telegram import InlineQueryResultArticle, ParseMode, \
    InputTextMessageContent, InlineKeyboardButton, InlineKeyboardMarkup, Emoji
from telegram.ext import InlineQueryHandler, CallbackQueryHandler

from store import TinyDBStore


def create_event_payload(event):
    event_string = json.dumps(event)
    eight_bit_string = base64.b64encode(event_string.encode('ascii'))
    return urllib.parse.quote(eight_bit_string.decode('ascii'))


def create_keyboard(event, user):
    buttons = [
        InlineKeyboardButton(
            text="Calendari",
            url='https://lukaville.github.com/create-event-bot/static/add.html#' + create_event_payload(event)
        ),
        InlineKeyboardButton(
            text="Afegeix-m'hi",
            callback_data='go_' + str(event.eid)
        )
    ]

    if event.get('place'):
        buttons.append(InlineKeyboardButton(
            text="Mapa",
            url='https://maps.google.com/?q=' + urllib.parse.quote(event.get('place'))
        ))

    return [buttons, []]


def format_date(param):
    timestamp = int(param)
    date = datetime.datetime.fromtimestamp(timestamp)
    return date.strftime("%m/%d/%Y %H:%M")


def create_event_message(event, user):
    message_text = "*{name}*\n{date}\n".format(
        name=event['name'],
        date=format_date(event['date'])
    )

    if 'description' in event:
        message_text += '_' + event['description'] + '_\n'

    if 'place' in event:
        message_text += Emoji.ROUND_PUSHPIN + ' ' + event['place'] + '\n'

    if 'users' in event and len(event['users']) > 0:
        message_text += '\nHi aniran: \n'
        for u in event['users']:
            if u.get('username'):
                message_text += '@' + u['username'] + ' '

            message_text += '(' + u['first_name']
            if u.get('last_name'):
                message_text += ' ' + u['last_name']
            message_text += ')\n'

    return message_text


class InlineModule(object):
    def __init__(self):
        self.handlers = [
            InlineQueryHandler(self.inline_query),
            CallbackQueryHandler(self.callback_handler)
        ]
        self.store = TinyDBStore()

    def callback_handler(self, bot, update):
        query = update.callback_query
        data = query.data
        user = query.from_user.__dict__

        (command, event_id) = tuple(data.split('_'))
        event = self.store.get_event(event_id)

        if command == 'go':
            event = self.toggle_user(event, user)

        bot.editMessageText(text=create_event_message(event, user),
                            inline_message_id=query.inline_message_id,
                            reply_markup=InlineKeyboardMarkup(inline_keyboard=create_keyboard(event, user)),
                            parse_mode=ParseMode.MARKDOWN)

    def toggle_user(self, event, user):
        if not event.get('users'):
            event['users'] = []

        if any(u['id'] == user['id'] for u in event['users']):
            event['users'].remove(user)
        else:
            event['users'].append(user)

        self.store.update_event(event)
        return event

    def inline_query(self, bot, update):
        query = update.inline_query.query
        user_id = update.inline_query.from_user.id
        user = update.inline_query.from_user.__dict__

        results = []
        events = self.store.get_events(user_id, query)

        for event in events:
            keyboard = create_keyboard(event, user)
            result = InlineQueryResultArticle(id=event.eid,
                                              title=event['name'],
                                              description=format_date(event['date']),
                                              thumb_url='https://i.imgur.com/BgTaSzk.png',
                                              input_message_content=InputTextMessageContent(
                                                  create_event_message(event, user),
                                                  parse_mode=ParseMode.MARKDOWN
                                              ),
                                              reply_markup=InlineKeyboardMarkup(inline_keyboard=keyboard))
            results.append(result)

        bot.answerInlineQuery(
            update.inline_query.id,
            results=results,
            switch_pm_text='Crea una excursió nova...',
            switch_pm_parameter='new',
            is_personal=True
        )

    def get_handlers(self):
        return self.handlers
