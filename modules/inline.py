# -*- coding: utf-8 -*-
import base64
import time
import datetime
from parsedatetime import parsedatetime
import locale
import json
import csv
from six.moves import urllib

from telegram import InlineQueryResultArticle, ParseMode, \
    InputTextMessageContent, InlineKeyboardButton, InlineKeyboardMarkup, Emoji
from telegram.ext import InlineQueryHandler, CallbackQueryHandler, ChosenInlineResultHandler

from store import TinyDBStore

from config import params, links, allowed_users, other_users


def create_event_payload(event):
    event_string = json.dumps(event)
    eight_bit_string = base64.b64encode(event_string.encode('ascii'))
    return urllib.parse.quote(eight_bit_string.decode('ascii'))


def create_keyboard(event, user):
    if event.get('invite'):
        button = [
            InlineKeyboardButton(
                text="\U0001F4E2 Entreu a CELP familiar",
                url=links['channel']
            )
        ]
        return [button, []]

    else:
        eventdate2= int(event['date'])

        today= datetime.datetime.now()
        day = str(today.day)
        month = str(today.month)
        year = str(today.year)
        hour = str(today.hour)
        minute = str(today.minute)
        today2= month + '/' + day + '/' + year + ' ' + hour + ':' + minute

        cal = parsedatetime.Calendar()
        time_struct, parse_status = cal.parse(today2)
        timestamp = time.mktime(datetime.datetime(*time_struct[:6]).timetuple())
        today3= int(timestamp)

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
                url='http://celapalma.org/calendari_celp/add.html#' + create_event_payload(event)
            )
        ]

        if event.get('route'):
            buttons.append(InlineKeyboardButton(
                text="\U0001F5FA Ruta",
                url=event.get('route')
            ))

        if today3 > eventdate2:
             return [buttons, []]
        else:
             return [button, button2, buttons, []]


def format_date(param):
    locale.setlocale(locale.LC_TIME, "ca_ES.utf8")
    timestamp = int(param)
    date = datetime.datetime.fromtimestamp(timestamp)
    return date.strftime("%A, %d %B %Y a les %H.%M hores")


def create_event_message(event, user):
    if event['name'] == 'Convideu al canal':
        if event['invite'] == 'yes':
            user_f = user['first_name']
            user_ln = user['last_name']
            user_u = user['username']
            if user_ln != "" and user_u != "":
               user_d= user_f + " " + user_ln + "* (podeu contactar-hi amb @" + user_u + ")"
            elif user_ln == "" and user_u != "":
               user_d= user_f + "* (podeu contactar-hi amb @" + user_u + ")" 
            elif user_ln != "" and user_u == "":
               user_d= user_f + " " + user_ln + "*"
            elif user_ln == "" and user_u == "":
               user_d= user_f + "*"
            message_text = 'Missatge del robot del CELP\n\n\u2709\uFE0F *' +user_d + " us convida al canal privat *«CELP familiar»*.\n\nPer entrar-hi premeu el botó \U0001F4E2 _Entreu a CELP familiar_, i a continuació seleccioneu *«JOIN»* o bé *«AFEGEIX-M'HI»*.\n\nSi us afegiu a aquest canal privat només rebreu informació de les excursions i tindreu l'opció d'apuntar-vos-hi, però això no és un grup, per tant ningú hi pot escriure."
            return message_text
    else:
        eventdate2= int(event['date'])

        today= datetime.datetime.now()
        day = str(today.day)
        month = str(today.month)
        year = str(today.year)
        hour = str(today.hour)
        minute = str(today.minute)
        today2= month + '/' + day + '/' + year + ' ' + hour + ':' + minute

        cal = parsedatetime.Calendar()
        time_struct, parse_status = cal.parse(today2)
        timestamp = time.mktime(datetime.datetime(*time_struct[:6]).timetuple())
        today3= int(timestamp)

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
            if today3 > eventdate2:
                message_text += '\nS\'hi van apuntar: \n'
            else:
                message_text += '\nHi aniran: \n'
            for u in event['users']:
                #message_text += '\U0001F449\U0001F3FC '
                message_text += '\u27A9 '
        
                message_text += u['first_name']
                if u.get('last_name'):
                    message_text += ' ' + u['last_name']
                if u.get('username') and eventdate2 > today3:
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
        if today3 > eventdate2:
             message_text += "\n\U0001F5D3 Excursió tancada"
        else:
             message_text += "\n\U0001F527 Instruccions d'ús dels botons: [aquí](http://telegra.ph/Instruccions-d%c3%bas-CELP-familiar-11-28)."

        return message_text


class InlineModule(object):
    def __init__(self):
        self.handlers = [
            InlineQueryHandler(self.inline_query),
            CallbackQueryHandler(self.callback_handler),
            ChosenInlineResultHandler(self.inline_stats)
        ]
        self.store = TinyDBStore()

    def inline_stats(self, bot, update):
        today= datetime.datetime.now()
        dayraw = today.day
        if int(dayraw) < 10:
           day = '0' + str(dayraw)
        else:
           day = str(dayraw)
        monthraw = today.month
        if int(monthraw) < 10:
           month = '0' + str(monthraw)
        else:
           month = str(monthraw)
        year = today.year
        today2= day + '/' + month + '/' + str(year)
        if update.chosen_inline_result:
            selected= update.chosen_inline_result.result_id
            user_id = update.chosen_inline_result.from_user.id
            user_f = update.chosen_inline_result.from_user.first_name
            user_ln = update.chosen_inline_result.from_user.last_name
            user_u = update.chosen_inline_result.from_user.username
            if user_ln == '':
                user_ln= 'NO'
            if user_u == '':
                user_u= 'NO'
            if selected == '1':
                 stat= today2 + ';user#id' + str(user_id) + ';' + str(user_f) + ';' + str(user_ln) + ';@' + str(user_u)
                 with open('invites.csv','a',newline='') as f:
                     writer=csv.writer(f)
                     writer.writerow([stat])

    def callback_handler(self, bot, update):
        query = update.callback_query
        data = query.data
        user = query.from_user.__dict__

        (command, event_id) = tuple(data.split('_'))
        event = self.store.get_event(event_id)

        eventdate2= int(event['date'])

        today= datetime.datetime.now()
        day = str(today.day)
        month = str(today.month)
        year = str(today.year)
        hour = str(today.hour)
        minute = str(today.minute)
        today2= month + '/' + day + '/' + year + ' ' + hour + ':' + minute

        cal = parsedatetime.Calendar()
        time_struct, parse_status = cal.parse(today2)
        timestamp = time.mktime(datetime.datetime(*time_struct[:6]).timetuple())
        today3= int(timestamp)

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

        if command == 'go' and eventdate2 > today3:
            event = self.toggle_user(event, user)

        if command == 'goman' and eventdate2 > today3:
            event = self.toggle_man(event, user)

        if command == 'gowoman' and eventdate2 > today3:
            event = self.toggle_woman(event, user)

        if command == 'goboy' and eventdate2 > today3:
            event = self.toggle_boy(event, user)

        if command == 'gogirl' and eventdate2 > today3:
            event = self.toggle_girl(event, user)

        if command == 'gocar' and eventdate2 > today3:
            event = self.toggle_car(event, user)

        if today3 > eventdate2:
            event = self.past_event(event, user)

        bot.editMessageText(text=create_event_message(event, user),
                            inline_message_id=query.inline_message_id,
                            reply_markup=InlineKeyboardMarkup(inline_keyboard=create_keyboard(event, user)),
                            parse_mode=ParseMode.MARKDOWN,
			    disable_web_page_preview=True)

        if data.startswith( 'goman' ):
            callback_query_id=query.id
            bot.answerCallbackQuery(callback_query_id=query.id, text="Heu canviat el nombre d'homes adults que assistiran a l'excursió")
        elif data.startswith( 'gowoman' ):
            callback_query_id=query.id
            bot.answerCallbackQuery(callback_query_id=query.id, text="Heu canviat el nombre de dones adultes que assistiran a l'excursió")
        elif data.startswith( 'goboy' ):
            callback_query_id=query.id
            bot.answerCallbackQuery(callback_query_id=query.id, text="Heu canviat el nombre de nens que assistiran a l'excursió")
        elif data.startswith( 'gogirl' ):
            callback_query_id=query.id
            bot.answerCallbackQuery(callback_query_id=query.id, text="Heu canviat el nombre de nenes que assistiran a l'excursió")
        elif data.startswith( 'gocar' ):
            callback_query_id=query.id
            bot.answerCallbackQuery(callback_query_id=query.id, text="Heu canviat el nombre de cotxes per a l'excursió")
        elif data.startswith( 'go' ):
            callback_query_id=query.id
            bot.answerCallbackQuery(callback_query_id=query.id, text="Heu canviat la vostra assistència a l'excursió")

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

    def past_event(self, event, user):
        self.store.update_event(event)
        return event

    def inline_query(self, bot, update):
        query = update.inline_query.query
        user_id = update.inline_query.from_user.id
        user = update.inline_query.from_user.__dict__

        if str(user_id) in allowed_users.values():
             results = []
             events = self.store.get_events(user_id, query)

             for event in events:
                 keyboard = create_keyboard(event, user)
                 result = InlineQueryResultArticle(id=event.eid,
                                                   title=event['name'],
                                                   description=event['description'],
                                                   thumb_url='http://celapalma.org/calendari_celp/inline_images/celp_bot_calendar.png',
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

        elif str(user_id) in other_users.values():
             results = []
             events = self.store.get_events(user_id, query)

             for event in events:
                 keyboard = create_keyboard(event, user)
                 result = InlineQueryResultArticle(id=event.eid,
                                                   title=event['name'],
                                                   description=event['description'],
                                                   thumb_url='http://celapalma.org/calendari_celp/inline_images/celp_bot_imatge.png',
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
                 #switch_pm_text='Crea una excursió nova...',
                 #switch_pm_parameter='new',
                 is_personal=True
             )

    def get_handlers(self):
        return self.handlers
