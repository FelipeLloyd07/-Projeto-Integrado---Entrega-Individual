# Entrega Individual — Trabalho e População Empregada

## Esta entrega tem um único gráfico

O gráfico compara a **taxa de desocupação por Unidade da Federação** entre o **3º trimestre de 2012** e o **3º trimestre de 2022**. O gráfico permite selecionar o total, os homens ou as mulheres.

Esta é a entrega individual. Os outros gráficos — formalidade, informalidade, rendimento e setores econômicos — pertencem ao dashboard completo do grupo, caso sejam exigidos na integração.

## Dados

Os dados são reais e foram obtidos da tabela oficial 4093 do SIDRA/IBGE, que apresenta a taxa de desocupação por UF e sexo.

## Como executar

Na pasta do projeto, abra o terminal e execute:

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Arquivos enviados

```text
app.py
README.md
RELATORIO.md
ENTREGA_INDIVIDUAL_EXPLICADA.md
FONTE_DADOS.md
requirements.txt
data/emprego_sexo.csv
```

A pasta `data` é necessária para o programa encontrar a base oficial.

## Como enviar para o GitHub

Crie um repositório individual no GitHub e envie todos os arquivos, mantendo a pasta `data`. Não envie somente o `app.py`.

## Fala para apresentação

“Minha entrega individual é sobre Trabalho e População Empregada. O gráfico compara a taxa de desocupação dos estados brasileiros entre o terceiro trimestre de 2012 e o terceiro trimestre de 2022. Também é possível selecionar o total, os homens ou as mulheres. A diferença entre as barras é observada em pontos percentuais. Usei dados reais da PNAD Contínua do IBGE, obtidos na tabela 4093 do SIDRA.”
