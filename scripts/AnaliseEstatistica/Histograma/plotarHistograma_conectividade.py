"""
Histograma de conectividade dos fragmentos (ISOLAMENTO_M) com intervalos da classificação.
Classificação: Alta (< 100 m), Média (100–500 m), Baixa (≥ 500 m) — baseada na distância ao vizinho mais próximo.
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
    serie = df["ISOLAMENTO_M"].dropna()

    config = definir_caracteristicas_histograma(
        bins=[0, 100, 500, float("inf")],
        labels=["Alta", "Média", "Baixa"],
        titulo="Distribuição da conectividade dos fragmentos de Mata Nativa\nBacia do Itabapoana (ES)",
        label_x="Classe de conectividade (distância ao vizinho, m)",
    )

    gerar_e_salvar_histogramas(
        serie=serie,
        config=config,
        nome_base="histograma_conectividade",
        pasta_saida=pasta_saida,
    )


if __name__ == "__main__":
    main()
