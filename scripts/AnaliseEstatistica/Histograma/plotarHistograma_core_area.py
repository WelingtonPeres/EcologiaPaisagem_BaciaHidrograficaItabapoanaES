"""
Histograma de área nuclear (core area) dos fragmentos.
Classe 0 (em risco) em barra separada; demais intervalos conforme Opção B até 2500+ ha.
Dados: MataNativa_Mesclagem_Fragmentos.csv - Bacia do Itabapoana (ES).
"""

import pandas as pd
from pathlib import Path

from histograma_core import (
    definir_caracteristicas_histograma,
    gerar_e_salvar_histogramas_contagens,
)

# Subir de Histograma -> AnaliseEstatistica -> scripts -> raiz do subprojeto
_RAIZ_SUBPROJETO = Path(__file__).resolve().parent.parent.parent.parent
PASTA_DADOS = _RAIZ_SUBPROJETO / "data"
ARQUIVO_CSV = PASTA_DADOS / "MataNativa_Mesclagem_Fragmentos.csv"
PASTA_SAIDA_HISTOGRAMAS = _RAIZ_SUBPROJETO / "Resultados" / "Histogramas"

# Opção B: 0 (em risco) + intervalos para positivos até > 2500 ha
BINS_POSITIVOS = [0, 1, 5, 10, 100, 500, 1000, 2500, float("inf")]
LABELS_POSITIVOS = [
    "(0 – 1]",
    "(1 – 5]",
    "(5 – 10]",
    "(10 – 100]",
    "(100 – 500]",
    "(500 – 1000]",
    "(1000 – 2500]",
    "> 2500",
]


def main() -> None:
    df = pd.read_csv(ARQUIVO_CSV)
    # Coluna de área nuclear (hectares); pode ser AREA_NUCLEAR_HA ou COREAREA_HE
    col = "AREA_NUCLEAR_HA" if "AREA_NUCLEAR_HA" in df.columns else "COREAREA_HE"
    serie = df[col].fillna(0)

    # Zero em risco: contagem separada
    n_zeros = (serie == 0).sum()
    serie_pos = serie[serie > 0]

    labels_ordenados = ["0 (em risco)"] + LABELS_POSITIVOS
    if len(serie_pos) == 0:
        contagens = pd.Series([n_zeros] + [0] * len(LABELS_POSITIVOS), index=labels_ordenados)
    else:
        # Classificar positivos com pd.cut (right=True: (0,1], (1,5], ...)
        classes_pos = pd.cut(
            serie_pos,
            bins=BINS_POSITIVOS,
            labels=LABELS_POSITIVOS,
            right=True,
        )
        counts_pos = classes_pos.value_counts()
        valores = [n_zeros]
        for lb in LABELS_POSITIVOS:
            valores.append(counts_pos.get(lb, 0))
        contagens = pd.Series(valores, index=labels_ordenados)

    config = definir_caracteristicas_histograma(
        titulo="Distribuição da área nuclear dos fragmentos de Mata Nativa\nBacia do Itabapoana (ES)",
        label_x="Área nuclear (ha)",
    )

    gerar_e_salvar_histogramas_contagens(
        contagens=contagens,
        config=config,
        nome_base="histograma_core_area",
        pasta_saida=PASTA_SAIDA_HISTOGRAMAS,
    )


if __name__ == "__main__":
    main()
