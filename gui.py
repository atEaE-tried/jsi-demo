from app import app

def main():
	window = app.JSIApp()
	window.mainloop()


# # Windowを生成する
# def createWindow() -> Tk:
# 	window = Tk()

# 	# Window setting
# 	window.title("JSI-mini Demo")
# 	window.geometry("800x600")
	
# 	# Header setting
# 	head = Frame(window)
# 	Label(head, text="JSI-mini Demo", font=("Helvetica", 16)).pack()
# 	head.pack()

# 	# Landing View setting
# 	main = Frame(window)
# 	main.pack()

# 	paddingX = 5
# 	paddingY = 5
# 	sticky = "w"

# 	## row
# 	row = 1
# 	Label(main, text="被験者氏名", wraplength=300, justify="left").grid(row=row, column=0, padx=paddingX, pady=paddingY, sticky=sticky)
# 	Entry(main).grid(row=row, column=1, padx=paddingX, pady=paddingY, sticky=sticky)
	
# 	## row
# 	row = 2
# 	Label(main, text="検査者氏名", wraplength=300, justify="left").grid(row=row, column=0,padx=paddingX, pady=paddingY, sticky=sticky)
# 	Entry(main).grid(row=row, column=1, padx=paddingX, pady=paddingY, sticky=sticky)

# 	return window

if __name__ == "__main__":
	main()