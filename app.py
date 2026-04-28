from flask import Flask, render_template, request, redirect, url_for
from modules.prediction import predict_delay
from modules.weather import get_weather
from modules.database import init_db, insert_shipment, get_shipments
from modules.utils import get_coordinates, calculate_distance

app = Flask(__name__)

init_db()ṇ

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add", methods=["POST"])
def add():
    try:
        source = request.form["source"].strip()
        destination = request.form["destination"].strip()

        lat1, lon1 = get_coordinates(source)
        lat2, lon2 = get_coordinates(destination)

        if lat1 is None or lat2 is None:
            return redirect(url_for("index"))   # ✅ no ugly page

        distance = calculate_distance(lat1, lon1, lat2, lon2)

        weather = get_weather(destination)
        risk, suggestion = predict_delay(distance, weather)

        insert_shipment(source, destination, distance, weather, risk, suggestion)

        return redirect(url_for("dashboard"))

    except Exception as e:
        print("ADD ERROR:", e)
        return redirect(url_for("index"))

@app.route("/dashboard")
def dashboard():
    shipments = get_shipments()

    enriched = []
    for s in shipments:
        lat1, lon1 = get_coordinates(s[1])
        lat2, lon2 = get_coordinates(s[2])

        enriched.append({
            "id": s[0],
            "source": s[1],
            "destination": s[2],
            "distance": s[3],
            "weather": s[4],
            "risk": s[5],
            "suggestion": s[6],
            "lat1": lat1,
            "lon1": lon1,
            "lat2": lat2,
            "lon2": lon2
        })

    latest = enriched[0] if enriched else None
    high_alert = latest and latest["risk"] == "High"

    return render_template(
        "dashboard.html",
        shipments=enriched,
        latest=latest,
        high_alert=high_alert
    )


if __name__ == "__main__":
    app.run(debug=True)