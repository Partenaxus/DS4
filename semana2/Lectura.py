#r: read
#w: write
#rb: read binary
#wb: write binary
def lee_archivo(archivo):
    with open(archivo,"r") as fh:
        texto = fh.read()
    return texto


if __name__ == "__main__":
    t = lee_archivo("episodio2.txt")
    print(t)