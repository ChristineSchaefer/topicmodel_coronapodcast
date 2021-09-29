# topicmodel_coronapodcast

***

Das Repository umfasst eine Implementierung des Gensim LDA Models.

Tutorial zur Implementierung unter: https://radimrehurek.com/gensim/auto_examples/tutorials/run_lda.html#sphx-glr-auto-examples-tutorials-run-lda-py

Für die Implementierung wurde ein Korpus der in den [NDR Corona Podcasts](https://www.ndr.de/nachrichten/info/podcast4684.html) an den Wissenschaftler Christian Drosten und and die Wissenschaftlerin Sandra Ciesek gestellten Fragen zusammengestellt. Das Korpus befindet sich innerhalb der Datei `podcast.csv`.

***
### Quickstart
***
Die Anwendung wurde in Python 3.9 geschrieben.

Klone das Repository

`git clone https://github.com/ChristineSchaefer/topicmodel_coronapodcast.git`

cd in den Ordner **topicmodel_coronapodcast**: hier liegt die requirements Datei und das Programm wird von hier ausgeführt (working dir)

`python -m pip install -r requirements.txt`

Mit der nachfolgenden Ausführung wird das gesamte Programm aufgerufen 
--> Laden des Korpus, Vorverarbeitung des Korpus, Training des LDA Models

`python main.py`

Informationen über die erfolgten Abläufe und Ergebnisse werden in der logging-Datei `lda.log` gespeichert.

***
### Codestruktur
***
```
📦topicmodel_coronapodcast
 ┣ 📂preprocessing
 ┃ ┣ 📂prepare_resources
 ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┣ 📜text_processing.py
 ┃ ┣ 📜__init__.py
 ┃ ┣ 📜helper.py
 ┣ 📂training
 ┃ ┣ 📜__init__.py
 ┣ 📜.gitignore
 ┣ 📜lda.log
 ┣ 📜main.py
 ┣ 📜podcast.csv
 ┣ 📜README.md
 ┣ 📜requirements.txt
```

***
### Implementierung
***
1. **Laden des Korpus**: Das Korpus ist als Tabelle in einer csv-Datei abgespeichert. Folgende Spalten sind vorhanden: id, Podcastfolge, Wissenschaftler:in, Fragen. Diese werden Zeile für Zeile eingelesen. Die Fragen werden in einer Liste abgespeichert und normalisiert, da beim Einlesen Sonderzeichen etc. übernommen werden, die für die weitere Verarbeitung nicht brauchbar sind.
2. **Vorverarbeitung**: Die Liste der Fragen werden tokenisiert und lemmatisiert. Außerdem können N-Gramme erstellt werden.
3. **Training**: Zum Training wird das LDA-Model von Gensim genutzt. Diesem werden Parameter übergeben, z.B. wie viele Topics gefunden werden sollen.

Die Module werden innerhalb des Main-Moduls nacheinander aufgerufen. 
