function contains(searchString, keyword) {
    return searchString.toLowerCase().indexOf(keyword.toLowerCase()) != -1;
}

function findKeyword(searchString) {
    for (var keyword in keywords) {
        var locales = keywords[keyword];
        for (var locale in locales) {
            var arr = locales[locale];
            for (var k in arr) {
                if (contains(searchString, arr[k])) {
                    return keyword;
                }
            }
        }
    }

    return "default";
}

function getImage(event) {
    var searchString = event.name;
    if (event.description) {
        searchString += event.description;
    }

    return findKeyword(searchString);
}

var keywords = {
    "cadí": {
        "ca": ["Cadí", "Serra del Cadí"],
    },
    "collserola": {
        "ca": ["Collserola"],
    },
    "garraf": {
        "ca": ["Garraf"],
    },
    "llobregat": {
        "ca": ["Delta del Llobregat", "Parc agrari del Baix Llobregat", "Riu Llobregat"],
    },
    "montseny": {
        "ca": ["Montseny"],
    },
    "montserrat": {
        "ca": ["Montserrat"],
    },
    "ordal": {
        "ca": ["Ordal"],
    },
    "pirineus": {
        "ca": ["Pirineu", "Pirineus"],
    }
};
