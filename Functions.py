FILEPATH= r"todos.txt"

def open_read(filepath=FILEPATH):
    """
    open todos text file and read its content
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
        return (todos_local)

def open_write(todos_arg, filepath=FILEPATH):
    """ open todos text file and change its content"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__=="__main__":
    print("This is functions file which you are running directly without main file.")
    print("If you used main file to call this file, its name would be Functions but if "
          "you directly call it, its name is main with __...__")