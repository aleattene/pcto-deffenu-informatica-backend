## SM - Sport Management

<hr>

**Anno Scolastico**: 2024/2025

**Studente**: Attene Davide

**Istituto Scolastico**: I.T.T. "Attilio Deffenu" - Olbia

<hr>

![Python](https://badgen.net/badge/Built%20with/Python/blue)
![Django](https://img.shields.io/badge/Built%20with-Django-092E20)
![Django Rest Framework](https://img.shields.io/badge/Built%20with-DRF-red)
[![Tests](https://github.com/aleattene/pcto-deffenu-informatica-backend/actions/workflows/tests_api.yml/badge.svg)](https://github.com/aleattene/pcto-deffenu-informatica-backend/actions/workflows/tests_api.yml)
[![codecov](https://codecov.io/gh/aleattene/pcto-deffenu-informatica-backend/graph/badge.svg?token=N1AMPIX1XF)](https://codecov.io/gh/aleattene/pcto-deffenu-informatica-backend)
[![GitHub commits](https://badgen.net/github/commits/aleattene/pcto-deffenu-informatica-backend)](https://github.com/aleattene/pcto-deffenu-informatica-backend/commits/)
[![GitHub last commit](https://img.shields.io/github/last-commit/aleattene/pcto-deffenu-informatica-backend)](https://github.com/aleattene/pcto-deffenu-informatica-backend/commits/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/aleattene/pcto-deffenu-informatica-backend/pulls)
[![License](https://img.shields.io/github/license/aleattene/pcto-deffenu-informatica-backend?color=blue)](https://github.com/aleattene/pcto-deffenu-informatica-backend/blob/main/LICENSE)
<br>
<br>

## Descrizione

Il progetto **SM - Sport Management** mira alla realizzazione di una **Web App Responsive** per un'associazione sportiva.

Le attività da svolgere e i task assegnati fanno riferimento al **progetto** [PCTO - Deffenu Informatica 2024/2025 ](https://github.com/users/aleattene/projects/3/)

Le principali funzionalità implementate includono:
- Gestione **anagrafiche** (atleti, allenatori, medici sportivi)
- Gestione **documentale** (certificazioni medico sportive)
- Gestione **pagamenti** (compensi allenatori)

Documentazione API disponibili al seguente link: <br>
https://pcto-deffenu.vercel.app/api/swagger/
<br><br>
  
## Struttura Progetto

Di seguito una breve descrizione della struttura del progetto:

| **Cartella/File** | **Descrizione** |
|--|--|
| `manage.py` | Script di gestione del progetto Django. |
| `requirements.txt` | Elenco delle dipendenze Python del progetto. |
| `README.md` | Documentazione e linee guida del progetto. |

<br>

## Avvio del Progetto

**Clonare il Repository**
```bash
git clone https://github.com/username/pcto-deffenu-informatica-backend.git
cd pcto-deffenu-informatica-backend
````

**Creare il file `.env.local` nella root del progetto con le seguenti Variabili d'ambiente:**
```bash
# Development
SECRET_KEY=your-django-secret-key
DEBUG=True
ENVIRONMENT=development
```

**Creare un ambiente virtuale ed attivarlo**
```bash
python -m venv nome_ambiente_virtuale
source nome_ambiente/bin/activate		# Linux/Mac
nome_ambiente\Scripts\activate			# Windows
```

**Installare le Dipendenze**
```bash
pip install -r requirements.txt
```

**Effettuare le Migrazioni**
```bash
python manage.py migrate
```

**Avviare il Server di Sviluppo**
```bash
python manage.py runserver
```
<br>


## API disponibili
Le API sono documentate in modo interattivo con Swagger. Una volta avviato il server, puoi accedere alla documentazione all'indirizzo:
http://localhost:8000/api/swagger/

<br>


## Contribuzione

Trattandosi di un progetto open-source è **aperto anche a contribuzioni esterne**. Se qualcuno fosse interessato, dopo aver creato una **issue** nel presente repository, può **attendere l'assegnazione del task** ed eventualmente procedere poi con l'implementazione di quanto approvato.

Per prima cosa effettuare il **fork del repository** e clonarlo localmente con il seguente comando:

```bash
# HTTPS
git clone https://github.com/username/pcto-deffenu-informatica-backend.git
```
oppure

```bash
SSH
git clone git@github.com:username/pcto-deffenu-informatica-backend.git
```

Questo comando genererà una folder/directory con lo stesso nome del repository, all'interno del quale spostarsi con il comando:

```bash
cd pcto-deffenu-informatica-backend
```

Avviare quindi il proprio IDE per visualizzare la **codebase** del progetto. Per contribuire creare immediatamente un **nuovo branch** partendo dal 'main' (branch principale) con il comando:

```bash
git checkout -b username-feature-da-implementare
```

A questo punto ci si troverà posizionati direttamente nel nuovo branch e sarà pertanto possibile **apportare** tutte le **modifiche** o nuove **feature** desiderate. Nel momento in cui si vuole far si che queste possano entrare a far parte della codebase principale, procedere nel seguente modo:

```bash
# Usare iterativamente lo stesso comando per tutti i file modificati
git add nome-file-modificato
```
 
E' anche possibile adottare un comando che ne permette l'aggiunta automatica di tutti i file, ma bisogna prestare maggiore attenzione in quanto saranno aggiunti all'area di staging tutti i file, inclusi magari quelli che non dovrebbero. Il comando è il seguente:
```bash
# Prestare la massima attenzione
git add .
```
Successivamente è quindi possibile effettuare il **commit** dei file con il seguente comando:

```bash
git commit -m "messaggio-di-commit"
```

ed infine **inviare** il tutto al proprio **repository remoto** (di cui si è fatto precedentemente il fork) con il comando:

```bash
git push origin username-feature-da-implementare
```

Andare quindi al **proprio repository remoto**, ed aprire una **Pull Request** (bottone verde **Compare and Pull Request**) dal branch `username-feature-da-implementare`del proprio repository verso il `main` del repository originale.

Attendere quindi che la **PR** venga **approvata**, **rifiutata** o richieda **modifiche** da apportare.

Se **approvata**, recarsi nuovamente nel proprio repository remoto ed effettuare la **sincronizzazione** del proprio `main` con quello del repository originale (dove è stato effettuato il merge della Pull Request).

Viceversa se vengono richieste delle **modifiche**, recarsi nuovamente nel proprio **branch locale**, effettuare le **modifiche** richieste ed **eseguire nuovamente** i comandi `add` , `commit` and `push` al fine di integrare la Pull Request con quanto precedentemente richiesto.

<br>

  
## Licenza

Per questa tipologia di progetto, è stata scelta la licenza **MIT**: https://en.wikipedia.org/wiki/MIT_License
  
<br>

