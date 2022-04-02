from dbConector import execute
from datetime import datetime
import random

def get_date():
    return datetime.today().date()


class Quote:
    
    def __init__(self):
        self.date = get_date()
        self.quote_of_day = self.get_random_quote()

    def get_quote_of_day(self):
        if self.new_date():
            self.quote_of_day = self.get_random_quote()

        return self.quote_of_day

    def get_random_quote(self):
        quotes = self.get_quotes()
        if len(quotes) == 0:
            return None

        try:
            return quotes[random.randint(0, len(quotes))]
        except:
            self.get_random_quote()
            
    def new_date(self):
        now = get_date()
        if self.date != now:
            self.date = now
            return True
        return False

    def get_quotes(self):
        sql = "SELECT * FROM quotes"
        quotes = [i for i in execute(sql)]
        return quotes

    def add_quote(self, quote, author):
        sql = "INSERT INTO quotes(text, author) VALUES (%s, %s)"
        execute(sql, quote, author)
