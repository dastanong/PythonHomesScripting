GET /homes
GET request to retrieve all homes

GET /create_homes
Seed all the csv data to database

---- Filter with multiple parameters *Please change the parameter value to filter -----
GET /homes?list=100
Search for home that list price is less <parameter value>

GET /homes?sell=100
Search for home that selling price is less <parameter value>

GET /homes?living=8
Search for home that at least live for how many people

GET /homes?rooms=5
Search for home that contain the total of rooms

GET /homes?beds=6
Search for home that at least has 6 beds

GET /homes?baths=3
Search for home that at least has 3 bathrooms

GET /homes?age=10
Search for home that age less than 10 years

GET /homes?arces=0.8
Search for home that unit of area at least 0.8

GET /homes?taxes=1000
Search for home that taxes is less than 1000