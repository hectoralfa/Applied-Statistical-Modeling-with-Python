import matplotlib.pyplot as plt
from .style_graphs import EstiloBase
from .helpers_graphs import aplicar_estilo_base, aplicar_titulo, mostrar_figura, cargar_fuentes

def scatter_estilo(
    df,
    x,
    y,
    grupo=None,
    titulo=None,
    subtitulo=None,
    nombre_eje_x=None,
    nombre_eje_y=None,
    ancho_fig=12,
    alto_fig=6,
    tam_punto=55,
    alpha=None,
    estilo=None,
    leyenda=True
):
    if estilo is None:
        estilo = EstiloBase()

    cargar_fuentes(tipo_letra=estilo.tipo_letra)

    if alpha is None:
        alpha = estilo.alpha

    fig, ax = plt.subplots(figsize=(ancho_fig, alto_fig), dpi=estilo.dpi)
    fig.patch.set_facecolor(estilo.fondo)
    ax.set_facecolor(estilo.fondo)

    if grupo is None:
        ax.scatter(df[x], df[y], s=tam_punto, alpha=alpha, color=estilo.paleta_colores[0])
    else:
        grupos = df[grupo].dropna().unique()
        color_map = {
            g: estilo.paleta_colores[i % len(estilo.paleta_colores)]
            for i, g in enumerate(grupos)
        }

        for g in grupos:
            sub = df[df[grupo] == g]
            ax.scatter(
                sub[x], sub[y],
                s=tam_punto,
                alpha=alpha,
                color=color_map[g],
                label=str(g)
            )

        if leyenda:
            ax.legend(frameon=False, fontsize=estilo.tam_leyenda, title=grupo)

    ax.set_xlabel(
        nombre_eje_x or x,
        fontsize=estilo.tam_eje_x,
        fontweight=estilo.weight_ejes,
        color=estilo.color_texto
    )
    ax.set_ylabel(
        nombre_eje_y or y,
        fontsize=estilo.tam_eje_y,
        fontweight=estilo.weight_ejes,
        color=estilo.color_texto
    )

    ax.grid(True, axis="y")

    aplicar_titulo(ax, titulo, estilo, subtitulo=subtitulo)
    aplicar_estilo_base(ax, estilo)

    return fig, ax