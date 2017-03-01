$(function () {
    var base64 = decodeURIComponent(window.location.hash.split('#')[1]);
    var event = JSON.parse(Base64.decode(base64));

    fillCard(event);
    addButtons(event);
});

function fillCard(event) {
    var description2 = event.description;
    var description3 = description2.replace(/\n/g, "</br></br>");
    var description4 = description3.replace(/<\/br><\/br><\/br><\/br>/g, "</br></br>");
    var description5 = description4.replace(/<\/br>1./g, "1.");
    var description6 = description5.replace(/<\/br>2./g, "2.");
    var description7 = description6.replace(/<\/br>3./g, "3.");
    var description8 = description7.replace(/<\/br>4./g, "4.");
    var description9 = description8.replace(/<\/br>5./g, "5.");
    var description = description9.replace(/<\/br>6./g, "6.");
    $('#title').html(event.name);
    $('#description').html(description);

    // Create place link
    if (event.place) {
    var place = $('#place');
    place.html('<img draggable="false" class="emoji" alt="󾔿" src="http://twemoji.maxcdn.com/16x16/1f4cd.png"> ' + event.place + '<br>');
    place.click(function () {
        window.open('http://www.openstreetmap.org/search?query=' + event.place);
    });
    };

    // Create parking link
    if (event.parking) {
    var parking = $('#parking');
    parking.html('<img draggable="false" class="emoji" alt="🚗" src="http://twemoji.maxcdn.com/16x16/1f697.png"> ' + event.parking + '<br>');
    parking.click(function () {
        window.open('http://www.openstreetmap.org/search?query=' + event.parking);
    });
    };

    // Create route link
    if (event.route) {
    var route = $('#route');
    route.html('<img draggable="false" class="emoji" alt="🔃" src="http://twemoji.maxcdn.com/16x16/1f503.png"> Mapa amb la ruta');
    route.click(function () {
        window.open(event.route);
    });

    // Create route iframe
    var iframe = '<center><iframe scrolling="yes" height="400" frameborder="0" width="100%" src="' + event.route +'"></iframe></center><br><br>'; 
    document.getElementById('iframe').innerHTML=iframe;
    };

    // Format and show date
    var date = new Date(parseInt(event.date) * 1000);

    var options = {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        weekday: 'long',
        hour: 'numeric',
        minute: 'numeric'
    };

    var formattedDate = date.toLocaleDateString('ca-ES', options);

    $('#date').html(formattedDate);

    // Preload and set image
    var image = getImage(event);
    var imageUrl = 'images/img_' + image + '.jpg';

    $('<img/>').attr('src', imageUrl).load(function () {
        $(this).remove();
        $('.picture').css('background-image', 'url(' + imageUrl + ')');
        showCard();
    });
}

function addButtons(event) {
    var data = {
        title: event.name,
        start: new Date(parseInt(event.date) * 1000),
        duration: 60
    };

    if (event.place) {
        data.address = event.place;
    }

    if (event.description) {
        data.description = event.description;
    }

    var calendar = createCalendar({
        data: data
    });
    $('.add').append(calendar);
}

function showCard() {
    $('.page').fadeIn(200);
}
