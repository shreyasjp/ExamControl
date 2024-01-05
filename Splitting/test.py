import mysql.connector as a
b=a.connect(host='localhost', user='root', passwd='root');
d=b.cursor();
d.execute('SELECT * FROM test.rooms JOIN test.room_class_specs ON test.rooms.RoomClassID = test.room_class_specs.RoomClassID;')

for i in d.fetchall():
    print(i)

d.execute('select * from test.prn_sub;')

for i in d.fetchall():
    print(i)