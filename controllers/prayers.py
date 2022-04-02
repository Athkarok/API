import requests as rq
from flask import request, jsonify, Blueprint

prayers_b = Blueprint("prayers", __name__, url_prefix="/prayers")

@prayers_b.route("/", methods=["GET"])
def prayers():
    try: 
        latitude = float(request.args.get("latitude")) 
        longitude = float(request.args.get("longitude"))
    except:
        return jsonify({"error": "Invalid Or Missing Inputs."})

    if latitude < -90 or latitude > 90 or longitude < -180 or longitude > 180:
        return jsonify({"error": "Invalid Latitude Or Longitude."})

    try: 
        req = rq.get(f"https://api.aladhan.com/v1/timings?latitude={latitude}&longitude={longitude}&method=4&adjustment=1")
    except:
        return jsonify({"error": "error from outer API."})

    response = req.json()["data"]
    data = jsonify({
        "code": 200,
        "timings": {
            "Fajr": response["timings"]["Fajr"],
            "Sunrise": response["timings"]["Sunrise"],
            "Dhuhr": response["timings"]["Dhuhr"],
            "Asr": response["timings"]["Asr"],
            "Sunset": response["timings"]["Sunset"],
            "Maghrib": response["timings"]["Maghrib"],
            "Isha": response["timings"]["Isha"],
            "Imsak": response["timings"]["Imsak"],
            "Midnight": response["timings"]["Midnight"]
        },
        "date": {
            "readable": response["date"]["readable"],
            "timestamp": response["date"]["timestamp"],
            "hijri": {
                "date": response["date"]["hijri"]["date"],
                "format": response["date"]["hijri"]["format"],
                "day": response["date"]["hijri"]["day"],
                "weekday": {
                    "en": response["date"]["hijri"]["weekday"]["en"],
                    "ar": response["date"]["hijri"]["weekday"]["ar"]
                },
                "month": {
                    "number": response["date"]["hijri"]["month"]["number"],
                    "en": response["date"]["hijri"]["month"]["en"],
                    "ar": response["date"]["hijri"]["month"]["ar"]
                },
                "year": response["date"]["hijri"]["year"],
                "holidays": response["date"]["hijri"]["holidays"]
            }
        }
        })
    
    return data