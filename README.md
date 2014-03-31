# Markov-Ketten-Beispiele


Dieses Repository enthält den Code, der für den Vortrag über Markovketten am 30. März 2014 auf dem Python-Barcamp in Köln von mir gehalten wurde. Der Code ist gut kommentiert, ohne das Wissen über den Vortrag jedoch vermutlich nur schwer verständlich.

*Nicht* mitgeliefert sind die Literaturquellen für die Erzeugung neuer Goethe-Zitate. Diese sind auf Projekt Gutenberg erhältlich.

## Grundlagen

Was hier gemacht wird, ist mittels einer Markovkette Text erzeugt. Die Markovkette hat als Zustände dabei Buchstabenkombinationen. Die Übergänge zwischen Kombinationen entsprechen den relativen Vorkommen in einem Eingabetext.

Um eine Ausgabe zu erzeugen wird zuerst ein `START_MARKER` eingefügt. Ausgehend von diesem werden die Buchstabenkombinationen durchlaufen, bis die Kette an einem `END_MARKER` ankommt.


## Benutzung

Alle Funktionen sind in `markov.py` enthalten. Dort einfach nachlesen.

Wenn nur neuer Text erstellt werden soll, müssen die literarischen Inputs in `goethe.py` eingetragen werden und die Datei dann ausgeführt werden.



## Übungsaufgabe

Lustige Effekte ergeben sich auch, wenn man nicht Text auf buchstabenbasis erzeugt, sondern Sätze aus Wort-Kombinationen. Die Zustandsmenge der Markovkette sind dann n-fache Kombinationen von Wörtern. Dafür sollte allerdings eine große Eingabemenge vorhanden sein. Siehe auch [Wikipedia über Markovketten](https://en.wikipedia.org/wiki/Markov_chain#Markov_text_generators).


# License information

Copyright (C) 2014 Johannes Spielmann

All files in this repository are licensed under the terms of the GNU General Public Licenses as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

For a full description of the license, please see the file

  LICENSE