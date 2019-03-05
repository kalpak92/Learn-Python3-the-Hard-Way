from sys import argv

script, filename = argv

def main(languages, encoding, errors):
	line = languages.readline()

	if line:
		print_line(line, encoding, errors)
		return main(line, encoding, errors)

def print_line(line, encoding, errors):
	next_line = line.strip()
	raw_bytes = next_line.encode(encoding, errors=errors)
	cooked_string = raw_bytes.decode(encoding, errors=errors)

	print(raw_bytes, "<==>", cooked_string)

languages = open(filename, encoding="utf-8")

main(languages, "utf-8", "strict")
