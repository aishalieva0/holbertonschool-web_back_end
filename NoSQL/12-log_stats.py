#!/usr/bin/env python3
"""provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


if __name__ == "__main__":
    """connects to db"""
    client = MongoClient("mongodb://localhost:27017/")

    db = client.logs
    nginx = db.nginx
    logs = nginx.count_documents({})
    print(f"{logs} logs")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")

    for method in methods:
        count = nginx.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_count = nginx.count_documents({"method": "GET", "path": "/status"})

    print(f"{status_count} status check")
