# smart_supply_chain
# Smart Supply Chain System 🚚📦

A web-based logistics intelligence platform that predicts delivery delays and helps optimize shipment decisions using real-time data like distance and weather conditions.

---

## 👨‍💻 What We Built

The Smart Supply Chain System allows users to enter shipment details (**Source → Destination**) and receive insights about possible delivery delays.

The system analyzes:

* 📏 Distance between locations
* 🌦️ Real-time weather conditions

Then predicts:

* Delay Risk: Low / Medium / High
* Suggestion: Safe / Monitor / Reroute

---

## 🧠 Core Idea

The goal of this project is to improve logistics planning by using live data and simple AI-based prediction logic.

Example:

* Long distance → Higher risk
* Rain / Storm → Higher risk

This helps logistics managers make smarter routing decisions.

---

## ⚙️ Tech Stack Used

### 🔹 Backend

* **Python**
* **Flask**
  Used for:
* API handling
* Business logic
* Database interaction

### 🔹 Database

* **SQLite**
  Used to store shipment records and prediction history.

### 🔹 Frontend

* **HTML**
* **CSS**
* **JavaScript**

Used for:

* Dashboard UI
* Forms and interactions
* Dynamic updates

### 🗺️ Map Integration

* **Leaflet.js**
  Used for:
* Displaying maps
* Route visualization
* Markers for source and destination

---

## 🌍 APIs & Resources Used

### 📍 OpenStreetMap (Nominatim API)

Converts city names into latitude and longitude coordinates.

Example:
Mumbai → `19.0760, 72.8777`

---

### 🌦️ OpenWeatherMap API

Fetches real-time weather information for shipment locations.

Used to check conditions like:

* Clear
* Rain
* Thunderstorm
* Clouds

---

### 📊 Chart.js

Used to create visual analytics graphs such as:

* Distance analysis
* Weather impact
* Delay risk chart

---

## 🧠 Prediction Logic (AI Part)

This project uses a **rule-based prediction system**.

### Factors considered:

1. **Distance**

   * Short → Low risk
   * Medium → Medium risk
   * Long → High risk

2. **Weather**

   * Clear → Low risk
   * Cloudy → Medium risk
   * Rain / Storm → High risk

### Output:

| Risk Level | Suggestion       |
| ---------- | ---------------- |
| ✔ Low      | Safe Route       |
| ⚠ Medium   | Monitor Shipment |
| 🚨 High    | Reroute Shipment |

---

## 🔄 System Flow

1. User enters shipment details
2. System fetches coordinates using Nominatim API
3. Calculates distance using Haversine Formula
4. Fetches weather using OpenWeatherMap API
5. Predicts delay risk
6. Stores shipment data in SQLite database
7. Displays results on:

   * Interactive Dashboard
   * Map Route
   * Graph Analysis

---

## 📊 Features Implemented

✅ Real-time weather integration
✅ Distance calculation using Haversine Formula
✅ Delay risk prediction system
✅ Interactive dashboard
✅ Route visualization using Leaflet
✅ Dynamic graph on row click
✅ Row highlight for better UX
✅ Modern landing page UI

---

## 📐 Distance Calculation Formula

The system uses the **Haversine Formula** to calculate distance between two coordinates.

[
d = 2r \cdot \arcsin(\sqrt{a})
]

Where:

[
a = \sin^2(\frac{\Delta \phi}{2}) + \cos(\phi_1)\cos(\phi_2)\sin^2(\frac{\Delta \lambda}{2})
]

---

## 🚀 Future Improvements

* Integrate Machine Learning model for better predictions
* Add live traffic analysis
* Multi-vehicle shipment tracking
* Admin panel for logistics managers
* Export reports as PDF/Excel

---

## ▶️ How to Run the Project

1. Clone the repository:

```bash
git clone <your-repo-link>
```

2. Navigate to project folder:

```bash
cd smart-supply-chain-system
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run Flask app:

```bash
python app.py
```

5. Open browser:

```cpp
http://127.0.0.1:5000/
```

---

## 👥 Team / Contributors

Developed as a logistics optimization web application project 🚚✨

---

This project demonstrates how real-time APIs and rule-based AI can improve supply chain efficiency.
