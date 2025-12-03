# PRO1 Grupp 1 Luftfuktightesmätare

## Syfte:
Testa luftfuktigheten för att se hur akrylfärg torkad i fuktig miljö 

## Analys av användare och kontext:
Målare inom byggbranchen + hobby målare som ska måla om hemma. 

#### Scenario:
Bosse 63år som har varit målare i 40 år han ska måla sina väggar hemmaverkstad i källaren. 
Han har monterat ner hyllor från väggarna och vill veta när de kan hängas upp igen för frugan är sur att hyllplanen står i hallen och tar plats. 
Han har målat med Alcro väggfärg som är akrylbaserad  
Eftersom källaren har en annan fukt vill han veta hur fuktigt det är innan han målar men även hur luftfuktigheten är i rummet när färgen torkar. Eftersom de påverkar torkningstiden + att för mycket fukt kan orsaka mögel (han vill inte göra frugan sur på att de skulle ske), behöver han en luftfuktighetsmätare så han kan avgöra luftens fuktighet samt veta om han ska sätta in en fläkt eller annat dylikt för att snabba på processen och minska luftfuktigheten i rummet. 


## Beskrivning av system

## Sensor DHT11
Vi kommer använda en DHT11 sensor vilket mäter temperatur och luftfuktighet
Senors har fyra pinnar vilkt är följande:
1. VCC - mäter ström i vårt fall använder vi en microcontroller NodeMCU ESP8266 som klara 3,3 volt
2. Data - som skickas till microcontorller och vidare till Arduino IDE
3. NC (not connected)- används ej
4. GND - Elektrisk krets går ut genom GND pinnen och tillbaka till microcontorller

### Hur den funkar
I sensor finns ett chip som mäter just luftfuktighet och temperatur, genom Data pinnen i sensorn skickas värderna  till NodeMCU och skickar vidare den seriala datan till
Ardunio eller annan applaikation genom USB.




## Visualisering
