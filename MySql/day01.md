#Day01笔记
##1、MySQL概述
###	1、什么是数据库
数据库是一个存储数据的仓库

###	2、哪些公司在用数据库
金融机构、购物网站、游戏网站、论坛网站... ...

###	3、提供数据库服务的软件
+ 1、软件分类
    +	MySQL、SQL_Server、Oracle、DB2、Mariadb、MongoDB ..
+	2、在生产环境中，如何选择使用哪个数据库软件
	  +	1、是否开源
	      + 1、开源软件
	          + MySQL、Mariadb、MongoDB
	      + 2、商业软件
	          + Oracle、DB2、SQL_Server
    +	2、是否跨平台
        + 1、不跨平台 ：SQL_Server
        + 2、跨平台
            + MySQL、Oracle、DB2、Mariadb、MongoDB
    +	3、公司类型
        + 1、商业软件：政府部门、金融机构
        + 2、开源软件：游戏网站、购物网站、论坛网站... 

### 4、MySQL特点
		1、关系型数据库
			1、关系型数据库特点
				1、数据是以行和列的形式存储的
				2、这一系列的行和列成为表
				3、表中的每一行叫一条记录
				4、表中的每一列叫一个字段
				5、表和表之间的逻辑关联叫关系
				6、关系型数据库的核心内容是 关系 即 二维表
			2、示例
				1、关系型数据库存储
					表1、学生信息表
						姓名     年龄  班级
						张三丰    25   AID1712
						金花婆婆  26   AID1711

					表2、班级信息表
						班级    班主任
						AID1712 侯大大
						AID1711 孙大大
				2、非关系型数据库存储
					{姓名:"张三丰",年龄:25,班级:"1712",班主任:"侯"}
					{姓名:"张三丰",年龄:25,班级:"1712",班主任:"侯"}
		2、跨平台
			可以在Unix、Linux、Windows上运行MySQL服务
		3、支持多种编程语言
			Python、java、php、... ...
##2、MySQL安装
	1、Ubuntu安装MySQL服务
		1、安装服务端
			sudo apt-get install mysql-server
		2、安装客户端
			sudo apt-get install mysql-client
	2、Windows安装MySQL服务
		1、下载MySQL安装包(Windows)
			mysql-install-**5.7**.msi
		2、双击、按照教程安装即可
##3、启动和连接Mysql服务
	1、服务端启动
		1、查看Mysql服务的状态
			sudo /etc/init.d/mysql status
		2、启动Mysql服务
			sudo /etc/init.d/mysql start
		3、停止Mysql服务
			sudo /etc/init.d/mysql stop
		4、重启Mysql服务
			sudo /etc/init.d/mysql restart
	2、客户端连接
		1、命令格式
			mysql -h主机名 -u用户名 -p密码
			mysql -hlocalhost -uroot -p123456
		2、本地连接可以省略 -h 选项
			mysql -uroot -p123456
		3、断开与服务器的连接
			exit   |   quit  |   \q
##4、基本SQL命令
	1、SQL命令的使用规则
		1、每条命令必须以 ; 结尾
		2、SQL命令不区分字母大小写
		3、使用 \c 终止命令的执行
	2、库的管理
		1、库的基本操作
			1、查看已有的库
				show databases;
			2、创建库(指定字符集)
				create database 库名 default charset=utf8;
			3、查看创建库的语句
				show create database 库名;
			4、查看当前所在库
				select database();
			5、切换库
				use 库名;
			6、查看库中已有表
				show tables;
			7、删除库
				drop database 库名;
		2、库的命名规则
			1、可以使用数字、字母、_,但是不能是纯数字
			2、库名区分字母大小写
			3、库名具有唯一性
			4、不能使用特殊字符和mysql关键字
		3、练习
			1、创建库AID1712db,指定字符集为utf8
			2、进入到库AID1712db中
			3、查看当前所在库
			4、查看库中已有表
			5、查看AID1712db的字符集
			6、删除库AID1712db
	3、表的管理
		1、表的基本操作
			1、创建表
				create table 表名(
				字段名 数据类型,
				字段名 数据类型,
				...
				);
			2、查看创建表的语句(字符集)
				show create table 表名;
			3、查看表结构
				desc 表名;
			4、删除表
				drop table 表名;
		2、注意
			1、所有的数据都是以文件的形式存储在数据库目录下
			2、数据库目录：/var/lib/mysql
		3、练习
			1、创建库python
			2、在python库中创建表py_mysql,字段有如下三个
				id kuname biaoname 数据类型自己定义
			3、查看创建表的语句
			4、查看py_mysql的表结构
			5、删除表py_mysql
	4、表记录的管理
		1、在表中插入记录
			1、insert into 表名 values(值1),(值2),....;
		2、查看表记录
			1、select * from 表名;
			2、select 字段名1,字段名2,... from 表名;
		3、练习
			1、查看所有的库
			2、创建一个新库studb
			3、在studb中创建一张表t1,字段有4个
				id name age score 数据类型自己定义
			4、查看t1的表结构
			5、在表t1中随便插入两条记录
			6、查看t1表中的所有记录
			7、查看创建表t1的语句(字符集)
##5、如何更改默认字符集
	1、方法
		通过更改Mysql的配置文件实现
	2、步骤
		1、获取root权限
			sudo -i
		2、修改mysql配置文件
			vi /etc/mysql/mysql.conf.d/mysqld.cnf
			[mysqld]
			character_set_server = utf8
		3、重启mysql服务
			sudo /etc/init.d/mysql restart		
##6、客户端把数据存储到数据库服务器上的过程
	1、连接到数据库服务器 : mysql -uroot -p
	2、选择库 : use 库名;
	3、创建/修改表
	4、断开与数据库的连接 ：exit | quit | \q
##7、数据类型
	1、数值类型(有符号signed 和 无符号unsigned)
		1、整型
			1、int 大整型(4个字节)
				取值范围：0~2**32 -1
			2、tinyint 微小整型(1个字节)
				1、有符号(signed默认) -128~127
				2、无符号(unsigned) 0~255
			3、smallint 小整型(2个字节)
				取值范围：0~65535
			4、bigint 极大整型(8个字节)
				取值范围：0~2**64 -1
		2、浮点型
			1、float(4个字节,最多显示7个有效位)
				1、用法
					字段名 float(m,n) m->总位数 n->小数位位数
					float(5,2) 取值范围：-999.99~999.99
				2、注意
					1、浮点型插入整数时会自动补全小数位数
					2、小数位如果多于指定的位数，会对下一位四舍五入
			2、double(8个字节,最多显示15个有效位)
				1、用法
					字段名 double(m,n)
			3、decimal(M+2个字节,最多显示28个有效位)
				1、用法
					decimal(M,D)
	2、字符类型
		1、char(定长)
			1、宽度取值范围：1~255
			2、不给定宽度默认宽度为1
		2、varchar(变长)
			1、取值范围：1~65535
			2、注意
				1、varchar没有默认宽度,必须给定一个宽度
				2、char和varchar使用时都给定宽度，但不能超过各自的范围
			3、char 和 varchar的特点
				1、char
					浪费存储空间,性能高
				2、varchar
					节省存储空间,性能低
			4、字符类型的宽度和数值类型的宽度的区别
				1、数值类型的宽度为显示宽度,只用于select查询时使用,和占用存储空间大小无关,可用zerofill查看效果
				2、字符类型的宽度超过则无法存储
		3、练习
			1、创建表stuinfo1712,utf8,字段要求：
				学号 : id 要求显示宽度为3,位数不够用0填充
				姓名 : name 变长，宽度20
				班级 : class 定长，宽度为7
				年龄 ：age 微小整型，不能输入负数
				身高 ：height 浮点型，小数位数2位
				工资 ：salary 浮点型，小数位2位，最大值99999.99

			2、在表中插入两条记录
			3、查询表中记录，只显示姓名、年龄和工资
				select name,age,salary from stuinfo1712;
			4、查看表结构
	3、枚举类型
		1、定义 ：字段值只能在列举的范围内选择
		2、enum 单选(最多有65535个不同的值)
			字段名 enum(值1,值2,...)
		3、set 多选(最多有64个不同的值)
			字段名 set(值1,值2,...)
			likes set("Study","Girl","Python","MySQL")
			"Study,Gril"
	4、日期时间类型
		1、year ：年 YYYY
		2、date ：日期 YYYYMMDD
		3、time ：时间 HHMMSS
		4、datetime ：日期时间 YYYYMMDDHHMMSS
		5、timestamp ：日期时间 YYYYMMDDHHMMSS
		6、注意
			1、datetime不给值默认返回NULL
			2、timestamp不给值默认返回系统当前时间
##8、表字段的操作
	1、语法 ：alter table 表名 执行动作;
		1、添加字段(add)
			1、添加到末尾
				alter table 表名 add 字段名 数据类型;
			2、添加到开始
				alter table 表名 add 字段名 数据类型 first;
			3、添加到指定位置
				alter table 表名 add 字段名 数据类型 after 字段名
		2、删除字段(drop)
			alter table 表名 drop 字段名;
		3、修改数据类型(modify)
			alter table 表名 modify 字段名 新的数据类型;
		4、修改字段名(change)
			alter table 表名 change 旧名 新名 数据类型;
		5、修改表名(rename)
			alter table 表名 rename 新表名;
作业
	1、填空题
		1、MySQL中的数据类型有 ____、____、____、____
		2、关系型数据库的核心内容是 ___ 即 ___
	2、简答题
		1、简述客户端把数据存储到数据库服务器上的过程
		2、char和varchar的区别？各自的特点
	3、操作题
		1、创建一个库school
		2、在库中创建表students来存储学生信息,字段如下
			学号(id) 要求显示宽度为3位,位数不够用0填充
			姓名(name)、年龄(age只能为正数)、成绩(score浮点)
			性别(sex单选)、爱好(likes多选)、入学时间(年月日)
		3、查看students的表结构
		4、在students表中增加一个字段id,加在第一列
		5、在表中任意插入5条记录
		6、查看所有学生的姓名、成绩和入学时间














