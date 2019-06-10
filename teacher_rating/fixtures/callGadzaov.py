import json

def create_chair():
	try:
		with open("Кафедра прикладной математики (ПМ).txt") as file:
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
			if word!='\t \t\t\t \t\t \t \n' and word!='\n'  and word!='\t\t\t\n':
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
			try:
				lastname.append(person[1])
			except:
				pass
			try:
				name.append(person[2])
			except:
				pass
			try:
				patronymic.append(person[3])
			except:
				pass
	for p in posts:
		try:
			print(p[0].split()[6])
			if p[0].split()[6] == 'старший' or p[0].split()[6] == 'Старший' or p[0].split()[6] == 'зав.':
				post.append(p[0].split()[6]+" ")	
			else:
				post.append(p[0].split()[6])
		except :
			post.append('')
	post.insert(0,'')
	print(post)
	for i in range(3):
		post.append('')
	print(lastname)
	data = []
	for i,man in enumerate(lastname):
		data.append({'model':'teacher_rating.teacher',
					'pk':82+i,
		 			  'fields':{'name': name[i],
					   'lastname': man,
					   'patronymic': patronymic[i],
					   'post': post[i],
					   	'desription':'',
				   		'chair':6}})
	print(data)

	with open("data_file.json", "w") as write_file:
		json.dump(data, write_file)



