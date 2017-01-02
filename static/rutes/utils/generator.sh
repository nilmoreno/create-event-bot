#!/bin/bash
#Script de bash per convertir fitxers GPX de GraphHopper en fitxers JS per llegir-los amb Hotline (plugin de Leaflet). Us cal el fitxer GPX desat a la carpeta /gpx
echo Escriviu el títol de la pàgina web:
read filetitle
echo Escriviu el nom del fitxer GPX sense extensió:
read filename
sed "s/replace-with-webpage-name/$filetitle/g" base.html > base2.html
sed "s/replace-with-gpx-name-for-coords/$filename/g" base2.html > base3.html
sed "s/replace-with-gpx-name/$filename/g" base3.html > ../$filename.html
rm base2.html
rm base3.html
cd ../gpx
sed 's/<trkpt lat="/  [/g' $filename.gpx > file.js
sed 's/" lon="/,/g' file.js > file2.js
sed 's/"><ele>.*<\/time><\/trkpt>/,/g' file2.js > file.js
sed 's/<?xml version=.*schema\/gpx\/1.1">/FIRST LINE/g' file.js > file2.js
sed 's/<metadata>.*<\/metadata>/SECOND LINE/g' file2.js > file.js
sed 's/<trk><name>.*<\/name><trkseg>/THIRD LINE/g' file.js > file2.js

sed '/<\/trkseg>/d' file2.js > file.js
sed '/<\/trk>/d' file.js > file2.js
sed '/<\/gpx>/d' file2.js > file.js

sed '3d' file.js > file2.js
sed '2d' file2.js > file.js
sed '1d' file.js > file2.js

perl -lne 'print $_, "", $.' file2.js > file.js
sed -e 's/$/],/' file.js > file2.js

sed '$ s/.$//' file2.js > file.js

echo '];' >> file.js
sed '1 i\var coords = [' file.js > file2.js

x=`cat file2.js | wc -l`
y=$(($x - 2))

echo 'var waypointnum='$y >> file2.js
rm file.js
mv file2.js ../assets/hiking-js/$filename.js


exit
