# README #

OpenSimulator stats analyzer is a set of tools to analyze data from OpenSimulator stats logs [OPENSIM-STATS-LOGS].

ostagraph.py is capable of accepting options from the command line from one off generation or from a batch file for
generation of a set of graphs at once.

All this needs much more documentation, but you can see an example batch generation file as batch/stdgraphs.json that
will produce a set of standard graphs for a simulator input fileset.

This can be trigged by a shell command such as 

$ ./ostagraphs.py --batch batch/stdgraphs.json --outdir graphs data/oscc/2014-09-02/logs/*.log

where outdir is the directory to place the generated graphs and the last argument is the place to find the stats log
files to use in graph generation.

# Requirements #

* Python >= 2.7
* matplotlib >= 1.3.1 (very probably early versions will also work).

# References #

[OPENSIM-STATS-LOGS] - http://opensimulator.org/wiki/Show_stats#stats_record

vim: ts=4:sw=4:et:tw=120



# README #

Der OpenSimulator-Statistikanalysator ist eine Sammlung von Tools zur Analyse von Daten aus OpenSimulator-Statistikprotokollen [OPENSIM-STATS-LOGS].

ostagraph.py kann Optionen von der Befehlszeile aus einer einzelnen Generation oder aus einer Stapeldatei für
gleichzeitige Erzeugung einer Menge von Graphen

All dies benötigt viel mehr Dokumentation, aber Sie können eine Beispiel-Batch-Generierungsdatei als batch / stdgraphs.json sehen
erstellt eine Reihe von Standardgraphen für eine Simulator-Eingabedateigruppe.

Dies kann durch einen Shell-Befehl wie z

$ ./ostagraphs.py --batch batch / stdgraphs.json --outdir graphs data / oscc / 2014-09-02 / logs / *. log

Dabei ist outdir das Verzeichnis, in dem die generierten Graphen abgelegt werden, und das letzte Argument ist der Ort, an dem das Statistikprotokoll zu finden ist
Dateien, die in der Diagrammgenerierung verwendet werden sollen.

# Bedarf #

* Python> = 2.7
* matplotlib> = 1.3.1 (sehr wahrscheinlich werden auch frühe Versionen funktionieren).

# Verweise #

[OPENSIM-STATS-LOGS] - http://opensimulator.org/wiki/Show_stats#stats_record

vim: ts = 4: sw = 4: et: tw = 120
