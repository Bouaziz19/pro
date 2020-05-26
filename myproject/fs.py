import django
import pyodbc
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=SYSCTA100_01_2020;UID=sa;PWD=sa')
cursor = conn.cursor()                        #Cursor Establishment
cursor.execute('select * from pv where z_id >= 830 order by z_id ')   #Execute Query

rs = cursor.fetchall()
print(rs)
for i in rs:
    print(i.N_FACT)