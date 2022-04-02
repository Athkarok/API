from flask import request, jsonify, Blueprint
from services.quote import Quote
from helpers.token import get_user_data
quote_b = Blueprint("quote", __name__, url_prefix='/quote')

quote = Quote()

@quote_b.route("/", methods=["GET", "POST"])
def quotes():

    if request.method == "GET":

        quotes = []
        for i in quote.get_quotes():
            quotes.append({
                "id": i[0],
                "quote": i[1],
                "author": i[2] if i[2] != None else ""
            })

        return {"quotes": quotes}

    if not (token_data := get_user_data(request.headers)):
        return jsonify({"error": "NOT ALLOWED TO ACCESS THIS RESOURCE."}), 403
    
    if token_data["role"] != "ADMIN":
        return jsonify({"error": "NOT ALLOWED TO ACCESS THIS RESOURCE."}), 403

    if request.method == "POST":
        req_data = request.get_json(force=True)

        if not "text" in req_data.keys():
            return jsonify({"error": "MUST PROVIDE TEXT."})

        text = req_data["text"]
        author = None

        if "author" in req_data.keys():
            author = req_data["author"]

        quote.add_quote(text, author)
        return jsonify({"success": "Quote added."})


@quote_b.route("/today", methods=["GET"])
def get_quote_of_day():
    q = quote.get_quote_of_day()

    if q is None:
        return {"error": "No Quotes"}

    return jsonify({
        "id": q[0],
        "quote": q[1],
        "author": q[2] if q[2] != None else ""
    })
