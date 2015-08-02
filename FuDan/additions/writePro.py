# coding=utf-8
import urllib2
import urllib
from lxml import etree
from urllib2 import URLError
import lxml.html
import xlwt
import xlrd
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from xlutils.copy import copy
import MySQLdb

rb = xlrd.open_workbook('result.xls')

suffixes = "人民检察院"

charteredCities  = ['北京市', '天津市', '上海市', '重庆市']

pro = ["省", "自治区", "特别行政区"]

country = ['市', '县', '区']


table = rb.sheets()[0]
file_name = table.row_values(143)[1]
os.chdir(table.name)
print file_name
file_object = open(file_name, 'r')
contentLine = ""
lineNo = 0
for line in file_object:
    if suffixes in line:
        contentLine = line
        break
    lineNo += 1
print contentLine

pos = str.find(contentLine, suffixes)
substr = contentLine[0: pos]
print substr
proName = ""

# if substr has province name, get it

for cc in charteredCities:
    if cc in substr:
        proName = cc
        break

for p in pro:
    if p in substr: 
        proName = substr[0: substr.find(p)+len(p)]
        break

if proName == "":
    for c in country:
        if c in substr:
            cityName = substr[0: substr.find(c) + len(c)]
            break
    if cityName != "":
        try:
            conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',db='myalltest',port=3306)
            cur=conn.cursor()
            cur.execute("SET NAMES utf8");
            sql = 'select * from privincetest where name = "%s"'
            sql = sql % cityName
            cur.execute(sql)
            results = cur.fetchall()
            for r in results:
				print r[2], "hello"
        except MySQLdb.Error, e:
            print e
# print proName
# print table.name
os.chdir('..')

rs = rb.sheet_by_index(0)
wb = copy(rb)
ws = wb.get_sheet(0)
ws.write(0, 10, "changed")
wb.save('test.xls')
