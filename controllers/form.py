import os
# flask modules
from flask import request, jsonify, Blueprint

from services.form import FormAdmin

from services.user import User

from helpers.token import get_user_data

# email services
from services.mail import MailAdmin
ma = MailAdmin()


form_b = Blueprint("form", __name__, url_prefix="/form")

form_admin = FormAdmin()

@form_b.route("/contact", methods=["POST"])
def suggestion():
    req_data = request.get_json(force=True)

    # Check if all required data exsisted
    for key in ["role", "message"]:
        if not key in req_data.keys():
            return jsonify({
                "error": "Missing Required Input."
            }), 400

    role = req_data["role"]
    message = req_data["message"]

    name = None
    if "name" in req_data.keys():
        name = req_data["name"]
    
    user = None
    user_id = None
    if (user_data := get_user_data(request.headers)):
        user_id = user_data["user_id"]
        user = User(user_id)

    form_admin.submit("Athkarok - sug", user_id, name, role, message)
    

    ma.send_template("general.html", "رسالة جديدة في فورم المقترحات.", 
    f"""
        اسم المرسل: {name if not user else user.get_full_name()},
        الغرض: {role},
        نص الرسالة: {message}
    """, [os.environ.get("M_ADMIN_EMAIL")])

    if user:
        ma.send_template("general.html", "تم إستلام رسالتكم.", 
        f"""مرحبا {user.first_name}, 
        نود إعلامكم بأنه تم إسلام رسالتكم بنجاح.

        نشكر لكم تواصلكم ❤️
        """, [user.email])

    return jsonify({"success": "Form Successfully submitted."})
