# O Custo da Distância: Análise Logística do Brasileirão (2003-2024)

Este repositório contém o conjunto de dados (datasets) e o código-fonte utilizados na elaboração do artigo **"O Custo da Distância: Como a logística interfere na tabela do Campeonato Brasileiro de futebol"**.

O projeto visa quantificar o impacto do desgaste logístico (quilometragem percorrida e tempo de descanso) no desempenho das equipes da Série A na era dos pontos corridos.

## Estrutura do Repositório

Arquivos principais contidos neste repositório:

- **`analise-km-brasileirao.ipynb`**: O Jupyter Notebook principal. Contém todo o pipeline de dados:
  - Carregamento dos dados.
  - Cálculo de distâncias geodésicas.
  - Implementação da lógica de "Rota Real" (sequência de jogos fora de casa).
  - Geração dos gráficos e análises estatísticas apresentadas no artigo.

- **`data2.csv`**: A base de dados primária contendo o histórico de partidas do Campeonato Brasileiro (2003-2024). Inclui datas, mandantes, visitantes, placares e locais das partidas.

- **`arena_coords.csv`**: Arquivo auxiliar com as coordenadas geográficas (latitude e longitude) dos estádios utilizados na competição.

- **`estado_coords.csv`**: Arquivo auxiliar com as coordenadas centrais dos estados brasileiros, utilizado para plotagem de mapas e agrupamentos regionais.

## Metodologia

Diferente de abordagens tradicionais que calculam apenas a distância linear "ida e volta" entre a sede do clube e o local do jogo, este projeto implementa um algoritmo de **Sequenciamento Logístico Real**.

Se um clube joga duas partidas consecutivas fora de casa (ex: joga quarta-feira em Porto Alegre e domingo no Rio de Janeiro), o algoritmo calcula o deslocamento entre essas duas cidades, simulando o itinerário real da delegação e oferecendo uma estimativa mais precisa do desgaste acumulado.

## Principais Análises Geradas

O notebook gera as visualizações que fundamentam as hipóteses do artigo:

1.  **Hegemonia Geográfica:** Histograma demonstrando a concentração massiva de clubes e sedes nos estados do Sul e Sudeste.
2.  **Desigualdade Logística (Boxplot):** Comparativo da distribuição de quilometragem anual por região, evidenciando a carga excessiva imposta aos clubes do Nordeste.
3.  **Matriz de Desgaste (Zona Crítica):** Gráfico cruzando *Distância Percorrida* vs. *Dias de Descanso*, identificando a queda de aproveitamento em cenários de alta viagem (>1.500km) e pouco repouso (≤3 dias).
4.  **Impacto no Jogo Seguinte:** Análise da correlação entre a distância do último deslocamento e a pontuação obtida na partida imediatamente posterior.
5.  **Mapa de Eficiência (Scatter Plot):** Cruzamento entre *Média de Pontos* e *Média de KM Viajados*, com linhas de corte que separam os clubes em quadrantes de eficiência e desgaste.
6.  **Custo do Rebaixamento (G4 vs Z4):** Comparativo da carga logística média entre as equipes que terminam no topo da tabela e as que são rebaixadas.

## Como Executar

Para reproduzir as análises, você precisará fazer upload dos arquivos CSVs no colab e rodar o notebook. 
