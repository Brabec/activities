import sys

def abrirArquivo(fname):
    with open(fname, "r") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    f.close()
    return content

if __name__ == "__main__":
    print ("This is the name of the script: ", sys.argv[0])
    print ("Number of arguments: ", len(sys.argv))
    print ("The arguments are: ", str(sys.argv))
    grafo = abrirArquivo(sys.argv[1])
    print(grafo)
    
