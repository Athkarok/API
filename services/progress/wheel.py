from dbConector import execute

class Wheel:

    def set_done(self, user_id):
        sql = "INSERT INTO wheel_sessions(user_id, finish_date) VALUES(%s, NOW())"
        execute(sql, user_id)

    def is_done(self, user_id):
        sql = "SELECT DISTINCT * FROM wheel_sessions WHERE user_id = %s && finish_date REGEXP DATE(NOW())"
        sessions = execute(sql, user_id)
        return True if len(sessions) > 0 else False

wheel = Wheel()