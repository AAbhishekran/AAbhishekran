def file(Filepath="text.txt"):
    with open(Filepath,"r") as localfile:
        todos = localfile.readlines()
        return todos

def write(Filepath="text.txt",Todos="todo"):
    with open(Filepath,"w") as localwrite:
        localwrite.writelines(Todos)

if __name__=="function":
    print("Welcom i am function file ")
