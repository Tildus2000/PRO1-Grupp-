# PRO1 Grupp 1 Luftfuktightesmätare

## Syfte:
Syftet är att skapa en luftfuktighetsmätare som kan mäta fukt och temp i ett rum som ska målas för att kunna göra miljön så optimalt som möjligt för väggfärg.

## Analys av användare och kontext:
Våra användare är byggmålare och som i detta fall målar inomhus. 
Källare har ofta inte samma isolering eller värme som resterande delar av ett hus, det är även vanligt med ökad luftfutkighet i dessa ytor. Temperatur och luftfuktighet har stor inverkarn på hur lång tid det tar för väggfärg att torka samt hur den torkar. Exempelivs ytor med högluftfuktighet torkar långsammare, som yrkesamm målare med deadlines vill man att torkniningsproccessen ska gå så snabbt som möjligt samt att resulatet ska bli så bra som möjligt.
Genom en DHT11 sensaor kan målare få viktigt infromation som avögr hur de ska göra för att uppnå bästa resultat, exemeplivs om rummet behöver element för att höja värmen, eller ventlation för att ändra luftfuktighetetn. Detta för att göra miljön så optimal som möjligt.

En väggfärg från Alcro som är ett vanligt märke inom målarbranchen, fungerar optimalt i 23 garder celcius och 50% luftfuktighet. Då är färgen klibbfri inom 50 minuter och övermålningsbar inom 2 timmar. 

#### Scenario:
Bosse 63år som har varit målare de senaste 40 åren ska måla om väggar i sin egna hemverkstad som ligger i källaren. Han har monterat ner hyllor och flyttat på verktyg som nu ligger och tar plats i hallen vilket gör frugan sur. Han vill så fort som möjligt bli klar och få tillbaka friden i hemmet. Han vet att Alcro väggfärg trivs och blir som bäst i rumstemperatur och med en relativ luftfuktighet på 40-60% dock är de betydligt svalare och högre luftfuktighet i källaren, vilket kommer gör att de tar längre tid för färgen att torka samt resluterar i ojämn torkning och ett ojämnt fulare reslutat. 
Detta vill Bosse såklart undvika och därför är han tacksam att han har sin luftighetsmätare där han kan kontrollera luften innan har börjar måla och hur den beteer sig under torkningsfasen, då kan han enkelt sätta in ett element, samt ventlation för att skapa den optimala miljön. 


## Beskrivning av system

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
 

## Visualisering
Vi tänker använda oss av en multi axis Line chart för att kunna se temp och luftfuktighet över tid. Detta för att realsitiskt se hur lång tid de tar för färgen att torka.

 <img width="400" height="200" alt="MultiAxis" src="https://github.com/user-attachments/assets/1b74b85f-b9c3-4baa-bc2c-b6025061ee7a" />

