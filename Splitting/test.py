class RoomInfo:
    def __init__(self, room_id, room_name, priority, total_seats, filled_seats, rows, columns, matrix):
        self.RoomID = room_id
        self.RoomName = room_name
        self.Priority = priority
        self.TotalSeats = total_seats
        self.FilledSeats = filled_seats
        self.Rows = rows
        self.Columns = columns
        self.Matrix = matrix
        self.IsFilled = self.calculate_is_filled()

    def calculate_is_filled(self):
        return self.FilledSeats == self.TotalSeats

import mysql.connector as a
b=a.connect(host='localhost', user='root', passwd='root')
d=b.cursor(buffered=True)

""" d.execute('select * from test.prn_sub;')
e=d.column_names;
f=list(e)
f.pop(0)
print(f)

for i in f:
    print('\n',i,'\n')
    z='select `'+i+'` from test.prn_sub where `'+i+'` is not null;'
    d.execute(z)
    rows = d.rowcount
    print(rows,'\n')
    g=d.fetchall()
    for j in g:
        print(j[0]) """

d.execute('SELECT * FROM test.rooms JOIN test.room_class_specs ON test.rooms.RoomClassID = test.room_class_specs.RoomClassID;')
rooms=[]
for i in d.fetchall():
    matrix=[[0] * 2*i[7] for _ in range(i[8])]
    rooms.append(RoomInfo(i[0],i[1],i[5],i[6],0,i[8],i[7],matrix))

print(rooms[0].RoomName)
print(rooms[5].Matrix)