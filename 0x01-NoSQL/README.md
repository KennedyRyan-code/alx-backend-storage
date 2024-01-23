# 0x01. NoSQL

## Resources
*Read or watch:*

[NoSQL Databases Explained](https://riak.com/resources/nosql-databases/)
[What is NoSQL ?](https://www.youtube.com/watch?v=qUV2j3XBRHc)
[MongoDB with Python Crash Course - Tutorial for Beginners](https://www.youtube.com/watch?v=E-1xI85Zog8)
[MongoDB Tutorial 2 : Insert, Update, Remove, Query](https://www.youtube.com/watch?v=CB9G5Dvv-EE)
[Aggregation](https://www.mongodb.com/docs/manual/aggregation/)
[Introduction to MongoDB and Python](https://realpython.com/introduction-to-mongodb-and-python/)
[mongo Shell Methods](https://www.mongodb.com/docs/manual/reference/method/)
[The mongo Shell](https://www.mongodb.com/docs/manual/reference/mongo/)

**Learning Objectives**

## General
- What NoSQL means
- What is difference between SQL and NoSQL
- What is ACID
- What is a document storage
- What are NoSQL types
- What are benefits of a NoSQL database
- How to query information from a NoSQL database
- How to insert/update/delete information from a NoSQL database
- How to use MongoDB

### More Info
**Install MongoDB 4.2 in Ubuntu 18.04
Official installation guide**

*$ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org
...
$  sudo service mongod status
mongod start/running, process 3627
$ mongo --version
MongoDB shell version v4.2.8
git version: 43d25964249164d76d5e04dd6cf38f6111e21f5f
OpenSSL version: OpenSSL 1.1.1  11 Sep 2018
allocator: tcmalloc
modules: none
build environment:
    distmod: ubuntu1804
    distarch: x86_64
    target_arch: x86_64
$
$ pip3 install pymongo
$ python3
>>> import pymongo
>>> pymongo.__version__
'3.10.1'*
* Potential issue if documents creation doesn’t work or this 
  error: Data directory /data/db not found., terminating ([source](https://bryantson.medium.com/fixing-data-db-not-found-error-in-macos-x-when-starting-mongodb-d7b82abb2479) and [source](https://stackoverflow.com/questions/37702957/mongodb-data-db-not-found))

*$ sudo mkdir -p /data/db*

