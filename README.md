# Seminararbeit
Codes zum Schreiben meiner Seminararbeit

Ersten paar codes :
In dem File parameter findet man die jeweiligen parameter der Pateintinnen, damit ich sie nicht in jedes File einfügen muss und eventuell schnell die codes für andere patienten/innen ausführeen kann 


Tfunction - Code:
hier habe ich eben einmal den Plot für die thyroid-function mit krümmung und set point und allem. funktioniert such eigentlich gut
Zum bestimmen der Nullstelle der Ableitung der Krümmung wollte ich das bisektionsverfahren verwenden, hat nicht funktioniert. Ich habe eine alternative variante gefunden, um die Nullstelle zu finden, diese macht aber im endeffekt soweiso dasselbe wie das Bisektionsverfahren.
Den set point, den ich im Plot hinausbekomme ist jedoch nicht geanz genu derselbe wie der den man mit den Formeln aus der Masterarbeit erhält. (sieht man beim pringt unten) Vielleicht aufgrund von der Ungenauigkeit von np.gardient was ich zur berechnung der Ableitung von der Krümmung verwende, wenn ich jedoch die ableitung der Krümmung händische eintippe funktioniert es wieder nicht. (für die Ableitung der T funktion habe ich es mit der Hand ausgerechnet, weil es eben sonst zu ungenau ist.)

HPfunction - Code:
Hier wieder Hpfunction mit krümmung, leider ohne set point. Es wird mir gesagt wenn ich den set point also die nullstelle der ableitung von der Krümmung ausrechne, dass die ableitung der Krümmung nicht vorzeichen wechselt, was aber in der Grafik offensichtlich schon so ist. Wenn der computer aber denkt es ändert sich das vorzeichen nicht dann funktioniert das bisektionsverfahren nicht und findet eben keine Nullstelle. GRund: viellleicht weil alles zu ungenau berechnet wird? 

solveivp:
sollte eigentlich passen,der Gupf der einen Kirve schaut ein wenig extrem aus aber die Anfangswerte stimmen nun.

gainfactor-analysis:
schaut derzeit so aus wie in masterarbeit, alles klappt gut.
