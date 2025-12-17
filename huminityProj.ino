#include <ESP8266WiFi.h>
#include <SimpleDHT.h>

#ifndef STASSID
#define STASSID "MDU_guest"
#define STAPSK "Frozen202512"
#endif

const char* ssid = STASSID;
const char* password = STAPSK;

const char* host = "10.132.169.159";  
const uint16_t port = 8000;

const int dht_pin = 13; 
SimpleDHT11 dht11;

void setup() {
  Serial.begin(9600);
  Serial.println();
  Serial.println("Booting…");

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  Serial.print("Connecting to WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }

  Serial.println("\nWiFi connected!");
  Serial.print("ESP IP address: ");
  Serial.println(WiFi.localIP());
}

void loop() 
{
  // ⬅️ 1. Läs DHT11 med felkontroll
  byte temperature = 0;
  byte humidity = 0;

  int err = dht11.read(dht_pin, &temperature, &humidity, NULL);
  if (err != SimpleDHTErrSuccess) {
    Serial.print("DHT11 read error: ");
    Serial.println(err);
    delay(1000);
    return;
  }

  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.println(" C");

  Serial.print("Humidity: ");
  Serial.print(humidity);
  Serial.println(" %");
  Serial.println();

  // ⬅️ 2. Skapa POST-data
  String postData = "temperature=" + String(temperature) +
                    "&humidity="   + String(humidity);

  Serial.print("Connecting to server ");
  Serial.print(host);
  Serial.print(":");
  Serial.println(port);

  WiFiClient client;
  if (!client.connect(host, port)) {
    Serial.println("Connection failed ❌");
    delay(5000);
    return;
  }

  Serial.println("Connected, sending POST…");

  // ⬅️ 3. Skicka HTTP POST
  String request  = "POST / HTTP/1.1\r\n";
  request        += "Host: " + String(host) + "\r\n";
  request        += "Content-Type: application/x-www-form-urlencoded\r\n";
  request        += "Content-Length: " + String(postData.length()) + "\r\n";
  request        += "Connection: close\r\n";
  request        += "\r\n";
  request        += postData;

  client.print(request);

  // (Valfritt) läs serversvar
  unsigned long timeout = millis();
  while (client.connected() && millis() - timeout < 2000) {
    while (client.available()) {
      char c = client.read();
      Serial.print(c);
      timeout = millis();
    }
  }

  client.stop();
  Serial.println("Connection closed\n");

  // ⬅️ 4. Vänta 5 sek innan nästa mätning (ändra till 10000 för 10 sek)
  delay(5000);
}
