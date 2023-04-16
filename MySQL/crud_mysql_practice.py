import mysql.connector
from mysql.connector import errorcode
import os

class Database():
    def __init__(self):
        self.connect()
        self.create_db()
        while True:
            print("[1] Add New Record")
            print("[2] Edit Record")
            print("[3] Delete Record")
            print("[4] Search Record")
            print("[5] Display All Record")
            choice = input("Enter your choice : ")

            if choice == "1":
                os.system('cls')
                code = input("Enter prduct code: ")
                name = input("Enter product name: ")
                price = float(input("Enter product price: "))

                self.add(code, name, price)
            elif choice == "2":
                os.system('cls')
                code = input("Enter prduct code: ")
                name = input("Enter product name: ")
                price = float(input("Enter product price: "))

                self.update(code, name, price)
            elif choice == "3":
                os.system('cls')
                code = input("Enter prduct code: ")

                self.delete(code)
            elif choice == "4":
                os.system('cls')
                code = input("Enter prduct code: ")

                self.search(code)
            elif choice == "5":
                os.system('cls')
                self.view()

            x = input("Return to main menu [y/n]? ")
            if x == 'y':
                os.system('cls')
                continue
            else:
                break

            exit(0)

    def connect(self):
        try:
            cnx = mysql.connector.connect(
                host="localhost",
                user="root",
                password="password"
            )
            return cnx
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                return False
            else:
                return False
            
    def create_db(self):
        cnx = self.connect()
        cursor = cnx.cursor()

        cursor.execute("CREATE DATABASE IF NOT EXISTS Sales")
        cursor.execute("USE Sales")
        query = """
        CREATE TABLE IF NOT EXISTS tbl_val (
            code varchar(255),
            product varchar(255),
            price float
        )
        """
        cursor.execute(query)

        cursor.close()
        cnx.close()

    def add(self, code, product, price):
        cnx = self.connect()
        cursor = cnx.cursor()

        cursor.execute("USE Sales")
        query = "INSERT INTO tbl_val(code, product, price) VALUES('%s', '%s', '%f')" % (code, product, price)

        cursor.execute(query)
        cnx.commit()

        cursor.close()
        cnx.close()

    def update(self, code, product, price):
        cnx = self.connect()
        cursor = cnx.cursor()

        cursor.execute("USE Sales")
        query = "UPDATE tbl_val SET product = '%s', price = '%f' WHERE code = '%s'" % (product, price, code)

        cursor.execute(query)
        cnx.commit()

        cursor.close()
        cnx.close()

    def delete(self, code):
        cnx = self.connect()
        cursor = cnx.cursor()

        cursor.execute("USE Sales")
        query = "DELETE FROM tbl_val WHERE code = %s"
        val = (code,)

        cursor.execute(query, val)
        cnx.commit()

        cursor.close()
        cnx.close()

    def view(self):
        cnx = self.connect()
        cursor = cnx.cursor()

        cursor.execute("USE Sales")
        cursor.execute("SELECT * FROM tbl_val")
        res = cursor.fetchall()
        for row in res:
            print(f"code = {row[0]}")
            print(f"product = {row[1]}")
            print(f"price = {row[2]}")
            print()

        cursor.close()
        cnx.close()
    
    def search(self, code):
        cnx = self.connect()
        cursor = cnx.cursor()

        cursor.execute("USE Sales")
        cursor.execute("SELECT * FROM tbl_val WHERE code = '%s'" % code)

        res = cursor.fetchall()
        for row in res:
            print(f"code = {row[0]}")
            print(f"product = {row[1]}")
            print(f"price = {row[2]}")
            print()

        cursor.close()
        cnx.close()

if __name__=="__main__":
    db = Database()
    