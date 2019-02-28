print('''.88b  d88. db    db db      d888888b d888888b d8888b. d8888b. d888888b d8b   db d888888b d88888b d8888b. 
88'YbdP`88 88    88 88      `~~88~~'   `88'   88  `8D 88  `8D   `88'   888o  88 `~~88~~' 88'     88  `8D 
88  88  88 88    88 88         88       88    88oodD' 88oobY'    88    88V8o 88    88    88ooooo 88oobY' 
88  88  88 88    88 88         88       88    88~~~   88`8b      88    88 V8o88    88    88~~~~~ 88`8b   
88  88  88 88b  d88 88booo.    88      .88.   88      88 `88.   .88.   88  V888    88    88.     88 `88. 
YP  YP  YP ~Y8888P' Y88888P    YP    Y888888P 88      88   YD Y888888P VP   V8P    YP    Y88888P 88   YD ''')                                                                                                       
                                                                                                       
x = input('Enter your text you want to repeat:')
y = input('Enter file name(no extension) you want to store it in:')
z = int(input('Enter no of time you want to repeat:'))

name = open(y+'.txt','w')
for n in range(0,z):
	lol = name.write(x)
	lol = name.write('\n')
name.close()
print("Your outputed text has been stored in "+y+'.txt')