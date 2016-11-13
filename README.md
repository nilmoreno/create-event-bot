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

Add your [allowed users id](https://github.com/nilmoreno/create-event-bot/blob/master/modules/commands.py#L156). <br/>You can know it with some bots like [@MyIDbot](http://telegram.me/myidbot).

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

* Bot images:
  * [Calendar](https://www.flickr.com/photos/dafnecholet/5374200948/in/photolist-9bUbH3-3xU18-9Tjoap-9Tjo7V-3qMfSb-rUyG8-6hEsk-3qMfY7-76v1pT-5SLjF-5vZnPr-bR4TB-2aNjrB-5jLKHc-7AC132-8QQ8K3-5U7uqn-9akFr6-9gZGC3-5r3sad-5r2wbo-5r2wGm-5r3nKN-5r3uYS-5r3uvA-sY9ob-aYAHs-cT9Bh-fgYtmY-9dQRes-5RHQEm-zBgjg-vj3yV-ymHeT-g8K8bv-7baY6F-aGRbBg-6hByqe-5r3rBf-5qY2DH-5r3tBY-5qY8AB-qm28Qn-5qY9ut-5qY3yF-5qYb28-rL7o8-5r2x8f-5qY85t-5NEAjs) by Dafne Cholet [(CC BY 2.0)](https://creativecommons.org/licenses/by/2.0/)
  * [Family hiking at Hart Prairie2](https://www.flickr.com/photos/rodeime/16422091068/in/photolist-r2avxb-nLgDxt-nmY3nS-pG2Gx4-cnr1Xm-o6NhJ8-47ieyA-cRBwrL-5mrndC-nYcXvg-pT3g6t-hf8xL-c8cmF1-anJkXy-fKraHx-9pAAVF-opY3Lc-fRXYD6-nPjF7i-G4M29N-3ufcsP-ftCVqD-sTqWz-8rad18-nPiUm8-heZ3o-fffrTu-8F18vH-oSa9bV-q1RjWn-ftCWk8-o2No4G-47ieRb-nmzKA5-hMwqt-p4VXad-MjU6h-a4KtL7-a4JNCj-nz3o6E-fMANoz-a4GrWt-a4FCZK-Mk1NL-eCX5B5-b6orYB-MjSzw-3oVbgu-FvV3L-gjU7bD) by Roderick Eime [(CC BY 2.0)](https://creativecommons.org/licenses/by/2.0/)
  * [Valley](https://www.flickr.com/photos/rubenholthuijsen/9389936465/) by Ruben Holthuijsen [(CC BY 2.0)](https://creativecommons.org/licenses/by/2.0/)
  * [Walk away](https://www.flickr.com/photos/atreyusan/5234228397/in/photolist-8YwMKc-bsXEdd-8mJb8E-Bq2if-miFGzH-miF5SQ-miFzs6-miEvaj-9DCAmt-BpX7k-5JV8UB-miEqn3-BpUxe-miGjz6-3F9ho9-miFrh8-BpZMe-miFFWP-BpXnh-82WcMB-miCUQv-BpYju-91mmWZ-bPY8v-miEmey-miHN4U-BpVM3-BpUpx-cfKd3y-Bq1wS-BpZ1Z-miDzgg-4oFQDd-8mF37R-BpWJC-9DFwjw-91prXU-miFQti-BpXha-BpWst-8mEBKZ-miGPSz-miHz83-miFWma-miFyLg-bPY8P-miDTsX-miHXiL-BpVUH-BpUEb) by Iñaki Pérez de Albéniz [(CC BY 2.0)](https://creativecommons.org/licenses/by/2.0/)

* Landscape images (add.html):
  * [Boots by the loch](https://www.flickr.com/photos/bods/6823262185/in/photolist-boX18t-eiqjrF-7Gni8Q-d4k1CC-7SwSoq-ecSfit-ecShfz-cgUitY-eiw4Vs-7u5mpz-oGPmek-aRSa9e-9dNCN4-2QLjZW-aSunSi-efhBsV-7CdRhE-Pd7mK-bDpKy1-q5dTZo-bBg3yQ-ebbDmL-efhzMc-jfNrRJ-bXjcZ4-3R7WMF-w4aj1r-6dWt7a-i7bVg1-hZ5YJt-4fbZju-aceLr8-nPf6yM-4HTbPK-9jEXYC-HUBNb7-rFtqNF-7KTXA-9gYUUs-4HTdvD-cSPab5-62P9zK-9cKkH-gXoqpd-c4sLJb-b8AKUt-9nVGkQ-2Jp4d-PMVZU-7mpksU) by Andrew Bowden [(CC BY-SA 2.0)](https://creativecommons.org/licenses/by-sa/2.0/)
  * [Calella de Palafrugell (Girona)](https://www.flickr.com/photos/asarasua/3865994698/in/photolist-9TjeFk-8usmpD-8xMGLz-8xQJC3-8v5Xa1-8xMGia-8xQ9E5-6TCex1-8usmQr-8xMGUM-8uskcv-8uvq2o-8uskBM-e7ZWWY-8xQHF1-8xM8J6-8xQ9oU-8uskVv-6TyeWr-8xQac7-o1jMLT-cGxT8h-ixxEEY-rERmgt-imdWtK-8xM7Sn-bSmbSt-8xQ873-nxUyhG-dNrcsF-e7ZWXb-viFSjy-bDru85-dNZCCT-sEETy7-sX3TGN-8xQHby-8xQ9gd-CUmdc1-8xQJRU-B4x3ms-sXgmSP-e7Uh6D-e7ZWXh-e7Uh5g-s1s5pV-bF53su-ok37CL-CvXxUF-ok37yC) by Asier Sarasua Aranberri [(CC BY-SA 2.0)](https://creativecommons.org/licenses/by-sa/2.0/)
  * [Collserola](https://www.flickr.com/photos/borkurdotnet/4711243128/in/photolist-8bjmrN-6U1cdV-9oHhws-kDVSL-4ry3jg-4vRDs4-8qPaow-4vWBvj-4ihZk-xLwhQh-r2BKCC-5ewt5v-8mZHVJ-7BHaxb-7BDmKR-8SBiy6-7xWmZM-8SBjhK-9AY6sv-pex5Za-7y1wSA-5eRGkC-7y16GC-7xWn7D-tQB2E-7y18pC-4hsKT-7y1ct1-4hsYV-7Sjuk9-7xWmBr-4hsPA-4BG8rg-c3zUuN-p7iuzc-87P3sc-cPxKrw-oQ4zZH-oQ5wbX-7y1bed-49ds8Z-49hvbd-7xWiBF-zxMLc-7y1aAm-4soCJd-pPfZii-7y15Pb-6KWdQV-i38Nhx) by Börkur Sigurbjörnsson [(CC BY 2.0)](https://creativecommons.org/licenses/by/2.0/)
  * [IMG_5042Montserrat_2400](https://www.flickr.com/photos/macskapocs/30637133196/in/photolist-NFijjq-nPyjEt-nPxCMW-nPzdNM-oiC2sd-pqPgRt-o3PiGh-o77Mjh-o6j2cx-BmimZ1-Mz4nDR-oiP9pt-nNn5Zo-o53pa5-f9Ak8y-nNPAe2-nPzdhM-o77NSY-B7NT3h-sQmC2J-oUf7iK-4fcT6s-jaCgTE-hTgtc-acoV5n-4fcPCU-91qgKF-6DphLj-p9ABjq-o7dvkH-cYhJGJ-4f8TRg-eznjB1-qZVhE6-rj9kqM-rAbdb5-6DphZS-BRGHig-o6Wn2g-t7Y87x-aAjCwK-91tmhm-nPHPmG-jaxRVB-vwoTXh-9DzaiB-8K4ws9-hTduE-yzKYt6-csEEu5) by Gergely Csatari [(CC BY-SA 2.0)](https://creativecommons.org/licenses/by-sa/2.0/)
  * [Munyanyes de Colera, les Alberes](https://www.flickr.com/photos/angela_llop/17947685259/in/photolist-cTyMcU-dHLNeX-dHLMRt-dHLNKz-dHLPDB-dHLQ7D-dHSe9N-dHSfVw-63CreQ-dHL4un-63DJdd-vpSaJY-7YCHmj-uKr2fC-vGrsfi-dHRxiC-63ybbF-dHL5ST-dHRwVG-dHL7fT-dHL46z-2nnV3-7GhJbg-dHRvLo-tkYzxi) by Angela Llop [(CC BY-SA 2.0)](https://creativecommons.org/licenses/by-sa/2.0/)
  * [paratges](https://www.flickr.com/photos/irinoko/3045640340/in/photolist-5D8GLm-bqecNn-bqe8PH-bqebbF-5BVgi8-85WeU6-5D8Dgs-zNL358-zMDsVh-zwgfSk-zPFjq4-zwamzA-zwfkVD-zw8BjQ-yRUmcc-zwavxq-yRTMmH-yRJJmy-zNL49x-yRUpsk-yRUbnx-zwa45L-zw9qT7-zwbm53-zwfy5t-zLsD5s-zw9GP5-zMDA6u-zw9wGG-zMDeu9-yRJYxE-zwbSA3-zLsoJJ-zMDMwL-zwgeX4-zw9CgN-zLsUi3-zwbD5A-yRJVdy-zLscnf-zMDVBy-zwbprU-zPF5gc-zLsPvY-zwfr1t-yRUnxZ-zNLFne-zwc783-zwgvUp-zLsy5s) by Irinoko [(CC BY 2.0)](https://creativecommons.org/licenses/by/2.0/)
  * [Pedraforca](https://www.flickr.com/photos/smartinmolina/8482411813/in/photolist-dVyzvx-dVE7JW-boYxE8-7fSwem-56A2WJ-56A2Au-dNfriy-cPvp7U-5XmyZG-56zXjG-56vNMM-56A3A1-56vQV2-JuuKz-aSjpv6-56zWQE-9BMaN-56vLV2-bmBwtP-56vQdB-Ju382-56zWYW-56vS1D-56A1Hh-56vRPa-56A1gf-56A63h-56zYTb-56vVgH-56vPeM-56vSJP-56vMJx-56vNkr-56vQwF-56vM7H-56vRqc-osF9VT-56vPCp-8qJRbr-8apnB2-oH8uJo-56A6bA-7fB5t6-56vPX8-56zXxW-56A4rw-ynEie-oK8vdo-56A221-56vSg6) by Sílvia Martín [(CC BY 2.0)](https://creativecommons.org/licenses/by/2.0/)
  * [Pirineus](https://www.flickr.com/photos/jordimarsol/3280913333/in/photolist-5ZVxeg-a5WtPr-a5Wtbg-dsZ995-aqW4Vj-a5Wxwv-bB19BZ-aqW1Y5-a5ZjPY-aqWgf1-vVVUra-dsZax5-a5ZmNL-dsYNnk-aqWuaj-3Q6X5G-a5ZnuQ-a5WwUc-9MqtH-aqVWN7-dsZ9ZA-4tqnH2-NTJAB-a5ZjK3-5hptwo-aceso4-artK8j-aqWaTm-dsYUTz-aqVqnQ-aqTrSa-aqSZpg-jWybF-5dUjyR-5ZVwsM-ayVQYM-a5ZkS7-6CQ3Cf-aqSSCD-nSCaXH-agSVfM-6FCKWw-ayVS36-ayVLd8-a5Zpzm-a5ZoMU-achai5-aqT31B-a5Wz26-a5Zn29) by Jordi Marsol [(CC BY 2.0)](https://creativecommons.org/licenses/by/2.0/)
  * [Sierra del Cadí I](https://www.flickr.com/photos/julen-iturbe/4821501013/in/photolist-8m4sgP-dafuit-8v4Zer-8m4s1k-dNftwE-8v8Gb7-Ep5XXX-dN9UVt-8v5FfV-8v5n8M-dN9VYV-eWRZZh-psjBMY-eR1Z6w-8v8o9N-8v7U8s-mQwSJR-mHD8gY-bmBXsr-bmBPGr-8v5J46-8v85Ds-8v5jux-8v8r6Q-8v4Vnn-8v7Tiy-8v57Pa-8v5NM8-8v89W3-8v7V4j-bmBDGa-8v5qMc-bmBThX-8v86oQ-8v7XBo-8v7YXd-AJwEGY-zNEuqq-aQPgTc-8v5KS4-8v8Kth-8v8Hew-8v8PC5-8v88cb-8v8rZS-8v5sTZ-8v8p8f-8v8DaQ-i6ZuH6-8v4WSr) by Julen Iturbe-Ormaetxe [(CC BY-SA 2.0)](https://creativecommons.org/licenses/by-sa/2.0/)

* Logo:
  * :copyright: [CELP logo](https://image.jimcdn.com/app/cms/image/transf/none/path/sab30b0734d33b1b6/image/ieb42f422f076b68d/version/1385465900/image.jpg) is a copyrighted logo, and can't be used without permissions.

Contact
-------

* lakonfrariadelavila *at* gmail *dot* com
