import sys
sys.path.append("..") 

from db import db

def main():
    query = """SELECT * FROM `db`.`tasks`;"""
    with db.cnx() as cnx:
        with cnx.cursor() as cursor:
            print("query: ", query)
            cursor.execute(query)
            for row in cursor:
                print(row)
if __name__ == "__main__":
    main()

