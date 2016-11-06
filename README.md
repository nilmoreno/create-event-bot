# Bot del CELP

* **CELP_bot** is a Telegram inline calendar based on [@createeventbot](https://telegram.me/createeventbot).
* This bot is private, only users with permissions.

General usage
-------------

Usage: @celp_bot [event name]

Installation
------------

* First, you need Python 3 (pre-installed on Ubuntu) and package manager:
```
$sudo apt-get install python-pip3
```

Then, you need to install requirements. Go to the directory where requirements.txt are, and run:
```
$sudo pip3 install -r requirements.txt
```

Copy source files to your local machine or server.

Add your [Telegram token](https://github.com/nilmoreno/create-event-bot/blob/master/bot.py#L31)

Add your [allowed users id](https://github.com/nilmoreno/create-event-bot/blob/master/modules/commands.py#L65). <br/>You can know it with some bots like [@MyIDbot](http://telegram.me/myidbot).

And finally launch the bot with (in the directory where bot.py are):
```
$python3 bot.py
```

Credits
-------

* [Create-event-bot](https://github.com/lukaville/create-event-bot) by Lukaville

* [Python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
* [Requests](https://github.com/kennethreitz/requests) by Kenneth Reitz
* [TinyDB](https://github.com/msiemens/tinydb/) by Markus Siemens
* [Parsedatetime](https://github.com/bear/parsedatetime) by Mike Taylor

* [Leaflet](http://leafletjs.com/)
* [Leaflet.Elevation](https://github.com/MrMufflon/Leaflet.Elevation) by Felix Bache
* [Leaflet.Control.Credits](https://github.com/gregallensworth/L.Control.Credits) by Greg Allensworth
* [Leaflet.Control.SidebySide](https://github.com/digidem/leaflet-side-by-side) by Digital Democracy
* [Leaflet GPX](https://github.com/mpetazzoni/leaflet-gpx) by Maxime Petazzoni

Contact
-------

* lakonfrariadelavila *at* gmail *dot* com
