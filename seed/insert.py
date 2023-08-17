import sys
sys.path.append("..") 

from db import db

def main():
    query = """INSERT INTO `tasks` (`id`, `task`, `completed`) VALUES 
            ('0', 'Buy milk', '0'), 
            ('1', 'Buy eggs', '0'), 
            ('2', 'Exercises', '1')"""
    with db.cnx() as cnx:
        with cnx.cursor() as cursor:
            print("query: ", query)
            cursor.execute(query)
        cnx.commit()
if __name__ == "__main__":
    main()

