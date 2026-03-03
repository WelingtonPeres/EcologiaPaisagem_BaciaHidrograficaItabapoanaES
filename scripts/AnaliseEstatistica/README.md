# Análise Estatística - Ecologia da Paisagem

Geração de histogramas dos dados de fragmentos de Mata Nativa da Bacia do Itabapoana (ES).

## Histogramas

### Como usar

**Opção 1 – Pelo script principal (recomendado)**

1. Abra o terminal na pasta `Histograma`.
2. Instale as dependências, se ainda não tiver: `pip install -r requirements.txt` (ou `pip install pandas matplotlib`)
3. Liste os histogramas disponíveis:  
   `python main_histogramas.py --list`
4. Gere um histograma ou todos:  
   `python main_histogramas.py --all` (gera todos)  
   ou o histograma desejado:  
   `python main_histogramas.py area_ha`  
   `python main_histogramas.py forma`  
   `python main_histogramas.py conectividade`  
   `python main_histogramas.py core_area`

**Opção 2 – Executando o módulo direto**

Na pasta `Histograma`:

```bash
python plotarHistograma_area_ha.py
python plotarHistograma_forma.py
python plotarHistograma_conectividade.py
python plotarHistograma_core_area.py
```

Os PNGs são gravados em **`Resultados/Histogramas/`** (a pasta é criada automaticamente se não existir). Cada variável gera dois arquivos: um por frequência e um por densidade (ex.: `histograma_area_ha.png` e `histograma_area_ha_densidade.png`).

### Cuidados

- **Dados:** Os scripts leem o CSV em `data/MataNativa_Mesclagem_Fragmentos.csv`. Confira se esse arquivo existe e se as colunas usadas estão presentes (`AREA_HA`, `INDICE_FORMA`, `ISOLAMENTO_M`, `AREA_NUCLEAR_HA` ou `COREAREA_HE`, etc.). Se o CSV tiver nomes de coluna diferentes, será preciso ajustar o módulo correspondente.
- **Pasta de trabalho:** Execute sempre a partir da pasta `Histograma` (onde estão `main_histogramas.py` e os `plotarHistograma_*.py`), para que os imports e o caminho dos dados funcionem.
- **Python:** Use um ambiente com `pandas` e `matplotlib` instalados. Em caso de erro de módulo não encontrado, ative o ambiente correto ou instale as dependências.


