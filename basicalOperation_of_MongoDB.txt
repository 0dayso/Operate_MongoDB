#显示存在的数据库
show dbs

#连接到某个数据库，如果不存在则创建该数据库
use person  #名为person的数据库

#显示某个数据库中所有的表
show tables

#显示某个表中的数据
db.表名.find()
#可以通过db.表名.find().pretty()打印出比较规整的数据

#获取帮助
help

#向表中插入数据
db.表名.insert({"name":"liudongqing","age":12})

#查询数据
db.表名.find({"name":"liudongqing"}) #获取name=liudongqing的所有记录

db.表名.find({"age":{$gt:20}})  #age大于20的
db.表名.find({"age":{$lt:20}})  #age小于20的

#逻辑与
db.表名.find({"name":"liudongqing","age":20})

#逻辑或
db.表名.find({$or:[{"name":"liudongqing"},{"age":12}]})

#删除
db.表名.remove({"name":"liudongqing"}) #默认删除所有
db.表名.remove({"name":"liudongqing"},{justOne:true})   #只删除一条

#remove all from collection
db.表名.remove({})

#drop a collection
db.表名.drop()
return true

#update()
#By default, the update() method updates a single document. Use the multi option to update all documents that match the criteria.

#To change a field value, MongoDB provides update operators, such as $set to modify values. Some update operators, such as $set, will create the field if the field does not exist.

use second
db.person.insert({"hobby":"basketball","name":"liudongqing"})
db.person.update({"hobby":"basketball"},{$set:{"name":"ldq"}})  #只更新一条
db.person.update({"hobby":"basketball"},{$set:{"name":"ldq"},{muti:true}})  #更新多条