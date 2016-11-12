# Bot del CELP

* **CELP_bot** is a Telegram inline calendar based on [@createeventbot](https://telegram.me/createeventbot).
* This bot is private, only users with permissions can create hikes :closed_lock_with_key:
* Idea: Organization administrators create hikes with this Telegram bot, and share it in a Telegram private channel. Members in this channel can join to the hike.
* Bot made for a hiking non-proffit organization: [**CELP** - Centre excursionista de la Palma de Cervelló](http://celapalma.jimdo.com/) 

Descripció
----------

> El robot està pensat perquè només alguns administradors del centre excursionista puguin crear excursions, aquest és el motiu pel qual el robot és privat.

> El robot es complementa amb un [canal privat a Telegram](https://telegram.org/faq_channels), on es comparteixen les excursions generades amb el robot. Des del canal tots els membres poden accedir a la informació de l'excursió i poden informar de si tenen intenció de participar-hi o no.

General usage
-------------

Usage: @celp_bot [hike name]

Installation
------------

* First, you need Python 3 (pre-installed on Ubuntu) and package manager:
```
$sudo apt-get install python-pip3
```

Copy source files to your local machine or server.

Then, you need to install requirements. Go to the directory where requirements.txt are, and run:
```
$sudo pip3 install -r requirements.txt
```

Add your [Telegram token](https://github.com/nilmoreno/create-event-bot/blob/master/bot.py#L31)

Add your [allowed users id](https://github.com/nilmoreno/create-event-bot/blob/master/modules/commands.py#L65). <br/>You can know it with some bots like [@MyIDbot](http://telegram.me/myidbot).

And finally launch the bot with (in the directory where bot.py are):
```
$python3 bot.py
```

Credits
-------

* [Create-event-bot](https://github.com/lukaville/create-event-bot) by Nickolay Chameev

* Python packages:
  * [Parsedatetime](https://github.com/bear/parsedatetime) by Mike Taylor
  * [Python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
  * [Requests](https://github.com/kennethreitz/requests) by Kenneth Reitz
  * [TinyDB](https://github.com/msiemens/tinydb/) by Markus Siemens
  * [Validators](https://github.com/kvesteri/validators) by Konsta Vesterinen

* To generate add.html page:
  * [Base64.js](https://github.com/dankogai/js-base64) by Dan Kogai
  * [jQuery](https://jquery.com/)
  * [OuiCal](https://github.com/carlsednaoui/add-to-calendar-buttons) by Carl Sednaoui
  * [Twemoji](https://github.com/twitter/twemoji) by Twitter

* Leaflet&Leaflet plugins:
  * [Leaflet](http://leafletjs.com/)
  * [Leaflet.Control.Credits](https://github.com/gregallensworth/L.Control.Credits) by Greg Allensworth
  * [Leaflet.Control.SidebySide](https://github.com/digidem/leaflet-side-by-side) by Digital Democracy
  * [Leaflet.Elevation](https://github.com/MrMufflon/Leaflet.Elevation) by Felix Bache
  * [Leaflet GPX](https://github.com/mpetazzoni/leaflet-gpx) by Maxime Petazzoni

* To generate gpx files:
  * [GraphHopper maps](https://graphhopper.com/maps/)

* Images:
  * [Calendar](https://www.flickr.com/photos/dafnecholet/5374200948/in/photolist-9bUbH3-3xU18-9Tjoap-9Tjo7V-3qMfSb-rUyG8-6hEsk-3qMfY7-76v1pT-5SLjF-5vZnPr-bR4TB-2aNjrB-5jLKHc-7AC132-8QQ8K3-5U7uqn-9akFr6-9gZGC3-5r3sad-5r2wbo-5r2wGm-5r3nKN-5r3uYS-5r3uvA-sY9ob-aYAHs-cT9Bh-fgYtmY-9dQRes-5RHQEm-zBgjg-vj3yV-ymHeT-g8K8bv-7baY6F-aGRbBg-6hByqe-5r3rBf-5qY2DH-5r3tBY-5qY8AB-qm28Qn-5qY9ut-5qY3yF-5qYb28-rL7o8-5r2x8f-5qY85t-5NEAjs) by Dafne Cholet [(CC BY 2.0)](https://creativecommons.org/licenses/by/2.0/)
  * [Family hiking at Hart Prairie2](https://www.flickr.com/photos/rodeime/16422091068/in/photolist-r2avxb-nLgDxt-nmY3nS-pG2Gx4-cnr1Xm-o6NhJ8-47ieyA-cRBwrL-5mrndC-nYcXvg-pT3g6t-hf8xL-c8cmF1-anJkXy-fKraHx-9pAAVF-opY3Lc-fRXYD6-nPjF7i-G4M29N-3ufcsP-ftCVqD-sTqWz-8rad18-nPiUm8-heZ3o-fffrTu-8F18vH-oSa9bV-q1RjWn-ftCWk8-o2No4G-47ieRb-nmzKA5-hMwqt-p4VXad-MjU6h-a4KtL7-a4JNCj-nz3o6E-fMANoz-a4GrWt-a4FCZK-Mk1NL-eCX5B5-b6orYB-MjSzw-3oVbgu-FvV3L-gjU7bD) by Roderick Eime [(CC BY 2.0)](https://creativecommons.org/licenses/by/2.0/)
  * [Valley](https://www.flickr.com/photos/rubenholthuijsen/9389936465/) by Ruben Holthuijsen [(CC BY 2.0)](https://creativecommons.org/licenses/by/2.0/)
  * [Walk away](https://www.flickr.com/photos/atreyusan/5234228397/in/photolist-8YwMKc-bsXEdd-8mJb8E-Bq2if-miFGzH-miF5SQ-miFzs6-miEvaj-9DCAmt-BpX7k-5JV8UB-miEqn3-BpUxe-miGjz6-3F9ho9-miFrh8-BpZMe-miFFWP-BpXnh-82WcMB-miCUQv-BpYju-91mmWZ-bPY8v-miEmey-miHN4U-BpVM3-BpUpx-cfKd3y-Bq1wS-BpZ1Z-miDzgg-4oFQDd-8mF37R-BpWJC-9DFwjw-91prXU-miFQti-BpXha-BpWst-8mEBKZ-miGPSz-miHz83-miFWma-miFyLg-bPY8P-miDTsX-miHXiL-BpVUH-BpUEb) by Iñaki Pérez de Albéniz [(CC BY 2.0)](https://creativecommons.org/licenses/by/2.0/)

* Logo:
  * :copyright: [CELP logo](https://image.jimcdn.com/app/cms/image/transf/none/path/sab30b0734d33b1b6/image/ieb42f422f076b68d/version/1385465900/image.jpg) is a copyrighted logo, and can't be used without permissions.

Contact
-------

* lakonfrariadelavila *at* gmail *dot* com
