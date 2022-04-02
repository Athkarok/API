from dbConector import execute

from services.zikr import ZikrAdmin
from helpers.validate import is_email

from werkzeug.security import generate_password_hash, check_password_hash

zikr_admin = ZikrAdmin()

class UserAdmin:

    # Adding user
    def add_user(self, email, username, password, first_name, last_name, phone_number):
        """
        0 : success user adedd.
        1 : error user already exists with same email.
        2 : error username is taken.
        3 : error phone number is used.
        """
        
        # Check if user is valid to register
        if self.user_exists(email):
            return 1
        if self.user_name_used(username):
            return 2
        if self.phone_num_used(phone_number):
            return 3

        # Modify NULL values
        last_name = "NULL" if last_name == "" else last_name
        phone_number = "NULL" if phone_number == "" else phone_number

        # Hash password
        password = generate_password_hash(password)

        # Insert new user
        sql = "INSERT INTO users (email, username, password, first_name, last_name, phone_number) VALUES (%s, %s, %s, %s, %s, %s)"
        execute(sql, email, username, password, first_name, last_name, phone_number)


        # Set default settings for new user
        self.set_defaults(self.get_id(email))
    
        return 0

    def set_defaults(self, id):
        self.set_default_settings(id)

    def set_default_settings(self, id):
        font_type = 1  # 1 = Questv1 *default
        font_size = 2  # 2 = medium size *default
        display_theem = 1  # 1 = auto *default
        sql = "INSERT INTO user_settings(user_id, font_type, font_size, display_theem) VALUES(%s, %s, %s, %s)"
        execute(sql, id, font_type, font_size, display_theem)

    # Get ID Methods
    def get_id(self, identity):
        # useing thier email
        if is_email(identity):
            sql = "SELECT id FROM users WHERE email = %s "
        else:
            sql = "SELECT id FROM users WHERE username = %s "
        id = execute(sql, identity)[0][0]
        return id

    def get_role(self, id):
        sql = "SELECT role FROM users WHERE id = %s"
        return execute(sql, id)[0][0]

    # Existing
    def user_exists(self, identity):

        if is_email(identity):
            sql = "SELECT COUNT(1) FROM users WHERE email = %s"
        else:
            sql = "SELECT COUNT(1) FROM users WHERE username = %s"

        exists = execute(sql, identity)[0][0]
        return True if exists == 1 else False

    def user_name_used(self, username):
        sql = "SELECT COUNT(1) FROM users WHERE username = %s"
        used = execute(sql, username)[0][0]
        return True if used == 1 else False

    def phone_num_used(self, phone_number):
        sql = "SELECT COUNT(1) FROM users WHERE phone_number = %s"
        used = execute(sql, phone_number)[0][0]
        return True if used == 1 else False

    # Matching
    def match_credentials(self, identity, password):
        """
        0 : success user credentials matched.
        1 : error username or password is wrong.
        """

        if is_email(identity):
            sql = "SELECT password FROM users WHERE email = %s"
        else:
            sql = "SELECT password FROM users WHERE username = %s"

        
        hash = execute(sql, identity)
        if len(hash) != 1:
            return 1 

        if check_password_hash(hash[0][0], password):
            return 0

        return 1

class GoogleUserAdmin(UserAdmin):

    # sub is unique Google userid
    def sign_user(self, email, sub, first_name, last_name):
        """
        0 : success user adedd.
        1 : user already exists with same sub.
        2 : user already exists with same email - means they has a normal account.
        """
        if self.user_exists(sub):
            return 1
        
        if self.user_exists(email):
            return 2

        # Insert new user
        sql = "INSERT INTO users (email, username, password, first_name, last_name) VALUES (%s, %s, %s, %s, %s)"
        execute(sql, email, sub, sub, first_name, last_name)
        
        # Set default settings for new user
        self.set_defaults(self.get_id(email))
        return 0
    