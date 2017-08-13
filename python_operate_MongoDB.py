from pymongo import MongoClient

client = MongoClient()
db = client.second  #名为second的数据库
r=db.coll.insert_one({"name":"liudongqing"})    #在名为coll的collection中插入一条数据
db.coll.insert_one({"age":20})
cursor=db.coll.find()   #获取coll中的数据
cursor2=db.coll.find({"age":20})    #获取coll中field age =20的documents
db.coll.insert_one({"age":20,"name":"liudongqing"})
db.coll.insert_one({"age":10,"name":"liudongqing"})
db.coll.insert_one({"age":5,"name":"liudongqing"})
cursor3=db.coll.find({"age":{"$gt":10}})    #greater than 10
cursor4=db.coll.find({"age":{"$lt":10}})    #less than 10
print(r)
for i in cursor:
    print(type(i))  #dict
for i in cursor2:
    print(i)
for i in cursor3:
    print(i)
for i in cursor4:
    print(i)

# 逻辑与
cursor5=db.coll.find({"age":10,"name":"liudongqing"})
for i in cursor5:
    print(i)
# 逻辑或
cursor6=db.coll.find({"$or":[{"age": 10},{"age": 5}]})
for i in cursor6:
    print(i)
result=db.coll.delete_many({"age":20})  #删除所有age=20的
print(result.deleted_count)
all=db.coll.find()
for i in all:
    print(i)