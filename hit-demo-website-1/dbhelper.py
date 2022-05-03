import mysql.connector
class DB:
    def __init__(self):
        #connect to DB
        try:
            self.conn = mysql.connector.connect(host='127.0.0.1',user='root',password='',database='hit1')
        except:
            print('Database error')
        else:
            print('Connected to Database')
            # cursor
            self.mycursor = self.conn.cursor()

    def search(self,email,password):
        # search
        query = """SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(email,password)
        self.mycursor.execute(query)
        data = self.mycursor.fetchall()
        return data

    def insert(self,name,email,password,gender,city):
        query ="""
        INSERT INTO `users` (`user_id`, `name`, `email`, `password`, `gender`, `city`) VALUES
        (NULL, '{}', '{}', '{}', '{}', '{}')""".format(name,email,password,gender,city)
        try:
            self.mycursor.execute(query)
        except:
            return 0
        else:
            self.conn.commit()
            return 1