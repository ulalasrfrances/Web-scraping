from urllib.request import urlopen
import re

url = "http://olympus.realpython.org/profiles/poseidon"
page = urlopen(url)
#print(page)
html_bytes = page.read()
#print(type(html_bytes))
html= html_bytes.decode("utf-8")
#print(html)
#print(type(html))
#print(len(html))
title_index = html.find("<title>")
#print(title_index)
index_inicio = title_index+len("<title>")
index_final = html.find("</title>")

title= html[index_inicio:index_final]
#print(title)

#Usamos expresiones regulares

print(re.findall("ab*c","ac"))
