from flask import Flask
from query_mongo import get_progress

# Building Flask

app = Flask(__name__)

minutes = get_progress("Samuel Cochran", "62b707d4e700f67ac1e2eff7")

for x in minutes:
    print(x)