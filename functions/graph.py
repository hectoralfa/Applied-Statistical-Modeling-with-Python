from .style_graphs import EstiloBase
from .scatter_graph import scatter_estilo
#from tendencia_estilo import tendencia_estilo
#from barras_estilo import barras_estilo

def graficar(tipo, estilo=None, **kwargs):
    if estilo is None:
        estilo = EstiloBase()

    if tipo == "scatter":
        return scatter_estilo(estilo=estilo, **kwargs)

    else:
        raise ValueError(f"Tipo de gráfica no soportado: {tipo}")