import MySQLdb
import MySQLdb
 
try:
    conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',db='ProvinceDataInfo',port=3306, charset="utf8")
    cur=conn.cursor()
    result = cur.execute('select * from provinceInfo')
    
    file_object = open('province.txt', 'r')
    sql = 'INSERT INTO provinceInfo (placeId, name) VALUES (%d ,"%s")'
    for line in file_object:
	    placeId = int(line.split(" ")[0])
	    name = line.split(" ")[1]
	    name = u"北京".encode('utf-8')
	    #print placeId, name
	    print type(name)
	    sql = sql % (placeId, name)
	    # print sql
	    cur.execute(sql)
	    sql = 'INSERT INTO provinceInfo (placeId, name) VALUES (%d ,"%s")'
    file_object.close()
    conn.commit()
    '''
    for row in cur.fetchall():
        print row[2]
        
     '''
    cur.close()
    conn.close()
except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])

test = "INSERT INTO provinceInfo (placenId, name) VALUES (%d ,%s)"
placeId = 10
name = "no"
test = test % (placeId, name)
print test
