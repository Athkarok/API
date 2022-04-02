from dbConector import execute

class ZikrSession:

    def get_done_groups(self, user_id):
        sql = "SELECT DISTINCT group_id FROM zikr_sessions WHERE user_id = %s && finish_date REGEXP DATE(NOW())"
        ids = [i[0] for i in execute(sql, user_id)]
        return ids

    def add_session(self, user_id, zik_group_id):
        sql = "INSERT INTO zikr_sessions(user_id, group_id, finish_date) VALUES(%s, %s, NOW())"
        execute(sql, user_id, zik_group_id)
        self.add_session_points(user_id, zik_group_id)

    def add_session_points(self, user_id, zikr_group_id):
        user_points = execute("SELECT points FROM users WHERE id = %s", user_id)[0][0]
        s_points = execute("SELECT SUM(repeat_times) FROM zikr where group_id = %s", zikr_group_id)[0][0]
        if s_points:
            execute("UPDATE users SET points = %s WHERE id = %s", user_points + s_points, user_id)


zikr_session = ZikrSession()