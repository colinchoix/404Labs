#!/usr/bin/env python3
import cgi, cgitb, os

cgitb.enable()

print("Content-Type: text/html\n")
print()

print("""<style>
            table {
            font-family: arial, sans-serif;
            border-collapse: collapse;
            width: 100%;
            }
            td, th {
            border: 1px solid #dddddd;
            text-align: left;
            padding: 8px;
            }
        </style> """)

print("""<table style="width:100%">""")
print("<tr> <th> Variable </th><th> Value </th><tr>")

for x in os.environ:
    print("<tr> <th>",x,"</th><th>",os.environ[x],"</th><tr>")

print("</table>")
