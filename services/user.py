from dbConector import execute


class UserSettings:
    """
    UserSettings: 
    - retrieve user settings
    - update user settings
    """
    
    def get_user_options(self, id):
        sql = """SELECT font_type, font_size, display_theem FROM users u
                JOIN user_settings us ON us.user_id = u.id
                WHERE u.id = %s """
        data = execute(sql, id)[0]
        self.font_type = data[0]
        self.font_size = data[1]
        self.display_theem = data[2]

    # user options
    def get_display_theem(self):
        return self.display_theem

    def get_font_size(self):
        return self.font_size

    def get_font_type(self):
        return self.font_type

    # update settings
    def update_settings(self, id, font_type, font_size, display_theem):
        if font_type != None:
            sql = "UPDATE user_settings SET font_type = %s WHERE user_id = %s"
            execute(sql, font_type, id)
        
        if font_size != None:
            sql = "UPDATE user_settings SET font_size = %s WHERE user_id = %s"
            execute(sql, font_size, id)

        if display_theem != None:
            sql = "UPDATE user_settings SET display_theem = %s WHERE user_id = %s"
            execute(sql, display_theem, id)

class UserData:
    """
    UserData: 
    - retrieve user data
    """

    def get_user_data(self, id):
        sql = "SELECT email, username, first_name, last_name, phone_number, points FROM users WHERE id = %s "
        
        data = execute(sql, id)[0]

        self.email = data[0]
        self.username = data[1]
        self.first_name = data[2]
        self.last_name = data[3]
        self.phone_number = data[4]
        self.points = data[5]

    # user data
    def get_email(self):
        return self.email

    def get_user_name(self):
        return self.username

    def get_full_name(self):
        last_name = ""
        if self.last_name != None:
            last_name = " " + self.last_name
        return self.first_name + last_name

    def get_phone_number(self):
        return self.phone_number

    def get_points(self):
        return self.points

class User(UserData, UserSettings):
    """
    User: 
    - retrieve user data and settings
    - update user settings
    """
    
    def __init__(self, id):
        self.id = str(id)
        self.get_user_data(id)
        self.get_user_options(id)

    def update_settings(self, font_type, font_size, display_theem):
        super().update_settings(self.id, font_type, font_size, display_theem)


