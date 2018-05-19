README

== USAGE ==

This is a program to test retrieval of textures from an OpenSimulator simulator instance.

To extract a list of texture ids for testing, you can use the command.

mysql -NB -u<user> -p<password> <db-name> -e "select id from assets where AssetType=0;" > textures.txt

against the ROBUST service database (assuming a grid configuration).

To perform the test, you will also need a valid capability URL.  You can obtain one by logging in a viewer 
and then executing "show caps" on the region console.  One of the lines will be something like

GetTexture                             /CAPS/301b5e2e-cf41-4b80-ad32-0123ca399ef3/

but with a different UUID.  These are only available for logged in viewers since they are uniquely
generated for a particular user and then disposed of when they log out or move away from the simulator.

The CAPS part is combined with the standard HTTP url to get the full GetTexture
capability URL.  Assuming that the simulator is at 127.0.0.1 with an HTTP port of 9000 (which is the default), 
this will be 

http://localhost:9000/CAPS/301b5e2e-cf41-4b80-ad32-0123ca399ef3/

This is used with the TextureLoadTest.exe, that has the usage syntax

TextureLoadTest.exe <GetTexture-capability-URL> <texture-ids-file>

For instance,

./TextureLoadTest.exe http://localhost:8002/CAPS/301b5e2e-cf41-4b80-ad32-0123ca399ef3/ textures.txt





README

== VERWENDUNG ==

Dies ist ein Programm, um den Abruf von Texturen von einer OpenSimulator Simulator Instanz zu testen.

Um eine Liste von Textur-IDs zum Testen zu extrahieren, können Sie den Befehl verwenden.

mysql -NB -u<user> -p<password> <db-name> -e "select id from assets where AssetType=0;" > textures.txt

gegen die RROBUST service database (unter Annahme einer Rasterkonfiguration).

Um den Test durchzuführen, benötigen Sie außerdem eine gültige Fähigkeits-URL. Sie können einen erhalten, indem Sie einen Viewer anmelden
und dann "show caps" auf der region console ausführen. Eine der Linien wird etwas wie sein

GetTexture                             /CAPS/301b5e2e-cf41-4b80-ad32-0123ca399ef3/

aber mit einer anderen UUID. Diese sind nur für angemeldete Viewer verfügbar, da sie eindeutig sind
für einen bestimmten Benutzer generiert und dann entsorgt, wenn sie sich abmelden oder vom Simulator weggehen.

Der CAPS-Teil wird mit der Standard-HTTP-URL kombiniert, um die vollständige GetTexture zu erhalten
Fähigkeits-URL. Unter der Annahme, dass der Simulator bei 127.0.0.1 mit einem HTTP-Port von 9000 ist (was der Standard ist),
Das wird sein

http://localhost:9000/CAPS/301b5e2e-cf41-4b80-ad32-0123ca399ef3/

Dies wird mit der TextureLoadTest.exe verwendet, die die Syntax für die Verwendung hat

TextureLoadTest.exe <GetTexture-capability-URL> <texture-ids-file>

Zum Beispiel,

./TextureLoadTest.exe http://localhost:8002/CAPS/301b5e2e-cf41-4b80-ad32-0123ca399ef3/ textures.txt
