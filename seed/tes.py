import sys

import mysqlx
sys.path.append("..")  # Add the parent directory to the sys.path

from db import db

def main():
    query ="""CREATE TABLE `olimpusx_main`.`q` (`id` INT NOT NULL , 
    `task` VARCHAR(255) NOT NULL , 
    `completed` BOOLEAN NOT NULL DEFAULT FALSE , 
    PRIMARY KEY (`id`)) ENGINE = InnoDB;"""
    with db.cnx() as cnx:
        with cnx.cursor() as cursor:
            try:
                cursor.execute(query)
            except mysqlx.connector.Error as err:
                print("Failed creating database: {}".format(err))
                exit(1)

if __name__ == "__main__":
    main()