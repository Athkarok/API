from dbConector import execute

class FormAdmin:

    def submit(self, form_name, user_id, name, role, message):
        sql = "INSERT INTO forms(form_name, user_id, name, role, message) VALUES(%s, %s, %s, %s, %s)"
        execute(sql, form_name, user_id, name, role, message)