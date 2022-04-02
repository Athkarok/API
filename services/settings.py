from dbConector import execute

class Settings:

    def get_font_size_ids(self):
        ids = [int(i[0]) for i in execute("SELECT id from font_sizes")]
        return ids

    def get_font_type_ids(self):
        ids = [int(i[0]) for i in execute("SELECT id from font_types")]
        return ids
    
    def get_display_theem_ids(self):
        ids = [int(i[0]) for i in execute("SELECT id from display_theems")]
        return ids
