#MySQL-Day02笔记
##1、名词介绍
	1、DB(Database)
		DB就是数据库，是存储数据的仓库
	2、DBMS(Database Management System)
		数据库管理系统
		管理数据库的软件，MySQL、Oracle ......
	3、DBS(Database System)
		数据库系统
		DBS = DB(存储) + DBMS(数据库软件) + 数据库应用(财务管理系统,人事管理系统) + 用户
##2、where条件子句(配合查询、修改、删除操作)
	1、语法格式
		select * from 表名 where 条件;
##3、表记录管理(删除、更改)
###	1、删除表记录
		1、delete from 表名 where 条件;
		2、注意
			delete语句后如果不加where条件子句会将表中所有记录全部删除
###	2、更新表记录
		1、update 表名 set 字段名=值1,... where 条件;
		2、注意
			update语句后如果不加where条件子句会将表中所有该字段的值更改
###	3、练习
		1、创建库SANGUO
			create database SANGUO;
		2、在SANGUO库中创建一张表sanguo,指定字符集utf8,字段如下：
			id name gongji fangyu sex country 数据类型及宽度自己定义
			create table sanguo(
			id int,
			name char(15),
			sex enum("男","女"),
			country char(10)
			)default charset=utf8;
		3、在sanguo表中插入记录
			1 曹操   男  魏国
			2 小乔   女  吴国
			3 诸葛亮 男  蜀国
			4 貂蝉   女  东汉
			5 赵子龙 男  蜀国
			6 魏延   男  蜀国
			insert into sanguo values
			(1,"曹操","男","魏国"),
			(2,"小乔","女","吴国"),
			(3,"诸葛亮","男","蜀国"),
			(4,"貂蝉","女","东汉"),
			(5,"赵子龙","男","蜀国"),
			(6,"魏延","男","蜀国");
		4、查找所有蜀国人的信息(select后加where条件)
			select * from sanguo where country="蜀国";
		5、查找一下女人的信息,只显示姓名和性别
			select name,sex from sanguo where sex="女";
		6、把曹操的国籍改为蜀国
			update sanguo set country="蜀国" where name="曹操";
		7、把魏延的性别改为 女，国籍改为 泰国
			update sanguo set sex="女",country="泰国" where name="魏延";
		8、把id为2的记录的名字改为司马懿，性别男，国家改为魏国
			update sanguo set name="司马懿",sex="男",country="魏国" where id=2;
		9、删除所有泰国人
			delete from sanguo where country="泰国";
		10、删除所有英雄记录
			delete from sanguo;
##4、运算符操作(配合查询、修改、删除)
###	1、数值比较&字符比较
		1、数值比较运算符：=、!=、>、>=、<、<=
		2、字符比较运算符：=、!=
		3、语法
			查：select * from 表名 where 字段名 运算符 数字/字符;
			改：update 表名 set 字段名=值,... where 运算符/字符;
			删：delete from 表名 where 字段名 运算符 数字/字符;
		4、练习
			1、找出攻击力高于150的英雄的名字和攻击力值
				select name,gongji from sanguo where gongji > 150;
			2、查找蜀国的英雄的信息
				select * from sanguo where country="蜀国";
			3、将赵云的攻击力改为 666 ，防御改为88
				update sanguo set gongji=666,fangyu=88 where name = "赵云";
			4、在表中插入一条记录，魏延
				insert into sanguo values(10,"魏延",101,1,"蜀国");
			5、删除表中名字为 魏延 的记录
				delete from sanguo where name = "魏延";
###	2、逻辑比较
		1、运算符：and(多个条件同时满足)  or(多个条件有一个条件满足就可以)
		2、练习
			1、找出攻击值大于200的蜀国英雄的名字及攻击值
				select name,gongji from sanguo where gongji > 200 and country="蜀国";
			2、将吴国英雄中攻击值为110的英雄的攻击值设置为100，防御值设置为60
				update sanguo set gongji=100,fangyu=60 where country="吴国" and gongji=110;
			3、查找蜀国和魏国的英雄
				select * from sanguo where country="蜀国" or country="魏国";	
###	3、范围内比较
		1、运算符：between and 、in 、not in
		2、语法
			字段名 between 值1 and 值2
			字段名 in (值1,值2,... ...)
			字段名 not in (值1,值2，... ...)
		3、示例
			1、查找攻击值在100-200之间的蜀国英雄信息
				select * from sanguo where gongji between 100 and 200 and country="蜀国";
			2、查找id在1,3,5,7中的英雄的id和姓名
				select id,name from sanguo where id in (1,3,5,7);
			3、找到蜀国和吴国以外的国家的女英雄
				select * from sanguo where country not in ("蜀国","吴国") and sex="F";
			4、找到编号为1或者3或者5的蜀国英雄和貂蝉的编号、姓名和国家
				select id,name from sanguo where id in (1,3,5) and country="蜀国" or name="貂蝉";
### 4、匹配空 非空
		1、空 ：is null
		2、非空 ：is not null
		3、练习
			1、查找姓名为NULL的蜀国女英雄信息
				select * from sanguo where name is null and country="蜀国" and sex="F";
			2、查找姓名为""的英雄的id、姓名和国家
				select id,name,country from sanguo where name="";
			2、注意
				1、null : 空值，必须用is 或者 is not去操作
				2、""   : 空字符串，用 = 或者 != 去操作
		练习：
			1、查找id在3,5,7中，并且攻击力大于150的 蜀国的英雄的记录
			select * from sanguo where id in (3,5,7) and gongji > 150;
			2、查找国家不是蜀国和吴国，或者防御力大于60的英雄的名字 防御力 和 国家
			select name,fangyu,country from sanguo where country not in("蜀国","吴国") or fangyu>60;
			3、将国家为吴国，并且攻击力在1-100之间的防御力改为88
			update sanguo set fangyu=88 where country="吴国" and gongji between 1 and 100;
			4、在表中插入一条记录，id为99，名字为黄月英，其他信息自己定
			insert into sanguo values(99,"黄月英",200,90,"蜀国");
			5、删除表中id为99，并且名字为黄月英的记录
			delete from sanguo where id = 99;
###	5、模糊比较
		1、语法
			字段名 like 表达式
		2、表达式
			1、_ : 匹配单个字符
			2、% : 匹配0到多个字符
		示例：
			1、select id,name from sanguo where name like "_%_"; # 名字至少有两个字符的
			2、select id,name from sanguo where name like "%"; # 匹配所有的记录
			3、select id,name from sanguo where name like "___"; # 匹配名字为三个字的记录
			4、select id,name from sanguo where name like "赵%"; # 匹配所有姓赵的记录
##5、SQL查询
###	1、总结(执行顺序)
		0、	select...聚合函数 from ...
		1、	where...
		2、	group by ...
		4、	having ...
		5、	order by ...
		6、	limit ...;
###	2、order by 
		1、作用：给查询的结果进行排序
		2、语法格式：order by 字段名 排序方式;
		2、排序方式
			1、ASC(默认) ：升序
			2、DESC ：降序
		3、练习
			1、将英雄按防御值从低到高排序
				select * from sanguo order by gongji asc;
			2、将蜀国英雄按攻击值从高到低排序
				select * from sanguo where country = "蜀国" order by gongji desc;
			3、将魏蜀两国的男英雄中名字为三个字的英雄按防御值升序排列
				select * from sanguo where country in ("蜀国","魏国") and sex="M" (and name like "___") order by fangyu asc;
###	3、limit(永远放在SQL语句的最后写)
		1、作用 ：限制显示查询记录的记录个数
		2、用法
			1、limit n -->显示几条记录
			2、limit m,n 
				m - > 从第几条记录开始显示，n表示显示几条
				## m的值是从0开始计算的，3则表示第四条记录
			3、练习
				1、查找攻击值前三名且名字不为空值的蜀国的英雄的姓名、攻击值及国家
					select name,gongji,country from sanguo where country="蜀国" and (name is not null) order by gongji desc limit 3;
				2、查找防御值倒数第二名至倒数第四名的蜀国英雄的记录
					select * from sanguo where country="蜀国" order by fangyu limit 1,3;
###	4、聚合函数
		1、分类
			1、avg(字段名) : 求字段的平均值
			2、sum(字段名) : 求字段的和
			3、max(字段名) : 求字段的最大值
			4、min(字段名) : 求字段的最小值
			5、count(字段名) : 统计该字段的记录的个数
		2、练习
			1、攻击力最强值是多少
				select max(gongji) as best from sanguo;
			2、统计一下表中id,name字段分别有多少条记录
				select count(id),count(name) from sanguo;
				# 空值NULL被统计，空字符串""不会被统计
			3、计算蜀国英雄的总攻击力
				select sum(gongji) from sanguo where country = "蜀国";
			4、统计蜀国英雄中攻击值大于200的英雄的数量
				select count(*) from sanguo where country="蜀国" and gongji>200;
###	5、group by 
		1、作用：给查询的结果进行分组
		示例：
			1、查询sanguo表中一共有几个国家
				select country from sanguo group by country;
			2、计算所有国家的平均攻击力
				select country,avg(gongji) from sanguo group by country;
			3、查找所有国家中 英雄数量最多 的前2名 的国家名称及英雄数量
				select country,count(*) as number from sanguo group by country order by number limit 2; 
			注意：
			 1、group by后的字段名必须要为select之后的字段名
			 2、group by处理的是group by之后的所有字段，如果查询字段和group by之后的字段不一致，则必须要对该字段值做聚合处理(聚合函数)
###	6、having
		1、作用 ：对查询的结果进行进一步筛选
		2、练习
			1、找出平均攻击力大于105的国家的前2名,显示国家名和平均攻击力
				select country,avg(gongji) as pjgj from sanguo group by country having pjgj>150 order by pjgj desc limit 2; 
		3、注意
			1、having语句通常与group by语句联合使用，用来过滤由group by语句返回的记录集
			2、having语句的存在弥补了where关键字不能与聚合函数联合使用的不足，where操作的是表中实际存在的字段，having操作的是聚合函数生成的显示列
###	7、distinct
		1、作用
			不显示字段的重复值
		2、练习
			1、sanguo表中一共有多少个国家
				select distinct country from sanguo;
			2、计算蜀国一共有多少个英雄
				select count(distinct name) from sanguo where country="蜀国";
			3、注意
				1、distinct处理的是distinct与from之间的所有字段，所有字段必须全部相同才能去重
				2、distinct不能对任何字段做聚合处理
###	8、查询表记录时做数学运算
		1、运算符
			+  -  *  /  %
		2、查询显示时所有英雄攻击力全部 * 10
			select id,name,country,gongji*10 as xgj from sanguo;
		3、查询显示时所有英雄的防御力 + 5
			select id,name,country,fangyu+5 as xfy from sanguo;

##6、约束
###	1、作用
		为了保证数据的完整性、一致性、有效性的规则
		可以限制无效的数据插入到数据表里面
###	2、约束分类
		1、默认约束(default)
			1、作用 ：在插入记录时，如果不为该字段赋值，则使用默认值
			2、格式 ：字段名 数据类型 default 值
		2、非空约束(not null)
			1、作用 ：不允许将该字段的值有NULL记录
			2、格式 ：字段名 数据类型 not null
###  3、索引(index)
	1、定义
		对数据库中表的一列或者多列的值进行排序的一种结构(MySQL中用二叉树Btree方式)
	2、优点
		可以加快数据的检索速度
	3、缺点
		1、当对表中的数据进行增加、删除和修改的时候，索引也要动态维护，降低了数据的维护速度
		2、索引需要占用物理空间	
###	4、索引类型
		1、普通索引(index)
			1、使用规则
				1、一个表中可以有多个index字段
				2、字段的值可以有重复，且可以为null值
				3、经常把做查询条件的字段设置为index字段
				4、index字段的key标志是MUL	
			2、创建
				1、创建表时创建
					index(字段名1),index(字段名2)
					create table t1(
					id int,
					name char(20),
					age tinyint unsigned,
					index(id),
					index(name)
					);
				2、在已有表中创建index
					1、语法
						create index 索引名 on 表名(字段名);
					注意：
						索引名一般和字段名一样
			3、查看普通索引
				1、desc 表名;  --> 查看key标志为MUL
				2、show index from 表名;
			4、删除索引
				drop index 索引名 on 表名;
				drop index id on t1;
				drop index name on t1;
				注意：
					删除普通索引只能一个一个删除
		2、唯一索引(unique key)
			1、使用规则
				1、一个表里面可以有个unique字段
				2、unique字段的值不允许重复，但可以为空
				3、unique的key标志是 UNI
			2、创建唯一索引
				1、创建表时创建
					1、方式1
						字段名 数据类型 unique,
						create table t7(
						id int unique,
						name char(15)
						);
					2、方式2
						unique(字段名),
						unique(字段名)
						create table t10(
						id int,
						name char(15),
						unique(id),
						unique(name)
						);
				2、已有表中创建
					create unique index 索引名 on 表名(字段名);
			3、删除唯一索引(unique)
				drop index 索引名 on 表名;
				注意：删除index、unique index只能一个一个删除







