# PYTHON API'S

## *TASK 0 - Basics of HTTP/HTTPS*

1 : Write a brief summary explaining the differences between HTTP and HTTPS.

=> HTTP is a protocol for fetching resources such as HTML documents.
The main difference with HTTPS is that this one is using an encrypted and secured way (called SSL) of HTTP calls for both request and response.
HTTPS is a more secure protocol because both response and resquest are encrypted. Nothing is encrypted with the original HTTP protocol


2 : A depiction or outline of the structure of an HTTP request and response.

**EXAMPLE**

<br>

=> Request: 
GET /api/users HTTP/1.1 --/ *This is a request to an API with "GET" method*
<br>
Host: example.com
<br>
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
<br>
Accept: application/json
<br>
Authorization: Bearer abcdef123456

**RESPONSE**

<br>

HTTP/1.1 200 OK --/ *status 200, request has been successful*
<br>
Content-Type: application/json
<br>
Content-Length: 85
<br>
Date: Mon, 29 Jun 2024 12:28:53 GMT
<br>

{<br>
  "id": 1,<br>
  "name": "John Doe",<br>
  "email": "john.doe@example.com"<br>
}

3 : Lists the common HTTP methods and status codes with their descriptions and possible use cases.

* **METHODS** :
<br>
=> *GET*: to make a request to a server and waiting for a response
<br>
=> *POST*: to post some content to a server
<br>
=> *PUT*: update a content to a server
<br>
=> *DELETE*: to delete content on a server

* **STATUS CODES**
<br>
* 1xx informational response : the request was received, continuing process
<br>
*Exemple*: code 101 => Switching Protocols, The requester has asked the server to switch protocols and the server has agreed to do so.<br><br>
2xx successful – the request was successfully received, understood, and accepted <br>
*Exemple*: code 200 => OK, Standard response for successful HTTP requests
<br><br>
3xx redirection – further action needs to be taken in order to complete the request <br>
*Exemple*: code 306 => Switch Proxy, No longer used. Originally meant "Subsequent requests should use the specified proxy."
<br><br>
4xx client error – the request contains bad syntax or cannot be fulfilled<br>
*Exemple*: code 404 => Not Found, The requested resource could not be found but may be available in the future <br><br>
5xx server error – the server failed to fulfil an apparently valid request<br>
*Exemple*: code 500 => Internal Server Error, A generic error message, given when an unexpected condition was encountered and no more specific message is suitable.

<br><br>

## *TASK 1 - Consume data from an API using command line tools (curl)*
1: Upon running curl --version, you should see details about your installed version of curl, including supported protocols.<br><br>
<br> **COMMAND ENTERERED**: curl --version <br><br>
=> *Result in the terminal*:<br>
curl 7.81.0 (aarch64-unknown-linux-gnu) libcurl/7.81.0 OpenSSL/3.0.2 zlib/1.2.11 brotli/1.0.9 zstd/1.4.8 libidn2/2.3.2 libpsl/0.21.0 (+libidn2/2.3.2) libssh/0.9.6/openssl/zlib nghttp2/1.43.0 librtmp/2.3 OpenLDAP/2.5.16 <br>
Release-Date: 2022-01-05 <br>
Protocols: dict file ftp ftps gopher gophers http https imap imaps ldap ldaps mqtt pop3 pop3s rtmp rtsp scp sftp smb smbs smtp smtps telnet tftp<br>
Features: alt-svc AsynchDNS brotli GSS-API HSTS HTTP2 HTTPS-proxy IDN IPv6 Kerberos Largefile libz NTLM NTLM_WB PSL SPNEGO SSL TLS-SRP UnixSockets zstd
<br><br>
2: Fetching posts from JSONPlaceholder should provide a JSON output of various posts, each having attributes like userId, id, title, and body.<br><br>
<br> **COMMAND ENTERERED**: curl https://jsonplaceholder.typicode.com/posts <br><br>
=> *Result in the terminal*:<br>
[<br>{
    "userId": 1, <br>
    "id": 1, <br>
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit", <br>
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"<br>
  }<br>
  ...<br>
]
<br><br>
3: Fetching only headers should give a concise output showing status codes and headers without the actual content.
<br><br>
<br> **COMMAND ENTERERED**: curl -I https://jsonplaceholder.typicode.com/posts
<br><br>
=> *Result in the terminal*:<br>
HTTP/2 200<br>
date: Thu, 30 May 2024 12:33:57 GMT<br>
content-type: application/json; charset=utf-8<br>
...<br>
age: 14455<br>
server: cloudflare<br>
cf-ray: 88bec16e6afe3704-YYZ<br>
alt-svc: h3=":443"; ma=86400<br><br>

4 : Making a POST request should yield a response from the server acknowledging the reception of the data. For JSONPlaceholder, it typically returns the created post with an id of 101 (since it doesn’t actually save the new post, but simulates the creation).
<br><br>
<br> **COMMAND ENTERERED**: curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
<br><br>
=> *Result in the terminal*:<br>
{<br>
  "title": "foo",<br>
  "body": "bar",<br>
  "userId": "1",<br>
  "id": 101<br>
}