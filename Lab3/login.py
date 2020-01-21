#!/usr/bin/env python3
import cgi, cgitb, os, secret
from templates import login_page, secret_page, after_login_incorrect
from http.cookies import SimpleCookie

cgitb.enable()

s = cgi.FieldStorage()
username = s.getfirst("username")
password = s.getfirst("password")

print("Content-Type: text/html")
formOK = username == secret.username and password == secret.password

c = SimpleCookie(os.environ["HTTP_COOKIE"])
c_username = None
c_password = None

if c.get("username"):
    c_username = c.get("username").value
if c.get("password"):
    c_password = c.get("password").value

cookieOK = c_username == secret.username and c_password == secret.password
if (cookieOK):
    username = c_username
    password = c_password


if (formOK):
    print("Set-Cookie: username=",username)
    print("Set-Cookie: password=",password)

print()

if (not username and not password):
    print(login_page())
elif (username == secret.username and password == secret.password ):
    print(secret_page(username, password))
else: 
    print(after_login_incorrect())

