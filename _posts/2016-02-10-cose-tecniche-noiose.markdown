---
layout: post
title:  "Cose tecniche noiose"
date:   2016-02-10 21:26:55 +0100
categories: nerderia
comments: true
---
Per prima cosa fatevi ringraziare: in tanti siete venuti a dare un'occhiata su questo sito e sembra che l'idea vi sia piaciuta molto.   
Non so dovremmo esserne felici oppure atterriti, ma abbiamo deciso in maniera non democratica di vedere solo il lato positivo.   
Vi rubo solo altre due righe per ringraziare due pagine Facebook in particolare:   
[Roba da Informatici](https://www.facebook.com/robadainformatici/) e [Generatore automatico di post di Salvini](https://www.facebook.com/gensav1/) per il gentilissimo feedback ricevuto.   
   
Questo post è dedicato ai tre o quattro nerd che si sono chiesti come sia possibile creare un linguaggio di programmazione come RusPython.   
Per cominciare, RusPython non è un fork di TrumScript, la logica è diversa e (non per vantarsi) RusPython ha anche qualche funzione in più.   
Detto questo, come tutti i compilatori/interpreti che ammorbano il mondo con la loro presenza, RusPython è composto da 2 elementi fondamentali.   
Il primo è il `lexer` che si occupa di analizzare i caratteri del codice sorgente ruspy e generare una lista di Token. 
Ad esempio quando il `lexer` si imbatte nel carattere `+`, lo etichetta come `PLUS` e continua a esaminare il resto del codice.   
Qando invece legge `Renzi` lo etichetta come `NAME`, `55` come `NUMBER` e così via.   
La seconda componente fondamentale è il `parser`. Il `parser` legge i token creati dal lexer e cerca di applicare una regola della grammatica generatrice del RusPython [che potete trovare qui](https://raw.githubusercontent.com/Eleirbag89/RusPython/master/Grammatica.txt).   
Potremmo parlare della grammatica per ore, ma giusto per fare una piccola introduzione, la grammatica definisce com'è fatto programma ruspy valido.   
Un `program` ad esempio è una lista di `statement` che termina con il token `PadaniaLibera`; uno `statement` può essere il token `ESPELLI` seguito da uno `statement`.   
Una volta capita quale regola applicare, il `parser` esegue il metodo associato alla regola e ritorna una stringa.   
La stringa finale ottenuta al termine del lavoro del parser è un normale listato in Python che posso, più o meno, far eseguire all'interprete Python così com'è.   
Più o meno perché ci sono alcuni aspetti (come i parametri di input in uno script) che devono essere aggiunti al volo.   
Per implementare `lexer` e `parser` ho usato una libreria chiamata [PLY](http://www.dabeaz.com/ply/) che mi ha snellito di molto il lavoro. L'alternativa è implementarvi il vostro `lexer` e `parser` casalingo come fa TrumScript. Qualunque sia la via del guerriero che sceglierete la struttura base rimane la stessa.   
Per il momento è tutto, se qualcuno è interessato all'argomento può contattarci e magari scriveremo qualche altro articolo più dettagliato sull'argomento.   
`PadaniaLibera` 
