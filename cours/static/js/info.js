// Ajoutez un message personnalisé pour l'onglet "resultats"
var messagesPersonnalises = {
    "ISSP": "Aucun résultat n'a été trouvé.",
    "FIL": "Aucun résultat n'a été trouvé.",
    "SITE": "Aucun résultat n'a été trouvé."
};

function openTab(e, tabName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tab-pane");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("nav-link");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    var tabElement = document.getElementById(tabName);
    if (tabElement.innerHTML.trim() === "") {
        // Utilisez le message personnalisé pour l'onglet vide
        tabElement.innerHTML = messagesPersonnalises[tabName];
    } else {
        tabElement.style.display = "block";
    }

    e.currentTarget.className += " active";}