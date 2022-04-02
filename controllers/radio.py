from flask import request, jsonify, Blueprint, redirect

radio_b = Blueprint("radio", __name__, url_prefix="/radio")

radios = {
    1:"https://stream.radiojar.com/4wqre23fytzuv",
    2:"https://stream.radiojar.com/8s5u5tpdtwzuv",
    3:"https://coran.ice.infomaniak.ch/coran.aac",
    4:"https://zayedquran.gov.ae/stream.php"
}

@radio_b.route("/", methods=["GET"])
def radio():
    if not (id := request.args.get("id")):
            return jsonify({
                "error": "Missing Or Invaild Input."
            })

    try: id = int(id)
    except: return jsonify({"error": "Invaild ID."})

    try: 
        return redirect(radios[id])
    except: 
        return jsonify({"error": "Invaild ID"})
