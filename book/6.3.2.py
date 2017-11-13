#!/usr/bin/env python3
# Python 3.6.2
# pip install pymongo==3.5.1 数据库驱动
'''
添加abc数据库用户权限
> use abc
> db.createUser(
   {
     user: "user_db_abc",
     pwd: "duliang",
     roles: [ "readWrite", "dbAdmin" ]
   }
)
'''
from pymongo import MongoClient
import datetime
import pprint

client = MongoClient("mongodb://user_db_abc:duliang@127.0.0.1:27017/abc")
db = client.get_database()
print(db.name)

'''
# 列出所有数据库名称 因为user_db_abc用户权限不够 先注释掉
dbs = client.database_names()
print(dbs)
'''

post = {"author": "Mike",
         "text": "My first blog post!",
         "tags": ["mongodb", "python", "pymongo"],
         "date": datetime.datetime.utcnow()}
posts = db.posts
post_id = posts.insert_one(post).inserted_id

print(posts.count())


# 列出当前数据库的所有集合
cols = db.collection_names(include_system_collections=False)
for i in cols:
    print(i)


#  查询文档
for post in posts.find():
    pprint.pprint(post)
