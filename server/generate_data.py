import sqlite3
import random
from datetime import datetime

connection = sqlite3.connect("src/database/driver.db")

cursor = connection.cursor()

def create_driver_type_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS DriverType
            (DriverTypeID INTEGER PRIMARY KEY AUTOINCREMENT,
            DriverTypeName TEXT NOT NULL);''')

def create_status_driver_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS StatusDriver
                (StatusDriverID INTEGER PRIMARY KEY AUTOINCREMENT,
                StatusName TEXT NOT NULL);''')

def create_month_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS Month
                (MonthID INTEGER PRIMARY KEY AUTOINCREMENT,
                MonthName TEXT NOT NULL);''')

# -- create table above first before create driver license to avoid foreign key constraint

def create_driver_license_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS DriverLicense (
                    DriverLicenseID	INTEGER PRIMARY KEY AUTOINCREMENT,
                    DriverTypeID	INTEGER NOT NULL,
                    BirthDay	INTEGER NOT NULL,
                    BirthMonthID	INTEGER NOT NULL,
                    BirthYear	INTEGER NOT NULL,
                    StatusDriverID	INTEGER NOT NULL,
                    FOREIGN KEY("DriverTypeID") REFERENCES "DriverType"("DriverTypeID"),
                    FOREIGN KEY("BirthMonthID") REFERENCES "Month"("MonthID"),
                    FOREIGN KEY("StatusDriverID") REFERENCES "StatusDriver"("StatusDriverID")
                );''')

    cursor.execute("INSERT INTO DriverLicense (DriverTypeID, BirthDay, BirthMonthID, BirthYear, StatusDriverID) VALUES (1, 1, 1, 2000, 1);")
    connection.commit()

    # set autoincrement from 1 (above insert) to 100000000
    cursor.execute("UPDATE SQLITE_SEQUENCE SET seq = 100000000 WHERE name = 'DriverLicense';")
    connection.commit()
    # delete the row with DriverLicenseID = 1 to start with 100000001
    cursor.execute("DELETE FROM DriverLicense WHERE DriverLicenseID = 1;")

def insert_driver_type_table():
    driver_type_data = [("บุคคลทั่วไป",), ("มือใหม่",), ("คนขับรถสาธารณะ",) ]
    cursor.executemany("""
        INSERT INTO DriverType (DriverTypeName) VALUES (?);
    """, driver_type_data)
    connection.commit() # we need to commit to save the changes


def insert_status_driver_table():
    status_driver_data = [("ปกติ",), ("หมดอายุ",), ("ถูกระงับ",) ]
    cursor.executemany("""
        INSERT INTO StatusDriver (StatusName) VALUES (?);
    """, status_driver_data)
    connection.commit()

def insert_month_table():
    month_data = [("มกราคม",), ("กุมภาพันธ์",), ("มีนาคม",), ("เมษายน",), ("พฤษภาคม",), ("มิถุนายน",), ("กรกฎาคม",), ("สิงหาคม",), ("กันยายน",), ("ตุลาคม",), ("พฤศจิกายน",), ("ธันวาคม",) ]
    cursor.executemany("""
        INSERT INTO Month (MonthName) VALUES (?);
    """, month_data )
    connection.commit()

# insert 3 table above first to avoid foreign key constraint #

# fucntion use with insert_driver_license_table
def statusTypeValue(age, driver_type):
    # 1 = ปกติ, 2 = หมดอายุ, 3 = ถูกระงับ
    if driver_type == 1:
        if age > 70:
            return 2
        elif age < 16:
            return 3
        else:
            return 1
    elif driver_type == 2:
        if age > 50:
            return 2
        elif age < 16:
            return 3
        else:
            return 1
    elif driver_type == 3:
        if age > 60:
            return 2
        elif age < 20:
            return 3
        else:
            return 1

    # (b_year := random.randint(1940, 2013)),
    # 2 if (age := today.year - b_year - ((today.month, today.day) < (bm, b_day))) > 70 else \
    # 3 if age < 16 else 1

# insert data with type with id for do inner join table
def insert_driver_license_table():
    num_license = 200
    driver_type = [1, 2, 3]
    status_driver = [1, 2, 3]
    month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    today = datetime.now()
    driver_license_data = [
        (
            (dt := random.choice(driver_type)),
            (b_day := random.randint(1, 31)) if (bm := random.choice(month)) in [1, 3, 5, 7, 8, 10, 12] else \
            (b_day := random.randint(1, 30)) if bm in [4, 6, 9, 11] else (b_day := random.randint(1, 28)),
            bm,
            (b_year := random.randint(1940, 2013)),
            statusTypeValue(today.year - b_year - ((today.month, today.day) < (bm, b_day)), dt)
        )
        for _ in range(num_license)
    ]

    try:
        print(driver_license_data)
        cursor.executemany("""
        INSERT INTO DriverLicense (DriverTypeID, BirthDay, BirthMonthID, BirthYear, StatusDriverID) VALUES (?, ?, ?, ?, ?);
        """, driver_license_data)
        connection.commit()
        print("Data inserted successfully!")
    except sqlite3.IntegrityError as e:
        print("Error inserting data:", e)


def delete_all_data_driving_license():
    cursor.execute("DELETE FROM DriverLicense;")
    connection.commit()

def delete_all_data_driver_type():
    cursor.execute("DELETE FROM DriverType;")
    connection.commit()

def delete_all_data_status_driver():
    cursor.execute("DELETE FROM StatusDriver;")
    connection.commit()

def delete_all_data_month():
    cursor.execute("DELETE FROM Month;")
    connection.commit()

def delete_all_data():
    delete_all_data_driving_license()
    delete_all_data_driver_type()
    delete_all_data_status_driver()
    delete_all_data_month()

def drop_driver_license_table():
    cursor.execute("DROP TABLE IF EXISTS DriverLicense;")
    connection.commit()

def drop_driver_type_table():
    cursor.execute("DROP TABLE IF EXISTS DriverType;")
    connection.commit()

def drop_status_driver_table():
    cursor.execute("DROP TABLE IF EXISTS StatusDriver;")
    connection.commit()

def drop_month_table():
    cursor.execute("DROP TABLE IF EXISTS Month;")
    connection.commit()

def drop_all_tables():
    drop_driver_license_table()
    drop_driver_type_table()
    drop_status_driver_table()
    drop_month_table()


# # # drop all data
drop_all_tables()

# # # drop specific table
# drop_driver_license_table()

# # # create DrivingLicense table
create_driver_type_table()
create_status_driver_table()
create_month_table()
create_driver_license_table()

# # # insert data into driving table
insert_driver_type_table()
insert_status_driver_table()
insert_month_table()

# --- FINISHED --- #

# # insert main data driverlicense
insert_driver_license_table()
