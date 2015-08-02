#coding=utf-8 
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

string = "北京"

def insertdb(name):
    global cur
    sql = 'INSERT INTO myalltest.test VALUES("%s")'
    sql = sql % name
    print sql
    cur.execute(sql)

try:
    conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',db='myalltest',port=3306, charset="utf8")
    cur=conn.cursor()
    result = cur.execute('select * from privincetest')
    
    results = cur.fetchall()

    for r in results:
        if r[2] == "上海市":
            print r[2]
        # print r[2]
    
    #  print name, type(name)
    # insertdb(name)
    '''
    sql = 'INSERT INTO myalltest.test VALUES("%s")'
    sql = sql % name
    print sql
    cur.execute(sql)
    conn.commit()
    '''
    cur.close()
    conn.close()
except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])

file_object = open('province.txt', 'r')
for line in file_object:
    placeId = int(line.split(" ")[0])
    name = line.split(" ")[1]
    #name = u"北京".encode('utf-8')
    if name =="北京市":
        print name, name == "北京市"
    # print type(name)
