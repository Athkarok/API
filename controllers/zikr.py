from services.zikr import Zikr, ZikrAdmin
from flask import request, jsonify, Blueprint
from helpers.token import get_user_data


zikr_b = Blueprint("zikr", __name__, url_prefix="/zikr")

zikr_admin = ZikrAdmin()


def is_valid_group_id(id):
    if int(id) in zikr_admin.get_group_Ids():
        return True
    return False


@zikr_b.route("/", methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
def zikrR():

    if request.method == "GET":
        if not (g_id := request.args.get("group_id")) or not is_valid_group_id(g_id):
            return jsonify({
                "error": "Missing Or Invaild group id."
            })

        zikrs = {"zikrs": []}
        for i in zikr_admin.get_zikrs_by_group(g_id):
            zikrs["zikrs"].append(
                {
                    "id": i[0],
                    "group_id": i[1],
                    "text": i[2],
                    "repeat_times": i[3],
                    "dalel": i[4],
                    "dalel_link": i[5],
                    "weak": i[6]
                }
            )

        return zikrs, 200

    if not (token_data := get_user_data(request.headers)):
        return jsonify({"error": "NOT ALLOWED TO ACCESS THIS RESOURCE."}), 403
    
    if token_data["role"] != "ADMIN":
        return jsonify({"error": "NOT ALLOWED TO ACCESS THIS RESOURCE."}), 403

    if request.method == "POST":
        req_data = request.get_json(force=True)

        # Check if all required data exsisted
        for key in ["group_id", "text", "repeat_times", "dalel", "dalel_link", "weak"]:
            if not key in req_data.keys():
                return jsonify({
                    "error": "Missing Or Invaild Input."
                }), 400

        # Check if group id valid
        g_id = req_data["group_id"]
        if not is_valid_group_id(g_id):
            return jsonify({
                "error": "Invaild group id."
            }), 400

        # Check if repeat_times valid
        rTimes = req_data["repeat_times"]
        if not type(rTimes) == int:
            return jsonify({
                "error": "Invaild repeat_times."
            }), 400

        # Check if weak valid
        weak = req_data["weak"]
        if not weak == 0 and not weak == 1:
            return jsonify({
                "error": "Invaild weak."
            }), 400

        # No validation
        text = req_data["text"]
        dalel = req_data["dalel"]
        dalelLink = req_data["dalel_link"]

        zikr_admin.add_zikr(g_id, text, rTimes, dalel, dalelLink, weak)
        return jsonify({
            "success": "Zikr added successfully."
        }), 200

    if request.method == "PUT":
        req_data = request.get_json(force=True)

        # Check if all required data exsisted
        for key in ["id", "group_id", "text", "repeat_times", "dalel", "dalel_link", "weak"]:
            if not key in req_data.keys():
                return jsonify({"error": "Missing Or Invaild Input."}), 400

        # Check if valid id
        if not type(id :=req_data["id"]) == int:
            return jsonify({"error": "Invalid id."}), 400

        # Check if group id valid
        g_id = req_data["group_id"]
        if not type(g_id) == int or not is_valid_group_id(g_id):
            return jsonify({"error": "Invaild group id."}), 400

        # Check if repeat_times valid
        rTimes = req_data["repeat_times"]
        if not type(rTimes) == int:
            return jsonify({"error": "Invaild repeat_times."}), 400

        # Check if weak valid
        weak = req_data["weak"]
        if not weak == 0 and not weak == 1:
            return jsonify({"error": "Invaild weak."}), 400

        # No validation
        text = req_data["text"]
        dalel = req_data["dalel"]
        dalelLink = req_data["dalel_link"]

        Zikr(id).update(g_id, text, rTimes, dalel, dalelLink, weak)
        return jsonify({"message": "zikr updated."}), 200

    if request.method == "PATCH":
        req_data = request.get_json(force=True)

        if not "id" in req_data.keys():
            return jsonify({"error": "Must Provide an ID."}), 400

        # Check if valid id
        if not type(id := req_data["id"]) == int:
            return jsonify({"error": "Invalid id."}), 400

        g_id = None; text = None; rTimes = None; dalel = None; dalelLink = None; weak = None

        if "group_id" in req_data.keys():
            # Check if group id valid
            g_id = req_data["group_id"]
            if not type(g_id) == int or not is_valid_group_id(g_id):
                return jsonify({"error": "Invaild group id."}), 400

        if "repeat_times" in req_data.keys():
            # Check if repeat_times valid
            rTimes = req_data["repeat_times"]
            if not type(rTimes) == int:
                return jsonify({"error": "Invaild repeat_times."}), 400

        if "weak" in req_data.keys():
            # Check if weak valid
            weak = req_data["weak"]
            if not weak == 0 and not weak == 1:
                return jsonify({"error": "Invaild weak."}), 400

        # No validation for the rest
        if "text" in req_data.keys():
            text = req_data["text"]
        if "dalel" in req_data.keys():
            dalel = req_data["dalel"]
        if "dalel_link" in req_data.keys():
            dalelLink = req_data["dalel_link"]
        Zikr(id).update(g_id, text, rTimes, dalel, dalelLink, weak)
        return jsonify({"message": "zikr updated."}), 200

    if request.method == "DELETE":
        req_data = request.get_json(force=True)

        if not "id" in req_data.keys() or not type(id :=req_data["id"]) == int:
            return jsonify({
            "error": "Invalid Input."
            }), 400

        zikr_admin.remove_zikr(id)
        
        return jsonify({"message": "zikr removed."}), 200

