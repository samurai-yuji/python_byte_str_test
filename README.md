### server_byte.py

```
$ python server_byte.py 
b'print("Hello, world!")\n'
<class 'bytes'>
simple.py
<_io.BufferedWriter name='server_directory/simple.py'>
b'print("Hello, world!")\n'
<class 'bytes'>
simple.py

$ python client_str.py 
<_io.TextIOWrapper name='simple.py' mode='r' encoding='UTF-8'>
$ python client_byte.py 
<_io.BufferedReader name='simple.py'>
```

### server_str.py

```
$ python server_str.py 
b'print("Hello, world!")\n'
<class 'bytes'>
simple.py
<_io.TextIOWrapper name='server_directory/simple.py' mode='w' encoding='UTF-8'>
ERROR:tornado.application:Uncaught exception POST /post/ (::1)
HTTPServerRequest(protocol='http', host='localhost:8888', method='POST', uri='/post/', version='HTTP/1.1', remote_ip='::1', headers={'Host': 'localhost:8888', 'User-Agent': 'python-requests/2.18.4', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Length': '175', 'Content-Type': 'multipart/form-data; boundary=ed68127b2e2044438e3b47ff403d9112'})
Traceback (most recent call last):
  File "/Users/xxxxx/.pyenv/versions/3.6.1/lib/python3.6/site-packages/tornado/web.py", line 1509, in _execute
    result = method(*self.path_args, **self.path_kwargs)
  File "server_str.py", line 14, in post
    f.write(program_content)
TypeError: write() argument must be str, not bytes
```

### server_byte_to_str.py

```
$ python server_byte_to_str.py 
b'print("Hello, world!")\n'
<class 'bytes'>
simple.py
<_io.TextIOWrapper name='server_directory/simple.py' mode='w' encoding='UTF-8'>
print("Hello, world!")

<class 'str'>
```
