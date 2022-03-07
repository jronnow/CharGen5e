import random

# Take a chance, roll the dice
# Also, it's a lot better than having to type "random.randrange" every single time
def roll(dice):
	return random.randrange(1, dice+1)

# 4d6, drop lowest
def AbilityScore():
	results = []
	for i in range(4):
		results.append(roll(6))
	sorted(results)
	# Drop lowest
	del results[0]
	return sum(results)

# If you want to generate the values and strategically assign them to abilities - will implement later
def ManualStats():
	stats = []
	for i in range(6):
		stats.append(AbilityScore())
	return stats

# If you want to simply roll stats down the sheet and live with your poor choices
def AutoStats():
	stats = {
	  "STR": AbilityScore(),
	  "DEX": AbilityScore(),
	  "CON": AbilityScore(),
	  "INT": AbilityScore(),
	  "WIS": AbilityScore(),
	  "CHA": AbilityScore()
	}
	return stats

# Choose between ManualStats and AutoStats - will implement alongside ManualStats
def ChooseMethod():
	while True:
		stats = input("Assign ability scores manually? Y/n")
		if stats.casefold() == "y":
			return AutoStats()
		elif stats.casefold() == "n":
			return ManualStats()
		else:
			print("Invalid input, please try again")

def SelectName():
	return random.choice(['Aadi', 'Aamir', 'Aarna', 'Aarush', 'Abbie', 'Ada', 'Addison', 'Adilene', 'Aidan', 'Alaysia', 'Alek', 'Alessia', 'Alexander', 'Aleyna', 'Alia', 'Aliah', 'Alice', 'Alton', 'Amia', 'Amyah', 'Anas', 'Angelina', 'Annabelle', 'Anne', 'Archer', 'Arlo', 'Arman', 'Ashlee', 'Ashly', 'Ashton', 'Audrey', 'August', 'Averi', 'Avian', 'Ayanna', 'Ayden', 'Ayleen', 'Baron', 'Benny', 'Blanca', 'Blythe', 'Brantly', 'Bridget', 'Brody', 'Bryanna', 'Caitlyn', 'Calista', 'Callie', 'Calliope', 'Camdyn', 'Carlton', 'Carver', 'Cassandra', 'Charity', 'Charli', 'Chelsey', 'Cherish', 'Christina', 'Claira', 'Claira', 'Clinton', 'Cole', 'Coleson', 'Colleen', 'Cooper', 'Corbyn', 'Corinne', 'Cory', 'Dakota', 'Dalila', 'Darien', 'Dashiell', 'Daylen', 'Della', 'Demario', 'Desean', 'Destin', 'Dewayne', 'Diamond', 'Donovan', 'Dontae', 'Dylan', 'Earl', 'Eian', 'Eisley', 'Eli', 'Elizabeth', 'Elora', 'Elyas', 'Emery', 'Esme', 'Estefania', 'Eve', 'Evelynn', 'Florence', 'Fredrick', 'Gabriela', 'Genevieve', 'German', 'Giovani', 'Giovanny', 'Grayson', 'Greyson', 'Hadassah', 'Hampton', 'Hamza', 'Hannah', 'Harmony', 'Heavenly', 'Henley', 'Herman', 'Inara', 'Isael', 'Issac', 'Izel', 'Jabari', 'Jada', 'Jair', 'Jaleah', 'Janae', 'Jane', 'Jariel', 'Jarvis', 'Jaycee', 'Jayceon', 'Jayden', 'Jaydon', 'Jaylynn', 'Jayson', 'Jazzlyn', 'Jeancarlos', 'Jenni', 'Jericho', 'Jessa', 'Jimmie', 'Jiovanni', 'Joslynn', 'Juliet', 'Kael', 'Kahlil', 'Kahlil', 'Kaiya', 'Kaliyah', 'Kalli', 'Kamren', 'Karson', 'Kasen', 'Katherine', 'Katie', 'Katrina', 'Kayden', 'Kaylie', 'Kaylin', 'Keven', 'Khloee', 'Khristian', 'Kirsten', 'Klayton', 'Knox', 'Korbin', 'Korbyn', 'Kye', 'Lachlan', 'Lamar', 'Lara', 'Leela', 'Leeland', 'Legend', 'Lester', 'Lilia', 'Lloyd', 'Logan', 'Lucian', 'Lucille', 'Lucy', 'Maddux', 'Malaki', 'Maleek', 'Maliah', 'Marcos', 'Marcus', 'Markel', 'Marvin', 'Masen', 'Maura', 'Mayah', 'Mccoy', 'Menachem', 'Mia', 'Mia', 'Mika', 'Milagros', 'Milan', 'Milla', 'Moriah', 'Natasha', 'Nathaly', 'Nathaly', 'Neveah', 'Neveah', 'Niall', 'Nicole', 'Nicolette', 'Nikole', 'Ocean', 'Paula', 'Perla', 'Petra', 'Philip', 'Phineas', 'Preslee', 'Prince', 'Princess', 'Raeleigh', 'Raleigh', 'Rayne', 'Rebecca', 'Reece', 'Rhea', 'Rocky', 'Rodrick', 'Roxana', 'Russell', 'Saylor', 'Scarlet', 'Sebastian', 'Selina', 'Seraphina', 'Shaniya', 'Shayan', 'Shyann', 'Sky', 'Stephon', 'Sunny', 'Syed', 'Taraji', 'Tavin', 'Teagan', 'Tess', 'Thorin', 'Tripp', 'Valentino', 'Wade', 'Wallace', 'Westen', 'Yael', 'Yamilet', 'Yarely', 'Yasmin', 'Youssef', 'Zaden', 'Zavion', 'Zayn', 'Zev', 'Zyon'])

# This will be a lot more complicated when ManualStats is implemented
Stats = AutoStats()

Level = roll(20)

# To do: add non-PHB races and implement mechanic for deciding whether to use them
Race = random.choice(['Dragonborn', 'Dwarf', 'Elf', 'Gnome', 'Half-Elf', 'Halfling', 'Half-Orc', 'Human', 'Tiefling'])

# To do: add non-PHB classes and implement mechanic for deciding whether to use them
Class = random.choice(['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard'])

# Because the people who wrote English didn't think numerical suffixes would ever be important
if Level == 1:
	suffix = "st"
elif Level == 2:
	suffix = "nd"
elif Level == 3:
	suffix = "rd"
else:
	suffix = "th"

CharacterText = SelectName() + " is a " + str(Level) + suffix + " level " + Race + " " + Class + " with a " + max(Stats, key=Stats.get) + " build."

print(CharacterText)
