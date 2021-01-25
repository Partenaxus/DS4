import plotly
from plotly import express as px


def function(x,m,b):
    '''
        x valor de coordenada x
        m valor de pendiente
        b intersección

        y valor que regresamos

    '''
    resultado =  (m*x)+b
    return resultado

def main(pendiente,interseccion):
    X = [x for x in range(0,10)]
    Y = []

    for x in X:
        y= function(x,pendiente,interseccion)
        Y.append(y)
    print("X", X)
    print("Y",Y)
    #plotly.express.line(x=X, y=Y,title="Linea")
    fig = px.line(x=X,y=Y,title="Linea")
    fig.show()

if __name__ == "__main__":
    pendiente = -5
    interseccion = 2
    main(pendiente,interseccion)
