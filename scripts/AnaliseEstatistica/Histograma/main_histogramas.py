"""
Script principal para gerar histogramas. Executa um módulo por nome via CLI.

Uso:
  python main_histogramas.py --list          Lista histogramas disponíveis
  python main_histogramas.py --all           Gera todos os histogramas
  python main_histogramas.py area_ha         Gera histograma(s) do módulo area_ha
"""

import argparse
import importlib
import sys
from pathlib import Path

# Garante que os módulos na mesma pasta sejam encontrados
_DIR = Path(__file__).resolve().parent
if str(_DIR) not in sys.path:
    sys.path.insert(0, str(_DIR))

MODULOS = {
    "area_ha": "plotarHistograma_area_ha",
    "forma": "plotarHistograma_forma",
    "conectividade": "plotarHistograma_conectividade",
    "core_area": "plotarHistograma_core_area",
}


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Gera histogramas a partir dos módulos registrados."
    )
    parser.add_argument(
        "nome",
        nargs="?",
        help="Nome do histograma a executar (ex.: area_ha)",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        dest="listar",
        help="Lista os histogramas disponíveis",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        dest="todos",
        help="Gera todos os histogramas registrados",
    )
    args = parser.parse_args()

    if args.listar:
        print("Histogramas disponíveis:")
        for chave in sorted(MODULOS):
            print(f"  {chave}")
        return

    if args.todos:
        for chave in sorted(MODULOS):
            modulo_nome = MODULOS[chave]
            mod = importlib.import_module(modulo_nome)
            main_fn = getattr(mod, "main", None)
            if main_fn is None:
                print(f"Aviso: módulo '{modulo_nome}' não define main(), pulando.", file=sys.stderr)
                continue
            print(f"Gerando: {chave}...")
            main_fn()
        print("Concluído.")
        return

    if not args.nome:
        parser.print_help()
        print("\nUse --list para listar os histogramas disponíveis.")
        sys.exit(1)

    nome = args.nome.strip().lower()
    if nome not in MODULOS:
        print(f"Erro: histograma '{nome}' não encontrado.", file=sys.stderr)
        print("Disponíveis:", ", ".join(sorted(MODULOS)), file=sys.stderr)
        sys.exit(1)

    modulo_nome = MODULOS[nome]
    mod = importlib.import_module(modulo_nome)
    main_fn = getattr(mod, "main", None)
    if main_fn is None:
        print(f"Erro: módulo '{modulo_nome}' não define função main().", file=sys.stderr)
        sys.exit(1)

    main_fn()


if __name__ == "__main__":
    main()
