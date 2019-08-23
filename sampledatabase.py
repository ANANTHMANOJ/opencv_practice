import psycopg2

conn = psycopg2.connect(database="downloads", user = "postgres", password = "amn", host = "127.0.0.1", port = "5432")
cur=conn.cursor()
cur.execute("select count(*) from download_datas")
rows=cur.fetchone()
print(rows[0])
print ("Opened database successfully")


msg1=''' <!DOCTYPE html>
<html>
<body>

  <form action="localhost:5000/download_file?url=" method="post" target="_blank" id="my-form">
  <input type="text" name="reference-number" id="reference-number" value="" />
  <input type="submit" value="submit" />
</form>'''

msg3='''

   <h3>There are {row[0]} dwonloads. Please enter the id (serial number) to view the status</h3>
  <form action="localhost:5000/download_file?id=" method="post" target="_blank" id="my-form">
  <input type="text" name="reference-number" id="reference-number" value="" />
  <input type="submit" value="submit" />
</form>'''#.foramt(row[0])

msg3='''
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
if row[0] ==0:
  return msg1+msg3
else:
  return msg1+msg2+msg3
