#! /usr/bin/env python3
import psycopg2
import sys

def main():

    #Connect to database
    conn = psycopg2.connect("dbname=apps2018data user=apps2018 password=hoser23709")

    #Create cursor and insert values to user table.
    cur = conn.cursor()

    #User table
    #Primary key: userID
    cur.execute("CREATE TABLE users( \
        userID int, \
        password varchar NOT NULL, \
        salt varchar NOT NULL, \
	    dob date NOT NULL, \
	    gender varchar NOT NULL, \
        creationDateServer timestamp with time zone DEFAULT CURRENT_TIMESTAMP, \
        CONSTRAINT users_pk PRIMARY KEY (userID) \
        );")

    #foodImages table
    #Primary Key: submissionID
    #Foreign Key: userID
    cur.execute("CREATE TABLE foodImages( \
        submissionID uuid, \
        userID int NOT NULL, \
        isProcessed bool NOT NULL, \
        imagePath varchar NOT NULL, \
        imageType varchar NOT NULL, \
        latitude real NOT NULL, \
        longitude real NOT NULL, \
        captureDateClient timestamp with time zone NOT NULL, \
        resultPath varchar, \
        classifier varchar, \
        accuracy real, \
        creationDateServer timestamp with time zone DEFAULT CURRENT_TIMESTAMP, \
        CONSTRAINT foodImages_pk PRIMARY KEY (submissionID) \
        );")

    #ocrImages table
    #Primary Key: submissionID
    #Foreign Key: userID
    cur.execute("CREATE TABLE ocrImages( \
        submissionID uuid, \
        userID int NOT NULL, \
        isProcessed bool NOT NULL, \
        imagePath varchar NOT NULL, \
        imageType varchar NOT NULL, \
        latitude real NOT NULL, \
        longitude real NOT NULL, \
        captureDateClient timestamp with time zone NOT NULL, \
        resultPath varchar, \
        creationDateServer timestamp with time zone DEFAULT CURRENT_TIMESTAMP, \
        CONSTRAINT ocrImages_pk PRIMARY KEY (submissionID) \
        );")

    #barcodes table
    #Primary Key: submissionID
    #Foreign Key: userID
    cur.execute("CREATE TABLE barcodes( \
        submissionID uuid, \
        userID int NOT NULL, \
        barcode int NOT NULL, \
        latitude real NOT NULL, \
        longitude real NOT NULL, \
        angle real, \
        captureDateClient timestamp with time zone NOT NULL, \
        creationDateServer timestamp with time zone DEFAULT CURRENT_TIMESTAMP, \
        CONSTRAINT barcodes_pk PRIMARY KEY (submissionID) \
        );")

    #calorieIntake table
    #Primary Key: submissionID
    #Foreign Key: userID
    cur.execute("CREATE TABLE calorieIntake( \
        userID int, \
        submissionDate date, \
        calories int NOT NULL, \
        TEE real NOT NULL, \
        steps int NOT NULL, \
        weight real NOT NULL, \
        foodCalorieIntake int NOT NULL, \
        captureDateClient timestamp with time zone NOT NULL, \
        creationDateServer timestamp with time zone DEFAULT CURRENT_TIMESTAMP, \
        CONSTRAINT calorieIntake_pk PRIMARY KEY (userID, submissionDate) \
        );")

    #Inserting foreign keys
    cur.execute("ALTER TABLE foodImages ADD CONSTRAINT foodImages_fk0 FOREIGN KEY(userID) REFERENCES users(userID) ON DELETE CASCADE; \
    	ALTER TABLE ocrImages ADD CONSTRAINT ocrImages_fk0 FOREIGN KEY(userID) REFERENCES users(userID) ON UPDATE CASCADE ON DELETE CASCADE; \
        ALTER TABLE barcodes ADD CONSTRAINT barcodes_fk0 FOREIGN KEY(userID) REFERENCES users(userID) ON UPDATE CASCADE ON DELETE CASCADE; \
        ALTER TABLE calorieIntake ADD CONSTRAINT calorieintake_fk0 FOREIGN KEY(userID) REFERENCES users(userID) ON UPDATE CASCADE ON DELETE CASCADE")

    #Commit database changes, close connection
    conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()

