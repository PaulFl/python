import pymysql

cinema_db = pymysql.connect("baulne.paulf.tk", "anton", "medvedev", "cinema") #Connection à la database cinema

cursor = cinema_db.cursor()

sql_request = "SELECT * FROM Acteurs"

cursor.execute(sql_request)

response = cursor.fetchall()

print(response)