#!/usr/bin/env python3
"""provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017/")

    db = client.logs
    nginx = db.nginx

    print(nginx.count_documents({}), "logs")
    print("Methods:")
    print("\n\tmethod GET: ", nginx.count_documents({"method": "GET"}))
    print("\n\tmethod POST: ", nginx.count_documents({"method": "POST"}))
    print("\n\tmethod PUT: ", nginx.count_documents({"method": "PUT"}))
    print("\n\tmethod PATCH: ", nginx.count_documents({"method": "PATCH"}))
    print("\n\tmethod DELETE: ", nginx.count_documents({"method": "DELETE"}))

    print(nginx.count_documents({"path": "/status"}), "status check")
