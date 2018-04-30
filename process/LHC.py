import csv
import datetime
from django.db import connection
import sys
from SurfaceHydrology.settings_secret import create_aiomysql

def formatData(file):
    for chunk in file.chunks():
        tem = chunk.decode().split('\r\n')

    lines = [row.split(',') for row in tem]
    # remove no data line
    if len(lines[-1]) <= 1:
        lines.pop()
    
    # remove first line if have not match array number
    if len(lines[0]) != len(lines[1]):
        lines.pop(0)
    
    # remove "" and "NAN" to None
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
    ReceiveDate = ""

    def get_para(self):
        return (self.tableName, self.field, self.data)

    # 插入資料庫
    def insert(self):
        SQLString = 'INSERT IGNORE INTO {} ({}) VALUES ({})'.format(self.tableName, ','.join(self.field), ','.join(['%s']*len(self.field)))

        with connection.cursor() as cursor:
            try:
                cursor.executemany(SQLString, self.data)
            except:
                cursor.close()
                # print(sys.exc_info()[0])
                return {"name": self.__class__.__name__, "result": False}
        return {"name": self.__class__.__name__, "result": True}

    # async 插入資料庫
    async def asyncInsert(self, loop):
        async with create_aiomysql(loop) as pool:
            async with pool.get() as conn:
                async with conn.cursor() as cur:
                    SQLString = 'INSERT IGNORE INTO {} ({}) VALUES ({})'.format(self.tableName, ','.join(self.field), ','.join(['%s']*len(self.field)))
                    try:
                        await cur.executemany(SQLString, self.data)
                        await conn.commit()
                    except:
                        cur.close()
                        return {"name": self.__class__.__name__, "result": False}
                return {"name": self.__class__.__name__, "result": True}

    # 取得統計資料
    def status(self):
        SQLString = 'select "all" ReceiveDate, count(*) count, min(TIMESTAMP) min, max(TIMESTAMP) max from {} \
            UNION \
            select ReceiveDate, count(*) count, min(TIMESTAMP) min, max(TIMESTAMP) max from {} group by ReceiveDate'\
            .format(self.tableName, self.tableName)
        
        with connection.cursor() as cursor:
            try:
                cursor.execute(SQLString)

                columns = [column[0] for column in cursor.description]
                results = []
                for row in cursor.fetchall():
                    results.append(dict(zip(columns, row)))

            except:
                cursor.close()
                # print(sys.exc_info()[0])
                return False
        return results

    # 取得站基本資料(名稱、欄位、資料數量統計)
    def Basic(self):
        return {
            "name": self.__class__.__name__,
            "field": self.field[1:-1],
            "status": self.status()
        }

    def calendarGraph(self, item):
        SQLString = 'select DATE_FORMAT(TIMESTAMP, "%Y-%m-%d") as date, count({}) as num from {} group by date order by date;'.format(item, self.tableName)
        with connection.cursor() as cursor:
            try:
                cursor.execute(SQLString)

                columns = [column[0] for column in cursor.description]
                results = []
                for row in cursor.fetchall():
                    r = [row[0], None if row[1] == None else float(row[1])]
                    results.append(dict(zip(columns, r)))

            except:
                cursor.close()
                # print(sys.exc_info()[0])
                return False
        return results

    # 取得時序資料
    def timeSeries(self, item, startTime, endTime):

        SQLString = 'select TIMESTAMP, {} from {} where TIMESTAMP BETWEEN %s and %s;'.format(str(item), self.tableName)
        
        print(item)
        print(SQLString)
        
        with connection.cursor() as cursor:
            try:
                cursor.execute(SQLString, [startTime, endTime])

                columns = [column[0] for column in cursor.description]
                results = []
                for row in cursor.fetchall():
                    r = [row[0], None if row[1] == None else float(row[1])]
                    results.append(dict(zip(columns, r)))

            except:
                cursor.close()
                a, b, c = sys.exc_info()
                print(a)
                print(b)
                print(c)
                return False
        return results

    # 取得資料陣列
    def outputData(self, startTime, endTime, items):
        SQLString = 'select TIMESTAMP, {} from {} where TIMESTAMP BETWEEN %s and %s'.format(','.join(items), self.tableName)
        with connection.cursor() as cursor:
            try:
                cursor.execute(SQLString, [startTime, endTime])

                columns = [column[0] for column in cursor.description]
                results = [row for row in cursor.fetchall()]

            except:
                cursor.close()
                # print(sys.exc_info()[0])
                return False
        return [columns] + results


class Capa2(siteObject):
    tableName = 'RAWDATA_Capa2'
    field = ['TIMESTAMP', 'T0', 'T10', 'T30', 'T50', 'T150', 'SF10', 'SF30', 'SF50', 'SF70', 'SF90', 'ReceiveDate']

    def readFile(self, file, ReceiveDate):
        lines = formatData(file)

        for i, line in enumerate(lines):

            if line[0] != '121':
                continue

            TIMESTAMP = formatTime(line[1], line[2], line[3])

            data = [TIMESTAMP]
            line[5:10] = [w if 0 <= float(w) < 200 else None for w in line[5:10]]
            data.extend(line[5:10])

            data += [trvalue(0.9304, 2.0575, line[10])]
            data += [trvalue(0.6961, 2.3896, line[11])]
            data += [trvalue(0.6961, 2.3896, line[12])]
            data += [trvalue(0.6961, 2.3896, line[13])]
            data += [trvalue(0.6961, 2.3896, line[14])]
            data += [ReceiveDate]

            lines[i] = data
        self.data = lines
        self.data.sort(key=lambda x: x[0])
        return self

class Capa3(siteObject):
    tableName = 'RAWDATA_Capa3'
    field = ['TIMESTAMP', 'T0', 'T10', 'T30', 'T50', 'SF10', 'SF30', 'SF50', 'SF70', 'SF90', 'ReceiveDate']
    
    def readFile(self, file, ReceiveDate):
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
            
            data += [ReceiveDate]

            lines[i] = data
        self.data = lines
        return self

class Capa4(siteObject):
    tableName = 'RAWDATA_Capa4'
    field = ["TIMESTAMP", "WS_ms_Avg", "WindDir", "AirTC_20_Avg", "RH_20", "AirTC_15_Avg", "RH_15", "AirTC_10_Avg", "RH_10", "AirTC_5_Avg", "RH_5", "NR_Wm2_Avg", "SEVolt_Avg", "Temp_C_Avg_1", "Temp_C_Avg_2", "Temp_C_Avg_3", "Temp_C_Avg_4", "Temp_C_Avg_5", "Temp_C_Avg_6", "Result1_Avg", "Result2_Avg", "Result3_Avg", "Result4_Avg", "Result5_Avg", "Inf_data", "Temp_C_Avg_7", "Rain_mm_Tot", "Pressure_Avg", "ReceiveDate"]
    
    def readFile(self, file, ReceiveDate):
        lines = formatData(file)
        del lines[0:4]

        for i, line in enumerate(lines):
            TIMESTAMP = str(datetime.datetime.strptime(line[0], '"%Y-%m-%d %H:%M:%S"'))

            data = [TIMESTAMP]
            data.extend(line[2:])

            data += [ReceiveDate]

            lines[i] = data

        self.data = lines
        return self

class Site(object):
    def create(self, typ):
        return globals()[typ]()