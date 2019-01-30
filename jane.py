def string_man():
	with open('a.svg', 'r') as f:
		data = f.read()

	start = data.find('<path')
	end = data.find('</g') + 4

	rep = data[start:end]

	data = data.replace(rep, '')

	f.close()

	with open('a.svg', 'w') as f:
		f.write(data)

string_man()
