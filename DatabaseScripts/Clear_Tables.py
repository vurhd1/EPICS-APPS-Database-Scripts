#! /usr/bin/env python3
import psycopg2
import sys


def main():

    #Connect to database
    conn = psycopg2.connect("dbname=apps2018data user=apps2018 password=hoser23709")

    #Create cursor and truncate (clear) all tables
    cur = conn.cursor()
    cur.execute("TRUNCATE TABLE users CASCADE")

    #Commit database changes, close connection
    conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()

