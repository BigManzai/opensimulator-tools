# README #

A simple couple of scripts for starting components of OpenSimulator.  This is an
alternative to the /etc/init.d script found elsewhere in this repository.

These scripts work using screen instances.

It would be possible to make these scripts much more sophisticated (e.g.
automatic detection of whether the grid services are running before starting a
simulator, etc.).  

However, currently they are deliberately being kept simple in order to keep the
user close to what is really happening.  This is to facilitate debugging and the
ability to deal with the many possible failure conditions.  This might change in
the future.

# Installation #

1. Copy src/* to a location of your choice
2. If you are using a Python earlier than 2.7m you will need to copy argparse.py
[1] into the same location.

# Configuration #

1.  Before use, you will need to copy config.py.example to config.py and
configure it for your OpenSimulator installation.

2.  There are also some optional configuration parameters in simctrl.py and
robustctrl.py though you wouldn't normally need to edit these.  These control
the name of the screen used, whether mono is started with the --debug switch,
etc.

# Use #

simctrl.py controls a simulator instance whilst robustctrl.py can control a
Robust grid service instance.

If the OpenSimulator installation is in standalone mode then it can be
controlled purely with the simctrl.py script.

Both these scripts provide a number of commands to control their components.
These are

start   - start an instance of the component.
stop    - stop the component if it is running.
restart - restart the component if it is running.
attach  - attach to the current screen instance of the component if it is running.
status  - get the current status of the component.

There are also a few optional switches

-a, --attach

Only valid for start and restart commands.  If set then osimctrl automatically
attaches you to the screen of the [re]started component.

-r, --autorestart

If a component fails, then automatically restart it.  If you use this option
then you can only stop the component with the stop command instead of manually
attaching to the screen and shutting it down (since the surrounding loop will
simply start it again).  Alternatively, you can send the signal SIGUSR1 to the
bash script which acts as the simple loop.  This will be a child process from
the screen instance).

-v, --verbose

If set then osimctrl prints out each command that it executes and other information.  
Useful for debugging

-h. --help

Display usage text

It provides start, stop, restart, attach and status commands, along with
--noattach and --autorestart options

# Files #

## robustctrl.py, simctrl.py ##
These files control a robust instance and a simulator respectively.

# Bugs #

Because stop currently involves stuff text onto the screen buffer, this will
fail if there is something already there.

# References #
[1] http://argparse.googlecode.com/hg/argparse.py





# README #

Ein paar Skripte zum Starten von Komponenten von OpenSimulator. Das ist ein
Alternative zum Script /etc/init.d, das an anderer Stelle in diesem Repository gefunden wurde.

Diese Skripte arbeiten mit screen instanzen.

Es wäre möglich, diese Skripte viel ausgefeilter zu machen (z.B.
automatische Erkennung, ob die Grid-Dienste vor dem Start von a ausgeführt werden
Simulator usw.).

Derzeit werden sie jedoch bewusst einfach gehalten, um die
Benutzer in der Nähe von dem, was wirklich passiert. Dies erleichtert Debugging und das
Fähigkeit, mit den vielen möglichen Fehlerbedingungen umzugehen. Dies könnte sich ändern
die Zukunft.

# Installation #

1. Kopieren Sie src / * an einen Ort Ihrer Wahl
2. Wenn Sie Python früher als 2.7m verwenden, müssen Sie argparse.py kopieren
[1] in den gleichen Ort.

# Aufbau #

1. Vor der Verwendung müssen Sie config.py.example in config.py und kopieren
Konfigurieren Sie es für Ihre OpenSimulator-Installation.

2. Es gibt auch einige optionale Konfigurationsparameter in simctrl.py und
robustctr.py, obwohl Sie diese normalerweise nicht bearbeiten müssen. Diese Kontrolle
der Name des verwendeten Bildschirms, ob Mono mit dem Schalter --debug gestartet wird,
etc.

# Benutzen #

simctrl.py steuert eine Simulatorinstanz, während robustctr.py eine
Robuste Grid-Service-Instanz.

Wenn sich die OpenSimulator-Installation im eigenständigen Modus befindet, kann dies der Fall sein
rein mit dem Skript simctrl.py gesteuert.

Beide Skripts enthalten eine Reihe von Befehlen zum Steuern ihrer Komponenten.
Diese sind

start - startet eine Instanz der Komponente.
stop - Stoppen Sie die Komponente, wenn sie ausgeführt wird.
Neustart - Starten Sie die Komponente neu, wenn sie ausgeführt wird.
attach - Anfügen an die aktuelle Bildschirminstanz der Komponente, wenn sie ausgeführt wird.
status - Ermittelt den aktuellen Status der Komponente.

Es gibt auch ein paar optionale Schalter

-a, --anhängen

Nur gültig für Start- und Neustartbefehle. Wenn gesetzt, osimctrl automatisch
verbindet Sie mit dem Bildschirm der [re] gestarteten Komponente.

-r, --autorestart

Wenn eine Komponente ausfällt, starten Sie sie automatisch neu. Wenn Sie diese Option verwenden
Dann können Sie die Komponente nur mit dem Befehl stop statt manuell stoppen
Anbringen an den Bildschirm und Herunterfahren (da die umgebende Schleife wird
starte es einfach nochmal). Alternativ können Sie das Signal SIGUSR1 an die
Bash-Skript, das als einfache Schleife fungiert. Dies wird ein Child-Prozess von sein
die Bildschirminstanz).

-v, --verbose

Wenn gesetzt, gibt osimctrl jeden ausgeführten Befehl und andere Informationen aus.
Nützlich zum Debuggen

-h. --Hilfe

Verwendungstext anzeigen

Es bietet Start, Stop, Neustart, Anfügen und Statusbefehle, zusammen mit
Optionen --noattach und --autorestart

# Dateien #

## robustctrl.py, simctrl.py ##
Diese Dateien steuern eine robuste Instanz bzw. einen Simulator.

# Fehler #

Da stop momentan einen Text in den Bildschirmpuffer einbezieht, wird dies der Fall sein
scheitern, wenn da schon etwas ist.

# Verweise #
[1] http://argparse.googlecode.com/hg/argparse.py