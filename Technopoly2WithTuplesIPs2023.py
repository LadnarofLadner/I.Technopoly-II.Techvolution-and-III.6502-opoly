import pygame, sys, random, os

#Meyer's_Original_Technpoly.py - TECHNOPOLY
print("Developed by Randall Meyer (with code partially derived from Stephen Hustedde's MONOPOLY ROLLS program.)\n")
print("""This game is a tool to teach three different lessons to students of the sciences and humanities.
The first game (I) can be played like that other more boring and inaccurate game developed in 1915 by Lizzie Maggie and sometimes referred to as 'The Landlord's Game'.
The second game, (II), provides a more accurate lesson of the TECHVOLUTION of the human animal, wherein each physical address is replaced
The Third Game, (III), has players collect Op Code Cards and Digital Data Cards, and actually hand program a schematic moidel of the vintage 6502 microproceesor from 1975.\n""")

player1 = [0, 0]
player2 = [0, 0]
player3 = [0, 0]
player4 = [0, 0]
player5 = [0, 0]
player6 = [0, 0]
player7 = [0, 0]
player8 = [0, 0]

characterlist = ["1. Lizzie-Maggie", "2. Mensch", "3. Peddle", "4. Woz", "5. Lillienfeld", "6. Cady", "7. Picard", "8. Hoerni"]



Count = 1

while Count == 1:

	print("How many Players? 2 to 8?")
	HowManyPlayers = input()
	HowManyPlayers = int(HowManyPlayers)

	if HowManyPlayers > 8:
		print("error")
		Count = 1
	else:
		if HowManyPlayers < 2:
			print("error")
			Count = 1
		else:
			print("OK")	
			Count = 0

Loop = 1
dLoop= 1
while Loop <= HowManyPlayers:
	print("Player")
	print (Loop)
	print("What character will you choose?")
	print ("1. Lizzie-Maggie, 2. Mensch, 3. Peddle, 4. Woz, 5. Lillienfeld, 6. Cady, 7. Picard, 8. Hoerni")
	characterchoice = input ()
	characterchoice = int(characterchoice)
	if 	Loop == 1:
		if (characterlist[characterchoice-1]) == 0:
			Loop
		else:
			print(characterlist[characterchoice-1])
			player1.insert(0, characterchoice)
			del characterlist[characterchoice-1]
			characterlist.insert(characterchoice-1,0)
			Loop = Loop + dLoop
	else: 
		if Loop == 2:
			if (characterlist[characterchoice-1]) == 0:
				print("Nope, unavailable; choose again")
				Loop
			else:
				print(characterlist[characterchoice-1])
				player2.insert(0, characterchoice)
				del characterlist[characterchoice-1]
				characterlist.insert(characterchoice-1,0)
				Loop = Loop + dLoop
		else:
			if Loop == 3:
				if (characterlist[characterchoice-1]) == 0:
					print("Nope, unavailable; choose again")
					Loop
				else:
					print(characterlist[characterchoice-1])
					player3.insert(0, characterchoice)
					del characterlist[characterchoice-1]
					characterlist.insert(characterchoice-1,0)
					Loop = Loop + dLoop
			else:
				if Loop == 4:
					if (characterlist[characterchoice-1]) == 0:
						print("Nope, unavailable; choose again")
						Loop
					else:
						print(characterlist[characterchoice-1])
						player4.insert(0, characterchoice)
						del characterlist[characterchoice-1]
						characterlist.insert(characterchoice-1,0)
						Loop = Loop + dLoop
				else:
					if Loop == 5:
						if (characterlist[characterchoice-1]) == 0:
							print("Nope, unavailable; choose again")
							Loop
						else:
							print(characterlist[characterchoice-1])
							player5.insert(0, characterchoice)
							del characterlist[characterchoice-1]
							characterlist.insert(characterchoice-1,0)
							Loop = Loop + dLoop
					else:
						if Loop == 6:
							if (characterlist[characterchoice-1]) == 0:
								print("Nope, unavailable; choose again")
								Loop
							else:
								print(characterlist[characterchoice-1])
								player6.insert(0, characterchoice)
								del characterlist[characterchoice-1]
								characterlist.insert(characterchoice-1,0)
								Loop = Loop + dLoop
						else:
							if Loop == 7:
								if (characterlist[characterchoice-1]) == 0:
									print("Nope, unavailable; choose again")
									Loop
								else:
									print(characterlist[characterchoice-1])
									player7.insert(0, characterchoice)
									del characterlist[characterchoice-1]
									characterlist.insert(characterchoice-1,0)
									Loop = Loop + dLoop
							else:
								if Loop == 8:
									if (characterlist[characterchoice-1]) == 0:
										print("Nope, unavailable; choose again")
										Loop
									else:
										print(characterlist[characterchoice-1])
										player8.insert(0, characterchoice)
										del characterlist[characterchoice-1]
										characterlist.insert(characterchoice-1,0)
										Loop = Loop + dLoop
								else:
									Loop == 9
									print("X")
									
									
	

spaces = ["Go (COLLECT 200$)", "Numbers", "Patent Fees", "Writing", "Serendipity ; Community Quest",
          "Metallic Circuits", "Time", "Innovation Station", "Math and Measure", "Logic",
          "Visiting College ; Research", "Optics", "Data Farm", "Chemistry", "Physics",
          "Electromagnetic Spectrum", "Electricity", "Magnetism", "Automata", "Parents Garage",
          "Vacuum Tubes", "Innovation Station", "Crystals", "Interconnection", "Satellites and Rockets",
          "Mechanical Computers", "Electro-Mechanical Computers", "Semiconductor Fabrication Facility", "Electronic Computers", "Go To College",
          "Memory", "Operating Systems", "Serendipity ; Community Quest", "Data Structures","Lasers and Fiber Optics",
          "Innovation Station", "Integrated Circuits", "Incorporation fees", "Microprocessors"]

current = 0
die1 = die2 = total = 0
doubles = 0
rolls = 0
print("Technopoly! You are currently on GO (COLLECT $200).")
roll_em = input("Press Enter to roll dice; Press q + Enter to end")

while (roll_em != "q")  :
	die1 = random.randint (1,6)
	die2 = random.randint (1,6)
	total = die1 + die2
	rolls += 1
	current = (current + total) % 39 # add total roll to current location and use modulus too
	mySpace = spaces[current]
	print('\nYou rolled a {0} and a {1} for a total of {2}. You\'re at "{3}".'.format(die1, die2, total, mySpace.upper()))
	roll_em = input("Press Enter to roll dice; Press q + Enter to end")


			
print (player1[0])
print (player2[0])
print (player3[0])
print (player4[0])
print (player5[0])
print (player6[0])
print (player7[0])
print (player8[0])

print(characterlist)

#Tuples (Unalterable Lists: IP Properties "rents")
# Text data will be ("name", "decimal number card", "binary number card", "hex number card", "decimal Age/Era", "Hex Age/Era", "Age/Era Name", rent, 4 improved rents, 2 Obsoleted Values, "decription and years") 

Tallymarks = ("Tallymarks and Glyphs", "00$D", "0000 0000$B" "00$H", "Stone Age", "00$D", "0$H", 2, 10, 30, 90, 160, 250, 30, 50, "", "43,000 to 44,200 BCE")
print(Tallymarks,)
Practical_Numbers = ("Practical Numbers", "01$D", "0000 0001$B" "01$H", "Iron Age", "01$D", "1$H", 2, 10, 30, 90, 160, 250, 30, 50, "", "4000 BCE")
print(Practical_Numbers,)
Base = ("Base", "02$D", "0000 0010$B" "02$H", "Iron Age", "01$D", "1$H", 2, 10, 30, 90, 160, 250, 30, 50, "", "3400 BCE")
print(Base,)
Positional = ("Positional", "03$D", "0000 0011$B" "03$H", "Iron Age", "01$D", "1$H", 2, 10, 30, 90, 160, 250, 30, 50, "", "2000 BCE")
print(Positional,)
Ratio = ("Ratio", "04$D", "0000 0100$B" "04$H", "Iron Age", "01$D", "1$H", 2, 10, 30, 90, 160, 250, 30, 50, "", "530 BCE")
print(Ratio,)
Infinity = ("Infinity", "05$D", "0000 0101$B" "05$H", "Classical Antiquity", "02$D", "5$H", 2, 10, 30, 90, 160, 250, 30, 50, "", "495 to 430 BCE")
print(Infinity,)
Permutations = ("Permutations", "06$D", "0000 0110$B" "06$H", "Classical Antiquity", "02$D", "2$H", 2, 10, 30, 90, 160, 250, 30, 50, "", "5th BCE")
print(Permutations,)
Axioms = ("Axioms", "07$D", "0000 0111$B" "07$H", "Classical Antiquity", "02$D", "2$H", 2, 10, 30, 90, 160, 250, 30, 50, "", "300 BCE")
print(Axioms,)
Trigonometry = ("Trigonometry", "08$D", "0000 1000$B" "08$H", "Classical Antiquity", "02$D", "2$H", 2, 10, 30, 90, 160, 250, 30, 50, "", "150 CE")
print(Trigonometry,)
Zero = ("Zero", "09$D", "0000 1001$B" "09$H", "Classical Antiquity", "02$D", "2$H", 2, 10, 30, 90, 160, 250, 30, 50, "", "224 to 993 CE")
print(Zero,)
Algebra = ("Algebra", "10$D", "0000 1010$B" "0A$H", "Classical Antiquity", "02$D", "2$H", 2, 10, 30, 90, 160, 250, 30, 50, "", "2nd CE")
print(Algebra,)
Primes = ("Primes", "11$D", "0000 1011$B" "0B$H", "Late Antiquity", "03$D", "3$H", 2, 10, 30, 90, 160, 250, 30, 50, "", "3rd CE")
print(Primes,)
Hindu_Arabic_Numerals = ("Hindu-Arabic Numerals", "12$D", "0000 1100$B" "0C$H", "Late Antiquity", "03$D", "3$H", 2, 10, 30, 90, 160, 250, 30, 50, "", "598 to 665 CE")
print(Hindu_Arabic_Numerals,)
Liber_Abaci = ("Liber Abaci", "13$D", "0000 1101$B" "0D$H", "High Middle Ages", "05$D", "5$H", 2, 10, 30, 90, 160, 250, 30, 50, "", "1205 CE")
print(Liber_Abaci,)
Signs_And_Notations = ("Signs and Notations", "14$D", "0000 1110$B" "0E$H", "Renaissance", "06$D", "6$H", 2, 10, 30, 90, 160, 250, 30, 50, "", "1461 CE")
print(Signs_And_Notations,)
Binary = ("Binary", "15$D", "0000 1111$B" "0F$H", "The Enlightenment", "07$D", "7$H", 2, 10, 30, 90, 160, 250, 30, 50, "", "1703 BCE")
print(Binary,)


Painting = ("Painting", "16$D", "0001 0000$B" "10$H", "Stone Age", "00$D", "0$H", 4, 20, 60, 180, 320, 450, 30, 50, "", "64,000+ BCE")
print(Painting,)
Petroglyphs = ("Petroglyphs", "17$D", "0001 0001$B" "11$H", "Stone Age", "00$D", "0$H", 4, 20, 60, 180, 320, 450, 30, 50, "", "10,000 to 12,000 BCE")
print(Petroglyphs,)
Clay_Tokens = ("Clay Tokens", "18$D", "0001 0010$B" "12$H", "Iron Age", "01$D", "1$H", 4, 20, 60, 180, 320, 450, 30, 50, "", "8,000 to 7,500 BCE")
print(Clay_Tokens,)
Logograms = ("Logograms", "19$D", "0001 0011$B" "13$H", "Iron Age", "01$D", "1$H", 4, 20, 60, 180, 320, 450, 30, 50, "", "5th Milennium BCE")
print(Logograms,)
Painting = ("Painting", "16$D", "0001 0000$B" "10$H", "Stone Age", "00$D", "0$H", 4, 20, 60, 180, 320, 450, 30, 50, "", "64,000+ BCE")
print(Painting,)
Painting = ("Painting", "16$D", "0001 0000$B" "10$H", "Stone Age", "00$D", "0$H", 4, 20, 60, 180, 320, 450, 30, 50, "", "64,000+ BCE")
print(Painting,)
Painting = ("Painting", "16$D", "0001 0000$B" "10$H", "Stone Age", "00$D", "0$H", 4, 20, 60, 180, 320, 450, 30, 50, "", "64,000+ BCE")
print(Painting,)
Painting = ("Painting", "16$D", "0001 0000$B" "10$H", "Stone Age", "00$D", "0$H", 4, 20, 60, 180, 320, 450, 30, 50, "", "64,000+ BCE")
print(Painting,)
Painting = ("Painting", "16$D", "0001 0000$B" "10$H", "Stone Age", "00$D", "0$H", 4, 20, 60, 180, 320, 450, 30, 50, "", "64,000+ BCE")
print(Painting,)
Painting = ("Painting", "16$D", "0001 0000$B" "10$H", "Stone Age", "00$D", "0$H", 4, 20, 60, 180, 320, 450, 30, 50, "", "64,000+ BCE")
print(Painting,)
Painting = ("Painting", "16$D", "0001 0000$B" "10$H", "Stone Age", "00$D", "0$H", 4, 20, 60, 180, 320, 450, 30, 50, "", "64,000+ BCE")
print(Painting,)
Painting = ("Painting", "16$D", "0001 0000$B" "10$H", "Stone Age", "00$D", "0$H", 4, 20, 60, 180, 320, 450, 30, 50, "", "64,000+ BCE")
print(Painting,)
Painting = ("Painting", "16$D", "0001 0000$B" "10$H", "Stone Age", "00$D", "0$H", 4, 20, 60, 180, 320, 450, 30, 50, "", "64,000+ BCE")
print(Painting,)
Painting = ("Painting", "16$D", "0001 0000$B" "10$H", "Stone Age", "00$D", "0$H", 4, 20, 60, 180, 320, 450, 30, 50, "", "64,000+ BCE")
print(Painting,)
Painting = ("Painting", "16$D", "0001 0000$B" "10$H", "Stone Age", "00$D", "0$H", 4, 20, 60, 180, 320, 450, 30, 50, "", "64,000+ BCE")
print(Painting,)
Painting = ("Painting", "16$D", "0001 0000$B" "10$H", "Stone Age", "00$D", "0$H", 4, 20, 60, 180, 320, 450, 30, 50, "", "64,000+ BCE")
print(Painting,)





print("\nThanks for playing ... you rolled",rolls,"times.\n")




