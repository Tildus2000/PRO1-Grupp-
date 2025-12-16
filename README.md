# Realtime Sensor Data Visualization

Detta repository demonstrerar hur sensor-data kan samlas in från en DHT11-sensor via
en ESP8266-microcontroller och skickas till en egenutvecklad Python-server, där datan
visualiseras i realtid i en webbaserad graf.

Projektet är uppdelat i firmware, backend och frontend.

Kod för Arduino IDE, HTML och Python finns som seprata filer i repot!

---

## Systemöversikt

DHT11 → ESP8266 (Arduino/C++) → HTTP → Python-server → CSV → HTTP → HTML/JS-graf

---

## Bill of Materials (BOM)

| Komponent | Antal | Kommentar |
|--------|------|---------|
| ESP8266 | 1 | Pulsivo kit |
| DHT11 | 1 | Temperatur & luftfuktighet |
| Breadboard | 1 | Valfritt men rekommenderas |
| Jumper wires | 3 | Koppling |
| USB-kabel (USB-C) | 1 | För flashning och ström |

---

## Steg 1 – Firmware (ESP8266)

1. Öppna firmware-koden i Arduino IDE
2. Uppdatera följande värden i koden:
   - WiFi SSID
   - WiFi-lösenord
   - Serverns IP-adress och port ( kan få fram IP genom att köra `ipconfig getifaddr en0` i terminalen)
3. Välj rätt board ( Generic ESP8266 module) & port (den som kommer upp när du kopplar ESP8266 till din dator)
4. Ladda upp koden till mikrokontrollern
5. Öppna serial monitor för att se att ESP8266 är kopplad till servern och sänder ut data

(Sensorn skickar sensorvärden periodiskt till servern via HTTP POST.)

---

## Steg 2 – Starta Python-servern

```bash
cd *servernamn*
python3 server.py
```

Servern är implementerad i Python 3 och körs lokalt.
Den tar emot sensor-data via HTTP, sparar värden i en CSV-fil och gör datan
tillgänglig för frontend dvs i webbläsaren via HTTP.

---

## Dataformat

Sensor-data skickas som JSON:

{
  "temperature": 22.5,
  "humidity": 45,
  "timestamp": 20000
}

---
## Steg 3 – Frontend (Graf)

* Öppna index.html i webbläsaren via localhost:*0000* (anges i terminalen)
* Grafen hämtar data från servern via HTTP
* Data visualiseras som en multi-axis line chart

Grafkoden är baserad på exempel från chartjs.org

---

## Verifiering

* ESP8266 skickar data kontinuerligt
* CSV-filen uppdateras på servern
* Grafen uppdateras i realtid
