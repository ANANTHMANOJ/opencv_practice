import wget                 #wget api to download fiel from given url
from time import sleep      
import psycopg2             #api to connect to POSTGRESQL
import json                 #importing api for using  JSON

STATUS_DICT = dict()

#Download class has all the required function to download file from the url
class Download(object):
    def __init__(self, u_id, url):
        self.u_id = u_id
        self.url = url
        self.status_dict = dict()
        
#bar_custom function is called iteratively when wget.download() is ran, it updates the database with size of file remaining and finished
    def bar_custom(self, current, total, width=80):
        value = {"finished": current, "remaining": total - current}  # the dictionary containing the current and remaining file size 
        try:
            STATUS_DICT[self.u_id].update(value)
            conn = psycopg2.connect(database="downloads", user = "postgres", password = "amn", host = "127.0.0.1", port = "5432")
            cur=conn.cursor()
            self.u_id=str(self.u_id)
            value=json.dumps(value)
            query='''update  download_datas set value=%s where uid=%s'''
            cur.execute(query,(value,self.u_id))
            conn.commit()
            conn.close()
        except KeyError:
            STATUS_DICT[self.u_id] = value
            
            
#following function is used for downloading by usin wget
    def downloads(self):
        wget.download(self.url, bar=self.bar_custom)
        

        
#DownloadStatus class is used for giving the status updates of the downloads
class DownloadStatus(object):
    def __init__(self, u_id):
        self.u_id = u_id

    def status(self):
        conn = psycopg2.connect(database="downloads", user = "postgres", password = "amn", host = "127.0.0.1", port = "5432")
        cur=conn.cursor()
        query='''select value from download_datas where uid=%s'''   #getting the status of the file of given id
        cur.execute(query,(self.u_id))
        rows=cur.fetchone()
        
        conn.commit()
        conn.close()
        print (rows[0])
        return rows[0] 


