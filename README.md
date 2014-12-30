silvestermails
==============

Verschickt vordefinierte Silvestermails

Gebrauch: silvestermails.py [-h] [-s [SUBJECT]] [-f [SENDER]] [-b [BODY]] [-r [RECIPIENTS]]

Argumente:
 * -h Ein kurzer Hilfetext
 * -s [SUBJECT] Der Betreff der Nachrichten, Voreinstllung ist "Ein frohes neues Jahr YYYY" mit dem jeweils aktuellen Jahr
 * -f [SENDER] Die Abersenderadresse, Voreinstllung ist "ich@domain.tld"
 * -b [BODY] Die Datei mit der Textvorlage, Voreinstellung ist "body.txt"
 * -r [RECIPIENTS] Die Datei mit den Empfängern, Voreinstellung ist "recipients.txt"
 
body.txt ist eine einfache Textdatei. Es kann der Platzhalter {name} verwendet werden.

In recipients.txt steht in jeder Zeile ein Empfänger. Die Zeilen beginnen mit einer E-Mailadresse gefolgt von einem Tabulator und dem Namen des Empfängers.
