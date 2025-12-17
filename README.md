# Realtime Sensor Data Visualization

Detta repository demonstrerar hur sensor-data kan samlas in från en DHT11-sensor via
en ESP8266-microcontroller och skickas till en egenutvecklad Python-server, där datan
visualiseras i realtid i en webbaserad graf. 

Projektet är uppdelat i firmware, backend och frontend.

Kod för Arduino IDE, HTML och Python finns som seprata filer i repot!

---

## Systemöversikt

DHT11 → ESP8266 (Arduino/C++) → HTTP → Python-server → CSV → HTTP → HTML/JS-graf

Systemet är uppbyggt kring en central server som fungerar som mellanhand.
ESP8266 skickar sensor-data till servern via HTTP.
Servern lagrar datan och gör den tillgänglig för frontend, som hämtar data via HTTP
för visualisering i realtid.



---

## Bill of Materials (BOM)

| Komponent | Antal | Kommentar |
|--------|------|---------|
| ESP8266 | 1 | Pulsivo kit |
| DHT11 | 1 | Temperatur & luftfuktighet |
| Breadboard | 1 | Valfritt men rekommenderas |
| Jumper wires | 3 | Koppling |
| Female to male kablar | 3| valfritt |
| USB-kabel (USB-C) | 1 | För flashning (& ström) |
| Powerbank | 1 | valfritt - för att ge ström |

Så här ska DHT11 och ESP8266 vara kopplad 


---

## Steg 1 – Firmware (ESP8266)

För att kunna koppla ESP8266 till WiFi behöver du ett nätverk som ger 2.4 GHz (2G). En annan modell/ nyare microcontroller kan klara 5G)

1. Öppna firmware-koden i Arduino IDE
2. Uppdatera följande värden i koden:
   - WiFi SSID
   - WiFi-lösenord
   - Serverns IP-adress ( IP framgår genom `ipconfig getifaddr en0` i terminalen)
   - Serverns port (anges i serverkoden och skrivs ut i terminalen vid start)
4. Ladda upp koden till microcontrollern
5. Öppna serial monitor för att se att ESP8266 är kopplad till servern och sänder ut data

(Sensorn skickar sensorvärden periodiskt till servern via HTTP POST.)

---

## Steg 2 – Starta Python-servern

```bash
cd *servermappensnamn*
python3 server.py
```

Servern är implementerad i Python 3 och körs lokalt.
Den tar emot sensor-data via HTTP, sparar värden i en CSV-fil och gör datan
tillgänglig för frontend dvs i webbläsaren via HTTP.

---

## Dataformat

Sensor-data skickas som JSON via HTTP:

```
  "temperature": 22.5,
  "humidity": 45,
  "timestamp": 20000
}
```
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
