#!/usr/bin/env python3


 
import os
import sys

arguments = sys.argv[1:]
if not arguments:
    print("informe o nome do arquivo de emails")
    sys.exit(1)

filename = arguments[0]
templatename = arguments[1]


path= os.curdir
filepath = os.path.join(path, filename) # emails.txt
templatepath = os.path.join(path, templatename) # email_tmpl.txt

for line in open(filepath):
    name, email = line.split(",") 

    print(f"enviando email para : {email}")
    print(
         open(templatepath).read() 
         % {
             "nome": name, 
             "produto": "caneta", 
             "texto": "Escrever muito bem", 
             "link": "https://meusite.com", 
             "quantidade": 5, 
             "preco": 50.5,
            }
        )
    print("-" * 50)
