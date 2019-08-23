from flask import Flask
from flask import request
from flask_limiter import Limiter 
from flask_limiter.util import get_remote_address
import psycopg2  
from views import Download, DownloadStatus
import json

app = Flask(__name__)
limiter= Limiter(
        app,
        key_func=get_remote_address)#,
       #default_limiter=["200 per day","50 per hour"])


@app.route('/download_file')
def user_download():
    url = request.args['url']
    conn = psycopg2.connect(database="downloads", user = "postgres", password = "amn", host = "127.0.0.1", port = "5432")
    cur=conn.cursor()
    
    # its better to insert into database and then have that id as unique id
    cur=conn.cursor()
    cur.execute("select count(*) from download_datas")
    rows=cur.fetchone()
    u_id=rows[0]+1
    query = '''insert into download_datas (uid) values (%s)'''
    cur.execute (query, str(u_id))
    conn.commit()
    conn.close()
    msg = f"your file is downloading!!!!!!!!!!! and file url is : {url}"
    #u_id = 2
    download_obj = Download(u_id, url)
    download_obj.downloads()
    return msg


@app.route('/download_status')
def download_status():
    u_id = request.args['id']
    status_obj = DownloadStatus(u_id)
    status_dict = status_obj.status()
    msg = f"total finished = {status_dict['finished']} bytes and remaining = {status_dict['remaining']} bytes"
    return msg


@app.route('/index')
def index():
    return ''' <!DOCTYPE html>
<html>
<body>

  <form action="localhost:5000/download_file?url=" method="post" target="_blank" id="my-form">
  <input type="text" name="reference-number" id="reference-number" value="" />
  <input type="submit" value="submit" />
</form>
<script type="text/javascript">
  var form       = document.querySelector('#my-form'),
      text_field = document.querySelector('#reference-number');

  function submitHandler(){
    // build the new url and open a new window
    var url = form.action +  text_field.value;
    window.open(url);

    // prevent form from being submitted because we already 
    // called the request in a new window
    return false;
  }

  // attach custom submit handler
  form.onsubmit = submitHandler;
</script>

</body>
</html>
>'''
    

    

if __name__ == '__main__':
    

    app.run(host='localhost', port=5000)
