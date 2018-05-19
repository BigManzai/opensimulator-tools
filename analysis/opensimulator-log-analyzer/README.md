# README #

A very primitive tool to do some analysis on OpenSimulator logs.

It will likely only be correct for the very latest OpenSimulator code (and then sometimes only dev code) as
it relies on picking out changeable log lines.

At the moment, only prints out 
  * Unique hypergrid, direct and total logins
  * Process memory stats if available.

Should be run against OpenSim.log (standalone) or Robust.log (grid).

Example: ola.py *.log



# README #

Ein sehr primitives Tool für die Analyse von OpenSimulator-Protokollen.

Es wird wahrscheinlich nur für den neuesten OpenSimulator-Code (und dann manchmal nur für den Entwickler-Code) als korrekt gelten
Es beruht auf der Auswahl veränderbarer Protokollzeilen.

Im Moment wird nur gedruckt
   * Einzigartiges Hypergrid, direkte und vollständige Logins
   * Prozessspeicher-Statistiken, falls verfügbar.

Sollte gegen OpenSim.log (Standalone) oder Robust.log (Grid) laufen.

Beispiel: ola.py * .log