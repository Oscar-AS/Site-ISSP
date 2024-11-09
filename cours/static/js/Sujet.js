// Messages personnalisés pour les onglets vides
var messagesPersonnalises = {
    "epreuves1": "Aucune épreuve n'a été trouvée pour cette section.",
    "corrections1": "Aucune correction n'a été trouvée pour cette section.",
    "epreuves2": "Aucune épreuve n'a été trouvée pour cette section.",
    "corrections2": "Aucune correction n'a été trouvée pour cette section.",
    "resultats": "Aucun résultat n'a été trouvé."
};

// Fonction pour ouvrir les onglets principaux
function openTab(e, tabName) {
    // Masquer tous les onglets principaux
    var tabcontent = document.getElementsByClassName("tab-pane");
    for (var i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Désactiver la classe "active" de tous les liens d'onglets
    var tablinks = document.getElementsByClassName("nav-link");
    for (var i = 0; i < tablinks.length; i++) {
        tablinks[i].classList.remove("active");
    }

    // Activer la classe "active" pour l'onglet sélectionné
    e.currentTarget.classList.add("active");

    // Afficher le contenu de l'onglet sélectionné
    var tabElement = document.getElementById(tabName);
    if (tabElement.innerHTML.trim() === "") {
        // Utiliser le message personnalisé si l'onglet est vide
        tabElement.innerHTML = messagesPersonnalises[tabName];
    } else {
        tabElement.style.display = "block";
    }

    // Si l'onglet "preselection" ou "selections" est ouvert, ouvrir également le premier sous-onglet "epreuves"
    if (tabName === 'preselection') {
        openSubTab(e, 'epreuves1');
    } else if (tabName === 'selections') {
        openSubTab(e, 'epreuves2');
    }
}

// Fonction pour ouvrir les sous-onglets
function openSubTab(e, subTabName) {
    // Masquer tous les sous-onglets
    var subtabcontent = document.getElementsByClassName("sub-tab-pane");
    for (var i = 0; i < subtabcontent.length; i++) {
        subtabcontent[i].style.display = "none";
    }

    // Désactiver la classe "active" de tous les liens de sous-onglets
    var subtablinks = document.getElementsByClassName("nav-link");
    for (var i = 0; i < subtablinks.length; i++) {
        subtablinks[i].classList.remove("active");
    }

    // Activer la classe "active" pour le lien de sous-onglet sélectionné
    e.currentTarget.classList.add("active");

    // Afficher le contenu du sous-onglet sélectionné
    var subTabElement = document.getElementById(subTabName);
    if (subTabElement.innerHTML.trim() === "") {
        // Utiliser le message personnalisé si le sous-onglet est vide
        subTabElement.innerHTML = messagesPersonnalises[subTabName];
    } else {
        subTabElement.style.display = "block";
    }
}

// Initialiser les onglets au chargement de la page
document.addEventListener("DOMContentLoaded", function () {
    // Sélectionner le premier lien d'onglet et déclencher un clic pour afficher le contenu par défaut
    var defaultTab = document.querySelector('.nav-tabs .nav-link');
    if (defaultTab) {
        defaultTab.click();
    }

    // Sélectionner le premier sous-onglet et l'afficher par défaut
    var defaultSubTab = document.querySelector('.sub-tab-pane');
    if (defaultSubTab) {
        defaultSubTab.style.display = "block";
    }
})


;
