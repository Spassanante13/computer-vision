# Players' Ball Possession Estimation During Football Matches

Questo progetto implementa un sistema di visione artificiale per la stima automatica del possesso palla, a livello individuale e di squadra, in ambito calcistico. Il sistema analizza filmati video di tipo broadcast per estrarre statistiche oggettive e scalabili.

## Indice
- [Obiettivi del Progetto](#obiettivi-del-progetto)
- [Architettura del Sistema](#architettura-del-sistema)
- [Tecnologie e Modelli](#tecnologie-e-modelli)
- [Metodologia e Raffinamento](#metodologia-e-raffinamento)
- [Risultati Sperimentali](#risultati-sperimentali)
- [Autori](#autori)

## Obiettivi del Progetto
L'analisi automatizzata del possesso palla mira a superare i limiti dell'annotazione manuale, soggetta a errori e tempi di esecuzione elevati. Le principali sfide affrontate riguardano:
* Tracking di oggetti di piccole dimensioni (palla) ad alta velocità.
* Gestione del motion blur e della risoluzione broadcast standard (~640px).
* Risoluzione di occlusioni frequenti tra i giocatori.
* Gestione di apparenze visive simili tra i componenti della stessa squadra.

## Architettura del Sistema
Il sistema è strutturato in una pipeline sequenziale:

1.  **Object Detection**: Localizzazione di palla, giocatori, portieri e arbitri.
2.  **Multi-Object Tracking (MOT)**: Associazione temporale delle rilevazioni per mantenere la continuità delle identità.
3.  **Re-Identification (ReID)**: Estrazione di descrittori visivi per il recupero dell'identità dopo lunghe occlusioni o uscite di campo.
4.  **Data Refinement**: Post-elaborazione tramite interpolazione dei dati mancanti e gestione dei conflitti di identificazione.
5.  **Possession Logic**: Calcolo dei tempi di possesso basato sull'intersezione spaziale tra le bounding box dei giocatori e della palla.

## Tecnologie e Modelli
* **Rilevamento**: YOLO11 (Ultralytics), ottimizzato tramite fine-tuning sul dataset SoccerNet.
* **Tracciamento**: BoT-SORT, che integra predizione del movimento e analisi dell'apparenza.
* **ReID**: OSNet (Omni-Scale Network) per l'estrazione di embedding robusti.
* **Dataset**: SoccerNet-Tracking 2022, basato su 12 partite della Swiss Super League.

## Metodologia e Raffinamento
Per migliorare l'accuratezza del sistema sono state integrate le seguenti componenti tecniche:
* **Algoritmo Ungarico**: Utilizzato per risolvere il problema dell'assegnazione ottimale tra i frame.
* **Swap Guard**: Meccanismo di sicurezza basato su soglie di confidenza degli embedding per prevenire lo scambio accidentale di ID tra giocatori vicini.
* **Interpolazione Lineare**: Applicata per stimare la posizione della palla nei frame in cui il rilevatore non fornisce output validi, garantendo continuità statistica.

## Risultati Sperimentali
Il sistema è stato valutato utilizzando metriche standard per il tracking multi-oggetto. Le performance sui soggetti umani (giocatori e arbitri) mostrano una Recall compresa tra il 97% e il 98%.

| Metrica | Risultato |
| :--- | :--- |
| Precision | 88.1% |
| Recall | 81.3% |
| MOTA | 63.0% |
| HOTA | 37.7% |

## Autori
Progetto realizzato per il corso di Computer Vision, A.A. 2025/2026, Sapienza Università di Roma.

* Davide Perniconi (1889270)
* Stefano Passanante (2158181)
* Robert Cristian Iacobus (1834884)