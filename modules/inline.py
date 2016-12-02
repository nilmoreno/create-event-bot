# -*- coding: utf-8 -*-
import base64
import datetime
import locale
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
    button = [
        InlineKeyboardButton(
            text="\U0001F465 Afegeix-m'hi / treu-me'n",
            callback_data='go_' + str(event.eid)
        )
    ]

    button2 = [
        InlineKeyboardButton(
            text="\U0001F468\U0001F3FB",
            callback_data='goman_' + str(event.eid)
        ),
        InlineKeyboardButton(
            text="\U0001F469\U0001F3FB",
            callback_data='gowoman_' + str(event.eid)
        ),
        InlineKeyboardButton(
            text="\U0001F466\U0001F3FC",
            callback_data='goboy_' + str(event.eid)
        ),
        InlineKeyboardButton(
            text="\U0001F467\U0001F3FC",
            callback_data='gogirl_' + str(event.eid)
        )
    ]

    if event.get('parking'):
        button2.append(InlineKeyboardButton(
            text="\U0001F697",
            callback_data='gocar_' + str(event.eid)
        ))

    buttons = [
        InlineKeyboardButton(
            text="\U0001F4C6 Calendari",
            url='http://www.konfraria.org/calendari_celp/add.html#' + create_event_payload(event)
        )
    ]

    if event.get('route'):
        buttons.append(InlineKeyboardButton(
            text="\U0001F5FA Ruta",
            url=event.get('route')
        ))

    return [button, button2, buttons, []]


def format_date(param):
    locale.setlocale(locale.LC_TIME, "ca_ES.utf8")
    timestamp = int(param)
    date = datetime.datetime.fromtimestamp(timestamp)
    return date.strftime("%A, %d %B %Y a les %H.%M hores")


def create_event_message(event, user):
    message_text = "*{name}*\n{date}\n".format(
        name=event['name'],
        date=format_date(event['date'])
    )

    if 'description' in event:
        message_text += '\n_' + event['description'] + '_\n'

    if 'place' in event:
        message_text += '\n' + Emoji.ROUND_PUSHPIN + ' ' + event['place'] + ' [(mapa)](http://www.openstreetmap.org/search?query=' + urllib.parse.quote(event.get("place")) + ')\n'

    if 'parking' in event:
        message_text += Emoji.AUTOMOBILE + ' ' + event['parking'] + ' [(mapa)](http://www.openstreetmap.org/search?query=' + urllib.parse.quote(event.get("parking")) + ')\n'

#   if 'route' in event:
#       message_text += '\n' + Emoji.CLOCKWISE_DOWNWARDS_AND_UPWARDS_OPEN_CIRCLE_ARROWS + ' [Mapa amb la ruta](' + event['route'] + ')'

    if 'users' in event and len(event['users']) > 0:
        message_text += '\nHi aniran: \n'
        for u in event['users']:
            #message_text += '\U0001F449\U0001F3FC '
            message_text += '\u27A9 '
            
            message_text += u['first_name']
            if u.get('last_name'):
                message_text += ' ' + u['last_name']
            if u.get('username'):
                message_text += ' [\U0001F4AC](https://telegram.me/' + u['username'] + ')'
            message_text += ' '

            if u.get('man') and u['man'] == 1:
                message_text += '\U0001F468\U0001F3FB'
            if u.get('man') and u['man'] == 2:
                message_text += '\U0001F468\U0001F3FB\U0001F468\U0001F3FB'
            if u.get('man') and u['man'] == 3:
                message_text += '\U0001F468\U0001F3FB\U0001F468\U0001F3FB\U0001F468\U0001F3FB'
            if u.get('man') and u['man'] == 4:
                message_text += '\U0001F468\U0001F3FB\U0001F468\U0001F3FB\U0001F468\U0001F3FB\U0001F468\U0001F3FB'
            if u.get('man') and u['man'] == 5:
                message_text += '\U0001F468\U0001F3FB\U0001F468\U0001F3FB\U0001F468\U0001F3FB\U0001F468\U0001F3FB\U0001F468\U0001F3FB'
            if u.get('woman') and u['woman'] == 1:
                message_text += '\U0001F469\U0001F3FB'
            if u.get('woman') and u['woman'] == 2:
                message_text += '\U0001F469\U0001F3FB\U0001F469\U0001F3FB'
            if u.get('woman') and u['woman'] == 3:
                message_text += '\U0001F469\U0001F3FB\U0001F469\U0001F3FB\U0001F469\U0001F3FB'
            if u.get('woman') and u['woman'] == 4:
                message_text += '\U0001F469\U0001F3FB\U0001F469\U0001F3FB\U0001F469\U0001F3FB\U0001F469\U0001F3FB'
            if u.get('woman') and u['woman'] == 5:
                message_text += '\U0001F469\U0001F3FB\U0001F469\U0001F3FB\U0001F469\U0001F3FB\U0001F469\U0001F3FB\U0001F469\U0001F3FB'
            if u.get('boy') and u['boy'] == 1:
                message_text += '\U0001F466\U0001F3FC'
            if u.get('boy') and u['boy'] == 2:
                message_text += '\U0001F466\U0001F3FC\U0001F466\U0001F3FC'
            if u.get('boy') and u['boy'] == 3:
                message_text += '\U0001F466\U0001F3FC\U0001F466\U0001F3FC\U0001F466\U0001F3FC'
            if u.get('boy') and u['boy'] == 4:
                message_text += '\U0001F466\U0001F3FC\U0001F466\U0001F3FC\U0001F466\U0001F3FC\U0001F466\U0001F3FC'
            if u.get('boy') and u['boy'] == 5:
                message_text += '\U0001F466\U0001F3FC\U0001F466\U0001F3FC\U0001F466\U0001F3FC\U0001F466\U0001F3FC\U0001F466\U0001F3FC'
            if u.get('girl') and u['girl'] == 1:
                message_text += '\U0001F467\U0001F3FC'
            if u.get('girl') and u['girl'] == 2:
                message_text += '\U0001F467\U0001F3FC\U0001F467\U0001F3FC'
            if u.get('girl') and u['girl'] == 3:
                message_text += '\U0001F467\U0001F3FC\U0001F467\U0001F3FC\U0001F467\U0001F3FC'
            if u.get('girl') and u['girl'] == 4:
                message_text += '\U0001F467\U0001F3FC\U0001F467\U0001F3FC\U0001F467\U0001F3FC\U0001F467\U0001F3FC'
            if u.get('girl') and u['girl'] == 5:
                message_text += '\U0001F467\U0001F3FC\U0001F467\U0001F3FC\U0001F467\U0001F3FC\U0001F467\U0001F3FC\U0001F467\U0001F3FC'
            if u.get('car') and u['car'] == 1:
                message_text += '\U0001F697'
            if u.get('car') and u['car'] == 2:
                message_text += '\U0001F697\U0001F697'
            if u.get('car') and u['car'] == 3:
                message_text += '\U0001F697\U0001F697\U0001F697'
            message_text += '\n'
            
    message_text += "\n\U0001F527 Instruccions d'ús dels botons: [aquí](http://telegra.ph/Instruccions-d%c3%bas-CELP-familiar-11-28)."

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

        if not event.get('users'):
            event['users'] = []

        if any(u['id'] == user['id'] for u in event['users']):
              if any(u['id'] == user['id'] and u['man'] == 0 for u in event['users']):
                    user.update({'man': 0})
              elif any(u['id'] == user['id'] and u['man'] == 1 for u in event['users']):
                    user.update({'man': 1})
              elif any(u['id'] == user['id'] and u['man'] == 2 for u in event['users']):
                    user.update({'man': 2})
              elif any(u['id'] == user['id'] and u['man'] == 3 for u in event['users']):
                    user.update({'man': 3})
              elif any(u['id'] == user['id'] and u['man'] == 4 for u in event['users']):
                    user.update({'man': 4})
              elif any(u['id'] == user['id'] and u['man'] == 5 for u in event['users']):
                    user.update({'man': 5})

              if any(u['id'] == user['id'] and u['woman'] == 0 for u in event['users']):
                    user.update({'woman': 0})
              elif any(u['id'] == user['id'] and u['woman'] == 1 for u in event['users']):
                    user.update({'woman': 1})
              elif any(u['id'] == user['id'] and u['woman'] == 2 for u in event['users']):
                    user.update({'woman': 2})
              elif any(u['id'] == user['id'] and u['woman'] == 3 for u in event['users']):
                    user.update({'woman': 3})
              elif any(u['id'] == user['id'] and u['woman'] == 4 for u in event['users']):
                    user.update({'woman': 4})
              elif any(u['id'] == user['id'] and u['woman'] == 5 for u in event['users']):
                    user.update({'woman': 5})

              if any(u['id'] == user['id'] and u['boy'] == 0 for u in event['users']):
                    user.update({'boy': 0})
              elif any(u['id'] == user['id'] and u['boy'] == 1 for u in event['users']):
                    user.update({'boy': 1})
              elif any(u['id'] == user['id'] and u['boy'] == 2 for u in event['users']):
                    user.update({'boy': 2})
              elif any(u['id'] == user['id'] and u['boy'] == 3 for u in event['users']):
                    user.update({'boy': 3})
              elif any(u['id'] == user['id'] and u['boy'] == 4 for u in event['users']):
                    user.update({'boy': 4})
              elif any(u['id'] == user['id'] and u['boy'] == 5 for u in event['users']):
                    user.update({'boy': 5})

              if any(u['id'] == user['id'] and u['girl'] == 0 for u in event['users']):
                    user.update({'girl': 0})
              elif any(u['id'] == user['id'] and u['girl'] == 1 for u in event['users']):
                    user.update({'girl': 1})
              elif any(u['id'] == user['id'] and u['girl'] == 2 for u in event['users']):
                    user.update({'girl': 2})
              elif any(u['id'] == user['id'] and u['girl'] == 3 for u in event['users']):
                    user.update({'girl': 3})
              elif any(u['id'] == user['id'] and u['girl'] == 4 for u in event['users']):
                    user.update({'girl': 4})
              elif any(u['id'] == user['id'] and u['girl'] == 5 for u in event['users']):
                    user.update({'girl': 5})

              if any(u['id'] == user['id'] and u['car'] == 0 for u in event['users']):
                    user.update({'car': 0})
              elif any(u['id'] == user['id'] and u['car'] == 1 for u in event['users']):
                    user.update({'car': 1})
              elif any(u['id'] == user['id'] and u['car'] == 2 for u in event['users']):
                    user.update({'car': 2})
              elif any(u['id'] == user['id'] and u['car'] == 3 for u in event['users']):
                    user.update({'car': 3})

        if command == 'go':
            event = self.toggle_user(event, user)

        if command == 'goman':
            event = self.toggle_man(event, user)

        if command == 'gowoman':
            event = self.toggle_woman(event, user)

        if command == 'goboy':
            event = self.toggle_boy(event, user)

        if command == 'gogirl':
            event = self.toggle_girl(event, user)

        if command == 'gocar':
            event = self.toggle_car(event, user)

        bot.editMessageText(text=create_event_message(event, user),
                            inline_message_id=query.inline_message_id,
                            reply_markup=InlineKeyboardMarkup(inline_keyboard=create_keyboard(event, user)),
                            parse_mode=ParseMode.MARKDOWN,
			    disable_web_page_preview=True)

    def toggle_user(self, event, user):
        if not event.get('users'):
            event['users'] = []

        if any(u['id'] == user['id'] for u in event['users']):
            event['users'].remove(user)
        else:
            user.update({'man': 0})
            user.update({'woman': 0})
            user.update({'boy': 0})
            user.update({'girl': 0})
            user.update({'car': 0})
            event['users'].append(user)

        self.store.update_event(event)
        return event

    def toggle_man(self, event, user):
        if not event.get('users'):
            event['users'] = []

        if any(u['id'] == user['id'] and u['man'] == 0 for u in event['users']):
               event['users'].remove(user)
               user.update({'man': 1})
               event['users'].append(user)
        elif any(u['id'] == user['id'] and u['man'] == 1 for u in event['users']):
               event['users'].remove(user)
               user.update({'man': 2})
               event['users'].append(user)
        elif any(u['id'] == user['id'] and u['man'] == 2 for u in event['users']):
               event['users'].remove(user)
               user.update({'man': 3})
               event['users'].append(user)
        elif any(u['id'] == user['id'] and u['man'] == 3 for u in event['users']):
               event['users'].remove(user)
               user.update({'man': 4})
               event['users'].append(user)
        elif any(u['id'] == user['id'] and u['man'] == 4 for u in event['users']):
               event['users'].remove(user)
               user.update({'man': 5})
               event['users'].append(user)
        elif any(u['id'] == user['id'] and u['man'] == 5 for u in event['users']):
               event['users'].remove(user)
               user.update({'man': 0})
               event['users'].append(user)
        else:
               not_user = yes

        self.store.update_event(event)
        return event

    def toggle_woman(self, event, user):
        if not event.get('users'):
            event['users'] = []

        if any(u['id'] == user['id'] and u['woman'] == 0 for u in event['users']):
               event['users'].remove(user)
               user.update({'woman': 1})
               event['users'].append(user)
        elif any(u['id'] == user['id'] and u['woman'] == 1 for u in event['users']):
               event['users'].remove(user)
               user.update({'woman': 2})
               event['users'].append(user)
        elif any(u['id'] == user['id'] and u['woman'] == 2 for u in event['users']):
               event['users'].remove(user)
               user.update({'woman': 3})
               event['users'].append(user)
        elif any(u['id'] == user['id'] and u['woman'] == 3 for u in event['users']):
               event['users'].remove(user)
               user.update({'woman': 4})
               event['users'].append(user)
        elif any(u['id'] == user['id'] and u['woman'] == 4 for u in event['users']):
               event['users'].remove(user)
               user.update({'woman': 5})
               event['users'].append(user)
        elif any(u['id'] == user['id'] and u['woman'] == 5 for u in event['users']):
               event['users'].remove(user)
               user.update({'woman': 0})
               event['users'].append(user)
        else:
               not_user = yes

        self.store.update_event(event)
        return event

    def toggle_boy(self, event, user):
        if not event.get('users'):
            event['users'] = []

        if any(u['id'] == user['id'] and u['boy'] == 0 for u in event['users']):
               event['users'].remove(user)
               user.update({'boy': 1})
               event['users'].append(user)
        elif any(u['id'] == user['id'] and u['boy'] == 1 for u in event['users']):
               event['users'].remove(user)
               user.update({'boy': 2})
               event['users'].append(user)
        elif any(u['id'] == user['id'] and u['boy'] == 2 for u in event['users']):
               event['users'].remove(user)
               user.update({'boy': 3})
               event['users'].append(user)
        elif any(u['id'] == user['id'] and u['boy'] == 3 for u in event['users']):
               event['users'].remove(user)
               user.update({'boy': 4})
               event['users'].append(user)
        elif any(u['id'] == user['id'] and u['boy'] == 4 for u in event['users']):
               event['users'].remove(user)
               user.update({'boy': 5})
               event['users'].append(user)
        elif any(u['id'] == user['id'] and u['boy'] == 5 for u in event['users']):
               event['users'].remove(user)
               user.update({'boy': 0})
               event['users'].append(user)
        else:
               not_user = yes

        self.store.update_event(event)
        return event

    def toggle_girl(self, event, user):
        if not event.get('users'):
            event['users'] = []

        if any(u['id'] == user['id'] and u['girl'] == 0 for u in event['users']):
               event['users'].remove(user)
               user.update({'girl': 1})
               event['users'].append(user)
        elif any(u['id'] == user['id'] and u['girl'] == 1 for u in event['users']):
               event['users'].remove(user)
               user.update({'girl': 2})
               event['users'].append(user)
        elif any(u['id'] == user['id'] and u['girl'] == 2 for u in event['users']):
               event['users'].remove(user)
               user.update({'girl': 3})
               event['users'].append(user)
        elif any(u['id'] == user['id'] and u['girl'] == 3 for u in event['users']):
               event['users'].remove(user)
               user.update({'girl': 4})
               event['users'].append(user)
        elif any(u['id'] == user['id'] and u['girl'] == 4 for u in event['users']):
               event['users'].remove(user)
               user.update({'girl': 5})
               event['users'].append(user)
        elif any(u['id'] == user['id'] and u['girl'] == 5 for u in event['users']):
               event['users'].remove(user)
               user.update({'girl': 0})
               event['users'].append(user)
        else:
               not_user = yes

        self.store.update_event(event)
        return event

    def toggle_car(self, event, user):
        if not event.get('users'):
            event['users'] = []

        if any(u['id'] == user['id'] and u['car'] == 0 for u in event['users']):
               event['users'].remove(user)
               user.update({'car': 1})
               event['users'].append(user)
        elif any(u['id'] == user['id'] and u['car'] == 1 for u in event['users']):
               event['users'].remove(user)
               user.update({'car': 2})
               event['users'].append(user)
        elif any(u['id'] == user['id'] and u['car'] == 2 for u in event['users']):
               event['users'].remove(user)
               user.update({'car': 3})
               event['users'].append(user)
        elif any(u['id'] == user['id'] and u['car'] == 3 for u in event['users']):
               event['users'].remove(user)
               user.update({'car': 0})
               event['users'].append(user)
        else:
               not_user = yes

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
                                              thumb_url='https://raw.githubusercontent.com/nilmoreno/create-event-bot/master/images/celp_bot_calendar.png',
                                              input_message_content=InputTextMessageContent(
                                                  create_event_message(event, user),
                                                  parse_mode=ParseMode.MARKDOWN,
						  disable_web_page_preview=True
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
