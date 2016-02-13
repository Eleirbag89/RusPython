# RusPython <img src="https://raw.githubusercontent.com/Eleirbag89/RusPython/master/RusPython_logo.png" />
Perché per Python ci vuole la RUSPA!!!

## Missione
RusPython è un linguaggio di programmazione ispirato dall'illustre Matteo Salvini.   
Crediamo fermamente che l'attuale stato dell'arte dei moderni linguaggi di programmazione non sia in grado di ricreare la sua magnificenza espressiva e contenutistica.   
Se anche tu condividi la nostra visione, RusPython è il linguaggio che fa per te!   
Spero che mentre Matteo riuscirà nella sua impresa di liberare la Padania da Roma ladrona, noi, nel nostro piccolo, libereremo il mondo dell'informatica dagli altri inutili, se non dannosi, linguaggi di programmazione.

## Installazione
RusPython è progettato per funzionare su Python 2.7.   
Per usarlo scarica ed estrai il file .zip  oppure clona il repository digitando

```bash
git clone https://github.com/Eleirbag89/RusPython.git
```

Aggiungi la cartella di RusPython al `PATH` usando uno dei due comandi seguenti (su Linux)

1. Temporaneo: Scrivi `export PATH=$PATH:/path/to/RusPython` nel terminale.
2. Permanente: Aggiungi `export PATH=$PATH:/path/to/RusPython` alla fine del tuo file `~/.bashrc`.

## Utilizzo
* Scrivi un file ruspy usando l'opportuna sintassi (in bocca al lupo).
* Esegui `RusPython /path/to/ruspy/file [parametri_input_script]`
* Benvenuto nel magico mondo di RusPython!

## Funzionalità
RusPython include diverse funzionalità perfette per ogni aspirante leader della Lega Nord:
* Non ci sono istruzioni per effettuare gli import. Non vogliamo che codice straniero ci rubi il lavoro.
* Tutti i programmi devono terminare con `PadaniaLibera`.
* Il linguaggio è insensibile alle minuscole/maiuscole. Anzi, è insensibile punto.
* È il primo linguaggio di programmazione ad usare le closure mentali.
* Il linguaggio è Turing Completo. A noi Padani non manca mai nulla.
* `Italia` viene sostituito automaticamente con il più appropriato `Roma Ladrona`
* Non esiste un equivalente del not. RusPython è il linguaggio del fare, non come gli altri linguaggi disfattisti.

## Grammatica
La grammatica del linguaggio è un pò complessa, ma solo attraverso un accurato studio delle arti retoriche è possibile rendere messaggi complessi diregiribili per l'uomo comune.   
Ecco un assaggio di cosa sarai in grado di fare

Operatori Aritmetici:
* `+` fa la somma
* `-` fa la sottrazione
* `*` fa la moltiplicazione
* `/` fa la divisione
* `minore` indica `più piccolo di`
* `maggiore` indica `più grande di`

Variabili:
* Puoi usare tutti gli spazi che vuoi per il nome delle tue variabili
* Usa `,` se devi differenziare due variabili consecutive
* Puoi effettuare un assegnamento così: `variabile è espressione` oppure `variabile sono espressione`
* Le stringhe sono racchiuse da doppi apici `"Stringa"`   
* Puoi generare un numero casuale in un intervallo con `scegliete variabile fra espressione e espressione`

Liste
* Creare una lista vuota: `raderemo al suolo variabile`
* Aggiungere un elemento alla lista: `nella variabile deporta indice`.   
Se vuoi anche specificare la posizione usa
`nella variabile deporta espressione nella cella indice`
* Leggere un elemento dalla lista: `dalla variabile sgombera indice`
* Ottenere la lunghezza della lista: `la dimensione di variabile`

Controllo del flusso
* Per creare un costrutto IF: `variabile è/sono espressione ? istruzioni [ALTRIMENTI istruzioni].` Oppure usa `minore` o `maggiore`
* Per creare un ciclo WHILE: `finche variabile OPERATORE espressioni; istruzioni.`
* Ciclare i valori di una lista: `per ogni variabile in variabile; istruzioni.`

Funzioni
* Definire una funzione usando: `attenzione variabile ! parametro [e parametro...] tornino a casa loro istruzioni basta`
* Richiamare una funzione usando: `ricordate variabile ! parametro [e parametro...] a casa loro`
* Far ritornare un valore ad una funzione: `espelli valore`

Input/Output
* Stampare sullo schermo; `urla espressione`   
* Leggere un valore numerico inserito dall'utente nel terminale `ditemi variabile cosa volete`
* I parametri passati allo script possono essere ottenuti in due modi:   
* Usando la lista `frontiera`   
* Usando la variabile `bingo bongo` per il primo parametro `bingo bongo bongo` per il secondo, `bingo bongo bongo bingo` per il terzo, `bingo bongo bongo bingo bongo bingo bongo bingo bongo` per l'ottavo e così via.   

Infine:   
A noi Padani non piace parlare dei propri errori, per cui molte volte il codice fallirà senza segnalare nulla.   
Pensate al debug come a un piccolo gioco fra di noi.

## Esempi
`Attenzione padani ! Gli Africani tornino a casa loro`   
`milioni sono 0 tutti sono 1`   
`gli Africani sono milioni? Espellili tutti.`    
`espelli gli Africani * Ricordate padani! Gli Africani-Tutti a casa loro`    
`Basta`   
`Urla ricordate padani! Bingo bongo a casa loro`   
`PadaniaLibera`   
Questo codice definisce una funzione chiamata "padani" che calcola il fattoriale in maniera ricorsiva.   

Di seguito la lista con tutti gli script creati fino ad ora e come utilizzarli
* Fattoriale: Calcola il fattoriale di un numero in input.   
Fattoriale di 5: `RusPython examples/Fattoriale.ruspy 5`
* Fibonacci: Calcola i primi n valori della sequenza di Fibonacci in base al numero in input.   
Primi 8: `RusPython examples/Fibonacci.ruspy 8`
* Hello world: Semplice programma di esempio.   
Lancialo con `RusPython examples/Hello_World.ruspy`
* Or(d)inamento: Ordina la sequenza in input.   
Esempio `RusPython examples/Ordinamento.ruspy 75 5 1 9 104 32`
* ParamList: stampa sullo schermo tutti i parametri in input.   
Esempio `RusPython examples/ParamList.ruspy 5 Borghezio 3.14`
* RitualeDelPo: gioca a indovinare il numero magico per ultimare il rituale.   
Esempio `RusPython examples/RitualeDelPo.ruspy`
* Matrimonio: Controlla se due parametri di input possono sposarsi.   
Esempio `RusPython examples/Matrimonio.ruspy 5 5`

## Attivati
Sentiti libero di contribuire al progetto con commit, idee, suggerimenti.   
Puoi creare fork e spinoff senza chiedere il permesso a nessuno (ok, però magari un piccolo link mettilo).   
Puoi contribuire anche scrivendo del codice RusPython e arricchendo la nostra galleria di esempi.

## Siccome in fondo siamo delle brave persone
Se questa pagina ti ha divertito, rifletti sulla possibilità di fare una donazione ad un ente benefico impegnato nell'aiuto di rifugiati e profughi.   
Se sei più sul lato hacktivist, potresti donare qualcosa al collettivo [Autistici/Inventati](http://www.autistici.org/it/donate.html)    
Inoltre puoi fare una donazione ai ragazzi dietro [TrumScript](https://github.com/samshadwell/TrumpScript), il progetto che ha ispirato tutto questo: [Shadwell](https://paypal.me/Shadwell).

## Siccome siamo al verde
Puoi offrirci una birra o due usando [Paypal](https://paypal.me/eleirbag89)    
Oppure puoi flattrarci   
[![Flattr this git repo](http://api.flattr.com/button/flattr-badge-large.png)](https://flattr.com/submit/auto?user_id=eleirbag89&url=https://github.com/Eleirbag89/RusPython&title=RusPython&language=it&tags=github&category=software) 
