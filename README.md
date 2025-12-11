# Flask-prosjekt -- Dokumentasjon

## 1. Forside

**Prosjekttittel: Sushibutikk**\
**Navn: Helen**\
**Klasse: 2IMI**\
**Dato: 13/11/25**\

**Kort beskrivelse av prosjektet:**\
*Skriv 2--4 setninger om hva applikasjonen gjør og hvilket tema den
bygger på.*
*Applikasjonen skal tilby deg å bestille mat (sushi), online.*
*Den bygger på et butikk tema, hvor man skal kunne handle.*
------------------------------------------------------------------------

## 2. Systembeskrivelse

**Formål med applikasjonen:**\
*Forklar hva du ønsket å oppnå med prosjektet.*
*Jeg ønsket å få en bedre forståelse for databaser og koblingen av de til en nettside. Jeg ville lære det vi har jobba med enda grundigere.*

**Brukerflyt:**\
*Beskriv hvordan brukeren bruker løsningen -- fra startside til lagring
av data.*
Brukeren åpner nettsiden. Møter på "logo", en velkomstmelding og en bestill knapp. Å trykke på "Bestill" knappen går videre til kundeinfo-siden. 
Brukeren fyller inn navn, telefonnummer og e-post. Trykker neste for å gå videre til menyen.
Brukeren ser alle retter som hentes fra meny-tabellen i databasen. Velger Èn rett ved hjelp av knapper med type radio, og da trykker "Betal". Flask tar imot valgt produkt, kobler det sammen med kunde-id fra session, og lagrer i bestilling-tabellen i databasen med tidspunktet også. 
Etter dette blir brukeren sendt til ordrebekreftelsessiden. Her ser brukeren en bekreftelse på hvilket produkt som ble bestilt og når, dataene er da lagret i databsen og kan hentes senere.

**Teknologier brukt:**

-   Python / Flask\
-   MariaDB\
-   HTML / CSS / JS\ (ikke js)
-   (valgfritt) Docker / Nginx / Gunicorn / Waitress osv. (ingen av disse)

------------------------------------------------------------------------

## 3. Server-, infrastruktur- og nettverksoppsett

### Servermiljø
Ubuntu VM med python og flask som fungerer som webserver. 



### Nettverksoppsett

-   Nettverksdiagram
-   IP-adresser\
-   Porter\
-   Brannmurregler


Klient (nettleser) → Flask (python) → MySQL/MariaDB (databse)
  

Eksempel:


    Klient → Waitress → MariaDB

### Tjenestekonfigurasjon

-   systemctl / Supervisor\
-   Filrettigheter\
-   Miljøvariabler


Html og css ligger i templates og static.
Miljøvariabel: app.sercet_key brukes til session. 

------------------------------------------------------------------------

## 4. Prosjektstyring -- GitHub Projects (Kanban)

-   To Do / In Progress / Done\
-   Issues\
-   Skjermbilde (valgfritt)

Refleksjon: Hvordan hjalp Kanban arbeidet?
Dette gjorde arbeidet mer organisert og ikke bare et rot skrublet rundt i hodet. Da har man styr på hva man må få gjort.

------------------------------------------------------------------------

## 5. Databasebeskrivelse

**Databasenavn: sushibutikk**

**Tabeller:**\
\| Tabell \| Felt \| Datatype \| Beskrivelse \|
\|--------\|-------\|-----------\|--------------\| \| customers \| id \|
INT \| Primærnøkkel \| \| customers \| name \| VARCHAR(255) \| Navn \|
\| customers \| address \| VARCHAR(255) \| Adresse \|

**SQL-eksempel:**

``` sql
CREATE TABLE customers (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  address VARCHAR(255)
);
```

------------------------------------------------------------------------

## 6. Programstruktur

    projectnavn/
     ├── app.py
     ├── templates/
     ├── static/
     └── .env

Databasestrøm:

    HTML → Flask → MariaDB → Flask → HTML-tabell

------------------------------------------------------------------------

## 7. Kodeforklaring

Forklar ruter og funksjoner (kort).
(/) viser forsiden (index.html).
(/info) håndterer både GET og POST. GET viser skjema for kundeinfo og POST tar imot dataene. Lagrer kunden i databsen og legger en kunde-id i session før brukeren sendes videre til neste side.
(/meny) viser meny med retter fra tabellen i databasen. POST tar imot valgt produkt, hnter produktnavn og viser bekreftelsesiden etter å trykke bestal. 
get_db lager og retunerer en kobling til databasen. 

------------------------------------------------------------------------

## 8. Sikkerhet og pålitelighet

-   .env\
-   Miljøvariabler\
-   Parameteriserte spørringer\
-   Validering\
-   Feilhåndtering

.env: passord og hemmelig nøkkel bør ligge i en .env fil og ikke i koden. (greit om det er for et lokalt skoleproskjekt.)

parametriske spørringer: sqlspørringer brukes for å hente eller lagre data i databasen gjennom python. parametre gjør spørringen trygg, og beskytter mot sql injection som er når noen prøver å manipulere databasen via input som å for eksempel slette data.  

validering: html inputene bruker required som betyr at brukeren må fylle inn alle felt. Flask henter input via request.form.get() som kan sjekke om et felt er tomt eller ikke.

Feilhåndtering: På meny siden sjekkes det om brukeren har valgt en rett og hvis ikke så kan du ikke gå videre og det forhindrer tomme bestillinger til å bli lagret i databasen. 

------------------------------------------------------------------------

## 9. Feilsøking og testing

-   Typiske feil\
-   Hvordan du løste dem\
-   Testmetoder




------------------------------------------------------------------------

## 10. Konklusjon og refleksjon

-   Hva lærte du?\
-   Hva fungerte bra?\
-   Hva ville du gjort annerledes?\
-   Hva var utfordrende?

------------------------------------------------------------------------

## 11. Kildeliste

-   w3schools\ for det meste pluss klassekamerater
-   flask.palletsprojects.com
