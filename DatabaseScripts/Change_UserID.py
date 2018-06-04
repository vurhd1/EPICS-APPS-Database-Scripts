#! /usr/bin/env python3
import psycopg2
import sys


def main():
    old_user_id = sys.argv[1]
    new_user_id = sys.argv[2]

    #Connect to database
    conn = psycopg2.connect("dbname=apps2018data user=apps2018 password=hoser23709")

    #Get the row where the userid matches the input
    cur = conn.cursor()
    cur.execute("UPDATE users SET userid = (%s) WHERE userid = (%s);", (new_user_id, old_user_id,))

    #Commit database changes, close connection
    conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()

