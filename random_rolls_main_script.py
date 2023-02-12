import random

#Meyer's_Original_Technpoly.py - TECHNOPOLY
print("Developed by Randall Meyer (with code partially derived from Stephen Hustedde's MONOPOLY ROLLS program.)\n")
print("""This game is a tool to teach three different lessons to students of the sciences and humanities.
The first game (I) can be played like that other more boring and inaccurate game developed in 1915 by Lizzie Maggie and sometimes referred to as 'The Landlord's Game'.
The second game, (II), provides a more accurate lesson of the TECHVOLUTION of the human animal, wherein each physical address is replaced
The Third Game, (III), has players collect Op Code Cards and Digital Data Cards, and actually hand program a schematic moidel of the vintage 6502 microproceesor from 1975.\n""")

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
print("Technopoly! You are currently on GO ")
roll_em = raw_input("Press the Enter key to roll the dice (enter x to end): ")

while (roll_em.upper() != "x") :
	die1 = random.randint(1,6)
	die2 = random.randint(1,6)
	total = die1 + die2
	rolls += 1
	current = (current + total) % 39 # add total roll to current location and use modulus too
	mySpace = spaces[current]
	print('\nYou rolled a {0} and a {1} for a total of {2}. You\'re at "{3}".'.format(die1, die2, total, mySpace.upper()))
	roll_em = raw_input("Press Enter to roll the dice again (enter x to end):")


	
print("\nThanks for playing ... you rolled",rolls,"times.\n")	






