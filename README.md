# Robot del CELP

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
  * [Map.Meurisse](http://map.meurisse.org/)

* Bot images:
  * [Calendar](https://www.flickr.com/photos/dafnecholet/5374200948/in/photolist-9bUbH3-3xU18-9Tjoap-9Tjo7V-3qMfSb-rUyG8-6hEsk-3qMfY7-76v1pT-5SLjF-5vZnPr-bR4TB-2aNjrB-5jLKHc-7AC132-8QQ8K3-5U7uqn-9akFr6-9gZGC3-5r3sad-5r2wbo-5r2wGm-5r3nKN-5r3uYS-5r3uvA-sY9ob-aYAHs-cT9Bh-fgYtmY-9dQRes-5RHQEm-zBgjg-vj3yV-ymHeT-g8K8bv-7baY6F-aGRbBg-6hByqe-5r3rBf-5qY2DH-5r3tBY-5qY8AB-qm28Qn-5qY9ut-5qY3yF-5qYb28-rL7o8-5r2x8f-5qY85t-5NEAjs) by Dafne Cholet [(CC BY 2.0)](https://creativecommons.org/licenses/by/2.0/)
  * [Family hiking at Hart Prairie2](https://www.flickr.com/photos/rodeime/16422091068/in/photolist-r2avxb-nLgDxt-nmY3nS-pG2Gx4-cnr1Xm-o6NhJ8-47ieyA-cRBwrL-5mrndC-nYcXvg-pT3g6t-hf8xL-c8cmF1-anJkXy-fKraHx-9pAAVF-opY3Lc-fRXYD6-nPjF7i-G4M29N-3ufcsP-ftCVqD-sTqWz-8rad18-nPiUm8-heZ3o-fffrTu-8F18vH-oSa9bV-q1RjWn-ftCWk8-o2No4G-47ieRb-nmzKA5-hMwqt-p4VXad-MjU6h-a4KtL7-a4JNCj-nz3o6E-fMANoz-a4GrWt-a4FCZK-Mk1NL-eCX5B5-b6orYB-MjSzw-3oVbgu-FvV3L-gjU7bD) by Roderick Eime [(CC BY 2.0)](https://creativecommons.org/licenses/by/2.0/)
  * [Valley](https://www.flickr.com/photos/rubenholthuijsen/9389936465/) by Ruben Holthuijsen [(CC BY 2.0)](https://creativecommons.org/licenses/by/2.0/)
  * [Walk away](https://www.flickr.com/photos/atreyusan/5234228397/in/photolist-8YwMKc-bsXEdd-8mJb8E-Bq2if-miFGzH-miF5SQ-miFzs6-miEvaj-9DCAmt-BpX7k-5JV8UB-miEqn3-BpUxe-miGjz6-3F9ho9-miFrh8-BpZMe-miFFWP-BpXnh-82WcMB-miCUQv-BpYju-91mmWZ-bPY8v-miEmey-miHN4U-BpVM3-BpUpx-cfKd3y-Bq1wS-BpZ1Z-miDzgg-4oFQDd-8mF37R-BpWJC-9DFwjw-91prXU-miFQti-BpXha-BpWst-8mEBKZ-miGPSz-miHz83-miFWma-miFyLg-bPY8P-miDTsX-miHXiL-BpVUH-BpUEb) by Iñaki Pérez de Albéniz [(CC BY 2.0)](https://creativecommons.org/licenses/by/2.0/)

* Landscape images [(testing images in add.html page)](http://konfraria.org/calendari_celp/images/test_images/images.html):

  * [Boots by the loch](https://www.flickr.com/photos/bods/6823262185/in/photolist-boX18t-eiqjrF-7Gni8Q-d4k1CC-7SwSoq-ecSfit-ecShfz-cgUitY-eiw4Vs-7u5mpz-oGPmek-aRSa9e-9dNCN4-2QLjZW-aSunSi-efhBsV-7CdRhE-Pd7mK-bDpKy1-q5dTZo-bBg3yQ-ebbDmL-efhzMc-jfNrRJ-bXjcZ4-3R7WMF-w4aj1r-6dWt7a-i7bVg1-hZ5YJt-4fbZju-aceLr8-nPf6yM-4HTbPK-9jEXYC-HUBNb7-rFtqNF-7KTXA-9gYUUs-4HTdvD-cSPab5-62P9zK-9cKkH-gXoqpd-c4sLJb-b8AKUt-9nVGkQ-2Jp4d-PMVZU-7mpksU) by Andrew Bowden [(CC BY-SA 2.0)](https://creativecommons.org/licenses/by-sa/2.0/)
  * Cadí: [Cadí](https://www.flickr.com/photos/utopiaecologica/8649268974/in/photolist-4KTkzL-52zi3r-dNftUb-dNfquS-dN9SKZ-B8MTdc-dN9TBK-dN9VYV-ebiLk9-31eTtX-dzBcVg-8v7WQb-8v5pQk-52b4wx-8m4sgP-dafuit-8v4Zer-8m4s1k-dNftwE-8v8Gb7-Ep5XXX-dN9UVt-dNfriy-8v5FfV-8v5n8M-eWRZZh-eR1Z6w-8v8o9N-8v7U8s-mQwSJR-mHD8gY-bmBXsr-bmBPGr-8v5J46-8v85Ds-8v5jux-8v8r6Q-8v4Vnn-8v7Tiy-8v57Pa-8v5NM8-8v89W3-8v7V4j-bmBDGa-8v5qMc-psjBMY-bmBThX-8v86oQ-8v7XBo-8v7YXd) by Albert Torelló [(CC BY-SA 2.0)](https://creativecommons.org/licenses/by-sa/2.0/)
  * Collserola: [Panorama_Tibidabo_2003](https://www.flickr.com/photos/friviere/1439626732/in/photolist-fqMBHr-3cdsSy-brE5Lu-6sbNXn-6sfZfo-fr2R79-rAkt78-6sbNsx-5GJUWF-6sfW6W-7KkmbA-5GJQZB-4UhNYt-6U1cAZ-6sbQut-dJqt9p-fqMBvi-8bkiak-5GP8xJ-dg4w7T-fqMzxH-fqMBfi-7KgqK6-6sbQKi-6sbPeT-ASUctF-6sfWUb-CkcvrX-9Vsjt2-6sfYeS-6EF6nT-4RM4PJ-6sfVtm-6sbP7p-6sfVB1-nReD9m-gjWs8k-2ESwo2-6sbRC4-8zQNFE-5GP7Sf-76mqTh-5GJRaz-aaVSCR-cw4Kd-fqMAwc-7MWU1W-5DBWiN-6sfVUA-fqMAKF/) by Paco Rivière [(CC BY-SA 2.0)](https://creativecommons.org/licenses/by-sa/2.0/)
  * Costa Brava: [Calella de Palafrugell (Girona)](https://www.flickr.com/photos/asarasua/3865994698/in/photolist-9TjeFk-8usmpD-8xMGLz-8xQJC3-8v5Xa1-8xMGia-8xQ9E5-6TCex1-8usmQr-8xMGUM-8uskcv-8uvq2o-8uskBM-e7ZWWY-8xQHF1-8xM8J6-8xQ9oU-8uskVv-6TyeWr-8xQac7-o1jMLT-cGxT8h-ixxEEY-rERmgt-imdWtK-8xM7Sn-bSmbSt-8xQ873-nxUyhG-dNrcsF-e7ZWXb-viFSjy-bDru85-dNZCCT-sEETy7-sX3TGN-8xQHby-8xQ9gd-CUmdc1-8xQJRU-B4x3ms-sXgmSP-e7Uh6D-e7ZWXh-e7Uh5g-s1s5pV-bF53su-ok37CL-CvXxUF-ok37yC) by Asier Sarasua Aranberri [(CC BY-SA 2.0)](https://creativecommons.org/licenses/by-sa/2.0/)
  * Delta de l'Ebre: [delta de l'ebre, catalonia](https://www.flickr.com/photos/49642992@N05/4557521613/in/photolist-bVhbY4-c44iE1-c1zavs-c8nZ4h-3eMcSg-ca2PDd-3G6hQA-c6Qdb1-6xXaiD-bZAoUW-4eRNS1-c69YKb-bV13DP-c5Hw3m-c34wN9-aBZ8ei-7WMJzu-bXMfkL-7WJuoR-qHGEJo-7WJuHv-c7KGjw-o4nwRK-7WJvbM-7WMH4W) by manelsubirats [(CC BY 2.0)](https://creativecommons.org/licenses/by/2.0/)
  * Delta del llobregat: [Llobregat](https://www.flickr.com/photos/franganillo/5811733901/in/photolist-dmct8U-bryUge-6K32dH-mLj1YZ-9RyE1D-5N3mCi-69fVWg-aTaYWr-9Qaz9M-8wTPxP-a178Ch-6GP4gY-9fochu-7xGaAn-98oANL-eJe3A2-7gNaQi-5mHzSC-8e77xW-8EK2hF-982Zu8-8rTXjA-8xcSnY-92MM4f-9iTmnv-5Ns9pk-ig8pDD-6VvZbn-aQ7Xh8-agsBHw-ig8MCQ-8NGJ6C-6t8RL9-4HUmiC-9mdmqe-9mgrgA-9mdmnn-5VkWkh-9mdmep-brWqQY-9mdmat-eWHXaP-ig8zFb-ig8nKQ-9mdmiP-ig8p5U-5UHTfa-ig8KDj-cPvqpS-6DRZYg) by Jorge Franganillo [(CC BY 2.0)](https://creativecommons.org/licenses/by/2.0/)
  * Garraf: [Paisatge](https://www.flickr.com/photos/122/3742328811/in/photolist-6GGpYx-6GGyXc-5LXR7g-5LXRoc-5M339f-5M34Mm-6GGrTB-5LXRgv-6GLshy-5LXQUr-6GGoin-6GGFVi-6GGnsr-5LXS7M-6GGutK-5M33oy-6GGA96-5M33x1-6GLM8b-6GGC2x-5M33dJ-6GLAi9-6GGCWZ-5M33GJ-5M35d3-6GGEWR-5LXQ3K-5M33Sw-5M35Hm-5LXQRP-5M35uw-6GLzoo-eWRTmf-eWRTaf-eWRTxm-LubsV-EEoY-EEp1-9jDiDw-9phF1B-eWEusv-EEoZ-6KhbqS-6Kd8eZ-cpXm-cpYn-9phEFe-9pkLDQ-eWRUEC-6LWLs6) by joan ggk [(CC BY 2.0)](https://creativecommons.org/licenses/by/2.0/)
  * Guilleries: [Sau](https://www.flickr.com/photos/nsrelm/8520353085/in/photolist-dYV38p-dYKEoB-qnhRLt-q5Rp6K-q5Tusa-q5L9ay-qn8Ang-qnfd2b-4KcLZ8-jM2Zf-jM31p-jM35C-jM2XB-dYKGFp-q5Tyei-qn7L2P-qnim1K-q5JAys-pqiBys-q5RUhv-qneEEy-qk1ZGd-4zZkdR-q5JTvJ-q5L5yA-G3RgKd-FaT2Rv) by Josep Enric [(CC BY-SA 2.0)](https://creativecommons.org/licenses/by-sa/2.0/)
  * l'Albera: [Munyanyes de Colera, les Alberes](https://www.flickr.com/photos/angela_llop/17947685259/in/photolist-cTyMcU-dHLNeX-dHLMRt-dHLNKz-dHLPDB-dHLQ7D-dHSe9N-dHSfVw-63CreQ-dHL4un-63DJdd-vpSaJY-7YCHmj-uKr2fC-vGrsfi-dHRxiC-63ybbF-dHL5ST-dHRwVG-dHL7fT-dHL46z-2nnV3-7GhJbg-dHRvLo-tkYzxi) by Angela Llop [(CC BY-SA 2.0)](https://creativecommons.org/licenses/by-sa/2.0/)
  * l'Ordal: [paratges](https://www.flickr.com/photos/irinoko/3045640340/in/photolist-5D8GLm-bqecNn-bqe8PH-bqebbF-5BVgi8-85WeU6-5D8Dgs-zNL358-zMDsVh-zwgfSk-zPFjq4-zwamzA-zwfkVD-zw8BjQ-yRUmcc-zwavxq-yRTMmH-yRJJmy-zNL49x-yRUpsk-yRUbnx-zwa45L-zw9qT7-zwbm53-zwfy5t-zLsD5s-zw9GP5-zMDA6u-zw9wGG-zMDeu9-yRJYxE-zwbSA3-zLsoJJ-zMDMwL-zwgeX4-zw9CgN-zLsUi3-zwbD5A-yRJVdy-zLscnf-zMDVBy-zwbprU-zPF5gc-zLsPvY-zwfr1t-yRUnxZ-zNLFne-zwc783-zwgvUp-zLsy5s) by Irinoko [(CC BY 2.0)](https://creativecommons.org/licenses/by/2.0/)
  * Montsant: [P1010329](https://www.flickr.com/photos/vor0nwe/9475912163/in/photolist-frmwxV-frknRr-fryqoN-frAekm-frAPAY-frkKUr-frzUD7-frAFHJ-4FwwGg-frzLGE-4BHtjH-f1QzsV-frmpqz-gntb3Q-frzFi9-frA31y-frjpTc-frzFWC-fryAuN-mUJPdM-frkJHF-frkCeP-frAQFC-frkzGR-frARsU-frkt6n-frjyvZ-gntrRT-frzWT7-frAK69-frjvvg-gntjr4-gnsWZr-frA2hh-4BMTfN-4BMQ1G-frALZu-frmtZt-frA2wG-frzPWs-frkL4Z-5eyzUt-frmron-frAFQY-frA13C-frjfUM-frkBjz-fryF6j-frzG6q-mULBuG) by vor0nve [(CC BY-SA 2.0)](https://creativecommons.org/licenses/by-sa/2.0/)
  * Montsec: [Montsec d'Ares](https://www.flickr.com/photos/smartinmolina/10252158445/in/photolist-bynZy1-byo1zU-byo1h1-bMhv4R-bynZVA-EhjujD-bMhJGV-72V4KX-72Z9mC-byo5Nb-bynY1b-bynW5y-72VvWe-EoFbdG-byo2fm-731au1-gBWZwv-mmMQWa-s3PFkM-72Vkqg-edLuux-Rvsw-72Z5ms-72WvMB-rRd73-72Vnkn-72YZyC-731pyy-72Zenm-72VQf8-72WpKa-72W9Je-72ZmmJ-72ZCvG-72WgJz-hgB4mp-edS9gE-7315kw-72V6C4-731mzs-k8ekEL-72Wqng-72VqUv-hgtJzT-hZPi75-72ZWHy-72WtQ8-qa8Hxn-mmLM82-72UYh4) by Sílvia Martín [(CC BY 2.0)](https://creativecommons.org/licenses/by/2.0/)
  * Montseny: [Montseny](https://www.flickr.com/photos/borkurdotnet/2561919016/in/photolist-4Uovgw-ehzMg7-bsBmAF-8VVo3i-fnwbeB-4Uof8Q-ehACfA-ehAwRE-fnLiz9-4UiZNK-4UiY4e-9Q2QK2-4UoakW-4UomYU-9gwinL-8nuCyY-d3SEFA-d3SyPs-d3SCQQ-d3SDSW-d3SykL-d3SBy3-d3SCc1-d3Sxej-d3SzYC-4UooM1-4Uj45Z-4UojvN-4UiV1T-FdJJs-9gwgoy-ec3zDf-ecqTMi-5CcH3z-5rAiM6-4utTQx-4uMhTf-4utV3c-4uwGpJ-egc3Pd-7t64Qm-7t63Uq-7t27dg-7t65kL-7t27nD-7t26kF-7t26Mc-7t26sT-wgzvFJ-vmSE9C) by Börkur Sigurbjörnsson [(CC BY 2.0)](https://creativecommons.org/licenses/by/2.0/)
  * Montserrat: [IMG_5042Montserrat_2400](https://www.flickr.com/photos/macskapocs/30637133196/in/photolist-NFijjq-nPyjEt-nPxCMW-nPzdNM-oiC2sd-pqPgRt-o3PiGh-o77Mjh-o6j2cx-BmimZ1-Mz4nDR-oiP9pt-nNn5Zo-o53pa5-f9Ak8y-nNPAe2-nPzdhM-o77NSY-B7NT3h-sQmC2J-oUf7iK-4fcT6s-jaCgTE-hTgtc-acoV5n-4fcPCU-91qgKF-6DphLj-p9ABjq-o7dvkH-cYhJGJ-4f8TRg-eznjB1-qZVhE6-rj9kqM-rAbdb5-6DphZS-BRGHig-o6Wn2g-t7Y87x-aAjCwK-91tmhm-nPHPmG-jaxRVB-vwoTXh-9DzaiB-8K4ws9-hTduE-yzKYt6-csEEu5) by Gergely Csatari [(CC BY-SA 2.0)](https://creativecommons.org/licenses/by-sa/2.0/)
  * Montsià: [Mirando por la Foradada II](https://www.flickr.com/photos/arrozconnori/7102958011/in/photolist-bPEvXi-bPEwRH-zqE8XQ-bPEnei-bAKRi5-np5JpP-e9sg3M-bPEszp-nn2PXQ-buxWvS-nkgNd5-e9sgfk-bPEtPX-bHsJdV-bHsHut-nnjjqc-25628d-9zqeAY-nn2RWu-bAKM9b-br3PwG-c78zQ9-bHsHka-bDXK4H-EN2QS-9zqgEq-EN31o-nkgK5S-bpt8vG-zGbkrJ-9zn9YT-bPEos6-9zqdgJ-bHsK1r-bHsHAV-9zn8WT-bHoWnv-buu9pE-2562kh-bDXJvn-251xoV-9znkdi-nkgJzJ-9zqec3-bPEmAa-bPEpnp-bHsKNt-25647L-bAKG9L-buxWQ9) by Oswaldo Rubio [(CC BY 2.0)](https://creativecommons.org/licenses/by/2.0/)
  * Montnegre: [View from the restaurant](https://www.flickr.com/photos/stvcr/2337680919/in/photolist-4yze6r-4Chn3n-5o1WPV-qKD55R-qKJgd3-qtnYfB-pP2rq4-5QpYtd-bqVcbi-mzEqVk-bqViKg-5QkLvn-5Qq1tm-dn2iMP-bqV6yX-5Qq3os-bqUYGP-qKNvvg-5QkJyP-mzFWuQ-bqVd7X-bqVbug-5Qq1MN-bqVoAp-n2dGex-5QpY21-5QpZgG-bqVee2-5Qq5cG-n2fQi5-5Qq6od-5Qq8j9-bqUVx4-bqVrwT-5QkLbM-5Qq7sh-5QkQcg-bqVhY8-n2fAws-5Qq4hE-5QpXRo-5Qq7CU-5Qq5zS-bqV8LM-5QkPt4-5Qq6YL-5QkRha-bqUSYV-5QkMfZ-4ugy1p) by stvcr [(CC BY-SA 2.0)](https://creativecommons.org/licenses/by-sa/2.0/)
  * Pedraforca: [Pedraforca](https://www.flickr.com/photos/smartinmolina/8482411813/in/photolist-dVyzvx-dVE7JW-boYxE8-7fSwem-56A2WJ-56A2Au-dNfriy-cPvp7U-5XmyZG-56zXjG-56vNMM-56A3A1-56vQV2-JuuKz-aSjpv6-56zWQE-9BMaN-56vLV2-bmBwtP-56vQdB-Ju382-56zWYW-56vS1D-56A1Hh-56vRPa-56A1gf-56A63h-56zYTb-56vVgH-56vPeM-56vSJP-56vMJx-56vNkr-56vQwF-56vM7H-56vRqc-osF9VT-56vPCp-8qJRbr-8apnB2-oH8uJo-56A6bA-7fB5t6-56vPX8-56zXxW-56A4rw-ynEie-oK8vdo-56A221-56vSg6) by Sílvia Martín [(CC BY 2.0)](https://creativecommons.org/licenses/by/2.0/)
  * Pirineus: [Pirineus](https://www.flickr.com/photos/jordimarsol/3280913333/in/photolist-5ZVxeg-a5WtPr-a5Wtbg-dsZ995-aqW4Vj-a5Wxwv-bB19BZ-aqW1Y5-a5ZjPY-aqWgf1-vVVUra-dsZax5-a5ZmNL-dsYNnk-aqWuaj-3Q6X5G-a5ZnuQ-a5WwUc-9MqtH-aqVWN7-dsZ9ZA-4tqnH2-NTJAB-a5ZjK3-5hptwo-aceso4-artK8j-aqWaTm-dsYUTz-aqVqnQ-aqTrSa-aqSZpg-jWybF-5dUjyR-5ZVwsM-ayVQYM-a5ZkS7-6CQ3Cf-aqSSCD-nSCaXH-agSVfM-6FCKWw-ayVS36-ayVLd8-a5Zpzm-a5ZoMU-achai5-aqT31B-a5Wz26-a5Zn29) by Jordi Marsol [(CC BY 2.0)](https://creativecommons.org/licenses/by/2.0/)
  * Ports de Beseït: [20131023_153244](https://www.flickr.com/photos/aka1936/10502178144/in/photolist-h13pEY-gZX83D-h12KLx-gZX7JW-gZZ7Mf-h11Wqj-gZX7iJ-h127s3-gZXC96-h13oUG-h11942-h11nxs-gZWPjd-gZYfG5-h12EY6-gZWG4y-gZYog5-gZYihq-gZXd5W-h11eud-h11eD9-gZZWD7-h11aAF-h11Qs7-gZZvZt-h13G8h-h12rw7-h12dSi-gZWsg1-gZX568-gZXT5h-gZXZC8-h13tMC-h14pPx-h11yAZ-gZYNFh-gZXrHg-h12asw-h13fEx-h12sHc-gZZTE1-h13AMB-h14gwm-gZZnSK-gZY8QG-h131jw-gZZQFL-gZXoJa-gZYp3n-h14jZd) by Albert [(CC BY 2.0)](https://creativecommons.org/licenses/by/2.0/)
  * Sant Llorenç de Munt: [la Mola, Sant Llorenç del Munt des de Montserrat](https://www.flickr.com/photos/angela_llop/16839712748/in/photolist-cbDcg-dowaTK-dowbLa-dowiC3-dowbPn-dowiQU-dowinu-dowdfv-dow8yp-dowgsY-dow8Ce-dowav2-Bmjmf-4cjtGT-dow9na-dowcuK-dowiKd-dowaD4-dowi8s-dow7Cg-dowdiH-dowjTW-dowfmG-dowfiS-dowftQ-dowcga-dowaZH-dowjgd-6DNdNF-dow7gg-dowf9A-dow9u2-dowg4G-dowiYJ-dowb7v-dowh2L-3JhKHR-3Jn4Ah-dowhTQ-dow8Qp-dowcok-6DNfWK-dowgNd-rE4VUY-qbWSMZ-qr5Qm5-qbP56E-pwnvqb-qbVg2e-qbP1Zu) by Angela Llop [(CC BY-SA 2.0)](https://creativecommons.org/licenses/by-sa/2.0/)

* Logo:
  * :copyright: [CELP logo](https://image.jimcdn.com/app/cms/image/transf/none/path/sab30b0734d33b1b6/image/ieb42f422f076b68d/version/1385465900/image.jpg) is a copyrighted logo, and can't be used without permissions.

Contact
-------

* lakonfrariadelavila *at* gmail *dot* com
