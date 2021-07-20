
# *** IMPORTS ***

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

 
# *** QUESTIONS AND ANSWER LISTS ***

techQuestionsList=[
'''The x86 instruction set was built by which
   company?''',

'Python is written in? (Base Language)',

'macOS is based on which older Operating System ?', #parameter for length

'Who created the Linux kernel?',

'What is the full-form of TOR ?',

'Which company acquired MySQL in 2010 ?',

'What is the default file system for Windows?',

'Who launched the first website?',

'Which game had the first recorded Easter Egg?',

'''Who created Unix and the C programming language
 along with Ken Thompson'''
]

techAnswersList=['Intel','C','Unix','Linus Trovalds','The Onion Project','Oracle','NTFS','CERN','Adventure','Dennis Ritchie']


historyQuestionsList=[
'''Which is the oldest civilization known to 
mankind ?''',

"Adolf Hitler was born in which country ?",

'''What is the name of the only Indian Governer 
General of India ? (last name only) ''',

'''The current monarch of the United Kingdom,
   belongs to the House of ________ ?''',

''' Who wrote the first draft of the 'Declaration 
of Indpendence' ? ''' ,

''' Under which Prussian statesman did Germany 
unify in 1871 ? ''',

''' What was the name of New York before being 
acquired by the English ?''',

''' Babur was related to which Turco-Mongol
 nomadic conqueror on his father's side ?''',

''' Who was the first female Chief Minister of an 
Indian State ?''',

'''The Second World War commenced with the invasion
of which country ?''']	

historyAnswersList=['Sumer','Austria','Rajagopalchari','Windsor','Thomas Jefferson','Otto von Bismarck','New Amsterdam','Timur','Sucheta Kripalani','Poland']


gkQuestionsList=[
'''Which is the tallest mountain in the world from 
sea floor?''',

'''Albert Einstien was awarded the Nobel Prize for
his dicoveries in ?''',

'''Who invented Calculas independently, alongside 
Isaac Newton?''',

'''Who was the first woman to circumnavigate the 
globe?''',

'What was the previous name of Mount Everest?',

'''What was the code name of the Indian Operation 
in the Kargil War?''',

"Who won the first men's FIFA World Cup?",

'''Which was the last Indian territory to be
 liberated from foreign rule''',

'''Which actor voiced both Darth Vader and The Lion 
King‘s Mufasa?''',

'The Republic of China is more commonly known as?'
]

gkAnswersList=['Mauna Kea','Photoelectric Effect','Leibniz','Jeanne Baret','Peak XV','Operation Vijay','Uruguay','Goa','James Earl Jones','Taiwan']


# *** FUNCTIONS ***

def main():
	#  FIRST WINDOW / MAIN MENU
	global mainroot,root,titleLabel,playBt,aboutBt,quitBt
	mainroot=Tk()
	mainroot.configure(bg='black')
	#mainroot.resizable(False,False)
	mainroot.title('QUIZ TIME!')
	mainroot.geometry('{}x{}'.format(940,600))

	root = Canvas(mainroot)
	root.pack(fill=BOTH,expand=1)

	#applying wallpaper to the canvas
	bg = PhotoImage(file='background.png')
	img1=root.create_image(0, 0, image=bg, anchor=NW)
	root.tag_lower(img1)

	titleLabel = Label(root,fg='#39FF14',bg='black',text="QUIZ TIME!",font=('Century Gothic',55,'bold'))
	titleLabel.place(x=290,y=45)

	playBt=ttk.Button(root,style='my.TButton',text='PLAY',command=registerWindow)
	playBt.place(x=405,y=235)

	aboutBt=ttk.Button(root,style='my.TButton',text='ABOUT',command=aboutWindow)
	aboutBt.place(x=405,y=315)

	quitBt=ttk.Button(root,style='my.TButton',text='QUIT',command=root.destroy)
	quitBt.place(x=405,y=395)

	# STYLING TTK BUTTONS
	ttk.Style().configure('my.TButton',font=('Consolas',12,'bold'))
	ttk.Style().configure('submit.TButton',font=('Consolas',12,'bold'),background='red')

	root.mainloop()

def registerWindow():
	global mainLabel,nameLabel,timerLabel,nameEntry,ageLabel,ageEntry,nextBt
	# REMOVING ROOT MENU'S WIDGETS
	titleLabel.place_forget()
	playBt.place_forget()
	aboutBt.place_forget()
	quitBt.place_forget()

	mainLabel = Label(root,fg='#39FF14',bg='black',text="~ ENTER DETAILS ~",font=('Century Gothic',30,'bold'))
	mainLabel.place(x=305,y=80)

	nameLabel = Label(root,fg='#39FF14',bg='black',width=20,text="Your Name:",font=('Century Gothic',20))
	nameLabel.place(x=300,y=180)
	nameEntry = ttk.Entry(root,width=35,font=('Calibri',11,'bold'))
	nameEntry.place(x=340,y=250)

	nextBt=ttk.Button(root,style='my.TButton',text='NEXT',command=selectGameModeWindow)
	nextBt.place(x=410,y=430)

	timerLabel=Label(root,fg='white',bg='black',text='',font=('Century Gothic',18))
	timerLabel.place(x=830,y=10)


def selectGameModeWindow():
	global mode1,mode2,mode3
	mainLabel.place_forget()
	nameLabel.place_forget()
	nameEntry.place_forget()
	nextBt.place_forget()

	mode1=ttk.Button(root,style='my.TButton',text='TECH',command=lambda:instructWindow('TECH'))
	mode1.place(x=405,y=150)

	mode2=ttk.Button(root,style='my.TButton',text='GENERAL KNOWLEDGE',command=lambda:instructWindow('GK'))
	mode2.place(x=385,y=245)

	mode3=ttk.Button(root,style='my.TButton',text='HISTORY',command=lambda:instructWindow('HISTORY'))
	mode3.place(x=405,y=345)


def instructWindow(mode):
	global Label0,Label1,nextBt2
	#if(ageEntry.get()!="" and nameEntry.get!="" ):
		# REMOVING REGISTER WINDOW'S WIDGETS
	mode1.place_forget()
	mode2.place_forget()
	mode3.place_forget()

	Label0 = Label(root,fg='#39FF14',bg='black',text="~ INSTRUCTIONS ~",font=('Century Gothic',30,'bold'))
	Label0.place(x=305,y=80)

	Label1= Label(root,fg='#39FF14',bg='black',text="1.   Don't Be Stupid ",font=('Century Gothic',16))
	Label1.place(x=355,y=295)

	nextBt2=ttk.Button(root,style='my.TButton',text='NEXT',command=lambda:questionWindow(mode))
	nextBt2.place(x=405,y=485)

def questionWindow(mode):
	global gameMode,quesLabel,answerEntry,submitButton,skipButton,qNum,resultLabel,scoreLabel,score,userdataList,endButton

	Label0.place_forget()
	Label1.place_forget()
	nextBt2.place_forget()

	gameMode=mode
	startTimer(0,0)

	# PLACING WIDGETS
	quesLabel=Label(root,fg='#39FF14',bg='black',text='',font=('Consolas',15,'bold'))
	quesLabel.place(x=210,y=160)        #Label for displaying questions


	answerEntry=ttk.Entry(root, width=28,font=('Calibri',11,'bold'))
	answerEntry.place(x=365,y=245)       #Entry for typing answers

	submitButton= ttk.Button(root,style='submit.TButton',text='SUBMIT',command=nextQues)
	submitButton.place(x=490,y=330)

	skipButton= ttk.Button(root,style='my.TButton',text='SKIP',command=skip)
	skipButton.place(x=340,y=330)

	scoreLabel=Label(root,fg='white',bg='black',text='SCORE - 0',font=('Century Gothic',18,'bold'))
	scoreLabel.place(x=20,y=10)

	resultLabel=Label(root,fg='#39FF14',bg='black',text='',font=('Calibri',12))
	resultLabel.place(x=400,y=385)

	endButton=ttk.Button(root,style='my.TButton',text='END QUIZ',command=completionWindow)

	# selecting mode to display the first question
	
	if gameMode=='TECH':
		quesLabel.configure(text='Q1'+' '+techQuestionsList[0])

	elif gameMode=='GK':
		quesLabel.configure(text='Q1'+' '+gkQuestionsList[0])

	elif gameMode=='HISTORY':
		quesLabel.configure(text='Q1'+' '+historyQuestionsList[0])

	# SETTING VARIABLES
	qNum=0
	score=0
	
	# ADDING DETAILS TO THE USER'S LIST 
	userdataList=[nameEntry.get()+'\t'+'\t',gameMode+'\t'+'\t']

def startTimer(m,s):
	global minutes,seconds
	minutes=m
	seconds=s

	if s <= 9:
		timerLabel.config(text='0'+str(m)+':'+'0'+str(s))
	else:
		timerLabel.config(text='0'+str(m)+':'+str(s))
	s+=1

	if s==59:
		m+=1
		s=0
	root.after(1000, lambda:startTimer(m,s))

def configMode():
	global QuestionsList,AnswersList

	# ASSIGNING THE GAME MODE, ITS Q & A LISTS

	if gameMode == 'TECH':
		QuestionsList = techQuestionsList
		AnswersList = techAnswersList

	elif gameMode == 'GK':
		QuestionsList = gkQuestionsList
		AnswersList = gkAnswersList

	elif gameMode == 'HISTORY':
		QuestionsList = historyQuestionsList
		AnswersList = historyAnswersList

def nextQues():
	global qNum,score,userdataList

	ans=answerEntry.get()
	resultLabel.configure(text='')

	configMode()

# CHECKING THE ANSWER (by matching corr. index no.)
	
	correctAnswer = AnswersList[qNum]
	# Special condition for last question
	if qNum==9 and ans.lower() == correctAnswer.lower():        
		score+=10
		scoreLabel.configure(text='SCORE '+ str(score))
		resultLabel.configure(text='Correct!',fg='#99ff33')

		# disabling the submit & skip buttons  after last question
		submitButton.configure(state='disabled')
		skipButton.configure(state='disabled')

		endButton.place(x=410,y=440)
		# adding user's score to the user's list
		userdataList.append(str(score)+'\t'+'\t') 


	elif ans.lower() == correctAnswer.lower():
		qNum+=1
		quesLabel.configure(text='Q'+ str(qNum+1) +' '+ QuestionsList[qNum]) #changing question
		answerEntry.delete(0, END)
		score+=10											                 # increasing score
		scoreLabel.configure(text='SCORE - '+ str(score))
		# showing result (1.if right)
		resultLabel.configure(text='Correct!',fg='#99ff33')

	else:
		# showing result (2.if wrong)
		resultLabel.configure(text='Wrong Answer, try again or skip to the next question',fg='red')

def getTime():
	global timeTaken
	if qNum==9:
		timerLabel.place_forget()
		timeTaken= str(minutes)+'m '+str(seconds) +'s'
		print(timeTaken)

		timeString=str(timeTaken+'\n')
		userdataList.append(timeString)


def completionWindow():
	global userdataList,completionLabel,nextBt3

	quesLabel.place_forget()
	answerEntry.place_forget()
	submitButton.place_forget()
	skipButton.place_forget()
	scoreLabel.place_forget()
	resultLabel.place_forget()
	endButton.place_forget()

	getTime() # calling function to get the time taken by the user

	timerLabel.config(text=' ')
	completionLabel=Label(root,text='~ QUIZ COMPLETED! ~',fg='#39FF14',bg='black',font=('Century Gothic',38,'bold'))
	completionLabel.place(x=230,y=200)

	nextBt3=ttk.Button(root,style='my.TButton',text='NEXT',command=resultWindow)
	nextBt3.place(x=405,y=485)

def resultWindow():
	completionLabel.place_forget()
	nextBt3.place_forget()

	headerLabel=Label(root,text='NAME         MODE         SCORE         TIME',fg='#007a21',bg='black',font=('Century Gothic',20,'bold'))
	headerLabel.place(x=200,y=70)

	exitBt=ttk.Button(root,style='my.TButton',text='EXIT',command=mainroot.destroy)
	exitBt.place(x=405,y=485)

	print(userdataList)

	f=open('userdata.txt','a+')
	f.writelines(userdataList)
	f.close()

	f=open('userdata.txt','r+')
	length=len(f.readlines() )
	f.close()
	xLen=200
	yLen=120

	f=open('userdata.txt','r+')
	for i in range(length):
		yLen+=40
		result=Label(root,text=f.readline(),fg='#39FF14',bg='black',font=('Consolas',14,'bold'))
		result.place(x=xLen,y=yLen)
	f.close()


# FOR THE SKIP BUTTON IN QUESTION WINDOW
def skip():

	configMode()
	global qNum,userdataList

	# Special condition for last question
	if qNum==9:
		messagebox.showinfo(' ','The correct answer was '+AnswersList[qNum-1])

		skipButton.configure(state='disabled')
		submitButton.configure(state='disabled')

		userdataList.append(str(score)+'\t'+'\t')
		endButton.place(x=410,y=440)

	else:
		# DISPLAYING NEXT QUESTION
		qNum+=1
		quesLabel.configure(text='Q'+ str(qNum+1) +' '+ QuestionsList[qNum])
		answerEntry.delete(0, END)

		# SHOWING THE CORRECT ANSWER FOR THE SKIPPED QUESTION
		messagebox.showinfo(' ','The correct answer was '+AnswersList[qNum-1])


def aboutWindow():
	global aboutLabel,backBt
	titleLabel.place_forget()
	playBt.place_forget()
	aboutBt.place_forget()
	quitBt.place_forget()

	aboutLabel=Label(root,fg='#39FF14',bg='black',text='''Made by Ekagra Nigam of XII-A using Python 3 and the
	 tkinter library for class 12th Final practical project''',font=('Consolas',15))
	aboutLabel.place(x=110,y=100)
	backBt=ttk.Button(root,style='my.TButton',text='BACK',command=back)
	backBt.place(x=410,y=430)

# What are you doing here?

def back(): # FOR THE BACK BUTTON IN ABOUT WINDOW
	# removing About window's widgets
	aboutLabel.place_forget()
	backBt.place_forget()

	 # recreating root menu
	titleLabel.place(x=310,y=60)
	playBt.place(x=425,y=180)
	aboutBt.place(x=425,y=260)
	quitBt.place(x=425,y=340)

# *** MAIN ***
if __name__ == "__main__":
	main()