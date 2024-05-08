#!/usr/bin/env python3
"""provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


if __name__ == "__main__":
    """connects to db"""
    client = MongoClient("mongodb://localhost:27017/")

    db = client.logs
    nginx = db.nginx

    print(nginx.count_documents({}), "logs")
    print("Methods:")
    print("\tmethod GET: ", nginx.count_documents({"method": "GET"}))
    print("\tmethod POST: ", nginx.count_documents({"method": "POST"}))
    print("\tmethod PUT: ", nginx.count_documents({"method": "PUT"}))
    print("\tmethod PATCH: ", nginx.count_documents({"method": "PATCH"}))
    print("\tmethod DELETE: ", nginx.count_documents({"method": "DELETE"}))

    print(nginx.count_documents({"path": "/status"}), "status check")
