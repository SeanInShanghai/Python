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

rb = xlrd.open_workbook('test.xls')

suffixes = "人民检察院"

charteredCities  = ['北京市', '天津市', '上海市', '重庆市']

pro = ["省", "自治区", "特别行政区"]

country = ['市', '县', '区']

startLine = 2 # start form line 2

conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',db='myalltest',port=3306)
cur=conn.cursor()
cur.execute("SET NAMES utf8")
sqlName = 'select * from myalltest.privincetest where name = "%s"'
sqlPlaceId = 'select * from myalltest.privincetest where placeId = "%d"'
# get file name from table
def getfilename(table, lineNo):
    file_name = table.row_values(lineNo)[1]
    return file_name


# get infor line
def getinforLine(filename, dirname):

    file_object = open(filename, 'r')
    contentLine = ""
    lineNo = 0
    
    for line in file_object:
        if suffixes in line:
            contentLine = line.split("\n")[0]
            break
    return contentLine


# get query Infor 
def getQueryInfo(substr):
    global pro
    global country
    global charteredCities
    
    result = ""
    citytype = 3
    for cc in charteredCities:
        if cc in substr:
            result = cc
            citytype = 0
            break
    
    if result == "":
        for p in pro:
            if p in substr:
                result = substr[0: substr.find(p) + len(p)]
                citytype = 1
                break
    
    if result == "":
        for c in country:
            if c in substr:
                result = substr[0: substr.find(c) + len(c)]
                citytype = 2
                break
    if result == "":
        citytype = 3
    
    return result, citytype
    

# get province name
def getProName(queryInfor, citytype):
    global cur
    global sqlName
    global sqlPlaceId
    
    provinceName = ""
    if citytype == 0:
        return queryInfor
    elif citytype == 3:
	    return "null"
    try:
        queryInfor = queryInfor.encode()
        cursql = sqlName % (queryInfor)
        length = cur.execute(cursql)
        if length == 0:
            return "null"
        result = cur.fetchall()
        placeId = result[0][1]
        placeId = str(placeId)[0:2]
        placeId = long(placeId + "0000")
        curPlaceIdSql = sqlPlaceId % placeId
        cur.execute(curPlaceIdSql)
        
        myResult = cur.fetchall()
        return myResult[0][2]
    except MySQLdb.Error, e:
	    print e
	    return "null"
        
sheetsLen = 6


for sheetNo in range(sheetsLen):
    rb = xlrd.open_workbook('test.xls')
    
    table = rb.sheets()[sheetNo]
    dirname = table.name
    
    rs = rb.sheet_by_index(sheetNo)
    wb = copy(rb)
    ws = wb.get_sheet(sheetNo)
    
    
    os.chdir(dirname)
    rows = table.nrows
    print sheetNo
    for curRow in range(1, rows):
        lineNo = curRow
        file_name = getfilename(table, lineNo)
        contentLine = getinforLine(file_name, dirname)
        # print contentLine, curRow
        pos = str.find(contentLine, suffixes)
        substr = contentLine[0: pos]
        queryInfor, citytype = getQueryInfo(substr)
        cityname = getProName(queryInfor, citytype)
        # print cityname
        print dirname, curRow
        ws.write(curRow, 6, cityname.encode().decode())
        
    os.chdir('..')
    wb.save('test.xls')

'''
rb = xlrd.open_workbook('test.xls')
sheetNo = 0
chinesename = "上海" + str(sheetNo)
table = rb.sheets()[sheetNo]
rs = rb.sheet_by_index(sheetNo)
wb = copy(rb)
ws = wb.get_sheet(sheetNo)
ws.write(0, 10, chinesename.encode().decode())
ws.write(0, 11, chinesename.encode().decode())
wb.save('test.xls')

rb = xlrd.open_workbook('test.xls')
sheetNo = 1
chinesename = "北京" + str(sheetNo)
table = rb.sheets()[sheetNo]
rs = rb.sheet_by_index(sheetNo)
wb = copy(rb)
ws = wb.get_sheet(sheetNo)
ws.write(0, 10, chinesename.encode().decode())
ws.write(0, 11, chinesename.encode().decode())
wb.save('test.xls')

rb = xlrd.open_workbook('test.xls')
sheetNo = 2
chinesename = "广州" + str(sheetNo)
table = rb.sheets()[sheetNo]
rs = rb.sheet_by_index(sheetNo)
wb = copy(rb)
ws = wb.get_sheet(sheetNo)
ws.write(0, 10, chinesename.encode().decode())
ws.write(0, 11, chinesename.encode().decode())

wb.save('test.xls')
'''
