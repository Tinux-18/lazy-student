from pymongo import MongoClient

####### Version 1

# pprint library is used to make the output look more pretty
from pprint import pprint

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
# client = MongoClient(
#     "mongodb+srv://lazystudent:CWDiyd7KRkdzLi0h@cluster0.4jo8n.mongodb.net/?retryWrites=true&w=majority")
# db = client.admin
# print(client.server_info())

# Issue the serverStatus command and print the results

# serverStatusResult = db.command("serverStatus")
# pprint(serverStatusResult)

######## Version 2


client = MongoClient("mongodb+srv://lazystudent:CWDiyd7KRkdzLi0h@cluster0.4jo8n.mongodb.net/?retryWrites=true&w=majority")
db = client.lazystudent
print(client.server_info())