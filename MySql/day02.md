#MySQL-Day02�ʼ�
##1�����ʽ���
	1��DB(Database)
		DB�������ݿ⣬�Ǵ洢���ݵĲֿ�
	2��DBMS(Database Management System)
		���ݿ����ϵͳ
		�������ݿ�������MySQL��Oracle ......
	3��DBS(Database System)
		���ݿ�ϵͳ
		DBS = DB(�洢) + DBMS(���ݿ����) + ���ݿ�Ӧ��(�������ϵͳ,���¹���ϵͳ) + �û�
##2��where�����Ӿ�(��ϲ�ѯ���޸ġ�ɾ������)
	1���﷨��ʽ
		select * from ���� where ����;
##3�����¼����(ɾ��������)
###	1��ɾ�����¼
		1��delete from ���� where ����;
		2��ע��
			delete�����������where�����Ӿ�Ὣ�������м�¼ȫ��ɾ��
###	2�����±��¼
		1��update ���� set �ֶ���=ֵ1,... where ����;
		2��ע��
			update�����������where�����Ӿ�Ὣ�������и��ֶε�ֵ����
###	3����ϰ
		1��������SANGUO
			create database SANGUO;
		2����SANGUO���д���һ�ű�sanguo,ָ���ַ���utf8,�ֶ����£�
			id name gongji fangyu sex country �������ͼ�����Լ�����
			create table sanguo(
			id int,
			name char(15),
			sex enum("��","Ů"),
			country char(10)
			)default charset=utf8;
		3����sanguo���в����¼
			1 �ܲ�   ��  κ��
			2 С��   Ů  ���
			3 ����� ��  ���
			4 ����   Ů  ����
			5 ������ ��  ���
			6 κ��   ��  ���
			insert into sanguo values
			(1,"�ܲ�","��","κ��"),
			(2,"С��","Ů","���"),
			(3,"�����","��","���"),
			(4,"����","Ů","����"),
			(5,"������","��","���"),
			(6,"κ��","��","���");
		4��������������˵���Ϣ(select���where����)
			select * from sanguo where country="���";
		5������һ��Ů�˵���Ϣ,ֻ��ʾ�������Ա�
			select name,sex from sanguo where sex="Ů";
		6���ѲܲٵĹ�����Ϊ���
			update sanguo set country="���" where name="�ܲ�";
		7����κ�ӵ��Ա��Ϊ Ů��������Ϊ ̩��
			update sanguo set sex="Ů",country="̩��" where name="κ��";
		8����idΪ2�ļ�¼�����ָ�Ϊ˾��ܲ���Ա��У����Ҹ�Ϊκ��
			update sanguo set name="˾��ܲ",sex="��",country="κ��" where id=2;
		9��ɾ������̩����
			delete from sanguo where country="̩��";
		10��ɾ������Ӣ�ۼ�¼
			delete from sanguo;
##4�����������(��ϲ�ѯ���޸ġ�ɾ��)
###	1����ֵ�Ƚ�&�ַ��Ƚ�
		1����ֵ�Ƚ��������=��!=��>��>=��<��<=
		2���ַ��Ƚ��������=��!=
		3���﷨
			�飺select * from ���� where �ֶ��� ����� ����/�ַ�;
			�ģ�update ���� set �ֶ���=ֵ,... where �����/�ַ�;
			ɾ��delete from ���� where �ֶ��� ����� ����/�ַ�;
		4����ϰ
			1���ҳ�����������150��Ӣ�۵����ֺ͹�����ֵ
				select name,gongji from sanguo where gongji > 150;
			2�����������Ӣ�۵���Ϣ
				select * from sanguo where country="���";
			3�������ƵĹ�������Ϊ 666 ��������Ϊ88
				update sanguo set gongji=666,fangyu=88 where name = "����";
			4���ڱ��в���һ����¼��κ��
				insert into sanguo values(10,"κ��",101,1,"���");
			5��ɾ����������Ϊ κ�� �ļ�¼
				delete from sanguo where name = "κ��";
###	2���߼��Ƚ�
		1���������and(�������ͬʱ����)  or(���������һ����������Ϳ���)
		2����ϰ
			1���ҳ�����ֵ����200�����Ӣ�۵����ּ�����ֵ
				select name,gongji from sanguo where gongji > 200 and country="���";
			2�������Ӣ���й���ֵΪ110��Ӣ�۵Ĺ���ֵ����Ϊ100������ֵ����Ϊ60
				update sanguo set gongji=100,fangyu=60 where country="���" and gongji=110;
			3�����������κ����Ӣ��
				select * from sanguo where country="���" or country="κ��";	
###	3����Χ�ڱȽ�
		1���������between and ��in ��not in
		2���﷨
			�ֶ��� between ֵ1 and ֵ2
			�ֶ��� in (ֵ1,ֵ2,... ...)
			�ֶ��� not in (ֵ1,ֵ2��... ...)
		3��ʾ��
			1�����ҹ���ֵ��100-200֮������Ӣ����Ϣ
				select * from sanguo where gongji between 100 and 200 and country="���";
			2������id��1,3,5,7�е�Ӣ�۵�id������
				select id,name from sanguo where id in (1,3,5,7);
			3���ҵ�������������Ĺ��ҵ�ŮӢ��
				select * from sanguo where country not in ("���","���") and sex="F";
			4���ҵ����Ϊ1����3����5�����Ӣ�ۺ������ı�š������͹���
				select id,name from sanguo where id in (1,3,5) and country="���" or name="����";
### 4��ƥ��� �ǿ�
		1���� ��is null
		2���ǿ� ��is not null
		3����ϰ
			1����������ΪNULL�����ŮӢ����Ϣ
				select * from sanguo where name is null and country="���" and sex="F";
			2����������Ϊ""��Ӣ�۵�id�������͹���
				select id,name,country from sanguo where name="";
			2��ע��
				1��null : ��ֵ��������is ���� is notȥ����
				2��""   : ���ַ������� = ���� != ȥ����
		��ϰ��
			1������id��3,5,7�У����ҹ���������150�� �����Ӣ�۵ļ�¼
			select * from sanguo where id in (3,5,7) and gongji > 150;
			2�����ҹ��Ҳ����������������߷���������60��Ӣ�۵����� ������ �� ����
			select name,fangyu,country from sanguo where country not in("���","���") or fangyu>60;
			3��������Ϊ��������ҹ�������1-100֮��ķ�������Ϊ88
			update sanguo set fangyu=88 where country="���" and gongji between 1 and 100;
			4���ڱ��в���һ����¼��idΪ99������Ϊ����Ӣ��������Ϣ�Լ���
			insert into sanguo values(99,"����Ӣ",200,90,"���");
			5��ɾ������idΪ99����������Ϊ����Ӣ�ļ�¼
			delete from sanguo where id = 99;
###	5��ģ���Ƚ�
		1���﷨
			�ֶ��� like ���ʽ
		2�����ʽ
			1��_ : ƥ�䵥���ַ�
			2��% : ƥ��0������ַ�
		ʾ����
			1��select id,name from sanguo where name like "_%_"; # ���������������ַ���
			2��select id,name from sanguo where name like "%"; # ƥ�����еļ�¼
			3��select id,name from sanguo where name like "___"; # ƥ������Ϊ�����ֵļ�¼
			4��select id,name from sanguo where name like "��%"; # ƥ���������Եļ�¼
##5��SQL��ѯ
###	1���ܽ�(ִ��˳��)
		0��	select...�ۺϺ��� from ...
		1��	where...
		2��	group by ...
		4��	having ...
		5��	order by ...
		6��	limit ...;
###	2��order by 
		1�����ã�����ѯ�Ľ����������
		2���﷨��ʽ��order by �ֶ��� ����ʽ;
		2������ʽ
			1��ASC(Ĭ��) ������
			2��DESC ������
		3����ϰ
			1����Ӣ�۰�����ֵ�ӵ͵�������
				select * from sanguo order by gongji asc;
			2�������Ӣ�۰�����ֵ�Ӹߵ�������
				select * from sanguo where country = "���" order by gongji desc;
			3����κ����������Ӣ��������Ϊ�����ֵ�Ӣ�۰�����ֵ��������
				select * from sanguo where country in ("���","κ��") and sex="M" (and name like "___") order by fangyu asc;
###	3��limit(��Զ����SQL�������д)
		1������ ��������ʾ��ѯ��¼�ļ�¼����
		2���÷�
			1��limit n -->��ʾ������¼
			2��limit m,n 
				m - > �ӵڼ�����¼��ʼ��ʾ��n��ʾ��ʾ����
				## m��ֵ�Ǵ�0��ʼ����ģ�3���ʾ��������¼
			3����ϰ
				1�����ҹ���ֵǰ���������ֲ�Ϊ��ֵ�������Ӣ�۵�����������ֵ������
					select name,gongji,country from sanguo where country="���" and (name is not null) order by gongji desc limit 3;
				2�����ҷ���ֵ�����ڶ��������������������Ӣ�۵ļ�¼
					select * from sanguo where country="���" order by fangyu limit 1,3;
###	4���ۺϺ���
		1������
			1��avg(�ֶ���) : ���ֶε�ƽ��ֵ
			2��sum(�ֶ���) : ���ֶεĺ�
			3��max(�ֶ���) : ���ֶε����ֵ
			4��min(�ֶ���) : ���ֶε���Сֵ
			5��count(�ֶ���) : ͳ�Ƹ��ֶεļ�¼�ĸ���
		2����ϰ
			1����������ǿֵ�Ƕ���
				select max(gongji) as best from sanguo;
			2��ͳ��һ�±���id,name�ֶηֱ��ж�������¼
				select count(id),count(name) from sanguo;
				# ��ֵNULL��ͳ�ƣ����ַ���""���ᱻͳ��
			3���������Ӣ�۵��ܹ�����
				select sum(gongji) from sanguo where country = "���";
			4��ͳ�����Ӣ���й���ֵ����200��Ӣ�۵�����
				select count(*) from sanguo where country="���" and gongji>200;
###	5��group by 
		1�����ã�����ѯ�Ľ�����з���
		ʾ����
			1����ѯsanguo����һ���м�������
				select country from sanguo group by country;
			2���������й��ҵ�ƽ��������
				select country,avg(gongji) from sanguo group by country;
			3���������й����� Ӣ��������� ��ǰ2�� �Ĺ������Ƽ�Ӣ������
				select country,count(*) as number from sanguo group by country order by number limit 2; 
			ע�⣺
			 1��group by����ֶ�������ҪΪselect֮����ֶ���
			 2��group by�������group by֮��������ֶΣ������ѯ�ֶκ�group by֮����ֶβ�һ�£������Ҫ�Ը��ֶ�ֵ���ۺϴ���(�ۺϺ���)
###	6��having
		1������ ���Բ�ѯ�Ľ�����н�һ��ɸѡ
		2����ϰ
			1���ҳ�ƽ������������105�Ĺ��ҵ�ǰ2��,��ʾ��������ƽ��������
				select country,avg(gongji) as pjgj from sanguo group by country having pjgj>150 order by pjgj desc limit 2; 
		3��ע��
			1��having���ͨ����group by�������ʹ�ã�����������group by��䷵�صļ�¼��
			2��having���Ĵ����ֲ���where�ؼ��ֲ�����ۺϺ�������ʹ�õĲ��㣬where�������Ǳ���ʵ�ʴ��ڵ��ֶΣ�having�������ǾۺϺ������ɵ���ʾ��
###	7��distinct
		1������
			����ʾ�ֶε��ظ�ֵ
		2����ϰ
			1��sanguo����һ���ж��ٸ�����
				select distinct country from sanguo;
			2���������һ���ж��ٸ�Ӣ��
				select count(distinct name) from sanguo where country="���";
			3��ע��
				1��distinct�������distinct��from֮��������ֶΣ������ֶα���ȫ����ͬ����ȥ��
				2��distinct���ܶ��κ��ֶ����ۺϴ���
###	8����ѯ���¼ʱ����ѧ����
		1�������
			+  -  *  /  %
		2����ѯ��ʾʱ����Ӣ�۹�����ȫ�� * 10
			select id,name,country,gongji*10 as xgj from sanguo;
		3����ѯ��ʾʱ����Ӣ�۵ķ����� + 5
			select id,name,country,fangyu+5 as xfy from sanguo;

##6��Լ��
###	1������
		Ϊ�˱�֤���ݵ������ԡ�һ���ԡ���Ч�ԵĹ���
		����������Ч�����ݲ��뵽���ݱ�����
###	2��Լ������
		1��Ĭ��Լ��(default)
			1������ ���ڲ����¼ʱ�������Ϊ���ֶθ�ֵ����ʹ��Ĭ��ֵ
			2����ʽ ���ֶ��� �������� default ֵ
		2���ǿ�Լ��(not null)
			1������ �����������ֶε�ֵ��NULL��¼
			2����ʽ ���ֶ��� �������� not null
###  3������(index)
	1������
		�����ݿ��б��һ�л��߶��е�ֵ���������һ�ֽṹ(MySQL���ö�����Btree��ʽ)
	2���ŵ�
		���Լӿ����ݵļ����ٶ�
	3��ȱ��
		1�����Ա��е����ݽ������ӡ�ɾ�����޸ĵ�ʱ������ҲҪ��̬ά�������������ݵ�ά���ٶ�
		2��������Ҫռ������ռ�	
###	4����������
		1����ͨ����(index)
			1��ʹ�ù���
				1��һ�����п����ж��index�ֶ�
				2���ֶε�ֵ�������ظ����ҿ���Ϊnullֵ
				3������������ѯ�������ֶ�����Ϊindex�ֶ�
				4��index�ֶε�key��־��MUL	
			2������
				1��������ʱ����
					index(�ֶ���1),index(�ֶ���2)
					create table t1(
					id int,
					name char(20),
					age tinyint unsigned,
					index(id),
					index(name)
					);
				2�������б��д���index
					1���﷨
						create index ������ on ����(�ֶ���);
					ע�⣺
						������һ����ֶ���һ��
			3���鿴��ͨ����
				1��desc ����;  --> �鿴key��־ΪMUL
				2��show index from ����;
			4��ɾ������
				drop index ������ on ����;
				drop index id on t1;
				drop index name on t1;
				ע�⣺
					ɾ����ͨ����ֻ��һ��һ��ɾ��
		2��Ψһ����(unique key)
			1��ʹ�ù���
				1��һ������������и�unique�ֶ�
				2��unique�ֶε�ֵ�������ظ���������Ϊ��
				3��unique��key��־�� UNI
			2������Ψһ����
				1��������ʱ����
					1����ʽ1
						�ֶ��� �������� unique,
						create table t7(
						id int unique,
						name char(15)
						);
					2����ʽ2
						unique(�ֶ���),
						unique(�ֶ���)
						create table t10(
						id int,
						name char(15),
						unique(id),
						unique(name)
						);
				2�����б��д���
					create unique index ������ on ����(�ֶ���);
			3��ɾ��Ψһ����(unique)
				drop index ������ on ����;
				ע�⣺ɾ��index��unique indexֻ��һ��һ��ɾ��







