# SmartGrid

# Opdracht

Houdt tijdens de opdracht rekening met de volgende requirements:

Batterijen mogen niet aan elkaar verbondenden zijn. Ook niet via een huis.
Een huis mag niet aan meerdere batterijen verbonden zijn.
Elk huis heeft een eigen unieke kabel nodig naar de batterij.
Er mogen meerdere kabels over dezelfde gridsegmenten lopen. Het blijven echter wel unieke kabels en leveren geen kostenvermindering op.
Verbind alle huizen in de eerste wijk aan een batterij. De maximumcapaciteit van de huizen mag die van de batterijen uiteraard niet overschrijden.
De batterijen kosten 5000 per stuk. De kabels kosten 9 per grid-segment. De kabels liggen op de gridlijnen, mogen ook gridpunten met een huis passeren, en de afstand van een huis tot een batterij wordt berekend volgens de Manhattan distance.

Bereken de kosten voor de in 1. geconfigureerde wijken. Probeer je SmartGrid te optimaliseren en vind een zo goed mogelijke configuratie van kabels.
Een nieuwe ontwikkeling in het kabelnetwerk biedt de mogelijkheid om meerdere huizen via een kabel aan een baterij te verbinden. Vanaf nu geldt de volgende requirement:

Huizen mogen via eenzelfde kabel aan een batterij verbonden zijn. Ze mogen dus een kabel delen.
Verbind alle huizen in de drie wijken aan een batterij. De maximumcapaciteit van de huizen mag die van de batterijen uiteraard niet overschrijden.
Optimaliseer het smartGrid voor de drie wijken.  
Advanced  
Nu is het zo, dat de batterijen misschien niet op de best mogelijke plaatsen staan. Het verplaatsen van batterijen vercompliceert de zaak enorm, maar de opdrachtgever wil het toch proberen, om inzicht in het probleem te krijgen.

Verplaats de batterijen, en probeer een beter resultaat te realiseren.
Het bedrijf SmartBatteryCompany heeft recentelijk drie types batterijen ontwikkeld, met verschillende capaciteiten en verschillende prijzen.
  
Batterijtype	Capaciteit	Prijs  
PowerStar	450	    900   
Imerse-II	900	1350  
Imerse-III	1800	1800    
Probeer een betere configuratie voor de wijken te vinden met deze batterijen. Je mag er zoveel gebruiken als je wil en kunnen op ieder gridpunt zonder huis geplaatst worden.

## Huidige mogelijkheden:
* Dataverwerking
  * Data van de locaties van de huizen en de gegenereerde stroomopwekking wordt ingelezen 
  * Output is in een .json file overzichtelijk gemaakt.
* Classes:
  * De classes zijn batterijen en huizen die in de superclass van district worden opgenomen. Met de algoritmes van random/closest wordt er een instantie van district gemaakt die weergegeven wordt door Bokeh.
  * Cable is een klasse die wordt geïnstantieerd door de algoritmes van 
* De districten kunnen op twee manieren onderverdeeld worden.
  * Random:
    * Random sluit de huizen aan op degene die nog in de batterij passen qua capaciteit. Uit deze batterijen wordt willekeurig er een aan het huis toegewezen.
  * Closest:
    * Closest sluit de huizen aan op de batterijen die deze nog qua capaciteit aan kunnen. Uit deze batterijen wordt de kortste route daarheen gekozen.
* Datavisualisatie
  * Momenteel wordt de aansluiting van de huizen op de batterijen weergegeven door middel van scatterplots en step graphs in visualise.py met Bokeh.

## Benodigdheden
* .json library
* bokeh library (pip3 install bokeh)
