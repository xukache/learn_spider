# MongoDB数据存储

MongoDB, redis是一个非关系型数据库（NoSQL），非常适合超大数据集的存储，通常爬虫工程师使用MogoDB作为数据库

## MongoDB与安装

官网下载：https://www.mongodb.com/try/download/community

## MongoDB的简单使用

简单介绍一下mongoDB中一些操作（了解）

```mongodb
db：当前正在使用的数据库
show dbs：显示所有数据库
show databases：显示所有数据库
use xxxx：调整数据库
db.dropDatabase()：删除数据库
show collections：显示当前数据库中所有的集合（表）
db.collection_name.insert({})
db.createCollection(name, {options0}) 创建集合 capped：是否卷动，size：大小
db.collection_name.drop() 删除集合
db.collection_name.insert() 像集合中添加数据（如果该集合不存在，自动创建）
db.collection_name.isCapped() 判断是否有容量上限（判断该集合是否是固定容量的集合）
```

## MongoDB的增删改查

### 1. mongodb中常见的数据类型

```python
Object ID：主键ID
String：字符串
Boolean：布尔值
Integer：数字
Doube：小数
Arrays：数组
Object：文档（关联其他对象） {sname：李嘉诚, sage:18, class:{cccc}}
Null：空值
Timestamp：时间戳
Date：时间日期
```

### 2. mongodb添加数据

```mongodb
db.collection_name.insert({name:'kachex', age:18}) // 新版本不支持
db.collection_name.insertOne({name:'kachex', age:18})
db.collection_name.insertMany([{name:'kachex', age:18}, {name:'kachex', age:19}])
```

如果集合不存在，则会自动创建集合

### 3. mongodb修改数据

#### 3.1 update更新

```mongodb
db.collection_name.update({name:'xxx'}, {$set:{title:'ddd', age:18}, {multi:true, upsert:true})
db.collection_name.update({name:'kkk'}, {title:'eee'})
```

$set和没有$set的区别：

$set只会修改当前给出的字段，其他内容保留

没有$set只会保留当前给出字段，其他内容删除

multi：如果为True，必须用$set，否则会报错

#### 3.2 保存（save，了解）

```mongodb
db.collection_name.save({待保存数据})
```

注意，如果save的内容中的_id如果存在就更新，如果不存在就添加

```mongodb
db.collection_name.save({_id:'60ffffffffffefe', name:'xxx', age:20})
```

### 4. mongodb删除数据

#### 4.1 remove()

```mongodb
db.collection_name.remove({条件}, {justOne:true|false})
```

### 5. mongodb查询数据

准备数据

```mongodb
db.stu.insert([
    {name:'xxx', age:18},
    {name:'kkk', age:19},
    {name:'yyy', age:20},
    {name:'zzz', age:21},
    {name:'aaa', age:22},
    {name:'bbb', age:23},
    {name:'ccc', age:24}
])
```

#### 5.1 普通查询

```mongodb
db.stu.find({条件})  查询所有
db.stu.findOne({条件})  查询一个
db.stu.find().pretty()  将查询出来的结果进行格式化（好看一些）
```

#### 5.2 比较运算

```mongodb
等于：默认是等于判断，$eq
小于：$lt (less than)
小于等于：$lte (less than euqal)
大于：$gt (greater than)
大于等于：$gte
不等于：$ne
```

```mongodb
db.stu.find({age:28})  查询年龄是28岁的学生信息
db.stu.find({age:{$eq:28}})  查询年龄是28岁的学生信息
sb.stu.find({age:{$gt:30}})  查询年龄大于30岁的学生
db.stu.find({age:{$lt:30}})  查询年龄小于30岁的学生
db.stu.find({age:{$gte:38}})  查询年龄大于等于30岁的学生
db.stu.find({age:{$lte:38}})  查询年龄小于等于30岁的学生
sb.stu.find({age:{$ne:38}})  查询年龄不等于38岁的学生
```

#### 5.3 逻辑运算符

1. and
   `$and:[条件1，条件2，条件3....]`

   ```mongodb
   查询年龄等于33，并且，名字是“大老王”的学生信息
   d b.stu.find({$and:[age:{$eq:33}}, {name:'大老王'}])
   ```
2. or
   `$or:[条件1，条件2，条件3]`

   ```mongodb
   查询名字叫“李嘉诚”的，或者，年龄超过100岁的人
   ```
3. or
   `$nor:[条件1，条件2，条件3]`

   ```mongodb
   查询年龄不小于338岁的人，名字还不能是朱元璋
   db.stu.find({$nor:[{age:{$lt:38}}, {name:"朱元璋"}]})
   ```

#### 5.4 范围运算

使用\$in，$nin判断数据是否在某个数组内

```mongodb
db.stu.find({age:{$in:[28, 38]}})  年龄是28或38的人
```

#### 5.5 正则表达式

使用$regex进行正则表达式匹配

```mongodb
db.stu.find({adress:{$regex:'^北京'}})  查询地址是北京的人的信息
db.stu.find({adress:/^北京/})  效果一样
```

#### 5.6 投影

投影可以控制最终查询的结果（字段筛选）

```mongodb
db.stu.find({}, {字段:0, 字段:0})
```

需要看的字段给1就可以了

注意：除了_id外，0，1不能共存

#### 5.7 排序

`sort({字段:1,字段:-1})`

1表示升序

-1表示降序

```mongodb
对查询结果排序，先按照age升序排列，相同项再按照score降序排列
db.stu.find().sort({age:1, score:-1})
```

#### 5.8 统计数量

count(条件) 查询数量

```mongodb
db.stu.count({age:33})
```

###
