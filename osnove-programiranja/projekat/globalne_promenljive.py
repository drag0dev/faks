ulogovanKorisnik = {} # trenutni ulogovani korisnik
korisnici = {} # svi korisnici
apartmani = {} # svi apartmani (dosutpnost predstavlja sta je domacin postavio bez uticaja sta je rezervisano ili ne)
dodatna_oprema = {} # sva dodatna oprema
rezervacije = {} # sve rezervacije
uloge = ['DOMACIN', 'ADMIN', 'GOST'] # uloge korisnika
status_rezervacije = ['KREIRANA', 'ODBIJENA', 'PRIHVACENA', 'ZAVRSENA', 'ODUSTANAK'] # statusi rezervacije
status_apartmana = ['AKTIVNO', 'NEAKTIVNO'] # statusi apartmana
broj_rezervacija = 0 # pracenje broja rezervacija u ovoj sesiji radi 5% popusta
neradni_dani = [] # dani i opsezi dana kada je neradno