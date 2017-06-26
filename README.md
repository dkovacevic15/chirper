# chirper

+ /admin - standardni django admin sistem
+ /api/users - podaci o korisnicima
+ api/users/[0-9]+ - podaci o korisniku sa pk-om iz URL
+ /api/posts - podaci o statusima
+ /api/posts/[0-9]+ - podaci o statusu sa pk-om iz URL
+ /api/auth - login sistem za api
+ /api/auth/token - zahtevi za JWT idu ovde


/api/posts prima zahteve za pravljenje postova, a slanje PUT requesta na api/posts/[neki broj] lajkuje ili odlajkuje taj post
od strane ulogovanog korisnika. Ovo je odvratna implementacija, ali je prilicno pogodna za testiranje kroz API. U realnoj
situaciji bih verovatno trazio unutar POST zahteva da li je toggleLiked=True ili slicno.

Ostavio sam standardni SessionAuthentication zbog lakseg testiranja.

Jedan od dostupnih naloga je korisnik sa username-om "dzoni" i passwordom "nidza123"
