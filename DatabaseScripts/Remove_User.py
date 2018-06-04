#! /usr/bin/env python3
import psycopg2
import sys


def main():
    user_id = sys.argv[1]

    #Connect to database
    conn = psycopg2.connect("dbname=apps2018data user=apps2018 password=hoser23709")

    #Delete the row where the userid matches the input
    #This will automatically delete the user in all other tables
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE userid = (%s)", (user_id,))

    #Commit database changes, close connection
    conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()

