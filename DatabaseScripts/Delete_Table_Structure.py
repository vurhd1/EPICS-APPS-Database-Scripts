#! /usr/bin/env python3
import psycopg2
import sys


def main():

    #Connect to database
    conn = psycopg2.connect("dbname=apps2018data user=apps2018 password=hoser23709")

    #Create cursor and insert values to user table.
    cur = conn.cursor()

    #Deleting foreign keys
    cur.execute("ALTER TABLE foodImages DROP CONSTRAINT IF EXISTS foodImages_fk0; \
	    ALTER TABLE ocrImages DROP CONSTRAINT IF EXISTS ocrImages_fk0; \
            ALTER TABLE barcodes DROP CONSTRAINT IF EXISTS barcodes_fk0; \
            ALTER TABLE calorieIntake DROP CONSTRAINT IF EXISTS calorieIntake_fk0;")

    #Deleteing users table
    cur.execute("DROP TABLE IF EXISTS users CASCADE;")

    # Deleteing foodImages table
    cur.execute("DROP TABLE IF EXISTS foodImages CASCADE;")

    # Deleteing ocrImages table
    cur.execute("DROP TABLE IF EXISTS ocrImages CASCADE;")

    # Deleteing barcodes table
    cur.execute("DROP TABLE IF EXISTS barcodes CASCADE;")

    # Deleteing calorieIntake table
    cur.execute("DROP TABLE IF EXISTS calorieIntake CASCADE;")

    #Commit database changes, close connection
    conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()

