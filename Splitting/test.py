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
subs={}

d.execute('select * from test.prn_sub;')
e=d.column_names;
f=list(e)
f.pop(0)

for i in f:
    z='select `'+i+'` from test.prn_sub where `'+i+'` is not null;'
    d.execute(z)
    rows = d.rowcount
    g=d.fetchall()
    for j in range(len(g)):
        subs[g[j][0]]=i



d.execute('SELECT * FROM test.rooms JOIN test.room_class_specs ON test.rooms.RoomClassID = test.room_class_specs.RoomClassID;')
rooms=[]
for i in d.fetchall():
    matrix=[[0] * 2*i[7] for _ in range(i[8])]
    rooms.append(RoomInfo(i[0],i[1],i[5],i[6],0,i[8],i[7],matrix))

counter=0
for i in range(2*rooms[0].Columns):
    for j in range(rooms[0].Rows):
        if(i%2==0):
            if len(g)<=counter:
                break
            rooms[0].Matrix[j][i] = subs[g[counter][0]]
        else:
            continue
        counter+=1

for i in range(rooms[0].Rows):
    for j in range(2*rooms[0].Columns):
        print(rooms[0].Matrix[i][j],end='\t')
    print()