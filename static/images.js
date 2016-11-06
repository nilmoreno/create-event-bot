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
    "albera": {
        "ca": ["l'Albera"],
    },
    "cadí": {
        "ca": ["Cadí", "Serra del Cadí"],
    },
    "collserola": {
        "ca": ["Collserola"],
    },
    "costabrava": {
        "ca": ["Costa Brava", "camí de ronda"],
    },
    "ebre": {
        "ca": ["Delta de l'Ebre"],
    },
    "garraf": {
        "ca": ["Garraf"],
    },
    "guilleries": {
        "ca": ["Guilleries"],
    },
    "llobregat": {
        "ca": ["Delta del Llobregat", "Parc agrari del Baix Llobregat", "Riu Llobregat"],
    },
    "montnegre": {
        "ca": ["Montnegre"],
    },
    "montsant": {
        "ca": ["Montsant"],
    },
    "montsec": {
        "ca": ["Montsec"],
    },
    "montseny": {
        "ca": ["Montseny"],
    },
    "montserrat": {
        "ca": ["Montserrat"],
    },
    "montsià": {
        "ca": ["Montsià"],
    },
    "ordal": {
        "ca": ["Ordal"],
    },
    "pedraforca": {
        "ca": ["Pedraforca"],
    },
    "pirineus": {
        "ca": ["Pirineu", "Pirineus"],
    },
    "ports": {
        "ca": ["Ports de Beseït"],
    },
    "santllorenc": {
        "ca": ["Sant Llorenç de Munt", "Sant Llorenç del Munt", "Sant Llorenç-Obac", "Sant Llorenç-l'Obac", "Obac"],
    }
};
