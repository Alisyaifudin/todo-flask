import sys
sys.path.append("..")  # Add the parent directory to the sys.path

from db import db

def main():
    query = """CREATE TABLE `db`.`tasks` (`id` INT NOT NULL , 
    `task` VARCHAR(255) NOT NULL , 
    `completed` BOOLEAN NOT NULL DEFAULT FALSE , 
    PRIMARY KEY (`id`)) ENGINE = InnoDB;"""
    with db.cnx() as cnx:
        with cnx.cursor() as cursor:
            print("query: ", query)
            cursor.execute(query)
if __name__ == "__main__":
    main()