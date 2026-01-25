\# Air Quality Monitor



A real-time air quality monitoring system using ESP32 and BME680 sensor with web dashboard visualization.



\## Features



\- 🌡️ Real-time temperature monitoring

\- 💧 Humidity tracking

\- 📊 Historical data visualization with interactive graphs

\- 🔄 Auto-refreshing dashboard (updates every 5 seconds)

\- 💾 Persistent data storage



\## Tech Stack



\*\*Hardware:\*\*

\- ESP32-DevKitC-32E microcontroller

\- Adafruit BME680 sensor (temperature, humidity, pressure, air quality)



\*\*Backend:\*\*

\- Python 3

\- Flask (REST API)

\- JSON file storage



\*\*Frontend:\*\*

\- HTML/CSS/JavaScript

\- Chart.js for data visualization



\## Project Structure

```

air-quality-monitor/

├── backend/

│   ├── app.py              # Flask API server

│   └── sensor\_data.json    # Data storage (generated at runtime)

├── frontend/

│   └── index.html          # Dashboard interface

└── README.md

```



\## Setup \& Installation



\### Backend



1\. Navigate to backend folder:

```bash

cd backend

```



2\. Install dependencies:

```bash

pip install flask flask-cors

```



3\. Run the server:

```bash

python app.py

```



Server will start on `http://127.0.0.1:5000`



\### Frontend



Simply open `frontend/index.html` in your browser.



\## API Endpoints



\*\*POST /api/data\*\*

\- Receives sensor data

\- Body: `{"temperature": number, "humidity": number}`

\- Returns: `{"status": "success"}`



\*\*GET /api/data\*\*

\- Retrieves all stored sensor data

\- Returns: Array of sensor readings with timestamps



\## Hardware Setup



\*Coming soon - waiting for hardware delivery\*



\## Future Improvements



\- \[ ] Add ESP32 firmware code

\- \[ ] Deploy backend to cloud (Render/Railway)

\- \[ ] Add pressure and air quality metrics

\- \[ ] Implement data export (CSV download)

\- \[ ] Add email/SMS alerts for threshold breaches

\- \[ ] Mobile app version



\## Author



Built as a portfolio project for internship applications.




git commit -m "Add comprehensive README"

git push

