#Day01�ʼ�
##1��MySQL����
###	1��ʲô�����ݿ�
���ݿ���һ���洢���ݵĲֿ�

###	2����Щ��˾�������ݿ�
���ڻ�����������վ����Ϸ��վ����̳��վ... ...

###	3���ṩ���ݿ���������
+ 1����������
    +	MySQL��SQL_Server��Oracle��DB2��Mariadb��MongoDB ..
+	2�������������У����ѡ��ʹ���ĸ����ݿ�����
	  +	1���Ƿ�Դ
	      + 1����Դ����
	          + MySQL��Mariadb��MongoDB
	      + 2����ҵ����
	          + Oracle��DB2��SQL_Server
    +	2���Ƿ��ƽ̨
        + 1������ƽ̨ ��SQL_Server
        + 2����ƽ̨
            + MySQL��Oracle��DB2��Mariadb��MongoDB
    +	3����˾����
        + 1����ҵ�������������š����ڻ���
        + 2����Դ��������Ϸ��վ��������վ����̳��վ... 

### 4��MySQL�ص�
		1����ϵ�����ݿ�
			1����ϵ�����ݿ��ص�
				1�����������к��е���ʽ�洢��
				2����һϵ�е��к��г�Ϊ��
				3�����е�ÿһ�н�һ����¼
				4�����е�ÿһ�н�һ���ֶ�
				5�����ͱ�֮����߼������й�ϵ
				6����ϵ�����ݿ�ĺ��������� ��ϵ �� ��ά��
			2��ʾ��
				1����ϵ�����ݿ�洢
					��1��ѧ����Ϣ��
						����     ����  �༶
						������    25   AID1712
						������  26   AID1711

					��2���༶��Ϣ��
						�༶    ������
						AID1712 ����
						AID1711 ����
				2���ǹ�ϵ�����ݿ�洢
					{����:"������",����:25,�༶:"1712",������:"��"}
					{����:"������",����:25,�༶:"1712",������:"��"}
		2����ƽ̨
			������Unix��Linux��Windows������MySQL����
		3��֧�ֶ��ֱ������
			Python��java��php��... ...
##2��MySQL��װ
	1��Ubuntu��װMySQL����
		1����װ�����
			sudo apt-get install mysql-server
		2����װ�ͻ���
			sudo apt-get install mysql-client
	2��Windows��װMySQL����
		1������MySQL��װ��(Windows)
			mysql-install-**5.7**.msi
		2��˫�������ս̳̰�װ����
##3������������Mysql����
	1�����������
		1���鿴Mysql�����״̬
			sudo /etc/init.d/mysql status
		2������Mysql����
			sudo /etc/init.d/mysql start
		3��ֹͣMysql����
			sudo /etc/init.d/mysql stop
		4������Mysql����
			sudo /etc/init.d/mysql restart
	2���ͻ�������
		1�������ʽ
			mysql -h������ -u�û��� -p����
			mysql -hlocalhost -uroot -p123456
		2���������ӿ���ʡ�� -h ѡ��
			mysql -uroot -p123456
		3���Ͽ��������������
			exit   |   quit  |   \q
##4������SQL����
	1��SQL�����ʹ�ù���
		1��ÿ����������� ; ��β
		2��SQL���������ĸ��Сд
		3��ʹ�� \c ��ֹ�����ִ��
	2����Ĺ���
		1����Ļ�������
			1���鿴���еĿ�
				show databases;
			2��������(ָ���ַ���)
				create database ���� default charset=utf8;
			3���鿴����������
				show create database ����;
			4���鿴��ǰ���ڿ�
				select database();
			5���л���
				use ����;
			6���鿴�������б�
				show tables;
			7��ɾ����
				drop database ����;
		2�������������
			1������ʹ�����֡���ĸ��_,���ǲ����Ǵ�����
			2������������ĸ��Сд
			3����������Ψһ��
			4������ʹ�������ַ���mysql�ؼ���
		3����ϰ
			1��������AID1712db,ָ���ַ���Ϊutf8
			2�����뵽��AID1712db��
			3���鿴��ǰ���ڿ�
			4���鿴�������б�
			5���鿴AID1712db���ַ���
			6��ɾ����AID1712db
	3�����Ĺ���
		1�����Ļ�������
			1��������
				create table ����(
				�ֶ��� ��������,
				�ֶ��� ��������,
				...
				);
			2���鿴�����������(�ַ���)
				show create table ����;
			3���鿴���ṹ
				desc ����;
			4��ɾ����
				drop table ����;
		2��ע��
			1�����е����ݶ������ļ�����ʽ�洢�����ݿ�Ŀ¼��
			2�����ݿ�Ŀ¼��/var/lib/mysql
		3����ϰ
			1��������python
			2����python���д�����py_mysql,�ֶ�����������
				id kuname biaoname ���������Լ�����
			3���鿴�����������
			4���鿴py_mysql�ı��ṹ
			5��ɾ����py_mysql
	4������¼�Ĺ���
		1���ڱ��в����¼
			1��insert into ���� values(ֵ1),(ֵ2),....;
		2���鿴����¼
			1��select * from ����;
			2��select �ֶ���1,�ֶ���2,... from ����;
		3����ϰ
			1���鿴���еĿ�
			2������һ���¿�studb
			3����studb�д���һ�ű�t1,�ֶ���4��
				id name age score ���������Լ�����
			4���鿴t1�ı��ṹ
			5���ڱ�t1��������������¼
			6���鿴t1���е����м�¼
			7���鿴������t1�����(�ַ���)
##5����θ���Ĭ���ַ���
	1������
		ͨ������Mysql�������ļ�ʵ��
	2������
		1����ȡrootȨ��
			sudo -i
		2���޸�mysql�����ļ�
			vi /etc/mysql/mysql.conf.d/mysqld.cnf
			[mysqld]
			character_set_server = utf8
		3������mysql����
			sudo /etc/init.d/mysql restart		
##6���ͻ��˰����ݴ洢�����ݿ�������ϵĹ���
	1�����ӵ����ݿ������ : mysql -uroot -p
	2��ѡ��� : use ����;
	3������/�޸ı�
	4���Ͽ������ݿ������ ��exit | quit | \q
##7����������
	1����ֵ����(�з���signed �� �޷���unsigned)
		1������
			1��int ������(4���ֽ�)
				ȡֵ��Χ��0~2**32 -1
			2��tinyint ΢С����(1���ֽ�)
				1���з���(signedĬ��) -128~127
				2���޷���(unsigned) 0~255
			3��smallint С����(2���ֽ�)
				ȡֵ��Χ��0~65535
			4��bigint ��������(8���ֽ�)
				ȡֵ��Χ��0~2**64 -1
		2��������
			1��float(4���ֽ�,�����ʾ7����Чλ)
				1���÷�
					�ֶ��� float(m,n) m->��λ�� n->С��λλ��
					float(5,2) ȡֵ��Χ��-999.99~999.99
				2��ע��
					1�������Ͳ�������ʱ���Զ���ȫС��λ��
					2��С��λ�������ָ����λ���������һλ��������
			2��double(8���ֽ�,�����ʾ15����Чλ)
				1���÷�
					�ֶ��� double(m,n)
			3��decimal(M+2���ֽ�,�����ʾ28����Чλ)
				1���÷�
					decimal(M,D)
	2���ַ�����
		1��char(����)
			1������ȡֵ��Χ��1~255
			2������������Ĭ�Ͽ���Ϊ1
		2��varchar(�䳤)
			1��ȡֵ��Χ��1~65535
			2��ע��
				1��varcharû��Ĭ�Ͽ���,�������һ������
				2��char��varcharʹ��ʱ���������ȣ������ܳ������Եķ�Χ
			3��char �� varchar���ص�
				1��char
					�˷Ѵ洢�ռ�,���ܸ�
				2��varchar
					��ʡ�洢�ռ�,���ܵ�
			4���ַ����͵Ŀ��Ⱥ���ֵ���͵Ŀ��ȵ�����
				1����ֵ���͵Ŀ���Ϊ��ʾ����,ֻ����select��ѯʱʹ��,��ռ�ô洢�ռ��С�޹�,����zerofill�鿴Ч��
				2���ַ����͵Ŀ��ȳ������޷��洢
		3����ϰ
			1��������stuinfo1712,utf8,�ֶ�Ҫ��
				ѧ�� : id Ҫ����ʾ����Ϊ3,λ��������0���
				���� : name �䳤������20
				�༶ : class ����������Ϊ7
				���� ��age ΢С���ͣ��������븺��
				���� ��height �����ͣ�С��λ��2λ
				���� ��salary �����ͣ�С��λ2λ�����ֵ99999.99

			2���ڱ��в���������¼
			3����ѯ���м�¼��ֻ��ʾ����������͹���
				select name,age,salary from stuinfo1712;
			4���鿴���ṹ
	3��ö������
		1������ ���ֶ�ֵֻ�����оٵķ�Χ��ѡ��
		2��enum ��ѡ(�����65535����ͬ��ֵ)
			�ֶ��� enum(ֵ1,ֵ2,...)
		3��set ��ѡ(�����64����ͬ��ֵ)
			�ֶ��� set(ֵ1,ֵ2,...)
			likes set("Study","Girl","Python","MySQL")
			"Study,Gril"
	4������ʱ������
		1��year ���� YYYY
		2��date ������ YYYYMMDD
		3��time ��ʱ�� HHMMSS
		4��datetime ������ʱ�� YYYYMMDDHHMMSS
		5��timestamp ������ʱ�� YYYYMMDDHHMMSS
		6��ע��
			1��datetime����ֵĬ�Ϸ���NULL
			2��timestamp����ֵĬ�Ϸ���ϵͳ��ǰʱ��
##8�����ֶεĲ���
	1���﷨ ��alter table ���� ִ�ж���;
		1�������ֶ�(add)
			1�����ӵ�ĩβ
				alter table ���� add �ֶ��� ��������;
			2�����ӵ���ʼ
				alter table ���� add �ֶ��� �������� first;
			3�����ӵ�ָ��λ��
				alter table ���� add �ֶ��� �������� after �ֶ���
		2��ɾ���ֶ�(drop)
			alter table ���� drop �ֶ���;
		3���޸���������(modify)
			alter table ���� modify �ֶ��� �µ���������;
		4���޸��ֶ���(change)
			alter table ���� change ���� ���� ��������;
		5���޸ı���(rename)
			alter table ���� rename �±���;
��ҵ
	1�������
		1��MySQL�е����������� ____��____��____��____
		2����ϵ�����ݿ�ĺ��������� ___ �� ___
	2�������
		1�������ͻ��˰����ݴ洢�����ݿ�������ϵĹ���
		2��char��varchar�����𣿸��Ե��ص�
	3��������
		1������һ����school
		2���ڿ��д�����students���洢ѧ����Ϣ,�ֶ�����
			ѧ��(id) Ҫ����ʾ����Ϊ3λ,λ��������0���
			����(name)������(ageֻ��Ϊ����)���ɼ�(score����)
			�Ա�(sex��ѡ)������(likes��ѡ)����ѧʱ��(������)
		3���鿴students�ı��ṹ
		4����students��������һ���ֶ�id,���ڵ�һ��
		5���ڱ����������5����¼
		6���鿴����ѧ�����������ɼ�����ѧʱ��













