# Multi Axis Line Chart

I vårt projekt använder vi en linjediagram-graf (multi axis line chart) för att visualisera de mätvärden som vi får in av sensorn. Koden bygger på  Chart.js kod, grafen visas i webbläsaren genom vår HTML-fil, och den uppdateras med data som skickas från ESP8266 mikrokontroller. Syftet med grafen är att vara ett tydligt och enkelt verktyg som hjälper användaren (Bosse) att förstå kilmatet i rummet.  
___

**Grafen är det viktigaste verktyget för att:**

- snabbt förstå rumsförhållanden 
- se om miljön behöver förbättras (avfuktare, ventilation, värme)
- Hjälpa målare att ta beslut
 
## Varför vi valde ett linjediagram: 

- Ger tydligt tidsutveckling, den förändras över tid och perfekt för klimatmättning.  
- Snabbt och Lätt att förstå för användaren (Bosse), hur fuktigheten förändras, om miljön är bra för målning m.m 
- Två data linjer passar bra för att just se både temperatur och luftfuktighet. Det går snabbt at se skillnader över tid.  
- Fokus på användarvänlighet 
 

## Från ESP8266 till graf

Vi har gjort en egen HTTP server i python. 
 
## Grafen visar två linjer över tid och uppdaterats automatiskt när nya värden skickas från vår ESP8266.: 

**En temperatur(c)** denna blå linje: om temperaturen är stabil, om rummet är kalt/varmt och hur temperaturen förändras över tid.  

**En luftfuktighet(%)** denna röd linje: om luftfuktighet har sjunkit till rätt nivå, den förändras långsam eller snabbt.  

 **Vi använder:**

- Röda linje (luftfuktighet)

- blå linje (temperatur) 
 
**Chart.js hanterar:**
* datapunkter 
* y-axlar 
* tid på x-axeln 
* animationer 
 

## Hur grafen fungerar: 
Så här fungerar den steg för steg: 
1. Sensorvärden mäts
   
DHT11-sensorn registrerar: 

- aktuell temperatur 
- aktuell luftfuktighet 
- Dessa värden läses av av ESP8266 via kod (Arduino IDE). 


2. ESP8266 skickar datan via WiFi 
ESP8266 skickar sensordatan till en webbsida. Kommunikationen sker  

(JSON-format), det är lätt att tolka  
Det gör att datan blir tillgänglig i realtid. 

 
 3. Webbsidan tar emot datan 
HTML-sidan innehåller JavaScript-kod som: 

- tar emot värdena 
- lägger till dem i grafens dataset 
- uppdaterar grafen automatiskt 
(grafen utvecklas live). 


4. Chart.js ritar upp grafen 
Chart.js skapar linjerna baserat på värdena.


