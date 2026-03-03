"""
Histograma de AREA_HA com intervalos da classificação TAMANHO.
Dados: MataNativa_Mesclagem_Fragmentos.csv - Bacia do Itabapoana (ES).
"""

import pandas as pd
from pathlib import Path

from histograma_core import (
    definir_caracteristicas_histograma,
    gerar_e_salvar_histogramas,
)

# Subir de Histograma -> AnaliseEstatistica -> scripts -> raiz do subprojeto
_RAIZ_SUBPROJETO = Path(__file__).resolve().parent.parent.parent.parent
PASTA_DADOS = _RAIZ_SUBPROJETO / "data"
ARQUIVO_CSV = PASTA_DADOS / "MataNativa_Mesclagem_Fragmentos.csv"
# Pasta de saída dos PNGs: Resultados/Histogramas (criada automaticamente se não existir)
PASTA_SAIDA_HISTOGRAMAS = _RAIZ_SUBPROJETO / "Resultados" / "Histogramas"


def main() -> None:
    df = pd.read_csv(ARQUIVO_CSV)
    pasta_saida = PASTA_SAIDA_HISTOGRAMAS
    serie = df["AREA_HA"].dropna()

    config = definir_caracteristicas_histograma(
        bins=[0, 5, 10, 100, 250, float("inf")],
        labels=["[0-5]", "[5-10]", "[10-100]", "[100-250]", "[>=250]"],
        titulo="Distribuição da área dos fragmentos de Mata Nativa\nBacia do Itabapoana (ES)",
        label_x="Área (ha)",
    )

    gerar_e_salvar_histogramas(
        serie=serie,
        config=config,
        nome_base="histograma_area_ha",
        pasta_saida=pasta_saida,
    )


if __name__ == "__main__":
    main()
