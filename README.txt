
Luffarschack av Timothy O'Flaherty


LUFFARSCHACK:
Programmet är ett spel som spelas från en konsoll för 1-2 personer.


FUNKTIONELLA BEROENDEN:
Programmet kräver följande paket för att fungera (och paketens egna funktionella beroenden).

	1. AppJar
	2. Pandas
	3. Numpy


ANSVARSFRISKRIVNING: 
Om ovanstående paket har egna funktionella beroenden, ansvarar inte programmets tillverkade 
för eventuella programfel.


INSTALLERING:
För att installera programmets beroenden, navigera i en terminal till 
programmet luffarschaks mapp och skriv: pip install -r requirements.txt.
Pip kommer att installera programmets beroenden, och beroendenas egna beroenden.


BÖRJA SPELA:
Spelet starts från python-filen 'tic_tac_toe.py' och ingen annan
fil behöver öppnas. Öppna filen i valfri lämplig IDE eller navigera i 
kommandotolken till mappen där programmet ligger och skriv in 'python tic_tac_toe.py'.


TESTNING AV FUNKTIONER:
Om du kör filen 'test_program.py' i en IDE och det står att 0 test kördes så pröva att
köra filen från kommandotolken genom att ställa dig i mappen där filen är och skriv in 
'python test_program.py' 


---------------------------------------------------------------------------------------------


MANUAL FÖR SPELET:
1. Skriv in namn på spelarna. Spelare 2 är valfri och för att spela i 
enspelarläge ger man spelare 2 namnet 'Skynet'.   



2. En meny med olika val printas ut, se exempel: 

	------TIC TAC TOE------
	[1] - Play Tic Tac Toe
	[2] - View scoreboard
	[3] - View game history
	[4] - Clear game history
	[5] - Quit

Skriv in siffran som representerar meny-valet du vill göra. Vad de olika meny-valen
innebär kommer förklaras i nästa punkt.


3.1. "[1] - Play Tic Tac Toe":
Anger användaren "1" kommer en fråga om hur stor spelplan spelarna vill ha. Förväntad inmatning
är en ensam siffra från 1 och uppåt. Om man anger "3" så kommer en spelplan
på 3x3 rutor att skapas (se exempel nedan).

	------TIC TAC TOE------
 	 Player 1 vs Player 2

	    0    1    2
	0 ['_', '_', '_']
	1 ['_', '_', '_']
	2 ['_', '_', '_']

	Enter coordinates separated with space ("X Y")
	Player 1's turn:

Spelare 1 börjar allid och kommer alltid att ha symbolen "X" som markör och spelare 2 kommer
ha symbolen "O". För att placera sin markör skrivar man in koordinater som representerar punkten
där man vill sätta symbolen. Koordinaterna ska anges med siffror separerade med ett mellanslag.
Spelet kommmer att fortsätta tills att någon av spelarna har vunnit eller tills det att alla 
punkter på spelplanen har fått en spelares markör (Oavgjort). När ett spel är slut återvänder
spelarna till huvudmenyn.

3.2. "[2] - View scoreboard":
Anger användaren "2" kommer först ett gui med statistik att öppnas. När användaren trycker på
"OK" stängs rutan och samma statistik presenteras i ett annat format i kommandotolken (Se nedan).
För att återvända till menyn kan användaren trycka på enter.

	------TIC TAC TOE------
        	 STATS         

	               | Win | Win % | Tie | Tie % | Tot.Games | Tot.moves | Avg.win moves | Avg.moves
	P1 (Player 1):     0     0.0     0     0.0           0           0             0.0         0.0
	P2 (Player 2):     0     0.0     0     0.0           0           0             0.0         0.0
	--------           -       -     -       -           -           -               -           -
	Total:             0     0.0     0     0.0           0           0             0.0         0.0

3.3. "[3] - View previous games":
Anger användaren "3" kommer resultaten av alla tidigare spelade spel att skrivas ut (se exempel nedan). 
För att återvända till menyn kan användaren trycka på enter.

	------TIC TAC TOE------

	2019-09-30 14:41:10
	Player 1 vs. Player 2
	Winner: Player 1(X)

	    0    1    2    
	0 ['_', 'X', 'O']
	1 ['_', 'X', '_']
	2 ['O', 'X', '_']


	----------------------

3.4. "[4] - Clear game history":
Anger användaren 4 kommer alla tidigare spel att raderas.

3.5. "[5] - Quit":
Anger användaren "5" Kommer spelet att stängas av.








