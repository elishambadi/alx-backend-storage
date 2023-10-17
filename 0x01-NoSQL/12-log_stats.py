#!/usr/bin/env python3
"""MongoDB Methods"""

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.logs
collection = db.nginx

totalLogs = collection.count_documents({})

methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
methodCounts = {m: collection.count_documents({"method": m}) for m in methods}

statusCheck = collection.count_documents({"method": "GET", "path": "/status"})

# Display the results
print(f"{totalLogs} logs")
print("Methods:")
for method in methods:
    print(f"\tmethod {method}: {methodCounts[method]}")
print(f"{statusCheck} status check")
