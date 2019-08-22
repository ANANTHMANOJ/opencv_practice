import psycopg2

conn = psycopg2.connect(database="downloads", user = "postgres", password = "amn", host = "127.0.0.1", port = "5432")
cur=conn.cursor()
cur.execute("select count(*) from download_datas")
rows=cur.fetchone()
print(rows[0])
print ("Opened database successfully")