# keylogger

Ideja je u pythonu napraviti program koji će se pokrenuti u pozadini bez ikakvih lako vidljivih vizualnih
indikacija da je pokrenut. Program će detektirati koja je tipka na tipkovnici pritisnuta te ju spremiti u
tekstualni dokument koji je sakriven u nevidljivom folderu na c disku. Program će također detektirati
koji je trenutno aktivni prozor te ukoliko je trenutno aktivni prozor neki od internetskih preglednika
_(npr. brave, chrome, edge, opera, firefox)_, onda će pokušati i spremiti URL stranice na kojoj se nalazimo
tako da znamo na kojoj stranici je unošen koji tekst. Program će napraviti „task“ u „task scheduler-u“
_(hrv. Planer zadatka)_ koji će pokretati program prilikom pokretanja računala ukoliko task već nije
napravljen. Keylogger je namjenjen za pokretanje na windows 10 operacijskim sustavima. U donjoj tablici
detaljnije je opisan plan realizacije ovog projekta.

<table>
    <thead>
        <tr>
            <th>Klase</th>
            <th>Metode</th>
            <th>Opis metode</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=2>Inicijalizacija</td>
            <td>createTask</td>
            <td>Kreira task u task scheduleru koji pokreće program prilikom pokretanja računala sa
administratorskim privilegijama ukoliko to bude potrebno. Prije nego kreira task prvo pogleda je li
task već postoji da ne pravi duplikate ili da ne izbaci error</td>
        </tr>
        <tr>
            <td>moveFile</td>
            <td>Kreira sakriveni folder na c disku koji posjeduje system atribut tako da je mala šansa da
bude vidljiv čak i ukoliko je korisnik postavio da su mu vidljivi skriveni folderi osim ako nije posebno
postavio da budu vidljivi i „protected operating system files“
</td>

<tr>
            <td rowspan=3>Keylogger</td>
            <td>getActiveWindow</td>
            <td>dohvaća koji je trenutno aktivni prozor (prozor u kojem trenutno radimo, koji nije
u pozadini ili minimiziran / postavljen sa strane) i zapisuje naslov tog prozora (windowtitle) u tekstni
dokument u kojem dohvaćamo svaki „keypress“</td>
        </tr>
        
<tr>
            <td>keyPressed</td>
            <td>dohvaća i zapisuje u tekstni dokument svaki pritisnuti gumb na tipkovnici te ukoliko su
određeni „specijalni“ gumbovi pritisnuti (poput shift ili enter gumbova) onda će ovisno o gumbu
zabilježiti da je zapisano ili veliko slovo umjesto maloga ili specijalni simbol <i>(ukoliko se drži npr. shift
dok se upisuje)</i> ili će tekst preći u novi red <i>(ukoliko je pritisnuta tipka enter)</i> što nam ujedno i govori
gdje je kraj unesenog teksta.</td>
        </tr>
        
<tr>
            <td>websiteURL</td>
            <td>ukoliko getAvtiveWindow detektira da je trenutno aktivni prozor neki od internetskih
preglednika ova metoda će zabilježiti URL web stranice na kojoj se trenutno nalazimo i zapisati je u
tekstualni dokument.</td>
        </tr>

<tr>
            <td>Nuke</td>
            <td>panicDetected</td>
            <td>metoda koja služi kao neka vrsta obrane od pokušaja analiziranja ovog programa od
strane stručnjaka za sigurnost. Ukoliko detektira da je trenutna lokacija aktivnog prozora skrivena
datoteka u kojoj se nalazi ovaj program onda će se ugasiti i izbrisati sa te lokacije ukoliko je to
moguće.</td>
        </tr>
    </tbody>
</table>

# Projekt je završen

## Ovaj dio je naknadno napisan. Ovdje ću opisati kako keylogger funkcionira.
______________________________________________________________________________________

Keylogger se sastoji od više datoteka. Svaka odrađuje svoj dio posla, npr. _Inicijalizator.pyw_ kreira sve potrebno za 
skrivanje i nesmetani rad keyloggera. _task kreator.exe_ koristi se za kreiranje taskova u task scheduleru a da se pri
tome ne aktivira windows defender. _Keylogger.pyw_ je dokument koji zapravo dohvaća keypress i naslove prozora kako bi
ih spremio u tekstualnu datoteku. _sender.pyw_ iz tekstualne datoteke svakih sat vremena šalje inpute na firebase kako
bih imao pristup logovima sa drugih uređaja. _deleter - runas admin.bat_ je jednostavni batch file koji je pomagao prilikom
testiranja. On briše sve tragove koje keylogger ostavi, scheduled taskove i skrivene foldere.
![defender](https://github.com/user-attachments/assets/cb652a20-df1d-4531-ade6-95901718e7f1 "Windows defender mi je 153 puta blokirao skriptu od izvršavanja")
______________________________________________________________________________________

## Funkcionalnosti koje nisu dodane

Postoji jedna funkcionalnost koju nisam na kraju dodao, a to je _"PanicDetected"_ klasa koja bi brisala skriveni folder
ukoliko bi netko ušao u njega. S obzirom da sam stalno ulazio u njega kako bih testirao i debugirao program, odlučio
sam ne napraviti tu metodu.
______________________________________________________________________________________

## Način rada

### Unutar _Inicijalizator.pyw_ datoteke napravljena je klasa "Inicijalizacija" koja sadrži nekoliko metoda.

Prva metoda koja se poziva je _moveFile()_. U njoj se zadaje putanja do foldera kojega želimo napraviti. Provjerava
se postoji li već _"skriveni_folder"_ ili ne i ukoliko <b>ne postoji</b> kreira se pomoću _makedirs_ metode iz _os_ modula.
Nakon što se kreira, postavljaju mu se atributi "Hidden" i "System". Nakon izrade skrivenog foldera, privremeno se premješta
_Inicijalizator.pyw_ unutar njega.

Nakon nje poziva se _downloadKeylogger()_ metoda. U njoj se s ovog repozitorija preuzima _Keylogger.pyw_ te se
sprema u kreirani skriveni folder.

Slijedećih nekoliko metoda također preuzimaju potrebne datoteke iz ovoga repozitorija, tako da je za "distribuciju" keyloggera
potrebno preuzeti i pokrenuti samo jednu datoteku.

Nakon što su preuzete sve datoteke i postavljene u skriveni folder, poziva se metoda _createTask()_. Ona iskorištava sigurnosni
propust u "fodhelper.exe" programu zbog kojeg se može zaobići consent UAC prompt. Nažalost credentials UAC prompt nisam uspio
zaobići, stoga je svejedno potrebno imati administratorske privilegije na računalu, ali ukoliko ih korisnik ima, neće mu se 
prikazati UAC prompt.![UAC_consent](https://github.com/user-attachments/assets/5cc7f9d6-d6ae-4cb1-bcee-07efd32ce329 "Consent UAC prompt - samo pita želimo li ili ne dopustiti pokretanje")
![UAC_credentials](https://github.com/user-attachments/assets/41134f63-d653-4613-9cbf-cecfab333e68 "Credentials UAC prompt - zahtjeva unos administratorske lozinke i korisničkog imena")

Na samom kraju poziva se metoda _deleteInitializationFiled()_ koja briše _Inicijalizator.pyw_ i _task kreator.exe_ jer više nisu potrebni.



