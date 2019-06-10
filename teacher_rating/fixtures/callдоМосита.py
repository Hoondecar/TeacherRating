import json

def create_chair():
	try:
		with open("Кафедра корпоративных информационных систем (КИС).txt") as file:
			name_chair = []
			for i in file:
				name_chair.append(i)
	except:
		print("ERROR")
	return(name_chair)

if __name__=="__main__":
	name_chair = create_chair()
	persons = []
	posts = []
	#print(name_chair)
	for i,word in enumerate(name_chair):
		if i%2 != 0:
			posts.append([word])
		else:
			if word!=[]:	
				persons.append(word.split())

	lastname = []
	name = []
	patronymic = []
	post = []
	chair = 'ВТ'
	for person in persons:
		lastname.append(person[1])
		name.append(person[2])
		patronymic.append(person[3])
	for p in posts:
		try:
			if p[1] == 'старший' or p[1] == 'Старший' or p[1] == 'зав.':
				post.append(p[1]+" "+p[2])	
			else:
				post.append(p[1])
		except :
			post.append('')
	data = []
	for i,man in enumerate(lastname):
		data.append({'model':'teacher_rating.teacher',
					'pk':48+i,
		 			  'fields':{'name': name[i],
					   'lastname': man,
					   'patronymic': patronymic[i],
					   'post': post[i],
					   	'desription':'',
				   		'chair':4}})
	print(data)

	with open("data_file.json", "w") as write_file:
		json.dump(data, write_file)



