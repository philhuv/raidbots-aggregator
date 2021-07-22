CHARACTER_FILE = 'characters.txt'

def get_characters():
	characters = open(CHARACTER_FILE, "r").read().split("\n")

	return characters if characters[-1] != '' else characters[:-1]

def add_character(char_name):
	characters = open(CHARACTER_FILE, "r").read().split('\n')
	if char_name in characters:
		return
	characters.append(char_name)
	f = open(CHARACTER_FILE, "a")
	f.write(f'{char_name}\n')
	f.close()