import mysql.connector as sql


class Dbconnection:
    def open(self):
        try: # connecting with database
            # print("--Database Is Connected:--")
            self.conn = sql.connect(host='localhost', database='SISDB', user='root', password='Harini2002')
            if self.conn.is_connected():
                print('Database connected..')
            else:
                print('Not Connected with Database')
            self.stmt = self.conn.cursor()
        except Exception as e:
            print(str(e) + "---Database Not Is Connected:--")

    def close(self):
        self.conn.close()
        print('Connection Close:')


obj = Dbconnection()
obj.open()