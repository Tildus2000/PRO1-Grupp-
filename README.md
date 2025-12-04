# PRO Bosse

## Syfte:
Syftet med projektet är att skapa en luftfuktighetsmätare som kan mäta fukt och temperatur i olika rum och miljöer. Detta för att kunna appliceras inom yrken som skulle ha användning av sådant, till exempel inom måleri där både fukt och temperatur är avgörande faktorer i väggfärgers slutresultat och för yrkesverksamhet att kunna avgöra vilken typ av färg som är bäst fungerande.

## Användare och kontext:
*  Vi har utgått från grupp 2 idé men valt ett annat område där en luftfuktighets sensor skulle kunna göra nytta.
*  Våra användare är byggmålare och som målar utrymmen med hög luffuktighet och lägre temperatur såsom i en källare.
*  Källare har ofta inte samma isolering eller värme som resterande delar av ett hus, det är även vanligt med ökad luftfutkighet på dessa ytor.
*  Temperatur och luftfuktighet har stor inverkarn på hur lång tid det tar för väggfärg att torka samt hur den torkar. Väggfärg från Alcro som är ett vanligt märke inom målarbranchen, fungerar optimalt i 23 garder celcius och 50% luftfuktighet. Då är färgen klibbfri inom 50 minuter och övermålningsbar inom 2 timmar. 
*  Genom en luftfuktighets sensor kan målare få användbar information och kunskap som avögr hur de ska göra för att få bästa resultat.

#### Scenario:
<img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/470969d9-9b8e-43c5-a075-3d0831aec2f6" />

Bosse 63 år har varit målare de senaste 40 åren, han ska måla om en vägg i sin egna hemverkstad som ligger i källaren. Han har monterat ner hyllor och flyttat på verktyg som nu ligger och tar plats i hallen, vilket gör frugan sur. Han vill så fort som möjligt bli klar och få tillbaka friden i hemmet. 
Han vet att Alcro väggfärg trivs och blir som bäst i rumstemperatur och med en relativ luftfuktighet på 40-60%.
Dock är de betydligt svalare och högre luftfuktighet i källaren, vilket kommer gör att de tar längre tid för färgen att torka och torkningen blir ojämn.
Detta vill Bosse såklart undvika, om han hade en luftfuktighetsmätare skulle kan kunna kontrollera luften under torkningsfasen. Genom att exempelvis sätta in ett element, samt avfuktare för att skapa en optimal miljö.


## Sensor DHT11
Vi kommer använda en DHT11 sensor vilket mäter temperatur och luftfuktighet
Senors har fyra pinnar vilkt är följande:
1. VCC - mäter ström i vårt fall använder vi en microcontroller NodeMCU ESP8266 som klara 3,3 volt
2. Data - som skickas till microcontorller och vidare till Arduino IDE
3. NC (not connected)- används ej
4. GND - Elektrisk krets går ut genom GND pinnen och tillbaka till microcontorller

#### Hur den funkar
I sensor finns ett chip som mäter just luftfuktighet och temperatur, genom Data pinnen i sensorn skickas värderna  till NodeMCU och skickar vidare den seriala datan till
Ardunio eller annan applaikation genom USB.

## Beskrivning av system

För att vårt projekt ska fungera krävs det flera tekniska delar och det bidra till komplett system som består av:

**Pulisvio / Kopplingsschema**

Visar hur mikrokontroller, DHT11-sensor, ström och kablar kopplas ihop korrekt. 

**Alla komponenter**

NodeMCU ESP8266, DHT11-sensor, Male-to-Female jumperkablar, USB-kabel, Power bank, tillsammans bildar de ett fungerande mätsystem. 

**DHT11-sensor**

Mäter temperatur och luftfuktighet inuti plastlådan och skickar värdena till mikrokontrollern för bearbetning.  

**Arduino-koden**

Programmet som styrsystemet: läser sensordata, bearbetar den och skickar den vidare. 

**WiFi (ESP8266)** 

Detta gör att vi kan följa temperatur och luftfuktighet direkt medan experimentet pågår inne i plastlådan, utan att dra extra kablar. 

**Powerbank** 

Ger ström så att systemet kan användas helt fristående, utan vägguttag, eller utan att koppla den till en dator. 

  
<img width="200" height="200" alt="pulsivobild" src="https://github.com/user-attachments/assets/a9d7441c-e17a-4a52-993a-ee900038cbc2" />

<img width="200" height="200" alt="dht11" src="https://github.com/user-attachments/assets/0b6f9938-eacd-4f37-8b72-ed660294fd24" />




## Material och utförande av test 
-	En plastlåda men små hål i – inte för mycket ventilation. 
-  Ca 4 msk med ljummet vatten i en lite skål, för att skapa fukt 
-	Ställa lådan på golvet där det är kallare 
-	Spackla en kartongbit/ en bit gipsskiva för att efterlikna en vägg ca 5x5cm
-	Måla tunt lager akrylfärg för att efterlikna väggfärg

## Visualisering
Vi tänker använda oss av en multi axis Line chart för att kunna se temp och luftfuktighet över tid. Detta för att realsitiskt se hur lång tid de tar för färgen att torka.

 <img width="400" height="200" alt="MultiAxis" src="https://github.com/user-attachments/assets/1b74b85f-b9c3-4baa-bc2c-b6025061ee7a" />

 ## Förväntade reslutat och nytta

Om prototypen fungerar som planerat, förväntar vi oss kunna uppnå syftet med projektet: att skapa en mätare som kan mäta både fukt och temperatur inom olika ytor inomhus. Genom att se vilka resultat vi får från olika ytor, fukt (%) och temperatur (°C), och jämföra dessa med de optimala förhållanden för att färgen ska täcka, kommer prototypen inte bara ge information om rummet utan även kunna rekommendera rätt produkt. Lyckas vi räknat vi även med att både den, såväl som informationen vi samlat in, kan vara av nytta för yrkesverksamma målare.
