import csv
import datetime
from django.db import connection

def formatData(file):
    for chunk in file.chunks():
        tem = chunk.decode().split('\r\n')

    lines = [row.split(',') for row in tem]
    if len(lines[-1]) <= 1:
        lines.pop()
    
    # remove "" to None
    return [[None if value == "" else value for value in line] for line in lines]

def formatTime(year, jd, hm):
    hm = '{}{}'.format('0'*(4-len(hm)), hm) if len(hm) < 4 else '2359' if hm == '2400' else hm
    jd = '{}{}'.format('0'*(3-len(jd)), jd) if len(jd) < 3 else jd
    TIMESTAMP = datetime.datetime.strptime('{}{}{}'.format(year, jd, hm), '%Y%j%H%M')  
    
    if str(TIMESTAMP.time()) == '23:59:00':
        TIMESTAMP = TIMESTAMP + datetime.timedelta(minutes = 1)
    
    return str(TIMESTAMP)

def trvalue(a, b, value):
    if float(value) <= 0:
        return None
    try:
        v = round(a*float(value)**b, 2)
        v = v if 0 <= v <= 1 else None
        return v
    except:
        print(value)

class siteObject(object):
    tableName = ""
    field = []
    data = []

    def get_para(self):
        return (self.tableName, self.field, self.data)

    def insert(self):
        SQLString = 'INSERT INTO {} ({}) VALUES ({})'.format(self.tableName, ','.join(self.field), ','.join(['%s']*len(self.field)))
        with connection.cursor() as cursor:
            try:
                cursor.executemany(SQLString, self.data)
            except:
                cursor.close()
                return False
        return True

class Capa3(siteObject):
    tableName = 'RAWDATA_Capa3'
    field = ['TIMESTAMP', 'T0', 'T10', 'T30', 'T50', 'SF10', 'SF30', 'SF50', 'SF70', 'SF90']
    
    def readFile(self, file):
        lines = formatData(file)

        for i, line in enumerate(lines):
            TIMESTAMP = formatTime(line[1], line[2], line[3])

            T = [line[13]]
            T.extend(line[4:7])
            T = [None if float(w) <= 0 else w for w in T]

            data = [TIMESTAMP]
            data.extend(T)

            data += [trvalue(0.9304, 2.0575, line[7])]
            data += [trvalue(0.6961, 2.3896, line[8])]
            data += [trvalue(0.6961, 2.3896, line[9])]
            data += [trvalue(0.6961, 2.3896, line[10])]
            data += [trvalue(0.6961, 2.3896, line[11])]

            lines[i] = data
        self.data = lines
        return self


class Site(object):
    def create(self, typ):
        return globals()[typ]()