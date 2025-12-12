# Multi Axis Line Chart

I vårt projekt använder vi en linjediagram-graf (multi axis line chart) för att visualisera de mätvärden som vi får in av sensorn. Koden bygger på  Chart.js kod, grafen visas i webbläsaren genom vår HTML-fil, och den uppdateras med data som skickas från ESP8266 mikrokontroller. Syftet med grafen är att vara ett tydligt och enkelt verktyg som hjälper användaren (Bosse) att förstå kilmatet i rummet.  

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

- Vi skapade en server i python som använder HTTP-protokoll för att kommunicera med Arduino (klinet) 
- Arduino skickar temperatur och luftfuktighetsdata via ESP8266 som en HTTP-POST förfrågan till servern
- Vår server tar emot datan och sparar den i en CSV-fil där alla data och mätningar över tid sparas.
- När vi öppnar webbläsaren görs en HTTP-GET förfrågan för att hämta HTML-sidan och sensordata. 
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


## Hämta data från servern
```JS
// Hämtar SENASTE värdet från Python-servern (endpoint /sensor)
    async function fetchSensorData() {
      const res = await fetch('/sensor'); // samma host+port som sidan
      if (!res.ok) {
        throw new Error('HTTP-fel: ' + res.status);
      }

      const json = await res.json();

      return {
        humidity: json.humidity,
        temperature: json.temperature
      };
    }
```
## Grafen
```JS
 const MAX_POINTS = 36; // senaste 3 timmarna (36 * 5 min)

    const data = {
      labels: [], // tidsstämplar (HH:MM)
      datasets: [
        {
          label: 'Luftfuktighet (%)',
          data: [],
          borderColor: 'rgb(255, 99, 132)',
          backgroundColor: 'rgba(255, 99, 132, 0.3)',
          yAxisID: 'y',
          tension: 0.3
        },
        {
          label: 'Temperatur (°C)',
          data: [],
          borderColor: 'rgb(54, 162, 235)',
          backgroundColor: 'rgba(54, 162, 235, 0.3)',
          yAxisID: 'y1',
          tension: 0.3
        }
      ]
    };
```
## Specifikationer om grafen
```JS
const config = {
      type: 'line',
      data: data,
      options: {
        responsive: true,
        interaction: {
          mode: 'index',
          intersect: false,
        },
        stacked: false,
        plugins: {
          title: {
            display: true,
            text: 'Luftfuktighet och temperatur - colorHue'
          },
          legend: {
            display: true
          }
        },
        scales: {
          x: {
            title: {
              display: true,
              text: 'Tid'
            }
          },
          y: {
            type: 'linear',
            display: true,
            position: 'left',
            title: {
              display: true,
              text: 'Luftfuktighet (%)'
            },
            suggestedMin: 0,
            suggestedMax: 100
          },
          y1: {
            type: 'linear',
            display: true,
            position: 'right',
            grid: {
              drawOnChartArea: false,
            },
            title: {
              display: true,
              text: 'Temperatur (°C)'
            }
          },
        }
      },
    };
```


## Skapa grafen 📊
```CPP
const ctx = document.getElementById('myChart').getContext('2d');
const myChart = new Chart(ctx, config);
```
Grafen kopplas till <canvas>-elementet och skapas med den konfiguration som definierats. 

## Skapa tidsstämplar 🕒 
```CPP
function getTimeLabel() {
  const now = new Date();
  const hh = now.getHours().toString().padStart(2, '0');
  const mm = now.getMinutes().toString().padStart(2, '0');
  return `${hh}:${mm}`;
}
```
Varje datapunkt får en tid i formatet HH:MM, som visas på X-axeln.

## Lägga till nya mätvärden 🔄 
```CPP
async function addNewReading() {
  try {
    const reading = await fetchSensorData();
    const label = getTimeLabel();

    if (data.labels.length >= MAX_POINTS) {
      data.labels.shift();
      data.datasets[0].data.shift();
      data.datasets[1].data.shift();
    }

    data.labels.push(label);
    data.datasets[0].data.push(reading.humidity);
    data.datasets[1].data.push(reading.temperature);

    myChart.update();
  } catch (err) {
    console.error('Kunde inte hämta sensor-data:', err);
  }
}
```

Funktionens ansvar:
- Hämta senaste sensorvärden
- Skapa tidsstämpel
Ta bort äldsta punkten om grafen är full
Lägga till nya värden
Uppdatera grafen visuellt

## Automatisk uppdatering ⏱️
```CPP
addNewReading();               // Kör direkt
setInterval(addNewReading, 10000); // Uppdaterar var 10:e sekund
```
Grafen håller sig uppdaterad automatiskt och visar alltid de senaste mätningarna.


