"""
Núcleo compartilhado para histogramas: configuração, plotagem (frequência e densidade)
e geração/salvamento dos PNGs. Os módulos por variável importam deste arquivo e
definem apenas bins, labels, título e coluna do CSV.
"""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def garantir_pasta_histogramas(pasta: Path) -> Path:
    """
    Verifica se o caminho da pasta existe; caso não exista, cria as pastas necessárias.
    Retorna o Path da pasta pronta para receber os arquivos de histograma.
    """
    pasta = Path(pasta)
    pasta.mkdir(parents=True, exist_ok=True)
    return pasta


def definir_caracteristicas_histograma(**kwargs) -> dict:
    """
    Retorna dicionário com características do histograma.
    Aceita kwargs para customizar valores padrão.
    """
    padrao = {
        "bins": [0, float("inf")],
        "labels": ["[0-inf]"],
        "cor_barras": "grey",
        "cor_borda": "black",
        "alpha": 1.0,
        "figsize": (10, 6),
        "titulo": "Histograma",
        "label_x": "Valor",
        "label_y_freq": "Frequência",
        "label_y_dens": "Densidade",
        "dpi": 150,
    }
    padrao.update(kwargs)
    return padrao


def plotar_histograma_normal(
    serie: pd.Series,
    ax: plt.Axes | None = None,
    config: dict | None = None,
) -> plt.Axes:
    """Histograma com frequência (contagem)."""
    if config is None:
        config = definir_caracteristicas_histograma()
    if ax is None:
        _, ax = plt.subplots(figsize=config["figsize"])

    area_class = pd.cut(serie, bins=config["bins"], labels=config["labels"], right=False)
    counts = area_class.value_counts().sort_index()

    x_pos = range(len(counts))
    bars = ax.bar(
        x_pos,
        counts.values,
        edgecolor=config["cor_borda"],
        color=config["cor_barras"],
        alpha=config["alpha"],
    )
    ax.bar_label(bars, labels=counts.values)
    ax.set_xticks(x_pos)
    ax.set_xticklabels(counts.index)
    ax.set_xlabel(config["label_x"])
    ax.set_ylabel(config["label_y_freq"])
    ax.set_title(config["titulo"])

    return ax


def plotar_histograma_densidade(
    serie: pd.Series,
    ax: plt.Axes | None = None,
    config: dict | None = None,
) -> plt.Axes:
    """Histograma com densidade (proporção)."""
    if config is None:
        config = definir_caracteristicas_histograma()
    if ax is None:
        _, ax = plt.subplots(figsize=config["figsize"])

    area_class = pd.cut(serie, bins=config["bins"], labels=config["labels"], right=False)
    counts = area_class.value_counts().sort_index()
    densidades = counts.values / len(serie)

    x_pos = range(len(counts))
    bars = ax.bar(
        x_pos,
        densidades,
        edgecolor=config["cor_borda"],
        color=config["cor_barras"],
        alpha=config["alpha"],
    )
    ax.bar_label(bars, labels=[f"{d:.2%}" for d in densidades])
    ax.set_xticks(x_pos)
    ax.set_xticklabels(counts.index)
    ax.set_xlabel(config["label_x"])
    ax.set_ylabel(config["label_y_dens"])
    ax.set_title(config["titulo"])

    return ax


def gerar_e_salvar_histogramas(
    serie: pd.Series,
    config: dict,
    nome_base: str,
    pasta_saida: Path,
) -> None:
    """
    Gera os dois histogramas (frequência e densidade) e salva como PNG.
    Arquivos: {nome_base}.png e {nome_base}_densidade.png
    Cria a pasta de saída se não existir (via garantir_pasta_histogramas).
    """
    pasta_saida = garantir_pasta_histogramas(pasta_saida)
    fig, ax = plt.subplots(figsize=config["figsize"])
    plotar_histograma_normal(serie, ax=ax, config=config)
    plt.tight_layout()
    plt.savefig(pasta_saida / f"{nome_base}.png", dpi=config["dpi"], bbox_inches="tight")
    plt.close(fig)

    fig, ax = plt.subplots(figsize=config["figsize"])
    plotar_histograma_densidade(serie, ax=ax, config=config)
    plt.tight_layout()
    plt.savefig(
        pasta_saida / f"{nome_base}_densidade.png",
        dpi=config["dpi"],
        bbox_inches="tight",
    )
    plt.close(fig)


def plotar_histograma_normal_contagens(
    contagens: pd.Series,
    ax: plt.Axes | None = None,
    config: dict | None = None,
) -> plt.Axes:
    """Histograma por frequência a partir de contagens já agregadas (ex.: zero separado)."""
    if config is None:
        config = definir_caracteristicas_histograma()
    if ax is None:
        _, ax = plt.subplots(figsize=config["figsize"])

    x_pos = range(len(contagens))
    bars = ax.bar(
        x_pos,
        contagens.values,
        edgecolor=config["cor_borda"],
        color=config["cor_barras"],
        alpha=config["alpha"],
    )
    ax.bar_label(bars, labels=contagens.values)
    ax.set_xticks(x_pos)
    ax.set_xticklabels(contagens.index)
    ax.set_xlabel(config["label_x"])
    ax.set_ylabel(config["label_y_freq"])
    ax.set_title(config["titulo"])
    return ax


def plotar_histograma_densidade_contagens(
    contagens: pd.Series,
    ax: plt.Axes | None = None,
    config: dict | None = None,
) -> plt.Axes:
    """Histograma por densidade (proporção) a partir de contagens já agregadas."""
    if config is None:
        config = definir_caracteristicas_histograma()
    if ax is None:
        _, ax = plt.subplots(figsize=config["figsize"])

    total = contagens.sum()
    densidades = contagens.values / total if total > 0 else contagens.values

    x_pos = range(len(contagens))
    bars = ax.bar(
        x_pos,
        densidades,
        edgecolor=config["cor_borda"],
        color=config["cor_barras"],
        alpha=config["alpha"],
    )
    ax.bar_label(bars, labels=[f"{d:.2%}" for d in densidades])
    ax.set_xticks(x_pos)
    ax.set_xticklabels(contagens.index)
    ax.set_xlabel(config["label_x"])
    ax.set_ylabel(config["label_y_dens"])
    ax.set_title(config["titulo"])
    return ax


def gerar_e_salvar_histogramas_contagens(
    contagens: pd.Series,
    config: dict,
    nome_base: str,
    pasta_saida: Path,
) -> None:
    """
    Gera os dois histogramas (frequência e densidade) a partir de contagens agregadas.
    Útil quando a primeira classe é especial (ex.: 0 em risco).
    """
    pasta_saida = garantir_pasta_histogramas(pasta_saida)
    fig, ax = plt.subplots(figsize=config["figsize"])
    plotar_histograma_normal_contagens(contagens, ax=ax, config=config)
    plt.tight_layout()
    plt.savefig(pasta_saida / f"{nome_base}.png", dpi=config["dpi"], bbox_inches="tight")
    plt.close(fig)

    fig, ax = plt.subplots(figsize=config["figsize"])
    plotar_histograma_densidade_contagens(contagens, ax=ax, config=config)
    plt.tight_layout()
    plt.savefig(
        pasta_saida / f"{nome_base}_densidade.png",
        dpi=config["dpi"],
        bbox_inches="tight",
    )
    plt.close(fig)
