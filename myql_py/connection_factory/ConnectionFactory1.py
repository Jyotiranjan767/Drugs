import pymysql
import csv
class ConnectionFactory():

	def __init__(self):
		pass

	def __connect(self, db="py1"):
		host = 'localhost'
		self.conn = pymysql.connect(host= host, port = 3306, 
			user = 'root', password = '', db = "py1")

		return self.conn

	def create_a_table (self, tableName ):
		query = """create table {tableName}(
					  empno decimal(4,0) NOT NULL,
					  ename varchar(10) default NULL,
					  job varchar(9) default NULL,
					  mgr decimal(4,0) default NULL,
					  hiredate date default NULL,
					  sal decimal(7,2) default NULL,
					  comm decimal(7,2) default NULL,
					  deptno decimal(2,0) default NULL
			)""".format(tableName = tableName)
		with self.__connect().cursor() as cur:

			cur.execute(query)


	def insert_data_into(self  ):
		list = ['7369','SMITH','CLERK','7902','1980-12-17','800.00','','20']
		# a  = list.append(3)
		print(list[0])
		query = [
		"""INSERT into emp values('7369','SMITH','CLERK','7902','1980-12-17','800.00',NULL,'20')""",
		"""INSERT INTO emp VALUES ('7499','ALLEN','SALESMAN','7698','1981-02-20','1600.00','300.00','30')""",
		"""INSERT INTO emp VALUES ('7521','WARD','SALESMAN','7698','1981-02-22','1250.00','500.00','30')""",
		"""INSERT INTO emp VALUES ('7566','JONES','MANAGER','7839','1981-04-02','2975.00',NULL,'20')""",
		"""INSERT INTO emp VALUES ('7654','MARTIN','SALESMAN','7698','1981-09-28','1250.00','1400.00','30')""",
		"""INSERT INTO emp VALUES ('7698','BLAKE','MANAGER','7839','1981-05-01','2850.00',NULL,'30')""",
		"""INSERT INTO emp VALUES ('7782','CLARK','MANAGER','7839','1981-06-09','2450.00',NULL,'10')""",
		"""INSERT INTO emp VALUES ('7788','SCOTT','ANALYST','7566','1982-12-09','3000.00',NULL,'20')""",
		"""INSERT INTO emp VALUES ('7839','KING','PRESIDENT',NULL,'1981-11-17','5000.00',NULL,'10')""",
		"""INSERT INTO emp VALUES ('7844','TURNER','SALESMAN','7698','1981-09-08','1500.00','0.00','30')""",
		"""INSERT INTO emp VALUES ('7876','ADAMS','CLERK','7788','1983-01-12','1100.00',NULL,'20')""",
		"""INSERT INTO emp VALUES ('7900','JAMES','CLERK','7698','1981-12-03','950.00',NULL,'30')""",
		"""INSERT INTO emp VALUES ('7902','FORD','ANALYST','7566','1981-12-03','3000.00',NULL,'20')""",
		"""INSERT INTO emp VALUES ('7934','MILLER','CLERK','7782','1982-01-23','1300.00',NULL,'10')"""]
		print(query[0])

		query1  = [

			"""INSERT INTO dept VALUES ('10','ACCOUNTING','NEW YORK')""",
			"""INSERT INTO dept VALUES ('20','RESEARCH','DALLAS')""",
			"""INSERT INTO dept VALUES ('30','SALES','CHICAGO')""",
			"""INSERT INTO dept VALUES ('40','OPERATIONS','BOSTON')"""

		]

		for i in range(len(query)):
			with self.__connect().cursor() as cur:
					cur.execute(query1[i])
			# raise IndexError("hris sirhui isru")

			# pass

	def delete_duplicate(self):
		query = """delete n1 from emp n1 , emp n2 where n1.empno= n2.empno"""

		with self.__connect().cursor() as cur:
			cur.execute(query)
	def drop_a_table(self, tableName):
		query = """drop table {}""".format(tableName)
		self.__connect().cursor().execute(query)

	def custom_csv(self, tableName):
		query = """create table {tableName}(
					  Name varchar(100) default NULL,
					  EmailId varchar(300) default NULL,
					  Phone INT(11) default NULL,
					  City varchar(300) default NULL,   
					  Course varchar(32) default NULL,  
					  CreateDate varchar(20) default NULL,
					  Time DATETIME default NULL,
					  Month varchar(30) default NULL,
					  Source varchar(30) default NULL,
					  Media varchar(30) default NULL
			)""".format(tableName = tableName)

		with self.__connect().cursor() as cur:


			cur.execute(query)	
	def insert_data_csv(self):
		try:	
			with open('C:\\Users\\luckie\\Desktop\\bunty_1.csv','r') as cs1:
				cs1_reader = csv.reader(cs1)
				dic = {}
				for line in cs1_reader:
					# print(type(line))
					# print(type(line[1]))
					# 	pass
					# print(cs1_reader)
			
					# for i in range(len(query)):
					with self.__connect().cursor() as cur:
						cur.execute("INSERT into bunty_ values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(line[0],line[1],line[2],line[3],line[4],line[5],
						line[6],line[7],line[8],line[9]))
						print(line[1])
		except UnicodeDecodeError("hris sirhui isru"):
			pass
x = ConnectionFactory()
x._ConnectionFactory__connect()
# x.create_a_table('bun1')
# x.insert_data_into()
# x.delete_duplicate()
# x.drop_a_table('dept')
# x.custom_csv('Bunty_')
x.insert_data_csv()