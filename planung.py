Stammbaum:
person:
- id #eg P42
- name: String, Name hat Methode der zusammensetzt (aktueller Name, sonst müsste man alle Ereignisse durchsuchen)
- last_name_change_event: id Ereignis

Geschlecht als Attribut von Ereignis Geburt

name:
- id #eg N42
- type: 0: bürgerlicher Name, 1: adeliger Name, 2: benutzerdefiniert, 3: …

name_types:


label:
- text: string, # heißt im code steht die Sprache in der es zuerst eingegeben wurde
- description: hover text, # zb confirmation 1 (Firmung), confirmation 2 (Konfirmation)
- Sprache

event:
- id #eg E242
- participants: list with ids and roles
- date
- type: 
    personal: birth, death, adoption, funeral, name change
    religious:
        personal: baptism, confirmation 1 (Firmung), confirmation 2 (Konfirmation), first communion, ordination, Austritt, excommunication
        family: marriage, divorce, annulment
    family: marriage, divorce, annulment, 
- endsevent: id, maybe list # aufzuhebendes Ereignis, zb geburt durch tod, heirat durch scheidung
- attributs

event_roles:
- id #eg R42
- type:
    primär: Ehepartner, Kind
    sekundär: Trauzeuge, Zeuge
    tertiär: Teilnehmer, Gast
    religiös: Taufpate, Firmpate, Konfirmationspate, Kommunionspate, Priester, Pastor, Bischof, Weihbischof, Papst (bei Exkummunikation), Gegenpapst (bei Heiligsprechung)



attributs_event:
- id #eg A42
- upperlevel: id
- type: 
    personal: Todesursache, Geschlecht (attribut von ereignis geburt)

(eg ec1 for custom type)
- name: test if not none
- date: Date
- place: String, 

place:
 #eg P42
- name: String
- upperlevel: id
- type: 

    Global Level:
    0: country ((Souveräner-) Staat)

    National/Regional Level:
    1: state (Staat), 2: province (Provinz), 3: federal state (Bundesland), 4: area (Region)

    Intermediate Level:
    5: district (Bezirk), 6: administrative region (Regierungsbezirk)

    Local Level:
    7: county (Kreis), 8: rural district (Landkreis), 9: district office (Bezirksamt), 10: independent city (Kreisfreie Stadt)

    Local Level:
    11: city (Stadt), 12: municipality (Gemeinde), 13: locality (Ort), 14: village (Dorf), 15: hamlet (Weiler), 16: settlement (Siedlung)

    Sub-Local Level:
    17: city district (Stadtteil), 18: locality part (Ortsteil), 19: municipal part (Gemeindeteil), 20: village part (Dorfteil), 21: hamlet part (Weilerteil), 22: settlement part (Siedlungsteil)

    Sub-Local Detail Level:
    23: church (Kirche), 24: cemetery (Friedhof), 25: street (Straße)

    House Number Level:
    26: house number (Hausnummer)

- title: 0: Kaiserreich, 1: Reich, 2: Königreich, 3: Großherzogtum, 4: Herzogtum, 5: Fürstentum, 6: Freistaat, 7: Freie- und Hansestadt, 8: Freie Hansestadt, 9: Hansestadt, 10: Markt, 11: Bundesrepublik

date:
# saved as gregorian calendar, maybe calculator for other calendars
- type: 0: point, 1: span, 2: around, 3: before, 4: after
- start: Date
- startquality: 0: exact, 1: approximate
- startdiscription
- end: Date
- endquality: 0: exact, 1: approximate
- enddiscription
- description

language:
-	text: String englische Bezeichnung
-	short: String (internationale Abkürzungen)
