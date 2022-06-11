# ProgettoAmod

## Organizzazione del progetto 

Problemi da analizzare
- Facility location capacitato
- Facility location non capacitato


Obiettivi
- Per entrambi i problemi si calcola la soluzione ottima e la si confronta con  2 lower  bound ottenuti con tecniche diverse e con una soluzione euristica ottenuta con l’algoritmo di ascesa duale.
- In più si vuole osservare quale è il più grande problema che riesce a risolvere in x minuti (da stabilire ancora) per ciascuna delle 8 versioni del problema(capacitato-pli , capacitato rilassato , capacitato-ascesa duale .. ecc)


I lower  bound sono  individuati con 
- rilassamento lineare
- rilassamento lagrangiano ( si provano più valori del moltiplicatore )
 
 
Il confronto tra le soluzione individuate con le varie tecniche riguarda
- Vicinanza alla soluzione ottima del pli ( errore relativo)
- tempi di esecuzione 


Per ogni istanza del problema:
si effettuano un certo numero di test con valori crescenti delle variabili decisionali  (ex da 100 a 1000 centri potenziali)
ad ogni esecuzione calcolo
- soluzione ottima
- lower bound 1
- lower bound 2
- soluzione dell'algoritmo di ascesa duale


Grafici da creare
- creo grafico in cui mostro come variano le soluzioni al variare delle dimensioni.
- creo grafico in cui mostro come variano gli errori relativi al variare delle dimensioni.
- creo grafico in cui mostro come tempi di esecuzione variano al variare delle dimensioni. 
- Creo grafico in cui mostro come rapporto tra tempo di esecuzione e dimensione varia al variare delle dimensioni ( all’aumento dei run di esecuzione)
- mettere a confronto grafici della soluzione capacitata con quella non capacitata
- grafico che confronta tempi e dimensioni del problema in x minuti di esecuzione(da stabilire)


## Parte implementativa
Verrà utilizzato python sfruttando l’API offerta da Gurobi.

Classi da creare

- Classe che modella problema di facility location capacitato
il costruttore riceve come parametri vettori contenenti il costo di setup, e allocazione(trasporto) , la domanda e la capacità dei centri
metodo che restituisce vincoli del problema


- Classe che modella problema di facility location capacitato
il costruttore riceve come parametri vettori contenenti il costo di setup, e allocazione(trasporto) 
metodo che restituisce vincoli del problema


- classe Solver che prevede una serie di metodi che restituiscono : tempo di esecuzione e soluzione ottima (o bound). I metodi sono: 
costruttore che riceve in ingresso la classe che modella il problema
1. metodo per calcolare soluzione ottima
2. metodo per calcolare lower  bound 1
3. metodo per calcolare lower  bound 2
4. metodo che implementa l’ascesa duale


- classe ParamGenerator che prevede una serie di metodi che accettano in ingresso la dimensione della lista che devono generare
1. metodo per generare la lista dei parametri dei costi di setup
2. metodo per generare la lista dei parametri dei costi di allocazione
3. metodo per generare la lista dei parametri della domanda dei clienti
4. metodo per generare la lista dei parametri della capacità dei centri 


## Informazioni utili
La classe ParamGenerator avrà al suo interno un generatore di numeri pseudo random. Con questo approccio si vuole effettuare un'analisi statistica generando più istanze dello stesso problema con la stessa dimensione. Quindi i valori che verranno mostrati nei grafici non saranno valori assoluti ottenuti dalla soluzione di una singola istanza del problema, ma da una media di soluzioni. Il generatore utilizzato sarà multi-stream garantendo in questo modo le condizioni di indipendenza.
