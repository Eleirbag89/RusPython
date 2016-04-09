---
layout: post
title:  "Come nasce un programma Ruspython"
date:   2016-04-09 08:15:55 +0100
categories: codice nerderia
comments: true
---
Sono stato abbastanza occupato in questi mesi e purtroppo lo sviluppo di RusPython ne ha un pò risentito.    
Da un bel pò volevo scrivere un post su quale sia l'iter che usiamo per scrivere dei programmi. Ci sono due macro-approcci al problema: scrivere un programma perché è divertente (come Matrimonio.ruspy) oppure approfittarne per estendere e testare nuove funzionalità dell'interprete Ruspython.    
Spesso però la linea di demarcazione non è così netta. Oggi infatti ho realizzato il programma `99 bottiglie.ruspy` che stampa sullo schermo la versione italiana della canzone [99 bottles of beer](http://www.99-bottles-of-beer.net/lyrics.html), uno degli esempi più classici usati per insegnare ai nabbi costrutti come i cicli while e for.   
Per prima cosa ho appuntato su un foglietto di carta un pò di pseudocodice:    
`for (int i=99; i>0;i--) {    
	print i "bottiglie di birra sul muro, "+i bottiglie`    
Ma mi sono stufato subito data la poca espressività dello pseudocodice, perciò ho deciso di realizzarlo direttamente in RusPython.   
Durante lo sviluppo però mi sono accorto di due problemi:

- Il primo è che c'era un bug nell'istruzione `finche` che non accettava l'operatore `maggiore`, che ho dovuto fixare (` maggiore ` doveva essere `maggiore`)    
- Non era possibile usare URLA per concatenare numeri e stringhe, quindi non potevo urla n+"bottiglie" senza che Python si lamentasse per la sua incapacità di concatenare numeri e stringhe.   

Per il secondo punto ho dovuto modificare il costrutto `urla` per permettergli di accettare diverse espressioni separate dalla congiunzione `e`.   
Il parser poi si occupa di inserire `str()` intorno ad ogni valore e finalmente tutto è andato per il meglio,   
Prima di poter continuare a lavorare sul mio codice ho riprovato tutti gli esempi già esistenti per essere certo che queste nuove modifiche non avessero distrutto qualche codice funzionante. Fortunatamente tutto è andato per il verso giusto e sono riuscito a terminare la versione definitiva di 99 bottiglie:    

`stranieri è 99`    
`padani è 1`    
`italiani è -1`    
`bottiglia è " bottiglia di birra"`    
`bottiglie è " bottiglie di birra"`    
`ruspa è " sul muro, "`    
`degrado è "."`    
`rom è "nessuna"`    
`albanesi è "Nessuna"`    
`zingari è "Prendine una, falla girare, "`    
`degrado della societa è "Vai al negozio comprane altre, 99 bottiglie di birra sul muro."`    
`cittadinanza è 0`    
`ottanta euro è 0`    
`finche stranieri maggiore italiani;`     
`stranieri maggiore padani? urla stranieri e bottiglie e ruspa e stranieri e bottiglie e degrado altrimenti`    
`stranieri è padani? urla stranieri e bottiglia e ruspa e stranieri e bottiglia e degrado.`    
`stranieri è 0? urla albanesi e bottiglia e ruspa e rom e bottiglia e degrado..`    
`stranieri è stranieri -1 stranieri maggiore ottanta euro?`    
`urla zingari e stranieri e bottiglie e ruspa altrimenti	stranieri è cittadinanza?`     
`urla zingari e rom e bottiglia e ruspa.`    
`stranieri è italiani?`    
`urla degrado della societa...`    
`PadaniaLibera`   


