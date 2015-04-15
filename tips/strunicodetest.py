# str是unicode经过编码之后得到的


u = u'汉'
print repr(u)
print len(u)

s = u.encode('UTF-8')
print repr(s)
print len(s)

u2 = s.decode('UTF-8')
print repr(u2)
print len(u2)

#内置的open()方法打开文件时，read()读取的是str，
#读取后需要使用正确的编码格式进行decode()。
#write()写入时，如果参数是unicode，则需要
#使用你希望写入的编码进行encode()，如果是其
#他编码格式的str，则需要先用该str的编码进行
#decode()，转成unicode后再使用写入的编码进
#行encode()。如果直接将unicode作为参数传入
#write()方法，Python将先使用源代码文件声明
#的字符编码进行编码然后写入。

# coding: UTF-8
 
f = open('test.txt')
s = f.read()
f.close()
print type(s) # <type 'str'>
# 已知是GBK编码，解码成unicode
u = s.decode('GBK')
 
f = open('test.txt', 'w')
# 编码成UTF-8编码的str
s = u.encode('UTF-8')
f.write(s)
f.close()


s = '你好'
ss = u'你好'
print s
print ss
print len(s)
print len(ss)

