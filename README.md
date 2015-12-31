silvestermails
==============

Verschickt vordefinierte Silvestermails

Gebrauch: silvestermails.py [-h] [-s [SUBJECT]] [-f [SENDER]] [-b [BODY]] [-r [RECIPIENTS]]

Argumente:
 * -h Ein kurzer Hilfetext
 * -s [SUBJECT] Der Betreff der Nachrichten, Voreinstllung ist "Ein frohes neues Jahr YYYY" mit dem jeweils aktuellen Jahr
 * -f [SENDER] Die Abersenderadresse, Voreinstllung ist "ich@domain.tld"
 * -b [BODY] Die Datei mit der Textvorlage, Voreinstellung ist "body.txt"
 * -r [RECIPIENTS] Die Datei mit den Empfängern, Voreinstellung ist "recipients.json"

Die Datei recipients.json definiert eine Liste an Empfängern. Jeder Empfänger benötigt die Felder "email" und "name".
body.txt ist eine einfache Textdatei mit Platzhaltern in der Form {name}.
Es können alle in recipients.json definierten Variablen verwendet werden.