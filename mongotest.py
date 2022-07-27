import pymongo

client = pymongo.MongoClient("mongodb+srv://vishal: password@cluster0.1uqi6.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    "name":"vishal",
    "email" : "vishal@gmail.com",
    "surname" : "kumar"
}
d = {
    "name":"vishal",
    "email" : "vishal@gmail.com",
    "surname" : "kumar"
}
d = {
    "name":"vishal",
    "email" : "vishal@gmail.com",
    "surname" : "kumar"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )

