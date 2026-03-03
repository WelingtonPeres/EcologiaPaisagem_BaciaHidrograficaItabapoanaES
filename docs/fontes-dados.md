# Fontes de dados

Catálogo das fontes de dados utilizadas no projeto Ecologia da Paisagem da Bacia do Itabapoana (ES). Os dados são organizados em `Projeto/Dados/` (ver [nomenclatura.md](nomenclatura.md)).

## IBGE

**Malhas territoriais**

- **Municípios do Espírito Santo:** Malhas municipais 2024 (versão completa).  
  Link: <https://www.ibge.gov.br/geociencias/organizacao-do-territorio/malhas-territoriais/15774-malhas.html>  
  No projeto: `Projeto/Dados/Dados_Brutos/ES_Municipios_2024_Completo/`

- **Unidades da Federação:** Malhas de UFs 2024 (versão completa).  
  Link: <https://www.ibge.gov.br/geociencias/organizacao-do-territorio/malhas-territoriais/15774-malhas.html>  
  No projeto: `Projeto/Dados/Dados_Brutos/BR_UF_2024_Completo/`

## ANA / SNIRH

**Bacias hidrográficas**

- **Divisão hidrográfica (microrregiões):** Conjunto de shapes de bacias hidrográficas (micro e mesorregiões).  
  Metadados: <https://metadados.snirh.gov.br/geonetwork/srv/por/catalog.search#/metadata/fb87343a-cc52-4a36-b6c5-1fe05f4fe98c>  
  No projeto: `Projeto/Dados/Dados_Brutos/BaciasHidrograficas_Completo/` (extração da Bacia do Itabapoana a partir de `micro_RH`).

## IJSN / Geobases (Espírito Santo)

**Uso e cobertura do solo**

- **Mapeamento de uso e cobertura do solo do ES (2019-2020):** Baseada no Ortofotomosaico ES 2019-2020 (imagens Kompsat 3/3A). Inclui as classes Mata Nativa e Mata Nativa em Estágio Inicial de Regeneração, utilizadas nas análises de fragmentos.  
  Link: <https://geobases.es.gov.br/links-para-img-kpst-19-20>  
  No projeto: `Projeto/Dados/Dados_Brutos/ijsn_mapeamento_uso_solo_2019_2020/`

---

**CRS adotado nas análises:** SIRGAS 2000 / UTM zone 24S (EPSG:31984). Camadas em outros SRC foram reprojetadas para esse CRS antes do processamento.
