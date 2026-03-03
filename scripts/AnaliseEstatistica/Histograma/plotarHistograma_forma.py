"""
Histograma de forma dos fragmentos (INDICE_FORMA) com intervalos da classificação por forma.
Classificação: Compacto (DI < 1,5), Alongado (1,5 ≤ DI < 2,0), Muito alongado (DI ≥ 2,0).
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
PASTA_SAIDA_HISTOGRAMAS = _RAIZ_SUBPROJETO / "Resultados" / "Histogramas"


def main() -> None:
    df = pd.read_csv(ARQUIVO_CSV)
    pasta_saida = PASTA_SAIDA_HISTOGRAMAS
    serie = df["INDICE_FORMA"].dropna()

    config = definir_caracteristicas_histograma(
        bins=[0, 1.5, 2.0, float("inf")],
        labels=["Compacto", "Alongado", "Muito alongado"],
        titulo="Distribuição da forma dos fragmentos de Mata Nativa\nBacia do Itabapoana (ES)",
        label_x="Classe de forma (índice DI)",
    )

    gerar_e_salvar_histogramas(
        serie=serie,
        config=config,
        nome_base="histograma_forma",
        pasta_saida=pasta_saida,
    )


if __name__ == "__main__":
    main()
