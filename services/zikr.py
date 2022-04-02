from dbConector import execute


class ZikrAdmin:

    def add_zikr(self, group_id, text, r_times, dalel, dalel_link, weak):
        sql = "INSERT INTO zikr(group_id, zikr_text, repeat_times, dalel, dalel_link, weak) VALUES(%s, %s, %s, %s, %s, %s)"
        execute(sql, group_id, text, r_times, dalel, dalel_link, weak)

    def remove_zikr(self, id):
        sql = "DELETE FROM zikr WHERE id = %s"
        execute(sql, id)

    def get_zikrs_by_group(self, group_id):
        sql = "SELECT * FROM zikr WHERE group_id = %s"
        data = execute(sql, group_id)
        return data

    def get_group_Ids(self):
        sql = "SELECT id FROM zikr_groups ORDER BY id"
        ids = [i[0] for i in execute(sql)]
        return ids


class Zikr:

    def __init__(self, zikr_id):
        self.id = zikr_id

    def update(self, group_id, text, r_times, dalel, dalel_link, weak):
        if not group_id == None:
            execute("UPDATE zikr SET group_id = %s WHERE id = %s", group_id, self.id)
        if not text == None:
            execute("UPDATE zikr SET zikr_text = %s WHERE id = %s", text, self.id)
        if not r_times == None:
            execute("UPDATE zikr SET repeat_times = %s WHERE id = %s", r_times, self.id)
        if not dalel == None:
            execute("UPDATE zikr SET dalel = %s WHERE id = %s", dalel, self.id)
        if not dalel_link == None:
            execute("UPDATE zikr SET dalel_link = %s WHERE id = %s", dalel_link, self.id)
        if not weak == None:
            execute("UPDATE zikr SET weak = %s WHERE id = %s", weak, self.id)
        