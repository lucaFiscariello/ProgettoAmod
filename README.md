# ProgettoAmod

## Organizzazione del progetto 

Problemi da analizzare
- Facility location capacitato
- Facility location non capacitato


Obiettivi
- Per entrambi i problemi si calcola la soluzione ottima e la si confronta con  3 lower  bound ottenuti con tecniche diverse;
- implementare algoritmo di ascesa duale;



I lower  bound sono  individuati con 
- rilassamento lineare
- rilassamento lagrangiano ( si provano più valori del moltiplicatore )
- algoritmo di ascesa duale
 
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


Grafici creati
- grafico in cui mostro come variano le soluzioni al variare delle dimensioni.
- grafico in cui mostro come variano gli errori relativi al variare delle dimensioni.
- grafico in cui mostro come tempi di esecuzione variano al variare delle dimensioni. 
- grafico in cui mostro come rapporto tra tempo di esecuzione e dimensione varia al variare delle dimensioni ( all’aumento dei run di esecuzione)
- Boxplot



## Parte implementativa
Il progetto verrà implementato in python sfruttando l’API offerta da Gurobi.

Classi create piu significative:

- Classe che modella problema di facility location capacitato

- Classe che modella problema di facility location non capacitato

- Classe Solver che prevede una serie di metodi:
  1. metodo per calcolare soluzione ottima
  2. metodo per calcolare lower  bound 1
  3. metodo per calcolare lower  bound 2
  4. metodo che implementa l’ascesa duale


- Classe ParamGenerator che prevede una serie di metodi che accettano in ingresso la dimensione della lista che devono generare:
  1. metodo per generare la lista dei parametri dei costi di setup
  2. metodo per generare la lista dei parametri dei costi di allocazione
  3. metodo per generare la lista dei parametri della domanda dei clienti
  4. metodo per generare la lista dei parametri della capacità dei centri 


## Informazioni utili
La classe ParamGenerator avrà al suo interno un generatore di numeri pseudo random. Con questo approccio si vuole effettuare un'analisi statistica generando più istanze dello stesso problema con la stessa dimensione. Quindi i valori che verranno mostrati nei grafici non saranno valori assoluti ottenuti dalla soluzione di una singola istanza del problema, ma da una media di soluzioni. Il generatore utilizzato sarà multi-stream garantendo in questo modo le condizioni di indipendenza.
