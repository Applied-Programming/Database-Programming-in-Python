import sys
sys.path.append('/usr/lib/python2.1/site-packages')
import MySQLdb
connection=MySQLdb.connect(host="localhost",db="Registration",user="root",passwd="new-password")
con=connection.cursor()
sql_stmt2="select * from regdetails"
try :
    con.execute(sql_stmt2)
    print "Records in the table are: "    
    count=con.rowcount
    print count
    i=0
    while i<count:
        result_set=con.fetchone()
        print "Name:", result_set[0]
        print "Date of birth:", result_set[1]
        print "Address:", result_set[2]
        print "Country:", result_set[3]
        print "Phone number:", result_set[4]
        print "Email id:", result_set[5]
        i=i+1
except:
    print 'Cannot display records'
con.close()