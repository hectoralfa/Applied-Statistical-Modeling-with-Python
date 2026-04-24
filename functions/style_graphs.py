from dataclasses import dataclass, field

@dataclass
class EstiloBase:
    tipo_letra: str = "Montserrat"
    fondo: str = "white"
    paleta_colores: list = field(default_factory=lambda: [
        "#0F1111", "#4C6A67", "#8FA8A6", "#A3C9A8", "#9B2247", "#D5B162"
    ])
    color_grid: str = "#D9D9D9"
    color_texto: str = "#222222"
    color_ejes: str = "#666666"

    tam_titulo: int = 18
    tam_subtitulo: int = 13
    tam_eje_x: int = 12
    tam_eje_y: int = 12
    tam_leyenda: int = 11

    weight_titulo: str = "bold"
    weight_ejes: str = "medium"
    weight_leyenda: str = "medium"

    alpha: float = 0.8
    grillas: bool = True
    dpi: int = 120

    grid_eje: str = "y"           # "x", "y", "both", None
    grid_alpha: float = 0.3
    grid_linewidth: float = 0.8