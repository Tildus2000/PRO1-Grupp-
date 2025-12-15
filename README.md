# Realtime sensor data Visualization

Detta repo demostrerar hur sensor data kan samlas in från en DHT 11 sensor via en ESP8266 microcontroller och vidare till en egenutvecklad python server, där datan visualiseras i realtid i en webbgraf. 

Projektet är uppdelat i firmware,backend och frontend

---
## Systemöversikt

DHT11->ESP8266 (Arduino/C++)->HTTP->Python server->CSV->HTTP->HTML/JS graf

---
## Bill of materials (BOM)

| Komponent | Antal | Kommentar |
|--------|------|---------|
| ESP8266 | 1 | Pulsivo kit |
| DHT11 | 1 | Temperatur & luftfuktighet |
| Breadboard | 1 | Valfritt men rekommenderas|
| Jumper wires | 3| koppling|
| USB (USB-C)-kabel | 1 | Flashing + strömkälla |

---

## Steg 1 - Firmwear (ESP8266)

1. Öppna i Arduino IDE
2. Uppdatera följande värden i koden:
   * WiFi SSID
   * WiFi lösenord
   * Severns IP-adress och port
3. Välj rätt borad (ESP8266)
4. Ladda upp koden till microcontroller

Sensorn skickar sensorvärden periodiskt via HTTP POST

---
## Steg 2 - Starta Python servern

```
cd *servernamn*
Python3 server.py
```
servern:
Servern är implementerad i Python 3 och körs lokalt.
Den tar emot sensor-data via HTTP, sparar värden i en CSV-fil
och gör datan tillgänglig för frontend via HTTP.

### Datafromat 
Senor data skcikas som JSON

```
{
  "temperature": 22.5,
  "humidity": 45,
  "timestamp": 20000
}
```
---
## Steg 3 - Frontend (graf)
1. öppna ditt index.html i webbläsaren genom localhost:0000 (angiva värdet som står i terminalen)
2. Grafen Hämtar data från servern via HTTP
3. Data visualiseras som en multi-axis line chart

Grafkoden är baserad på JSchart.com

---
## Verifiering 
* Esp8266 skickar data kontinuleigt
* CSV-filen uppdateras på servern
* Grafen uppdateras realtid
