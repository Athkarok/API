from flask import request, jsonify, Blueprint
# zikr
from services.zikr import ZikrAdmin
# progress
from services.progress.zikr_session import zikr_session
from services.progress.wheel import wheel
# helpers
from helpers.token import login_required, get_user_data


progress_b = Blueprint("progress", __name__, url_prefix="/progress")


@progress_b.route("/wheel", methods=["POST"])
@login_required
def set_wheel_done():
    user_id = get_user_data(request.headers)["user_id"]

    wheel.set_done(user_id)
    return jsonify({"success": "Wheel session successfully added."}), 200


zikr_admin = ZikrAdmin()


@progress_b.route("/zikr", methods=["POST"])
@login_required
def add_zikr_session():
    user_id = get_user_data(request.headers)["user_id"]

    req_data = request.get_json(force=True)
    group_id = req_data["group_id"]

    if group_id not in zikr_admin.get_group_Ids():
        return jsonify({
            "error": "wrong group_id."
        }), 400

    zikr_session.add_session(user_id, group_id)
    return jsonify({
        "success": "Zikr session successfully added."
    })

