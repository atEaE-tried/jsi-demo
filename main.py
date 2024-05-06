from model import jsi_mini

def main():
	list = jsi_mini.ItemList()
	for item in list:
		print(item.title)

if __name__ == "__main__":
	main()