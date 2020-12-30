import re
pa=input('Enter your password: ')
if len(pa)>=8:
	if(re.findall(r'[a-z]',pa)):
		if(re.findall(r'[A-Z]',pa)):
			if(re.findall(r'[1-9]',pa)):
				if(re.findall(r'[$*@]',pa)):
					print("strong")
					exit()
print("reenter")
	
