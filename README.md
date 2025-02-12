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

Ovaj dio je naknadno napisan. Ovdje ću opisati kako keylogger funkcionira.
______________________________________________________________________________________

Keylogger se sastoji od više datoteka. Svaka odrađuje svoj dio posla, npr. _Inicijalizator.pyw_ kreira sve potrebno za 
skrivanje i nesmetani rad keyloggera. _task kreator.exe_ koristi se za kreiranje taskova u task scheduleru a da se pri
tome ne aktivira windows defender. (Ne)zanimljiva činjenica je to da mi je prilikom testiranja windows defender 153 puta
blokirao izvršavanja skripte dok nisam shvatio da ne smijem koristiti cmd ili powershell prilikom iskorištavanja exploita.
            ![defender](https://github.com/user-attachments/assets/cb652a20-df1d-4531-ade6-95901718e7f1)



