import sqlite3
from datetime import datetime

class DriverLicenseModel:
    def __init__(self, db_path="./src/database/driver.db"):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        # cursor = self.conn.cursor()
        # cursor.execute("PRAGMA journal_mode=WAL")
        # self.conn.commit()
        # self.conn.close()
    
    # display all DriverName from DriverType table
    def get_available_driver_type(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM DriverType")
        result = cursor.fetchall()
        cursor.close()
        return result

    # display all StatusDriverName from StatusDriver table
    def get_available_status_driver(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM StatusDriver")
        result = cursor.fetchall()
        cursor.close()
        return result

    # display all DriverLicense from DriverLicense table
    def get_all_driver_license(self):
        cursor = self.conn.cursor()
        cursor.execute("""SELECT DriverLicenseID, DriverTypeName, BirthDay, MonthName, BirthYear, StatusName
                        FROM DriverLicense INNER JOIN DriverType USING (DriverTypeID)
                        INNER JOIN StatusDriver USING (StatusDriverID)
                        INNER JOIN Month ON (DriverLicense.BirthMonthID = Month.MonthID)
                       """)

        result = cursor.fetchall()
        cursor.close()
        return result
    
    # display specific DriverLicense from DriverLicense table depends on DriverLicenseID
    def get_specific_driver_license(self, driverLicenseID):
        cursor = self.conn.cursor()
        cursor.execute("""SELECT DriverLicenseID, DriverTypeID, DriverTypeName, BirthDay, MonthID, MonthName, BirthYear, StatusDriverID, StatusName
                        FROM DriverLicense INNER JOIN DriverType USING (DriverTypeID)
                        INNER JOIN StatusDriver USING (StatusDriverID)
                        INNER JOIN Month ON (DriverLicense.BirthMonthID = Month.MonthID)
                        WHERE DriverLicenseID = ?
                       """, (driverLicenseID, ))
        result = cursor.fetchone()
        cursor.close()
        return result if result else None

    def get_report_driver_type_number(self):
        cursor = self.conn.cursor()
        cursor.execute("""SELECT DriverTypeID, DriverTypeName, COUNT(*) 
                            FROM DriverLicense INNER JOIN DriverType USING (DriverTypeID)
                            GROUP BY DriverTypeID""")
        result = cursor.fetchall()
        cursor.close()
        return result if result else None

    def get_report_status_driver_number(self):
        cursor = self.conn.cursor()
        cursor.execute(""" SELECT StatusDriverID, StatusName, COUNT(*) 
                            FROM DriverLicense INNER JOIN StatusDriver USING (StatusDriverID)
                            GROUP BY StatusDriverID""")
        result = cursor.fetchall()
        cursor.close()
        return result if result else None
    
    # display age of specific driver license
    def get_age_of_driver_license(self, driverLicenseID):
        cursor = self.conn.cursor()
        cursor.execute("""SELECT BirthDay, BirthMonthID, BirthYear FROM DriverLicense WHERE DriverLicenseID = ?""", (driverLicenseID, ))
        result = cursor.fetchone()
        cursor.close()
        if not result:
            return None

        birth_day, birth_month, birth_year = result
        today = datetime.now()
        age = today.year - birth_year - ((today.month, today.day) < (birth_month, birth_day))

        return age

    def change_status_driver_license(self, driverLicenseID, driverTypeID):

        print("---- FROM MODEL ----")
        print(driverLicenseID)
        print(driverTypeID)
        print(f"Type of driverLicenseID: {int(driverLicenseID)}, Value: {driverLicenseID}")

        cursor = self.conn.cursor()
        cursor.execute("UPDATE DriverLicense SET DriverTypeID = ? WHERE DriverLicenseID = ?", (int(driverTypeID), driverLicenseID))
        self.conn.commit()
        cursor.close()
        return True