import sqlite3
from sqlite3 import Error


class Connection:

    def __init__(self, db_file):
        self.db_file = db_file

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_file)
        print(f"Connected to {self.db_file}, sqlite version: {sqlite3.version}")
        return self.conn

    def __exit__(self, type, exc_value, traceback):
        self.conn.close()

    def cursor(self):
        if self.conn:
            return self.conn.cursor

class SqlService:

    def __init__(self, db_file):
        self.db_file = db_file

    def select_all(self):
        with Connection('sqlite.db') as connection:
            cur = connection.cursor()
            cur.execute('''SELECT * FROM cars;''')
            rows = cur.fetchall()
            return rows

    def add_car(self, marka, model, rocznik, kolor, moc, bezwypadkowy):
        with Connection(self.db_file) as connection:
            sql = f'''INSERT INTO cars (marka, model, rocznik, kolor, moc, bezwypadkowy)
                    VALUES('{marka}', "{model}", {rocznik}, "{kolor}", {moc}, {bezwypadkowy})'''
            cur = connection.cursor()
            cur.execute(sql)
            connection.commit()
            return cur.lastrowid

    def get_car(self, id):
        with Connection(self.db_file) as connection:
            sql = f'''SELECT * FROM cars WHERE Id = {id} '''
            cur = connection.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
            return rows[0]

    def update_car(self,id, marka, model, rocznik, kolor, moc, bezwypadkowy):
        with Connection(self.db_file) as connection:
            sql = f'''UPDATE cars SET marka = '{marka}' , model = '{model}',rocznik = '{rocznik}',kolor = '{kolor}',moc = '{moc}',bezwypadkowy='{bezwypadkowy}' WHERE Id = {id}'''
            cur = connection.cursor()
            cur.execute(sql)
            connection.commit()
            return cur.lastrowid

    def delete_car(self, id):
        with Connection(self.db_file) as connection:
            sql = f'''DELETE FROM cars WHERE Id = {id} '''
            cur = connection.cursor()
            cur.execute(sql)
            connection.commit()
            return cur.lastrowid

    def create_table(self):
        with Connection(self.db_file) as connection:
            sql_create_cars_table = """CREATE TABLE IF NOT EXISTS cars (
                                            id integer PRIMARY KEY,
                                            marka text,
                                            model text,
                                            rocznik integer,
                                            kolor text,
                                            moc integer,
                                            bezwypadkowy boolean
                                        );"""

            try:
                c = connection.cursor()
                c.execute(sql_create_cars_table)
                connection.commit()
            except:
                print("Error! cannot create the database connection.")

    def main(self):

        try:
            self.create_table()
        except Exception as e:
            print(e)

      #  try:
       #     car = self.add_car("mercedes", "klasa", 2020, "czarny", 400, True)
        #    print("Add car: ", car)
        #except:
         #   print("Can't add a car")


service = SqlService("sqlite.db")
if __name__ == '__main__':
    print(service.main())
    print(service.select_all())