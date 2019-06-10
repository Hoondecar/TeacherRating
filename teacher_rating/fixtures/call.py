import json

def create_chair():
	try:
		with open("Кафедра практической и прикладной информатики (ППИ).txt") as file:
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
	post_descr = []
	#print(name_chair)
	for i,word in enumerate(name_chair):
		if i%2 != 0:
			if word!='\t\t\t\t \t\t\t \t\t \t \n' and word!='\t\t\n':
				post_descr.append(word)
			else:
				if post_descr!=[]:	
					posts.append(post_descr)
					post_descr=[]
		else:	
			persons.append(word.split())

	lastname = []
	name = []
	patronymic = []
	post = []
	description = []
	chair = 'ВТ'
	for person in persons:
		if person !=[]:
			try:
				lastname.append(person[1])
			except:
				lastname.append('')
			try:
				name.append(person[2])
			except:
				name.append('')
			try:
				patronymic.append(person[3])
			except:
				patronymic.append('')
	for p in posts:
		try:
			if p[0].split()[2] == 'старший' or p[0].split()[2] == 'Старший' or p[0].split()[2] == 'заведующий':
				post.append(p[0].split()[2]+" "+p[0].split()[3])	
			else:
				post.append(p[0].split()[2])
			description.append(p[1:])
		except :
			post.append('')
	descriptions = []
	string = ''
	for word in description:
		for i in word:
			string += i.expandtabs(0)
		descriptions.append([string.replace('\n','. ')])
		string = ''
	data = []
	print(name)
	for i,man in enumerate(lastname):
		data.append({'model':'teacher_rating.teacher',
					'pk':80+i,
		 			  'fields':{'name': name[i],
					   'lastname': man,
					   'patronymic': patronymic[i],
					   'post': post[i],
					   	'desription':str(descriptions[i][0]),
				   		'chair':7}})
	print(data)

	with open("data_file.json", "w") as write_file:
		json.dump(data, write_file)



