def interface():
	print("My cal program")
	keeprun = True
	while keeprun:
		print("Option")
		print("9 -Quit")
		choice = input("Enter your choice:")
		if choice == '9':
        keeprun = False
			return
		return
if __name__ == "__main__":
	interface()
