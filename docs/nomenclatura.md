# Nomenclatura

Convenção de nomes para arquivos e camadas no projeto Ecologia da Paisagem da Bacia do Itabapoana (ES).

## Estrutura de pastas

- **Projeto/Dados/Dados_Brutos/** – Camadas baixadas das fontes (IBGE, ANA, IJSN), sem alteração de SRC.
- **Projeto/Dados/Recortes_Bacia/** – Camadas recortadas ou extraídas para a área da Bacia do Itabapoana (ES).
- **Projeto/Dados/Fragmentos_Analise/** – Camada principal de fragmentos com métricas calculadas.

## Sufixo UTM

Arquivos e camadas reprojetados para SIRGAS 2000 / UTM zone 24S (EPSG:31984) recebem o sufixo **`_UTM`**.

Exemplos:

- `Bacia_BH_Itabapoana_AreaEstudo_UTM.gpkg`
- `UsoSolo_BH_Itabapoana_ES_Recorte_UTM.gpkg`
- `MataNativa_BH_Itabapoana_ES_Extracao_UTM` (camada no projeto)
- `Municipios_ES_Analise_UTM.gpkg`

## Padrão para recortes e extrações

**Formato geral:** `[Dados]_[Recorte]_[Objetivo]_[CRS]`

- **[Dados]** – Nome da base (ex.: Bacia, UsoSolo, MataNativa).
- **[Recorte]** – Área de recorte (ex.: BH_Itabapoana_AreaEstudo, BH_Itabapoana_ES_Recorte).
- **[Objetivo]** – Finalidade (ex.: AreaEstudo, Extracao).
- **[CRS]** – Quando em UTM 24S: `_UTM` no nome do arquivo ou da camada.

Exemplos:

| Descrição                    | Nome do arquivo/camada                          |
|-----------------------------|-------------------------------------------------|
| Bacia do Itabapoana (UTM)   | `Bacia_BH_Itabapoana_AreaEstudo_UTM.gpkg`       |
| Uso do solo recortado (UTM)| `UsoSolo_BH_Itabapoana_ES_Recorte_UTM.gpkg`     |
| Mata Nativa extraída (UTM) | `MataNativa_BH_Itabapoana_ES_Extracao_UTM`      |
| Fragmentos (camada final)   | `Fragmentos_MataNativa_BH_I_ES.gpkg`            |

## Camadas no QGIS

Os nomes das camadas no projeto QGIS seguem o nome do arquivo GeoPackage ou do shapefile. Quando há apenas uma camada por arquivo, o nome da camada costuma coincidir com o nome do arquivo (sem extensão).

## Dados tabulares e resultados

- **data/** – CSV e tabelas exportadas (ex.: `MataNativa_Mesclagem_Fragmentos.csv`).
- **Resultados/Histogramas/** – Gráficos gerados pelos scripts (ex.: `histograma_area_ha_densidade.png`).
- **Resultados/Maps/** – Mapas temáticos (PDF e imagens).
