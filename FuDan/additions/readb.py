#coding=utf-8 
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


cityName = "北京市"
try:
	conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',db='myalltest',port=3306)
	cur=conn.cursor()
	cur.execute("SET NAMES utf8");
	sql = 'select * from myalltest.privincetest where name = "%s"'
	sql = sql % cityName
	cityName = "北京市".encode()
	sql = 'select * from myalltest.privincetest where name = "%s"' % (cityName)
	# sql = 'select * from myalltest.privincetest where id= 7026'
	# sql = "select * from myalltest.privincetest"
	# print sql
	length = cur.execute(sql)
	print length
	results = cur.fetchall()
	for r in results:
		print r[2].encode().decode('utf-8'), type(r[2])
except MySQLdb.Error, e:
	print e
