import pygame, sys, random, os

#Meyer's_Original_Technpoly.py - TECHNOPOLY
print("Developed by Randall Meyer (with code partially derived from Stephen Hustedde's MONOPOLY ROLLS program.)\n")
print("""This game is a tool to teach three different lessons to students of the sciences and humanities.
The first game (I) can be played like that other more boring and inaccurate game developed in 1915 by Lizzie Maggie and sometimes referred to as 'The Landlord's Game'.
The second game, (II), provides a more accurate lesson of the TECHVOLUTION of the human animal, wherein each physical address is replaced
The Third Game, (III), has players collect Op Code Cards and Digital Data Cards, and actually hand program a schematic moidel of the vintage 6502 microproceesor from 1975.\n""")

#Choose which game to play?

print("Which game do you want to play? 1. I Technopoly, 2. II. Techvolution, or 3. III. 6502-opoly?")
gamechoice = input ()
if	gamechoice == 1:
	import ITechnopoly
else:
	if	gamechoice == 3:
		import III6502opoly
	else:
		gamechoice == 2
		print("You chose game II., 'Techvolution'")

#Player stats, in a list; 0th turn order, 1st player name, 2nd money, 3rd number of color IPs, 4th number of RRs and utilities, 5th total IPs, 6th number of mortgaged IPs, 7th Net Liquidated Worth, 8th current lap number, 9th current era, 10th leading or lagging #, ?   ,? ...

player1 = [1, 0, '{0:,}'.format(1500), 0, 0, 0, 0, 0, 0, 0, 0]
player2 = [2, 0, '{0:,}'.format(1500), 0, 0, 0, 0, 0, 0, 0, 0]
player3 = [3, 0, '{0:,}'.format(1500), 0, 0, 0, 0, 0, 0, 0, 0]
player4 = [4, 0, '{0:,}'.format(1500), 0, 0, 0, 0, 0, 0, 0, 0]
player5 = [5, 0, '{0:,}'.format(1500), 0, 0, 0, 0, 0, 0, 0, 0]
player6 = [6, 0, '{0:,}'.format(1500), 0, 0, 0, 0, 0, 0, 0, 0]
player7 = [7, 0, '{0:,}'.format(1500), 0, 0, 0, 0, 0, 0, 0, 0]
player8 = [8, 0, '{0:,}'.format(1500), 0, 0, 0, 0, 0, 0, 0, 0]

charactertuple = ("1. Lizzie-Maggie", "2. Mensch", "3. Peddle", "4. Woz", "5. Lilienfeld", "6. Cady", "7. Picard", "8. Hoerni")
charactertuplejustnames = ("Lizzie-Maggie", "Mensch", "Peddle", "Woz", "Lilienfeld", "Cady", "Picard", "Hoerni")




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
			Count = 0

characterliststillavailable = ["1. Lizzie-Maggie", "2. Mensch", "3. Peddle", "4. Woz", "5. Lilienfeld", "6. Cady", "7. Picard", "8. Hoerni"]			
characterlistassigned = []
characterliststillavailableminuszeros = ["1. Lizzie-Maggie", "2. Mensch", "3. Peddle", "4. Woz", "5. Lilienfeld", "6. Cady", "7. Picard", "8. Hoerni"]
Loop = 1
dLoop = 1

Loop = 1
while Loop <= HowManyPlayers:
	print("Player ", (Loop), ",")
	print("what character will you choose?")
	print (characterliststillavailable)
	if 	Loop == 1:
		characterchoice = input ()
		characterchoice = int(characterchoice)
		characterchoiceindex = (characterchoice - 1)
		characterchoice1  = (characterchoiceindex + 0)
		print(characterliststillavailable[characterchoice1])
		player1.insert(1, characterchoice)
		player1.pop(2)
		characterliststillavailable.pop(characterchoiceindex)
		characterliststillavailable.insert(characterchoiceindex, 0)
		characterlistassigned.insert(0, (characterchoiceindex))
		Loop = (Loop + dLoop)
	elif Loop == 2:
		characterchoice = input ()
		characterchoice = int(characterchoice)
		characterchoiceindex = (characterchoice - 1)
		characterchoice2  = (characterchoiceindex + 0)
		if characterliststillavailable[characterchoiceindex] == 0:
			print("Error! This character has already been chosen. Please choose an available character.")
			Loop = 2
		else:
			print(characterliststillavailable[characterchoiceindex])
			player2.insert(1, characterchoice)
			player2.pop(2)
			characterliststillavailable.pop(characterchoiceindex)
			characterliststillavailable.insert(characterchoiceindex, 0)
			characterlistassigned.insert(1, (characterchoiceindex))
			Loop = (Loop + dLoop)
	elif Loop == 3:
		characterchoice = input ()
		characterchoice = int(characterchoice)
		characterchoiceindex = (characterchoice - 1)
		characterchoice3  = (characterchoiceindex + 0)
		if characterliststillavailable[characterchoiceindex] == 0:
			print("Error! This character has already been chosen. Please choose an available character.")
			Loop = 3
		else:
			print(characterliststillavailable[characterchoiceindex])
			player3.insert(1, characterchoice)
			player3.pop(2)
			characterliststillavailable.pop(characterchoiceindex)
			characterliststillavailable.insert(characterchoiceindex, 0)
			characterlistassigned.insert(2, (characterchoiceindex))
			Loop = (Loop + dLoop)
	elif Loop == 4:
		characterchoice = input ()
		characterchoice = int(characterchoice)
		characterchoiceindex = (characterchoice - 1)
		characterchoice4  = (characterchoiceindex + 0)
		if characterliststillavailable[characterchoiceindex] == 0:
			print("Error! This character has already been chosen. Please choose an available character.")
			Loop = 4
		else:
			print(characterliststillavailable[characterchoiceindex])
			player4.insert(1, characterchoice)
			player4.pop(2)
			characterliststillavailable.pop(characterchoiceindex)
			characterliststillavailable.insert(characterchoiceindex, 0)
			characterlistassigned.insert(3, (characterchoiceindex))
			Loop = (Loop + dLoop)
	elif Loop == 5:
		characterchoice = input ()
		characterchoice = int(characterchoice)
		characterchoiceindex = (characterchoice - 1)
		characterchoice5  = (characterchoiceindex + 0)
		if characterliststillavailable[characterchoiceindex] == 0:
			print("Error! This character has already been chosen. Please choose an available character.")
			Loop = 5
		else:
			print(characterliststillavailable[characterchoiceindex])
			player5.insert(1, characterchoice)
			player5.pop(2)
			characterliststillavailable.pop(characterchoiceindex)
			characterliststillavailable.insert(characterchoiceindex, 0)
			characterlistassigned.insert(4, (characterchoiceindex))
			Loop = (Loop + dLoop)
	elif Loop == 6:
		characterchoice = input ()
		characterchoice = int(characterchoice)
		characterchoiceindex = (characterchoice - 1)
		characterchoice6  = (characterchoiceindex + 0)
		if characterliststillavailable[characterchoiceindex] == 0:
			print("Error! This character has already been chosen. Please choose an available character.")
			Loop = 6
		else:
			print(characterliststillavailable[characterchoiceindex])
			player6.insert(1, characterchoice)
			player6.pop(2)
			characterliststillavailable.pop(characterchoiceindex)
			characterliststillavailable.insert(characterchoiceindex, 0)
			characterlistassigned.insert(5, (characterchoiceindex))
			Loop = (Loop + dLoop)
	elif Loop == 7:
		characterchoice = input ()
		characterchoice = int(characterchoice)
		characterchoiceindex = (characterchoice - 1)
		characterchoice7  = (characterchoiceindex + 0)
		if characterliststillavailable[characterchoiceindex] == 0:
			print("Error! This character has already been chosen. Please choose an available character.")
			Loop = 7
		else:
			print(characterliststillavailable[characterchoiceindex])
			player7.insert(1, characterchoice)
			player7.pop(2)
			characterliststillavailable.pop(characterchoiceindex)
			characterliststillavailable.insert(characterchoiceindex, 0)
			characterlistassigned.insert(6, (characterchoiceindex))
			Loop = (Loop + dLoop)
	elif Loop == 8:
		characterchoice = input ()
		characterchoice = int(characterchoice)
		characterchoiceindex = (characterchoice - 1)
		characterchoice8  = (characterchoiceindex + 0)
		if characterliststillavailable[characterchoiceindex] == 0:
			print("Error! This character has already been chosen. Please choose an available character.")
			Loop = 8
		else:
			print(characterliststillavailable[characterchoiceindex])
			player8.insert(1, characterchoice)
			player8.pop(2)
			characterliststillavailable.pop(characterchoiceindex)
			characterliststillavailable.insert(characterchoiceindex, 0)
			characterlistassigned.insert(7, (characterchoiceindex))
			Loop = (Loop + dLoop)
	else: 
		print("loop done")
Loop = (Loop + dLoop)
			

print(characterlistassigned)
print(player1)
print(player2)
print(player3)
print(player4)
print(player5)
print(player6)
print(player7)
print(player8)
									
spaces = ["Go (COLLECT 200$)", "Numbers", "Patent Fees", "Writing", "Serendipity ; Community Quest",
          "Metallic Circuits", "Time", "Innovation Station", "Math and Measure", "Logic",
          "Visiting College ; Research", "Optics", "Data Farm", "Chemistry", "Physics",
          "Electromagnetic Spectrum", "Electricity", "Magnetism", "Automata", "Parents Garage",
          "Vacuum Tubes", "Innovation Station", "Crystals", "Interconnection", "Satellites and Rockets",
          "Mechanical Computers", "Electro-Mechanical Computers", "Semiconductor Fabrication Facility", "Electronic Computers", "Go To College",
          "Memory", "Operating Systems", "Serendipity ; Community Quest", "Data Structures","Lasers and Fiber Optics",
          "Innovation Station", "Integrated Circuits", "Incorporation fees", "Microprocessors"]

PlayerTurnsSequence = [1, 2, 3, 4, 5, 6, 7, 8]
current = 0
die1 = die2 = total = 0
doubles = 0
rolls = 0



Loop = 1
while Loop <= HowManyPlayers:
	if 	Loop == 1:
		a = characterlistassigned[Loop-1]
		print("Technopoly!", (charactertuplejustnames[a]), ", you are currently on GO).")
		print(charactertuplejustnames[a], ',')
		roll_em = input("Press Enter to roll dice; Press q + Enter to end")
		if (roll_em != "q")  :
			die1 = random.randint (1,6)
			die2 = random.randint (1,6)
			total = die1 + die2
			rolls += 1
			current = (current + total) % 39 # add total roll to current location and use modulus too
			mySpace = spaces[current]
			print("")
			print(charactertuplejustnames[a])
			print('you have rolled a {0} and a {1} for a total of {2}.'.format(die1, die2, total))
			print(charactertuplejustnames[a])
			print('you have landed on "{0}".'.format(mySpace.upper()))
			Purchase = input("Press 0 to purchase or 1 to pay rent")
			if (Purchase == "0"):
				print('Cost to purchase "{0}" is .'.format(mySpace.upper()))
				print('"{0}"'.format(spaces[current]))
				print("acknowledgedebug0")				
			else:
				print("rent is")
				print('IP fees are "{0}" $s .'.format(mySpace.upper()))
				print('"{0}"'.format(spaces[current]))
				print("acknowledgedebug1")
				Loop = (Loop + 1)
		else:
			Loop = (Loop +1)
	elif Loop == 2:
		a = characterlistassigned[Loop-1]
		print("Technopoly!", (charactertuplejustnames[a]))
		print(", you are currently on GO).")
		print(charactertuplejustnames[a])
		print(',')
		roll_em = input("Press Enter to roll dice; Press q + Enter to end")
		while (roll_em != "q")  :
			die1 = random.randint (1,6)
			die2 = random.randint (1,6)
			total = die1 + die2
			rolls += 1
			current = (current + total) % 39 # add total roll to current location and use modulus too
			mySpace = spaces[current]
			print("")
			print(charactertuplejustnames[a])
			print('you have rolled a {0} and a {1} for a total of {2}.'.format(die1, die2, total))
			print(charactertuplejustnames[a])
			print('you have landed on "{0}".'.format(mySpace.upper()))
			print("Purchase = 0 or pay rent = 1?")
			Purchase = input()
			if Purchase == 1:
				print("rent is")
				print('IP fees are "{0}" $s .'.format(mySpace.upper()))
				print('"{0}"'.format(spaces[current]))
				print("acknowledge")
				Loop = (Loop + 1)
			else:
				print('Cost to purchase "{0}" is .'.format(mySpace.upper()))
				print('"{0}"'.format(spaces[current]))
				print("acknowledge")
				Loop = (Loop + 1)
	else:
		print("finished")
		



#for P in PlayerTurnsSequence:
#	if P <= HowManyPlayers:
		


			
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

# On second thought? Nested List; one tuple, on list. list is alterable. ["owned/unowned-available O = 1 / U-A = 0", "owner number 0, and 1 to 8", "IP chargeable C = 1 NC = 0", "Mortgaged M = 1 U = 0", "Houses #, 0-4", "Hotel #, 0-2", "#-of-this-players-previous-ownership-of-this-exact-timeline, 0-16"]  
# Oops? Can Tuples and Lists be mixed in a nested list? Probably not?

Tallymarks = ("Tallymarks and Glyphs", "00$D", "0000 0000$B" "00$H", "Stone Age", "00$D", "0$H", 2, 10, 30, 90, 160, 250, 30, 50, "", "43,000 to 44,200 BCE")
Tallymarks2 = [0,0,0,0,0,0,0]
print(Tallymarks,)
Practical_Numbers = ("Practical Numbers", "01$D", "0000 0001$B" "01$H", "Iron Age", "01$D", "1$H", 2, 10, 30, 90, 160, 250, 30, 50, "", "4000 BCE")
Practical_Numbers = [0,0,0,0,0,0,0]
print(Practical_Numbers,)
Base = ("Base", "02$D", "0000 0010$B" "02$H", "Iron Age", "01$D", "1$H", 2, 10, 30, 90, 160, 250, 30, 50, "", "3400 BCE")
Base = [0,0,0,0,0,0,0]
print(Base,)
Positional = ("Positional", "03$D", "0000 0011$B" "03$H", "Iron Age", "01$D", "1$H", 2, 10, 30, 90, 160, 250, 30, 50, "", "2000 BCE")
Positional = [0,0,0,0,0,0,0]
print(Positional,)
Ratio = ("Ratio", "04$D", "0000 0100$B" "04$H", "Iron Age", "01$D", "1$H", 2, 10, 30, 90, 160, 250, 30, 50, "", "530 BCE")
Ratio = [0,0,0,0,0,0,0]
print(Ratio,)
Infinity = ("Infinity", "05$D", "0000 0101$B" "05$H", "Classical Antiquity", "02$D", "5$H", 2, 10, 30, 90, 160, 250, 30, 50, "", "495 to 430 BCE")
Infinity = [0,0,0,0,0,0,0]
print(Infinity,)
Permutations = ("Permutations", "06$D", "0000 0110$B" "06$H", "Classical Antiquity", "02$D", "2$H", 2, 10, 30, 90, 160, 250, 30, 50, "", "5th BCE")
Permutations = [0,0,0,0,0,0,0]
print(Permutations,)
Axioms = ("Axioms", "07$D", "0000 0111$B" "07$H", "Classical Antiquity", "02$D", "2$H", 2, 10, 30, 90, 160, 250, 30, 50, "", "300 BCE")
Axioms = [0,0,0,0,0,0,0]
print(Axioms,)
Trigonometry = ("Trigonometry", "08$D", "0000 1000$B" "08$H", "Classical Antiquity", "02$D", "2$H", 2, 10, 30, 90, 160, 250, 30, 50, "", "150 CE")
Trigonometry = [0,0,0,0,0,0,0]
print(Trigonometry,)
Zero = ("Zero", "09$D", "0000 1001$B" "09$H", "Classical Antiquity", "02$D", "2$H", 2, 10, 30, 90, 160, 250, 30, 50, "", "224 to 993 CE")
Zero = [0,0,0,0,0,0,0]
print(Zero,)
Algebra = ("Algebra", "10$D", "0000 1010$B" "0A$H", "Classical Antiquity", "02$D", "2$H", 2, 10, 30, 90, 160, 250, 30, 50, "", "2nd CE")
Algebra = [0,0,0,0,0,0,0]
print(Algebra,)
Primes = ("Primes", "11$D", "0000 1011$B" "0B$H", "Late Antiquity", "03$D", "3$H", 2, 10, 30, 90, 160, 250, 30, 50, "", "3rd CE")
Primes = [0,0,0,0,0,0,0]
print(Primes,)
Hindu_Arabic_Numerals = ("Hindu-Arabic Numerals", "12$D", "0000 1100$B" "0C$H", "Late Antiquity", "03$D", "3$H", 2, 10, 30, 90, 160, 250, 30, 50, "", "598 to 665 CE")
Hindu_Arabic_Numerals = [0,0,0,0,0,0,0]
print(Hindu_Arabic_Numerals,)
Liber_Abaci = ("Liber Abaci", "13$D", "0000 1101$B" "0D$H", "High Middle Ages", "05$D", "5$H", 2, 10, 30, 90, 160, 250, 30, 50, "", "1205 CE")
Liber_Abaci = [0,0,0,0,0,0,0]
print(Liber_Abaci,)
Signs_And_Notations = ("Signs and Notations", "14$D", "0000 1110$B" "0E$H", "Renaissance", "06$D", "6$H", 2, 10, 30, 90, 160, 250, 30, 50, "", "1461 CE")
Signs_And_Notations = [0,0,0,0,0,0,0]
print(Signs_And_Notations,)
Binary = ("Binary", "15$D", "0000 1111$B" "0F$H", "The Enlightenment", "07$D", "7$H", 2, 10, 30, 90, 160, 250, 30, 50, "", "1703 BCE")
Binary = [0,0,0,0,0,0,0]
print(Binary,)


Painting = ("Painting", "16$D", "0001 0000$B" "10$H", "Stone Age", "00$D", "0$H", 4, 20, 60, 180, 320, 450, 30, 50, "", "64,000+ BCE")
Painting = [0,0,0,0,0,0,0]
print(Painting,)
Petroglyphs = ("Petroglyphs", "17$D", "0001 0001$B" "11$H", "Stone Age", "00$D", "0$H", 4, 20, 60, 180, 320, 450, 30, 50, "", "10,000 to 12,000 BCE")
Petroglyphs = [0,0,0,0,0,0,0]
print(Petroglyphs,)
Clay_Tokens = ("Clay Tokens", "18$D", "0001 0010$B" "12$H", "Iron Age", "01$D", "1$H", 4, 20, 60, 180, 320, 450, 30, 50, "", "8,000 to 7,500 BCE")
Clay_Tokens = [0,0,0,0,0,0,0]
print(Clay_Tokens,)
Logograms = ("Logograms", "19$D", "0001 0011$B" "13$H", "Iron Age", "01$D", "1$H", 4, 20, 60, 180, 320, 450, 30, 50, "", "5th Milennium BCE")
Logograms = [0,0,0,0,0,0,0]
print(Logograms,)
Hieroglyphics = ("Hieroglyphics", "20$D", "0001 0100$B" "14$H", "Iron Age", "01$D", "1$H", 4, 20, 60, 180, 320, 450, 30, 50, "", "64,000+ BCE")
Hieroglyphics = [0,0,0,0,0,0,0]
print(Hieroglyphics,)
Cuneiform = ("Cuneiform", "21$D", "0001 0101$B" "15$H", "Iron Age", "01$D", "1$H", 4, 20, 60, 180, 320, 450, 30, 50, "", "64,000+ BCE")
Cuneiform = [0,0,0,0,0,0,0]
print(Cuneiform,)
Alphabet = ("Alphabet", "22$D", "0001 0110$B" "16$H", "Iron Age", "01$D", "1$H", 4, 20, 60, 180, 320, 450, 30, 50, "", "64,000+ BCE")
Alphabet = [0,0,0,0,0,0,0]
print(Alphabet,)
Block_Printing = ("Block_Printing", "23$D", "0001 0111$B" "17$H", "Classical Antiquity", "02$D", "2$H", 4, 20, 60, 180, 320, 450, 30, 50, "", "64,000+ BCE")
Block_Printing = [0,0,0,0,0,0,0]
print(Block_Printing,)
Velum = ("Velum", "24$D", "0001 1000$B" "18$H", "Classical Antiquity", "02$D", "2$H", 4, 20, 60, 180, 320, 450, 30, 50, "", "64,000+ BCE")
Velum = [0,0,0,0,0,0,0]
print(Velum,)
Gall_Ink = ("Gall Ink", "25$D", "0001 1001$B" "19$H", "Late Antiquity", "02$D", "2$H", 4, 20, 60, 180, 320, 450, 30, 50, "", "64,000+ BCE")
Gall_Ink = [0,0,0,0,0,0,0]
print(Gall_Ink,)
Gutenberg_Press = ("Gutenberg Press", "26$D", "0001 1010$B" "1A$H", "Late Middle Ages", "05$D", "5$H", 4, 20, 60, 180, 320, 450, 30, 50, "", "64,000+ BCE")
Gutenberg_Press = [0,0,0,0,0,0,0]
print(Gutenberg_Press,)
Letter_Copying_Press = ("Letter Copying Press", "27$D", "0001 1011$B" "1B$H", "The Enlightenment", "07$D", "7$H", 4, 20, 60, 180, 320, 450, 30, 50, "", "64,000+ BCE")
Letter_Copying_Press = [0,0,0,0,0,0,0]
print(Letter_Copying_Press,)
Daguerreotype = ("Daguerreotype", "28$D", "0001 1100$B" "1C$H", "Modern Atomic Science", "08$D", "8$H", 4, 20, 60, 180, 320, 450, 30, 50, "", "64,000+ BCE")
Daguerreotype = [0,0,0,0,0,0,0]
print(Daguerreotype,)
Typewriter = ("Typewriter", "29$D", "0001 1101$B" "1D$H", "Modern Atomic Science", "08$D", "8$H", 4, 20, 60, 180, 320, 450, 30, 50, "", "64,000+ BCE")
Typewriter = [0,0,0,0,0,0,0]
print(Typewriter,)
Xerography = ("Xerography", "30$D", "0001 1110$B" "1E$H", "The Radioactive Age", "11$D", "B$H", 4, 20, 60, 180, 320, 450, 30, 50, "", "64,000+ BCE")
Xerography = [0,0,0,0,0,0,0]
print(Xerography,)
Word_Processor = ("Word Processor", "31$D", "0001 1111$B" "1F$H", "Age of the Microprocessor", "15$D", "F$H", 4, 20, 60, 180, 320, 450, 30, 50, "", "64,000+ BCE")
Word_Processor = [0,0,0,0,0,0,0]
print(Word_Processor,)


#a = ("", "32$D", "0010 0000$B" "20$H", "Iron Age", "01$D", "1$H", 6, 30, 90, 270, 400, 550, 50, 50, "", "2,000 to 4,000 BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "33$D", "0010 0001$B" "21$H", "Iron Age", "01$D", "1$H", 6, 30, 90, 270, 400, 550, 50, 50, "", "2,000 to 4,000 BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "34$D", "0010 0010$B" "22$H", "Iron Age", "01$D", "1$H", 6, 30, 90, 270, 400, 550, 50, 50, "", "2,000 to 4,000 BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "35$D", "0010 0011$B" "23$H", "Iron Age", "01$D", "1$H", 6, 30, 90, 270, 400, 550, 50, 50, "", "2,000 to 4,000 BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "36$D", "0010 0100$B" "24$H", "Iron Age", "01$D", "1$H", 6, 30, 90, 270, 400, 550, 50, 50, "", "2,000 to 4,000 BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "37$D", "0010 0101$B" "25$H", "Iron Age", "01$D", "1$H", 6, 30, 90, 270, 400, 550, 50, 50, "", "2,000 to 4,000 BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "38$D", "0010 0110$B" "26$H", "Iron Age", "01$D", "1$H", 6, 30, 90, 270, 400, 550, 50, 50, "", "2,000 to 4,000 BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "39$D", "0010 0111$B" "27$H", "Iron Age", "01$D", "1$H", 6, 30, 90, 270, 400, 550, 50, 50, "", "2,000 to 4,000 BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "40$D", "0010 1000$B" "28$H", "Iron Age", "01$D", "1$H", 6, 30, 90, 270, 400, 550, 50, 50, "", "2,000 to 4,000 BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "41$D", "0010 1001$B" "29$H", "Iron Age", "01$D", "1$H", 6, 30, 90, 270, 400, 550, 50, 50, "", "2,000 to 4,000 BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "42$D", "0010 1010$B" "2A$H", "Iron Age", "01$D", "1$H", 6, 30, 90, 270, 400, 550, 50, 50, "", "2,000 to 4,000 BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "43$D", "0010 1011$B" "2B$H", "Iron Age", "01$D", "1$H", 6, 30, 90, 270, 400, 550, 50, 50, "", "2,000 to 4,000 BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "44$D", "0010 1100$B" "2C$H", "Iron Age", "01$D", "1$H", 6, 30, 90, 270, 400, 550, 50, 50, "", "2,000 to 4,000 BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "45$D", "0010 1101$B" "2D$H", "Iron Age", "01$D", "1$H", 6, 30, 90, 270, 400, 550, 50, 50, "", "2,000 to 4,000 BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "46$D", "0010 1110$B" "2E$H", "Iron Age", "01$D", "1$H", 6, 30, 90, 270, 400, 550, 50, 50, "", "2,000 to 4,000 BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "47$D", "0010 1111$B" "2F$H", "Iron Age", "01$D", "1$H", 6, 30, 90, 270, 400, 550, 50, 50, "", "2,000 to 4,000 BCE")
#a = [0,0,0,0,0,0,0]
#print(,)


#a = ("", "48$D", "0011 0001$B" "30$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "49$D", "0011 0000$B" "31$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "50$D", "0011 0000$B" "32$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "51$D", "0011 0000$B" "33$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "52$D", "0011 0000$B" "34$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "53$D", "0011 0000$B" "35$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "54$D", "0011 0000$B" "36$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "55$D", "0011 0000$B" "37$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "56$D", "0011 0000$B" "38$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "57$D", "0011 0000$B" "39$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "58$D", "0011 0000$B" "3A$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "59$D", "0011 0000$B" "3B$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "60$D", "0011 0000$B" "3C$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "61$D", "0011 0000$B" "3D$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "62$D", "0011 0000$B" "3E$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "63$D", "0011 0000$B" "3F$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)


#a = ("", "64$D", "0100 0000$B" "40$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "65$D", "0100 0000$B" "41$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "66$D", "0100 0000$B" "42$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "67$D", "0100 0000$B" "43$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "68$D", "0100 0000$B" "44$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "69$D", "0100 0000$B" "45$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "70$D", "0100 0000$B" "46$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "71$D", "0100 0000$B" "47$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "72$D", "0100 0000$B" "48$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "73$D", "0100 0000$B" "49$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "74$D", "0100 0000$B" "4A$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "75$D", "0100 0000$B" "4B$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "76$D", "0100 0000$B" "4C$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "77$D", "0100 0000$B" "4D$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "78$D", "0100 0000$B" "4E$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "79$D", "0100 0000$B" "4F$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)


#a = ("", "80$D", "0101 0000$B" "50$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "81$D", "0101 0000$B" "51$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "82$D", "0101 0000$B" "52$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "83$D", "0101 0000$B" "53$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "84$D", "0101 0000$B" "54$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "85$D", "0101 0000$B" "55$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "86$D", "0101 0000$B" "56$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "87$D", "0101 0000$B" "57$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "88$D", "0101 0000$B" "58$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "89$D", "0101 0000$B" "59$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "90$D", "0101 0000$B" "5A$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "91$D", "0101 0000$B" "5B$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "92$D", "0101 0000$B" "5C$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "93$D", "0101 0000$B" "5D$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "94$D", "0101 0000$B" "5E$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "95$D", "0101 0000$B" "5F$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)


#a = ("", "96$D", "0110 0000$B" "60$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "97$D", "0110 0000$B" "61$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "98$D", "0110 0000$B" "62$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "99$D", "0110 0000$B" "63$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "100$D", "0110 0000$B" "64$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "101$D", "0110 0000$B" "65$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "102$D", "0110 0000$B" "66$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "103$D", "0110 0000$B" "67$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "104$D", "0110 0000$B" "68$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "105$D", "0110 0000$B" "69$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "106$D", "0110 0000$B" "6A$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "107$D", "0110 0000$B" "6B$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "108$D", "0110 0000$B" "6C$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "109$D", "0110 0000$B" "6D$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "110$D", "0110 0000$B" "6E$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "111$D", "0110 0000$B" "6F$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)


#a = ("", "112$D", "0111 0000$B" "70$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "113$D", "0111 0000$B" "71$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "114$D", "0111 0000$B" "72$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "115$D", "0111 0000$B" "73$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "116$D", "0111 0000$B" "74$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "117$D", "0111 0000$B" "75$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "118$D", "0111 0000$B" "76$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "119$D", "0111 0000$B" "77$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "120$D", "0111 0000$B" "78$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "121$D", "0111 0000$B" "79$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "122$D", "0111 0000$B" "7A$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "123$D", "0111 0000$B" "7B$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "124$D", "0111 0000$B" "7C$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "125$D", "0111 0000$B" "7D$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "126$D", "0111 0000$B" "7E$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "127$D", "0111 0000$B" "7F$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)


#a = ("", "128$D", "1000 0000$B" "80$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "129$D", "1000 0000$B" "81$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "130$D", "1000 0000$B" "82$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "131$D", "1000 0000$B" "83$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "132$D", "1000 0000$B" "84$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "133$D", "1000 0000$B" "85$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "134$D", "1000 0000$B" "86$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "135$D", "1000 0000$B" "87$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "136$D", "1000 0000$B" "88$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "137$D", "1000 0000$B" "89$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "138$D", "1000 0000$B" "8A$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "139$D", "1000 0000$B" "8B$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "140$D", "1000 0000$B" "8C$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "141$D", "1000 0000$B" "8D$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "142$D", "1000 0000$B" "8E$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "143$D", "1000 0000$B" "8F$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)


#a = ("", "144$D", "1001 0000$B" "90$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "145$D", "1001 0000$B" "91$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "146$D", "1001 0000$B" "92$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "147$D", "1001 0000$B" "93$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "148$D", "1001 0000$B" "94$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "149$D", "1001 0000$B" "95$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "150$D", "1001 0000$B" "96$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "151$D", "1001 0000$B" "97$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "152$D", "1001 0000$B" "98$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "153$D", "1001 0000$B" "99$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "154$D", "1001 0000$B" "9A$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "155$D", "1001 0000$B" "9B$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "156$D", "1001 0000$B" "9C$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "157$D", "1001 0000$B" "9D$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "158$D", "1001 0000$B" "9E$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "159$D", "1001 0000$B" "9F$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)


#a = ("", "160$D", "1010 0000$B" "A0$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "161$D", "1010 0000$B" "A1$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "162$D", "1010 0000$B" "A2$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "163$D", "1010 0000$B" "A3$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "164$D", "1010 0000$B" "A4$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "165$D", "1010 0000$B" "A5$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "166$D", "1010 0000$B" "A6$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "167$D", "1010 0000$B" "A7$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "168$D", "1010 0000$B" "A8$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "169$D", "1010 0000$B" "A9$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "170$D", "1010 0000$B" "AA$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "171$D", "1010 0000$B" "AB$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "172$D", "1010 0000$B" "AC$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "173$D", "1010 0000$B" "AD$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "174$D", "1010 0000$B" "AE$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "175$D", "1010 0000$B" "AF$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)


#a = ("", "176$D", "1011 0000$B" "B0$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "177$D", "1011 0000$B" "B1$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "178$D", "1011 0000$B" "B2$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "179$D", "1011 0000$B" "B3$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "180$D", "1011 0000$B" "B4$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "181$D", "1011 0000$B" "B5$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "182$D", "1011 0000$B" "B6$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "183$D", "1011 0000$B" "B7$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "184$D", "1011 0000$B" "B8$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "185$D", "1011 0000$B" "B9$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "186$D", "1011 0000$B" "BA$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "187$D", "1011 0000$B" "BB$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "188$D", "1011 0000$B" "BC$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "189$D", "1011 0000$B" "BD$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "190$D", "1011 0000$B" "BE$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "191$D", "1011 0000$B" "BF$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)


#a = ("", "192$D", "1100 0000$B" "C0$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "193$D", "1100 0000$B" "C1$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "194$D", "1100 0000$B" "C2$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "195$D", "1100 0000$B" "C3$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "196$D", "1100 0000$B" "C4$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "197$D", "1100 0000$B" "C5$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "198$D", "1100 0000$B" "C6$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "199$D", "1100 0000$B" "C7$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "200$D", "1100 0000$B" "C8$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "201$D", "1100 0000$B" "C9$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "202$D", "1100 0000$B" "CA$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "203$D", "1100 0000$B" "CB$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "204$D", "1100 0000$B" "CC$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "205$D", "1100 0000$B" "CD$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "206$D", "1100 0000$B" "CE$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "207$D", "1100 0000$B" "CF$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)


#a = ("", "208$D", "1101 0000$B" "D0$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "209$D", "1101 0001$B" "D1$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "210$D", "1101 0010$B" "D2$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "211$D", "1101 0011$B" "D3$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "212$D", "1101 0100$B" "D4$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "213$D", "1101 0101$B" "D5$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "214$D", "1101 0110$B" "D6$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "215$D", "1101 0111$B" "D7$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "216$D", "1101 1000$B" "D8$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "217$D", "1101 1001$B" "D9$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "218$D", "1101 1010$B" "DA$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "219$D", "1101 1011$B" "DB$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "220$D", "1101 1100$B" "DC$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "221$D", "1101 1101$B" "DD$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "222$D", "1101 1110$B" "DE$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "223$D", "1101 1111$B" "DF$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)


#a = ("", "224$D", "1110 0000$B" "E0$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "225$D", "1110 0000$B" "E1$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "226$D", "1110 0000$B" "E2$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "227$D", "1110 0000$B" "E3$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "228$D", "1110 0000$B" "E4$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "229$D", "1110 0000$B" "E5$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "230$D", "1110 0000$B" "E6$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "231$D", "1110 0000$B" "E7$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "232$D", "1110 0000$B" "E8$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "233$D", "1110 0000$B" "E9$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "234$D", "1110 0000$B" "EA$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "235$D", "1110 0000$B" "EB$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "236$D", "1110 0000$B" "EC$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "237$D", "1110 0000$B" "ED$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "238$D", "1110 0000$B" "EE$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "239$D", "1110 0000$B" "EF$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)


#a = ("", "240$D", "1111 0000$B" "F0$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "241$D", "1111 0000$B" "F1$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "242$D", "1111 0000$B" "F2$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "243$D", "1111 0000$B" "F3$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "244$D", "1111 0000$B" "F4$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "245$D", "1111 0000$B" "F5$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "246$D", "1111 0000$B" "F6$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "247$D", "1111 0000$B" "F7$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "248$D", "1111 0000$B" "F8$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "249$D", "1111 0000$B" "F9$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "250$D", "1111 0000$B" "FA$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "251$D", "1111 0000$B" "FB$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "252$D", "1111 0000$B" "FC$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "253$D", "1111 0000$B" "FD$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "254$D", "1111 0000$B" "FE$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "255$D", "1111 0000$B" "FF$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)


#a = ("", "256$D", "*0000 0000$B" "*00$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "257$D", "*0000 0000$B" "*01$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "258$D", "*0000 0000$B" "*02$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "259$D", "*0000 0000$B" "*03$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "260$D", "*0000 0000$B" "*04$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "261$D", "*0000 0000$B" "*05$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "262$D", "*0000 0000$B" "*06$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "263$D", "*0000 0000$B" "*07$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "264$D", "*0000 0000$B" "*08$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "265$D", "*0000 0000$B" "*09$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "266$D", "*0000 0000$B" "*0A$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "267$D", "*0000 0000$B" "*0B$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "268$D", "*0000 0000$B" "*0C$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "269$D", "*0000 0000$B" "*0D$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "270$D", "*0000 0000$B" "*0E$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "271$D", "*0000 0000$B" "*0F$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)


#a = ("", "272$D", "*0001 0000$B" "*10$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "273$D", "*0001 0000$B" "*11$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "274$D", "*0001 0000$B" "*12$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "275$D", "*0001 0000$B" "*13$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "276$D", "*0001 0000$B" "*14$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "277$D", "*0001 0000$B" "*15$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "278$D", "*0001 0000$B" "*16$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "279$D", "*0001 0000$B" "*17$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "280$D", "*0001 0000$B" "*18$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "281$D", "*0001 0000$B" "*19$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "282$D", "*0001 0000$B" "*1A$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "283$D", "*0001 0000$B" "*1B$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "284$D", "*0001 0000$B" "*1C$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "285$D", "*0001 0000$B" "*1D$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "286$D", "*0001 0000$B" "*1E$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "287$D", "*0001 0000$B" "*1F$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)


#a = ("", "288$D", "*0010 0000$B" "*20$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "289$D", "*0010 0000$B" "*21$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "290$D", "*0010 0000$B" "*22$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "291$D", "*0010 0000$B" "*23$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "292$D", "*0010 0000$B" "*24$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "293$D", "*0010 0000$B" "*25$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "294$D", "*0010 0000$B" "*26$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "295$D", "*0010 0000$B" "*27$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "296$D", "*0010 0000$B" "*28$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "297$D", "*0010 0000$B" "*29$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "298$D", "*0010 0000$B" "*2A$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "299$D", "*0010 0000$B" "*2B$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "300$D", "*0010 0000$B" "*2C$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "301$D", "*0010 0000$B" "*2D$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "302$D", "*0010 0000$B" "*2E$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "303$D", "*0010 0000$B" "*2F$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)


#a = ("", "304$D", "*0011 0000$B" "*30$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "305$D", "*0011 0000$B" "*31$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "306$D", "*0011 0000$B" "*32$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "307$D", "*0011 0000$B" "*33$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "308$D", "*0011 0000$B" "*34$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "309$D", "*0011 0000$B" "*35$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "310$D", "*0011 0000$B" "*36$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "311$D", "*0011 0000$B" "*37$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "312$D", "*0011 0000$B" "*38$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "313$D", "*0011 0000$B" "*39$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "314$D", "*0011 0000$B" "*3A$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "315$D", "*0011 0000$B" "*3B$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "316$D", "*0011 0000$B" "*3C$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "317$D", "*0011 0000$B" "*3D$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "318$D", "*0011 0000$B" "*3E$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "319$D", "*0011 0000$B" "*3F$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)


#a = ("", "320$D", "*0100 0000$B" "*40$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "321$D", "*0100 0000$B" "*41$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "322$D", "*0100 0000$B" "*42$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "323$D", "*0100 0000$B" "*43$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "324$D", "*0100 0000$B" "*44$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "325$D", "*0100 0000$B" "*45$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "326$D", "*0100 0000$B" "*46$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "327$D", "*0100 0000$B" "*47$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "328$D", "*0100 0000$B" "*48$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "329$D", "*0100 0000$B" "*49$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "330$D", "*0100 0000$B" "*4A$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "331$D", "*0100 0000$B" "*4B$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "332$D", "*0100 0000$B" "*4C$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "333$D", "*0100 0000$B" "*4D$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "334$D", "*0100 0000$B" "*4E$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "335$D", "*0100 0000$B" "*4F$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)


#a = ("", "336$D", "*0101 0000$B" "*50$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "337$D", "*0101 0001$B" "*51$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "338$D", "*0101 0010$B" "*52$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "339$D", "*0101 0011$B" "*53$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "340$D", "*0101 0100$B" "*54$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "341$D", "*0101 0101$B" "*55$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "342$D", "*0101 0110$B" "*56$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "343$D", "*0101 0111$B" "*57$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "344$D", "*0101 1000$B" "*58$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "345$D", "*0101 1001$B" "*59$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "346$D", "*0101 1010$B" "*5A$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "347$D", "*0101 1011$B" "*5B$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "348$D", "*0101 1100$B" "*5C$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "349$D", "*0101 1101$B" "*5D$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "350$D", "*0101 1110$B" "*5E$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)
#a = ("", "351$D", "*0110 1111$B" "*5F$H", "Stone Age", "01$D", "1$H", 0, 0, 0, 000, 000, 000, 00, 00, "", " BCE")
#a = [0,0,0,0,0,0,0]
#print(,)





print("\nThanks for playing ... you rolled",rolls,"times.\n")




