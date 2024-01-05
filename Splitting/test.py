import mysql.connector as a
b=a.connect(host='localhost', user='root', passwd='root')
d=b.cursor(buffered=True)
d.execute('SELECT * FROM test.rooms JOIN test.room_class_specs ON test.rooms.RoomClassID = test.room_class_specs.RoomClassID;')

d.execute('select * from test.prn_sub;')
e=d.column_names;
f=list(e)
f.pop(0)
print(f)

for i in f:
    print(i)
    d.execute('select `'+i+'` from test.prn_sub where `'+i+'` is not null;')
    g=d.fetchall()
    for j in g:
        print(j[0])