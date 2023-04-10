#!/usr/bin/lua

req = require('requests')
sess = req.Session()

Mino_sql = function() --TODO: (1)Login with obtained creds (2)Post sql query (3)fetch hashes   
  Url = 'http://10.10.184.38/index.php'
  post = sess.post{Url, {data="'email': 'M!n0taur', 'password': 'aminotauro'"}}
  print(post.text)

end
Mino_sql()
