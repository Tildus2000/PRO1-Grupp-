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

  <img width="1287" height="645" alt="graf" src="https://github.com/user-attachments/assets/eea873cd-9de3-44b4-a0c8-b359443180de" />

 

## Från ESP8266 till graf

- Vi skapade en server i python  använder HTTP-protokoll för att kommunicera med Arduino (klinet) 
- Arduino skickar temperatur och luftfuk enhetsdata vis ESP8266 som en HTTP-POST förfrågan till servern
- Vår server tar emot datan och sparar den i en CSV-fil där alla data och mätningar över tid sparas.
- När vi öppnar webbläsaren gör en HTTP-GET förfrågan för att hämta HTML-sidan och sensordata. 
- Servern svara då med JSON-objekt, vilket ger ett dataformat som är enkelt att läsa för oss och webbsidan
- Javascript som vi har använt för att skapa grafen läser in Jason datan och ritar då upp grafen med värden i realtid.

```
PORT = 8000
HTML_FILENAME = "graf.html"
CSV_FILENAME = "sensor_data.csv"
```
- Vilken port servern kör på (8000).
- Vilken HTML-fil som är startsidan (grafen).
- Vilken CSV-fil som används som “datalager” för alla mätninga

  ``` if __name__ == "__main__":
    with socketserver.ThreadingTCPServer(("", PORT), SensorHandler) as httpd:
        print(f"Server kör på port {PORT}")
        print("Öppna:  http://localhost:8000/  (eller http://172.20.10.5:8000/ på annan enhet)")
        httpd.serve_forever() ```

- Startar själva HTTP-servern.
- Använder Sensor Handler för att hantera alla GET- och POST-anrop.
- serve_forever() gör att servern står och lyssnar hela tiden.

 
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


