import csv
import datetime
from django.db import connection
import sys

def formatData(file):
    for chunk in file.chunks():
        tem = chunk.decode().split('\r\n')

    lines = [row.split(',') for row in tem]
    if len(lines[-1]) <= 1:
        lines.pop()
    
    # remove "" to None
    return [[None if (value == "" or value == '"NAN"') else value for value in line] for line in lines]

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
        SQLString = 'INSERT IGNORE INTO {} ({}) VALUES ({})'.format(self.tableName, ','.join(self.field), ','.join(['%s']*len(self.field)))
        
        print(SQLString)
        with connection.cursor() as cursor:
            try:
                cursor.executemany(SQLString, self.data)
            except:
                cursor.close()
                print(sys.exc_info()[0])
                return False
        return True

class Capa2(siteObject):
    tableName = 'RAWDATA_Capa2'
    field = ['TIMESTAMP', 'T0', 'T10', 'T30', 'T50', 'T150', 'SF10', 'SF30', 'SF50', 'SF70', 'SF90']

    def readFile(self, file):
        lines = formatData(file)

        for i, line in enumerate(lines):
            TIMESTAMP = formatTime(line[1], line[2], line[3])

            data = [TIMESTAMP]
            line[5:10] = [w if 0 <= float(w) < 200 else None for w in line[5:10]]
            data.extend(line[5:10])

            data += [trvalue(0.9304, 2.0575, line[10])]
            data += [trvalue(0.6961, 2.3896, line[11])]
            data += [trvalue(0.6961, 2.3896, line[12])]
            data += [trvalue(0.6961, 2.3896, line[13])]
            data += [trvalue(0.6961, 2.3896, line[14])]

            lines[i] = data
        self.data = lines
        self.data.sort(key=lambda x: x[0])
        return self

class Capa3(siteObject):
    tableName = 'RAWDATA_Capa3'
    field = ['TIMESTAMP', 'T0', 'T10', 'T30', 'T50', 'SF10', 'SF30', 'SF50', 'SF70', 'SF90']
    
    def readFile(self, file):
        lines = formatData(file)

        for i, line in enumerate(lines):
            TIMESTAMP = formatTime(line[1], line[2], line[3])

            T = [line[13]]
            T.extend(line[4:7])
            T = [w if 0 <= float(w) < 200 else None for w in T]

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

class Capa4(siteObject):
    tableName = 'RAWDATA_Capa4'
    field = ["TIMESTAMP", "WS_ms_Avg", "WindDir", "AirTC_20_Avg", "RH_20", "AirTC_15_Avg", "RH_15", "AirTC_10_Avg", "RH_10", "AirTC_5_Avg", "RH_5", "NR_Wm2_Avg", "SEVolt_Avg", "Temp_C_Avg_1", "Temp_C_Avg_2", "Temp_C_Avg_3", "Temp_C_Avg_4", "Temp_C_Avg_5", "Temp_C_Avg_6", "Result1_Avg", "Result2_Avg", "Result3_Avg", "Result4_Avg", "Result5_Avg", "Inf_data", "Temp_C_Avg_7", "Rain_mm_Tot", "Pressure_Avg"]
    
    def readFile(self, file):
        lines = formatData(file)
        del lines[0:4]

        for i, line in enumerate(lines):
            TIMESTAMP = str(datetime.datetime.strptime(line[0], '"%Y-%m-%d %H:%M:%S"'))

            data = [TIMESTAMP]
            data.extend(line[2:])

            lines[i] = data

        self.data = lines
        return self

class Site(object):
    def create(self, typ):
        return globals()[typ]()