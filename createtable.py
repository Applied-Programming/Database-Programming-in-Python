#!/usr/local/ActivePython-2.1/bin/python
import sys
sys.path.append('/usr/lib/python2.1/site-packages')
import MySQLdb
connection=MySQLdb.connect(host="localhost",db="Registration",user="root",passwd="new-password")
con=connection.cursor()
sql_stmt='create table regdetails (cName varchar(20),cDob date, cAdd varchar(50), cCountry varchar(20),cPhone varchar(15),cemail varchar(20))'
try :
    con.execute(sql_stmt)
    print 'Table created'
except:
    print 'Cannot create table'
con.close()