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
    "montseny": {
        "ca": ["Montseny"],
    },
    "montserrat": {
        "ca": ["Montserrat"],
    },
    "ordal": {
        "ca": ["Ordal"],
    },
    "repair": {
        "en": ["repair", "fridge repair", "handyman", "electrician", "diy"],
        "ru": ["ремонт", "ремонт холодильника", "мастер", "электрик", "самоделк"],
    },
    "swimming": {
        "en": ["swim", "swimming", "swims"],
        "ru": ["плавание", "бассейн"]
    }
};
