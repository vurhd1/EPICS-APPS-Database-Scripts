#! /usr/bin/env python3
import psycopg2
import sys


def main():
    user_id = sys.argv[1]

    #Connect to database
    conn = psycopg2.connect("dbname=apps2018data user=apps2018 password=hoser23709")

    #Get the row where the userid matches the input
    cur = conn.cursor()
    cur.execute("SELECT gender FROM users WHERE userid = (%s)", (user_id,))

    #Print the user gender
    userGender = cur.fetchone()[0]
    #userGender = user_id = " : " + userGender
    print(userGender)

    #Commit database changes, close connection
    conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()

