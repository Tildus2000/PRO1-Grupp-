#!/usr/bin/env python3
import http.server
import socketserver
import urllib.parse
import csv
import os
import json
import datetime

PORT = 8000
HTML_FILENAME = "BossesGraf.html"
CSV_FILENAME = "sensor_data.csv"


class SensorHandler(http.server.SimpleHTTPRequestHandler):
    # ---- GET ----
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        # 1) Start-sida: skicka ut Grafen.html
        if path == "/" or path == f"/{HTML_FILENAME}":
            try:
                with open(HTML_FILENAME, "rb") as f:
                    content = f.read()
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(content)))
                self.end_headers()
                self.wfile.write(content)
            except FileNotFoundError:
                self.send_error(404, "graf.html hittades inte")
            return

        # 2) /data → ALL historisk data som JSON-lista
        if path == "/data":
            data = []
            if os.path.exists(CSV_FILENAME):
                with open(CSV_FILENAME, newline="", encoding="utf-8") as f:
                    reader = csv.reader(f)
                    for row in reader:
                        # timestamp, method, temp, hum
                        if len(row) == 4 and row[1] == "POST":
                            ts, _, temp, hum = row
                            try:
                                temp_f = float(temp)
                                hum_f = float(hum)
                            except ValueError:
                                continue
                            data.append(
                                {
                                    "time": ts,
                                    "temperature": temp_f,
                                    "humidity": hum_f,
                                }
                            )

            payload = json.dumps(data).encode("utf-8")
            self.send_response(200)
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)
            return

        # 3) /sensor → SENASTE värdet som ett objekt
        if path == "/sensor":
            last = None
            if os.path.exists(CSV_FILENAME):
                with open(CSV_FILENAME, newline="", encoding="utf-8") as f:
                    reader = csv.reader(f)
                    for row in reader:
                        if len(row) == 4 and row[1] == "POST":
                            last = row

            if not last:
                payload = json.dumps({"error": "no data yet"}).encode("utf-8")
                self.send_response(404)
                self.send_header("Access-Control-Allow-Origin", "*")
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(payload)))
                self.end_headers()
                self.wfile.write(payload)
                return

            ts, _, temp, hum = last
            try:
                temp_f = float(temp)
                hum_f = float(hum)
            except ValueError:
                temp_f = None
                hum_f = None

            payload = json.dumps(
                {
                    "time": ts,
                    "temperature": temp_f,
                    "humidity": hum_f,
                }
            ).encode("utf-8")

            self.send_response(200)
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)
            return

        # Annars: statiska filer etc
        return super().do_GET()

    # ---- POST från ESP8266 ----
    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length).decode("utf-8")

        params = urllib.parse.parse_qs(body)
        temp = params.get("temperature", [None])[0]
        hum = params.get("humidity", [None])[0]

        timestamp = datetime.datetime.now().isoformat(timespec="seconds")

        # Skriv till CSV: timestamp, method, temp, hum
        os.makedirs(os.path.dirname(CSV_FILENAME), exist_ok=True) if os.path.dirname(CSV_FILENAME) else None
        with open(CSV_FILENAME, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, "POST", temp, hum])

        print(f"Got data: temp={temp}, hum={hum}")

        payload = json.dumps({"status": "ok"}).encode("utf-8")
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)


if __name__ == "__main__":
    with socketserver.ThreadingTCPServer(("", PORT), SensorHandler) as httpd:
        print(f"Server kör på port {PORT}")
        print("Öppna:  http://localhost:8000/ i din webbläsare")
        httpd.serve_forever()
