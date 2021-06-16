# Text Editor - Notepad style application that can open, edit, and save text documents.
# Optional: Add syntax highlighting and other features.

while(True):
    def choice_text():
        choice = int(input(
            "enter 1 to read a text file\nenter 2 for creating a new text file\nenter 3 for editing a already text file\nenter 4 for deleting a already text file\n"))
        if choice == 1:
            read_text()
        elif choice == 2:
            new_text()
        elif choice == 3:
            edit_text()
        elif choice == 4:
            del_text()
        else:
            print("invalid input sorry")

    def read_text():
        name = input("enter the text file name:\n")
        name = name+".txt"
        f = open(name, "r")
        context = f.read()
        print(context)
        f.close()

    def new_text():
        name = input("what do you want to name  the file as:\n")
        name = name+".txt"
        f = open(name, "w+")
        string = input(
            "enter the string you want to input in to the file you have created:\n")
        f.write(string)
        f.close()

    def edit_text():
        name = input("enter the file name:\n")
        name = name+".txt"
        f = open(name, "a+")
        string = input(
            "enter the string you want to input in to the file you have created:\n")
        f.write(string)
        f.close()

    def del_text():
        import os
        name = input("enter the file name:\n")
        name = name+".txt"
        if os.path.exists(name):
            os.remove(name)
            print("removed succesfully ")
        else:
            print("The file does not exist")
    c = int(input("enter 1 to continue\nenter to 2 to end"))
    if c == 1:
        choice_text()
    else:
        break
