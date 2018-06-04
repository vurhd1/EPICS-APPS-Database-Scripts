#! /usr/bin/env python3
import psycopg2
import sys


def main():
    user = sys.argv[1]
    password = sys.argv[2]
    salt = sys.argv[3]
    creationDate = sys.argv[4]

    #Connect to database
    conn = psycopg2.connect("dbname=apps2018data user=apps2018 password=hoser23709")

    #Create cursor and insert values to user table.
    cur = conn.cursor()
    cur.execute("INSERT INTO users(userID, password, salt, creationDate) VALUES (%s, %s, %s, %s);", (user, password, salt, creationDate))

    #Commit database changes, close connection
    conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()

