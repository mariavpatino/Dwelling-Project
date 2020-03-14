from flask import Flask, jsonify, render_template
from bs4 import BeautifulSoup as bs
import requests

import time
import pandas as pd
import datetime as dt
# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo



#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# @app.route("/scrape")
# def scraping():
#     # Create connection variable
#     conn = 'mongodb://localhost:27017'

#     # Pass connection to the pymongo instance.
#     client = pymongo.MongoClient(conn)

#     # Connect to a database. Will create one if not already available.
#     db = client.mission_to_mars

#     # Drops collection if available to remove duplicates
#     db.marsDictionary.drop()

#     updated_scrape = scrape()
#     db.marsDictionary.insert_one(updated_scrape)

#     now = dt.datetime.now()
#     dt_string = now.strftime("%B %d, %Y @ %H:%M:%S")
#     return render_template('scrape.html', updateTime =dt_string)

@app.route("/")
def home():
    # Create connection variable
    conn2 = 'mongodb://localhost:27017'
    city_names = []

    # Pass connection to the pymongo instance.
    client2 = pymongo.MongoClient(conn2)

    # Connect to a database. Will create one if not already available.
    db2 = client2.Dwelling_db
    print("---------------------Here------------------")
    cities = db2.zip_lat_lon.find()

    for x in cities:
        temp = {
            'city': x['City'],
            'latlong' : f"[{x['Latitude']},{x['Longitude']}"
        }
        city_names.append(temp)
    # print(rStations)
    
    
    return render_template('index.html', cityNames = city_names)


if __name__ == "__main__":
    app.run(debug=True)
