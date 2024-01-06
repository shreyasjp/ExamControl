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
prn=[]

d.execute('SELECT * FROM test.rooms JOIN test.room_class_specs ON test.rooms.RoomClassID = test.room_class_specs.RoomClassID order by test.room_class_specs.Priority desc;')
rooms=[]
for i in d.fetchall():
    matrix=[[0] * 2*i[7] for _ in range(i[8])]
    rooms.append(RoomInfo(i[0],i[1],i[5],i[6],0,i[8],i[7],matrix))

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
        prn.append(g[j][0])

totStuds = len(subs)
counter = 0

rooms_required=[]
seats_available=0
for i in range(len(rooms)):
    if(totStuds-seats_available<=10):
        print('Students Left:',totStuds-seats_available)
        break
    if(seats_available<totStuds):
        rooms_required.append(rooms[i])
        seats_available+=rooms[i].TotalSeats

for i in rooms_required:
    if not(i.IsFilled):
        for j in range(2*i.Columns):
            for k in range(i.Rows):
                    if i.FilledSeats <= i.TotalSeats/2:
                        if(j%2==0):
                            i.Matrix[k][j] = subs[prn[counter]]+'-'+str(prn[counter])
                            counter+=1
                            i.FilledSeats+=1
                    else:
                        continue

for i in rooms_required:
    if not(i.IsFilled):
        for j in range(2*i.Columns):
            for k in range(i.Rows):
                    if(i.Matrix[k][j]==0):
                        i.Matrix[k][j] = subs[prn[counter]]+'-'+str(prn[counter])
                        counter+=1
                        i.FilledSeats+=1

for i in rooms_required:
    for j in range(i.Rows):
        for k in range(2*i.Columns):
            print(i.Matrix[j][k],end='\t\t')
        print()
    print()

""" counter=0
for i in range(2*rooms_required[5].Columns):
    for j in range(rooms_required[5].Rows):
        if(i%2==0):
            if len(g)<=counter:
                break
            rooms_required[5].Matrix[j][i] = g[counter][0]
        else:
            continue
        counter+=1

for i in range(rooms_required[5].Rows):
    for j in range(2*rooms_required[5].Columns):
        print(rooms_required[5].Matrix[i][j],end='\t')
    print() """