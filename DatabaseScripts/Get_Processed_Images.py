#! /usr/bin/env python3
import psycopg2
import sys


def main():
    user_id = sys.argv[1]

    #Connect to database
    conn = psycopg2.connect("dbname=apps2018data user=apps2018 password=hoser23709")

    #Access the processed image rows for the given userid
    cur = conn.cursor()
    cur.execute("SELECT imagePath, resultPath FROM foodImages WHERE userid = (%s) AND isProcessed = true", (user_id,))
    print("Total Images: " + str(cur.rowcount) + "\n")

    #Access and print original and processed images
    imageRow = cur.fetchone()
    while imageRow is not None:
        originalImage = imageRow[0]
        processedImage = imageRow[1]
        
        print("Original Image: " + originalImage)
        print("Processed Image: " + processedImage + "\n")
        imageRow = cur.fetchone()

    #Commit database changes, close connection
    conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()

