import random
def disp(n):
	if n==0:
		return "Rock"
	elif n==1:
		return "Paper"
	elif n==2:
		return "Scissors"

def play():
	ch_alpha=str(input("Enter your choice. (R/P/S)"))
	if ch_alpha!='R' and ch_alpha!='P' and ch_alpha!='S':	
		print("Invalid Input")
		play()
	l=['R','P','S']
	ch=l.index(ch_alpha)
	cpu_ch=random.randint(0,2)
	print(f"You chose {disp(ch)}. CPU chose {disp(cpu_ch)}")
	if ch==cpu_ch:
		print("Draw")
	elif (ch==0 and cpu_ch==1) or (ch==1 and cpu_ch==2) or (ch==2 and cpu_ch==0):
		print("CPU wins")
	else:
		print("You win!")
	choice=str(input(("Continue?(Y/N)")))
	if choice=='Y':
		play()
play()
