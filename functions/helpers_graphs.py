from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

def aplicar_estilo_base(ax, estilo):

    if estilo.grid_eje is None:
        ax.grid(False)

    else:
        ax.grid(
            estilo.grillas,
            axis=estilo.grid_eje,   # "x", "y" ,"both"
            color=estilo.color_grid,
            linewidth=estilo.grid_linewidth,
            alpha=estilo.grid_alpha
        )

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax.spines["left"].set_color(estilo.color_ejes)
    ax.spines["bottom"].set_color(estilo.color_ejes)

    ax.tick_params(axis="x", colors=estilo.color_ejes, labelsize=estilo.tam_eje_x)
    ax.tick_params(axis="y", colors=estilo.color_ejes, labelsize=estilo.tam_eje_y)


def cargar_fuentes(ruta_fonts=None, tipo_letra="Montserrat"):

    plt.rcParams["svg.fonttype"] = "none"

    base_dir = Path(__file__).resolve().parent

    if ruta_fonts is None:
        ruta = base_dir / "0_fonts"
    else:
        ruta = Path(ruta_fonts)

    if not ruta.exists():
        print(f"⚠️ No se encontró la carpeta de fuentes: {ruta}")
        return

    font_files = fm.findSystemFonts(fontpaths=[str(ruta)])

    for font_file in font_files:
        fm.fontManager.addfont(font_file)

    plt.rcParams["font.family"] = tipo_letra


def aplicar_titulo(ax, titulo, estilo, subtitulo=None):
    if titulo:
        ax.set_title(
            titulo,
            fontsize=estilo.tam_titulo,
            fontweight=estilo.weight_titulo,
            color=estilo.color_texto,
            pad=16
        )

    if subtitulo:
        ax.text(
            0, 1.02, subtitulo,
            transform=ax.transAxes,
            fontsize=estilo.tam_subtitulo,
            color=estilo.color_ejes,
            ha="left",
            va="bottom"
        )

def mostrar_figura(fig):
    plt.tight_layout()
    plt.show()
