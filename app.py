from flask import Flask, jsonify, request
from flask_migrate import Migrate
from extensions import db
from models import Home
import csv
from schemas import HomeSchema

app = Flask(__name__)
url = "postgres://postgres:postgres@localhost:5432/homes_db"
app.config["SQLALCHEMY_DATABASE_URI"] = url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
def home():
    homes = Home.query.all()

    json_homes = HomeSchema(many=True).dumps(homes)

    return jsonify(json_homes)

@app.route("/create_homes")
def addHome():
    with open("homes.csv", mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        homesList = list()

        for row in csv_reader:
            newHome = Home()
            newHome.sell_price = row["Sell"]
            newHome.list_price = row[" \"List\""]
            newHome.living = row[" \"Living\""]
            newHome.rooms = row[" \"Rooms\""]
            newHome.beds = row[" \"Beds\""]
            newHome.bathrooms = row[" \"Baths\""]
            newHome.age = row[" \"Age\""]
            newHome.arces = row[" \"Acres\""]
            newHome.taxes = row[" \"Taxes\""]
            homesList.append(newHome)

        for home in homesList:
            db.session.add(home)
            
        if len(homesList) > 0:
            db.session.commit()

        return "Create homes successfully"

@app.route("/homes")
def searchHome():
    list_price = request.args.get("list")
    sell_price = request.args.get("sell")
    living = request.args.get("living")
    rooms_num = request.args.get("rooms")
    beds = request.args.get("beds")
    baths = request.args.get("baths")
    age = request.args.get("age")
    arces = request.args.get("arces")
    taxes = request.args.get("taxes")

    query = Home.query

    if list_price is not None :
        query = query.filter(Home.list_price < list_price)
    if sell_price is not None:
        query = query.filter(Home.sell_price < sell_price)
    if living is not None:
        query = query.filter(Home.living <= living)
    if rooms_num is not None:
        query = query.filter(Home.rooms == rooms_num)
    if beds is not None:
        query = query.filter(Home.beds <= beds)
    if baths is not None:
        query = query.filter(Home.baths <= baths)
    if age is not None:
        query = query.filter(Home.age < age)
    if arces is not None:
        query = query.filter(Home.arces <= arces)
    if taxes is not None:
        query = query.filter(Home.taxes < taxes)

    json_homes = HomeSchema(many=True).dumps(query)
    return jsonify(json_homes)

app.run(debug=True)