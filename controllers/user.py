# flask modules
from flask import request, jsonify, make_response, Blueprint
# user
from services.user import User
from services.user_admin import UserAdmin, GoogleUserAdmin
# Progress Objects
from services.progress.zikr_session import zikr_session
from services.progress.wheel import wheel
# settings
from services.settings import Settings
# validation
from helpers.validate import is_email, is_username, valid_password
# token handler
from helpers.google_auth import verify_token
from helpers.token import login_required, generate_token, get_user_data
# email services
from services.mail import MailAdmin
ma = MailAdmin()


user_b = Blueprint("user", __name__, url_prefix="/user")


user_admin = UserAdmin()


@user_b.route("/register", methods=["POST"])
def register():
    req_data = request.get_json(force=True)

    email = req_data["email"]
    if not is_email(email):
        return make_response(jsonify({
            "error": "Invalid Email."
        })), 400

    username = req_data["username"]
    if not is_username(username):
        return make_response(jsonify({
            "error": "Invalid username."
        })), 400

    password = req_data["password"]
    if not valid_password(password):
        return make_response(jsonify({
            "error": "Invalid password."
        })), 400

    fname = req_data["fname"]
    lname = req_data["lname"]
    phone_number = req_data["phone_number"]

    code = user_admin.add_user(
        email, username, password, fname, lname, phone_number)

    if code == 0:
        ma.send_template(
            "general.html",
            "تم تسجيلكم في تطبيق أذكارك.",
            f"""
                مرحبًا {fname},
                شكرًا لاستخدامك تطبيق أذكارك، نفعكم الله به وكتب لنا ولكم الأجر والثواب.
                مع تحيات إدارة التطبيق.
                """, [email])
        id = user_admin.get_id(email)
        return make_response(jsonify({
            "code": code,
            "token": generate_token(id, user_admin.get_role(id))
        })), 201

    elif code == 1:
        return make_response(jsonify({
            "code": code,
            "error": "user already exists."
        })), 409

    elif code == 2:
        return make_response(jsonify({
            "code": code,
            "error": "username is used."
        })), 409

    elif code == 3:
        return make_response(jsonify({
            "code": code,
            "error": "phone number is used."
        })), 409

    else:
        return make_response(jsonify({
            "error": code
        }))


@user_b.route("/login", methods=["POST"])
def login():

    req_data = request.get_json(force=True)

    for key in ["handle", "password"]:
        if not key in req_data.keys():
            return make_response(jsonify({
                "error": "Missing Required Input."
            })), 400

    handle = req_data["handle"]
    password = req_data["password"]

    code = user_admin.match_credentials(handle, password)

    if code == 0:
        id = user_admin.get_id(handle)
        return make_response(jsonify({
            "code": code,
            "token": generate_token(id, user_admin.get_role(id))
        })), 200

    return make_response(jsonify({
        "code": code,
        "error": "اسم المستخدم أو كلمة المرور خاطئة، أعد المحاولة أو أنشئ حساب جديد."
    })), 200


google_admin = GoogleUserAdmin()


@user_b.route("/sign_google", methods=["POST"])
def sign_google():
    req_data = request.get_json(force=True)

    if not "id_token" in req_data.keys():
        return jsonify({"error": "Missing Or Invaild Input."})

    if user := verify_token(req_data["id_token"]):
        code = google_admin.sign_user(
            user["email"], user["sub"], user["given_name"], user["family_name"])

        if code == 0:
            ma.send_template(
                "general.html",
                "تم تسجيلكم في تطبيق أذكارك.",
                f"""
                مرحبًا {user["given_name"]},
                شكرًا لاستخدامك تطبيق أذكارك، نفعكم الله به وكتب لنا ولكم الأجر والثواب.
                مع تحيات إدارة التطبيق.
                """, [user["email"]])

        if code == 2:
            id = google_admin.get_id(user["email"])
        else:
            id = google_admin.get_id(user["sub"])

        return jsonify({
            "success": "User Successfully Signed",
            "token": generate_token(id, user_admin.get_role(id))
        })

    return jsonify({"error": "Invaild Google Token."}), 403


@user_b.route("/@me")
@login_required
def current_user():
    user_id = get_user_data(request.headers)["user_id"]

    current_user = User(user_id)

    return jsonify({
        "code": 0,
        "full_name": current_user.get_full_name(),
        "points": current_user.get_points(),
        "settings": {
            "theem": current_user.get_display_theem(),
            "font_type": current_user.get_font_type(),
            "font_size": current_user.get_font_size(),
        },
        "progress": {
            "wheel": wheel.is_done(user_id),
            "group_ids": zikr_session.get_done_groups(user_id)
        }
    }), 200


settings = Settings()


@user_b.route("/settings", methods=["POST"])
@login_required
def update_settings():
    req_data = request.get_json(force=True)

    font_type = None
    font_size = None
    display_theem = None

    if "font_type" in req_data.keys():
        font_type = req_data["font_type"]
        if not font_type in settings.get_font_type_ids():
            return jsonify({"error": "Invalid Font Type ID."}), 400

    if "font_size" in req_data.keys():
        font_size = req_data["font_size"]
        if not font_size in settings.get_font_size_ids():
            return jsonify({"error": "Invalid Font Size ID."}), 400

    if "disply_theem" in req_data.keys():
        display_theem = req_data["disply_theem"]
        if not display_theem in settings.get_display_theem_ids():
            return jsonify({"error": "Invalid Display Theem ID."}), 400

    c_user = User(get_user_data(request.headers)["user_id"])
    c_user.update_settings(font_type, font_size, display_theem)

    return jsonify({
        "code": 0,
        "success": "settings updated."
    }), 200
