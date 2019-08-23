import wget
from time import sleep
import psycopg2
import json

STATUS_DICT = dict()


class Download(object):
    def __init__(self, u_id, url):
        self.u_id = u_id
        self.url = url
        self.status_dict = dict()

    def bar_custom(self, current, total, width=80):
        value = {"finished": current, "remaining": total - current}
        try:
            STATUS_DICT[self.u_id].update(value)
            # write to the database, for example for id = 2
            # query = f"update table set value = value"
            #  id      value
            #   1      {"finished":1,"remaining":2}
            #   2      {"finished":3,"remaining":4}
            conn = psycopg2.connect(database="downloads", user = "postgres", password = "amn", host = "127.0.0.1", port = "5432")
            
            cur=conn.cursor()
            self.u_id=str(self.u_id)
            
            value=json.dumps(value)
            query='''update  download_datas set value=%s where uid=%s'''
            cur.execute(query,(value,self.u_id))
            conn.commit()
            conn.close()

        except KeyError:
            # query = f"update table set value = value"
            STATUS_DICT[self.u_id] = value

    def downloads(self):
        wget.download(self.url, bar=self.bar_custom)


class DownloadStatus(object):
    def __init__(self, u_id):
        self.u_id = u_id

    def status(self):
        # this will return u the dictionary containing download status
        # query the database where the id = u_id
        # query = select value from table where id = u_id
        # then return the value
        conn = psycopg2.connect(database="downloads", user = "postgres", password = "amn", host = "127.0.0.1", port = "5432")
        cur=conn.cursor()
        query='''select value from download_datas where uid=%s'''
        cur.execute(query,(self.u_id))
        rows=cur.fetchone()
        
        conn.commit()
        conn.close()
        print (rows[0])
        return rows[0]


