# Redis简单使用

## Redis安装

压缩包解压，配置环境变量

给redis多配置几个东西（修改redis的配置文件，redis:windows-service）

1. 关闭bind

   ```
   # bind 127.0.0.1 ::1  # 注释掉它
   ```
2. 关闭保护模式 windows不用设置

   ```
   protected-mode no  # 设置为no
   ```
3. 设置密码

   ```
   requirepass 123456  # 设置密码
   ```

将redis配置到服务器中

```
# 将redis安装到windows服务
redis-server.exe --service-install redis.windows.conf --loglevel verbose
# 卸载服务
redis-server --service-uninstall
# 开启服务
redis-server --service-start
# 停止服务
redis-server --service-stop
```

使用redis-cli连接redis

```
redis-cli -h ip地址 -p 端口 --raw  # raw可以让redis显示出中文（windows无效）
auth 密码  # 如果有密码可以这样登录，没有，下一步
```

### redis常见数据类型

整个redis可以看做一个超大号的大字典，想要区分不同的系统，可以在key上做文章。redis常见的数据类型有5个。

命令规则：命令 key 参数

1. string
   字符串，redis最基础的数据类型
   常用命令

   ```
   set key value  # 添加一条数据
   get key  # 查看一条数据
   incr key  # 让该key对应的数据自增1（原子性，安全）
   incrby key count  # 让该key对应的value自增 count
   type key  #查看数据类型（set进去的东西一律全是字符串）
   ```

   例如

   ```
   set name zhangsan  # 添加数据 name = zhangsan
   get name  # 查看数据 zhangsan

   set age 10
   get age  # 10
   incr age  # 11
   get age  # 1
   incrby age 5  # 16
   get age
   ```
2. hash

   哈希，相当于字典

   常见操作

   ```
   hset key k1 v1  # 将k1, v1存储在key上
   hget key k1  # 将key上的k1提取出来
   hmset key k1 v1 k2 v2 k3 v3...  # 一次性将多个k,v存储在key
   hmget key k1 k2...  # 一次性将key中的k1, k2...提取出来
   hgetall key  # 一次性将key中所有内容全部提取
   hkeys key  # 将key中所有的k全部提取
   hvals key  # 将key中所有的v全部提取
   ```

   例如

   ```
   hmset stu id 1 name sylar age 18
   hmget stu name age  # syalr 18
   hgetall stu # id 1 name sylar age 18
   hkeys stu  # id name age
   hvals stu  # 1 syalr 18
   ```
3. list

   列表，底层是一个双向链表，可以从左边和右边进行插入，记住每次插入都要记得这货是个双向链表

   常见操作

   ```
   lpush key 数据1 数据2 数据3....  # 从左边插入数据
   rpush key 数据1 数据2 数据3....  # 从右边插入数据
   lrange key start stop  # 从start到stop提取数据

   llen key  # 返回key对应列表的长度
   lpop key  # 从左边删除一个，并返回被删除元素
   rpop key  # 从右边删除一个，并返回被删除元素
   ```

例如：

```
lpush banji yiban erban sanban siban
lrange banji 0 -1  # yiban erban sanban siban
rpush ban ban1 ban2 ban3
lrange ban 0 -1  # ban1 ban2 ban3
lpop ban  # ban1
llen key  # 2
```

4. set
   set 是无序的超大集合。无序，不重复
   常见操作

   ```
   SADD key 值  # 向集合内存入数据
   smembers key  # 查看集合内所有元素
   scard key  # 查看key中元素的个数
   sismember key val  # 查看key中是否包含val
   sunion key1 key2  # 并集
   sdiff key1 key2  # 差集合，在key1中，但不在key2中的数据
   sinter key1 key2  # 计算交集，在key1和key2中都出现了的
   spop key  # 随机从key中删除一个数据
   srandmember key count  # 随即从key中查询count个数据
   ```

例如：

```
sadd stars 柯震东 吴亦凡 张默 房祖名
sadd stars 吴亦凡  # 重复的数据是存储不进去的
smembers stars  # 柯震东 吴亦凡 张默 房祖名
sismember stars 吴亦凡  # 吴亦凡在stars里吗 1 在 0 不在

sadd my 周杰伦 吴亦凡 房祖名
sinter stars my  # 计算交集 吴亦凡 房祖名

spop my  # 随机删除一个
srandmember my 2  # 从集合中随机查看2个
```

5. zset
   有序集合，也是不可重复的，并且存储的数据也是redis最基础的string数据，但是在存储数据的同时存储了相同个score，表示分值，redis就是通过这个score作为排序的规则的
   常用操作

   ```
   zadd key s1 m1 s2 m2 ...  # 向key中存入 m1 m2 分数分别为s1 s2
   zrange key start stop [withscores]  # 查看从start 到stop中的所有数据【是否要分数】
   zrevrange key start stop  # 倒叙查看start到stop的数据
   zcard key  # 查看zset的数据个数
   zcount key min max  # 查看分数在min和max之间的数据量
   zincrby key score member  # 将key中member的分值score
   zscore key m  # 查看key中m的分值
   ```

例如：

```
zadd fam 1 sylar 2 alex 3 tory  # 添加三个数据
zrange fam 0 -1 withscores  # 正序查看
zrevrange fam 0 -1 withscores  # 倒叙查看
zincrby fam 10 alex  # 给alex加10分
zadd fam 100 alex  # 给alex修改分数为100分
zscore fam alex  # 查看alex的分数
zcard fam  # 查看fam的数据个数
```


数据保存完一定要save一下

## python搞定redis
