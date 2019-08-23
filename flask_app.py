from flask import Flask                                 #api for flask
from flask import request
from flask_limiter import Limiter 
from flask_limiter.util import get_remote_address
import psycopg2                                         #api for connecting with POSTGRESQL
from views import Download, DownloadStatus              #importing the python script having required classes
import json                                             #api to import json

app = Flask(__name__)
limiter= Limiter(                                       #initializing for rate limits
        app,
        key_func=get_remote_address),
       default_limits=["200 per day","50 per hour"])

#The following funtion to download the file from given url
#It take the url from the form in html  through POST method, assigns the unique id and enters it into database

@app.route('/download')                                 
def user_download():
    url = request.args['url']           # getting the url  
    conn = psycopg2.connect(database="downloads", user = "postgres", password = "amn", host = "127.0.0.1", port = "5432")
    cur=conn.cursor()                  # connecting to database
    cur.execute("select count(*) from download_datas")
    rows=cur.fetchone()                # getting the number of rows already in database so that unique_id can be generated accordingly
    u_id=rows[0]+1
    query = '''insert into download_datas (uid) values (%s)'''
    cur.execute (query, str(u_id))     #inserting the id into the database
    conn.commit()
    conn.close()
    msg = f"your file is downloading!!!!!!!!!!! and file url is : {url}"
    #u_id = 2
    index()                                                                     #check
    download_obj = Download(u_id, url)  
    download_obj.downloads()
    return msg

#function to display the status of download
@app.route('/status')
def download_status():
    u_id = request.args['id']        #getting the id of the download from the url, sent using get method
    status_obj = DownloadStatus(u_id)   
    status_dict = status_obj.status()    #initializing and calling the status() to get the status of the download of given id
    total={status_dict['finished']}+{status_dict['remaining']}   #calculating the total size of the file
    msg = f"total finished = {status_dict['finished']} bytes and remaining = {status_dict['remaining']} bytes and total={total}"   #displaying the message
     msg1=   ''' <!DOCTYPE html>
<html>
<body>

  <form action="localhost:5000/download_file?id={u_id}" method="get" target="_blank" id="my-form">
  total finished = {status_dict['finished']} bytes and remaining = {status_dict['remaining']} bytes and total={total}
  <input type="submit" value="refresh" />
</form>
<script type="text/javascript">
  var form       = document.querySelector('#my-form'),
      

  function submitHandler(){
    // build the new url and open a new window
    var url = form.action
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
    return msg







@app.route('/index')
def index():
    conn = psycopg2.connect(database="downloads", user = "postgres", password = "amn", host = "127.0.0.1", port = "5432")
    cur=conn.cursor()
    
    # its better to insert into database and then have that id as unique id
    #cur=conn.cursor()
    cur.execute("select count(*) from download_datas")
    rows=cur.fetchone()
  #check sampledatabase  
     #html to take the url and to show the status
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
    

    

if __name__ == '__main__':  #main function
    

    app.run(host='localhost', port=5000)
