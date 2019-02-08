# coding: utf-8
#
# Copyright © Lyra Network.
# This file is part of Lyra plugin for Odoo. See COPYING.md for license details.
#
# Author:    Lyra Network (https://www.lyra-network.com)
# Copyright: Copyright © Lyra Network
# License:   http://www.gnu.org/licenses/agpl.html GNU Affero General Public License (AGPL v3)

LYRA_CURRENCIES = {
    'CAD': u'124',
    'CNY': u'156',
    'DKK': u'208',
    'NOK': u'578',
    'CHF': u'756',
    'GBP': u'826',
    'USD': u'840',
    'BGN': u'975',
    'EUR': u'978',
}

LYRA_AUTH_RESULT = {
    "00": u"Transaction approuvée ou traitée avec succès",
    "02": u"Contacter l’émetteur de carte",
    "03": u"Accepteur invalide",
    "04": u"Conserver la carte",
    "05": u"Ne pas honorer",
    "07": u"Conserver la carte, conditions spéciales",
    "08": u"Approuver après identification",
    "12": u"Transaction invalide",
    "13": u"Montant invalide",
    "14": u"Numéro de porteur invalide",
    "15": u"Emetteur de carte inconnu",
    "17": u"Annulation client",
    "19": u"Répéter la transaction ultérieurement",
    "20": u"Réponse erronée (erreur dans le domaine serveur)",
    "24": u"Mise à jour de fichier non supportée",
    "25": u"Impossible de localiser l’enregistrement dans le fichier",
    "26": u"Enregistrement dupliqué, ancien enregistrement remplacé",
    "27": u"Erreur en « edit » sur champ de lise à jour fichier",
    "28": u"Accès interdit au fichier",
    "29": u"Mise à jour impossible",
    "30": u"Erreur de format",
    "31": u"Identifiant de l’organisme acquéreur inconnu",
    "33": u"Date de validité de la carte dépassée",
    "34": u"Suspicion de fraude",
    "38": u"Date de validité de la carte dépassée",
    "41": u"Carte perdue",
    "43": u"Carte volée",
    "51": u"Provision insuffisante ou crédit dépassé",
    "54": u"Date de validité de la carte dépassée",
    "55": u"Code confidentiel erroné",
    "56": u"Carte absente du fichier",
    "57": u"Transaction non permise à ce porteur",
    "58": u"Transaction interdite au terminal",
    "59": u"Suspicion de fraude",
    "60": u"L’accepteur de carte doit contacter l’acquéreur",
    "61": u"Montant de retrait hors limite",
    "63": u"Règles de sécurité non respectées",
    "68": u"Réponse non parvenue ou reçue trop tard",
    "75": u"Nombre d’essais code confidentiel dépassé",
    "76": u"Porteur déjà en opposition, ancien enregistrement conservé",
    "90": u"Arrêt momentané du système",
    "91": u"Emetteur de cartes inaccessible",
    "94": u"Transaction dupliquée",
    "96": u"Mauvais fonctionnement du système",
    "97": u"Echéance de la temporisation de surveillance globale",
    "98": u"Serveur indisponible routage réseau demandé à nouveau",
    "99": u"Incident domaine initiateur",
}
