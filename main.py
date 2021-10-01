# The INV shell v0.1b
# Template shell to run your own functions as commands.
# Useful for sandboxing, optimizing your work, anything really
# Add commands to the func_dict along with the function they'll execute when called

def test(): #test function to see if everything works, ignore it
	print("success")

def default(): #is called whenever the user types a command that isn't in the dictionary
	print("unknown command\ntype 'help' to see all available commands")

def help(): #prints all commands and where their equivalent function is stored in the cpu (yes, its pointer, really)
	for key, value in func_dict.items():
		print(key, ' : ', value)
	print("exit : closes shell") #the exit command is in the main loop (in main function, while running loop) so it isn't in the func_dict

func_dict = {'test':test, 'help':help, 'default':default} #dictionary with all commands and their equivalent function
def main():
	running = True
	while running:
		cmd = input("> ")
		if cmd == "exit":
			break
		func_dict.get(cmd, default)()



if __name__ == "__main__":
	main()