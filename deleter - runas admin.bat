taskkill /f /im pythonw.exe
taskkill /f /im pyw.exe
rmdir /s /q "C:\skriveni_folder"
schtasks /delete /f /tn "KeyloggerTask"
schtasks /delete /f /tn "KeylogSender"