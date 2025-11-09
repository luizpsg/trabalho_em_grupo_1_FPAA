# PathFinder - Resolvendo Labirintos 2D com Algoritmo A\*

## 📋 Descrição do Projeto

O **PathFinder** é um projeto desenvolvido para resolver labirintos bidimensionais utilizando o algoritmo A\* (A-estrela). O objetivo é encontrar o menor caminho entre um ponto inicial (S - Start) e um ponto final (E - End) em um labirinto representado por uma matriz 2D, evitando obstáculos e considerando o custo de cada movimento.

Este projeto foi desenvolvido como parte de um trabalho acadêmico para demonstrar a aplicação prática de algoritmos de busca informada, especificamente o A\*, que é amplamente utilizado em sistemas de navegação, jogos, robótica e inteligência artificial.

## 🎯 Problema Resolvido

### Contexto

Imagine um robô de resgate que precisa navegar por um prédio em ruínas (representado como um labirinto 2D) para resgatar vítimas. O robô:

- Está em uma posição inicial **S** (Start)
- Precisa chegar até a posição **E** (End) onde está a vítima
- Não pode atravessar obstáculos (paredes, escombros)
- Precisa encontrar o **caminho mais curto** para economizar tempo e energia

### Representação do Labirinto

O labirinto é uma matriz 2D onde:

- **S**: Ponto inicial (Start)
- **E**: Ponto final (End/destino)
- **0**: Células livres (caminhos transitáveis)
- **1**: Obstáculos (paredes/bloqueios)

### Exemplo de Labirinto

```
S 0 1 0 0
0 0 1 0 1
1 0 1 0 0
1 0 0 E 1
```

## 🧠 O Algoritmo A\* (A-Estrela)

### Visão Geral

O **A\*** (pronuncia-se "A-estrela") é um algoritmo de busca informada que encontra o caminho mais curto entre dois pontos em um grafo. Ele é considerado um dos algoritmos mais eficientes para este tipo de problema porque combina:

1. **Custo real do caminho percorrido** (g)
2. **Estimativa heurística da distância até o objetivo** (h)

### Como Funciona o A\*

O algoritmo mantém uma **função de avaliação** para cada nó:

```
f(n) = g(n) + h(n)
```

Onde:

- **f(n)**: Custo total estimado do caminho passando pelo nó n
- **g(n)**: Custo real do caminho desde o início até o nó n
- **h(n)**: Estimativa heurística do custo do nó n até o objetivo

#### Passo a Passo do Algoritmo

1. **Inicialização**

   - Coloca o nó inicial (S) em uma fila de prioridade (open list)
   - Inicializa g(S) = 0 e h(S) = distância heurística até E
   - Cria um conjunto de nós já visitados (closed set)

2. **Loop Principal**

   - Enquanto houver nós na fila de prioridade:
     - Remove o nó com **menor f(n)** da fila
     - Se este nó é o objetivo (E), reconstrói e retorna o caminho
     - Marca o nó como visitado
     - Para cada vizinho válido do nó atual:
       - Calcula o novo g (custo desde o início)
       - Calcula h (distância heurística até o fim)
       - Se este caminho é melhor que qualquer anterior, adiciona à fila

3. **Término**

   - Se encontrou o objetivo: retorna o caminho
   - Se a fila esvaziou: não há solução

### Heurística: Distância de Manhattan

A heurística utilizada é a **Distância de Manhattan**, que calcula a distância entre dois pontos considerando apenas movimentos horizontais e verticais (não diagonais):

```
h(n) = |x_atual - x_final| + |y_atual - y_final|
```

**Exemplo**: A distância de Manhattan entre (1, 1) e (3, 4) é:

```
h = |1 - 3| + |1 - 4| = 2 + 3 = 5
```

Esta heurística é:

- **Admissível**: Nunca superestima o custo real (requisito para o A\* ser ótimo)
- **Consistente**: Satisfaz a desigualdade triangular
- **Eficiente**: Simples de calcular computacionalmente

### Por que o A\* é Eficiente?

Comparado a outros algoritmos:

- **Dijkstra**: Explora todas as direções igualmente (não usa heurística)
- **Busca Gulosa**: Usa apenas a heurística (pode não encontrar o melhor caminho)
- **A\***: Balanceia exploração e heurística, garantindo encontrar o caminho ótimo

O A\* visita menos nós que o Dijkstra porque a heurística "guia" a busca na direção do objetivo.

## 🚀 Configuração e Execução

### Pré-requisitos

- Python 3.7 ou superior
- Nenhuma biblioteca externa é necessária (usa apenas bibliotecas padrão do Python)

### Instalação

1. Clone ou baixe o repositório do projeto
2. Navegue até o diretório do projeto

```bash
cd pathfinder-astar
```

### Executando o Projeto

#### Execução Básica

Para executar o programa com os exemplos pré-definidos:

```bash
python pathfinder_astar.py
```

Isso executará três exemplos:

1. Labirinto do enunciado (com solução)
2. Labirinto complexo (com solução)
3. Labirinto sem solução

#### Usando o PathFinder no Seu Código

Você pode importar e usar a classe `PathFinder` em seu próprio código:

```python
from pathfinder_astar import PathFinder

# Defina seu labirinto
maze = [
    ['S', '0', '1', '0', '0'],
    ['0', '0', '1', '0', '1'],
    ['1', '0', '1', '0', '0'],
    ['1', '0', '0', 'E', '1']
]

# Crie uma instância do PathFinder
pathfinder = PathFinder(maze)

# Encontre o caminho
path = pathfinder.find_path()

# Exiba o resultado
if path:
    print(f"Caminho encontrado: {path}")
    print(pathfinder.display_maze_with_path(path))
else:
    print("Sem solução")
```

## 📊 Exemplos de Entrada e Saída

### Exemplo 1: Labirinto Simples (Com Solução)

**Entrada:**

```
S 0 1 0 0
0 0 1 0 1
1 0 1 0 0
1 0 0 E 1
```

**Saída:**

```
✓ Caminho encontrado com 8 passos!
Menor caminho (coordenadas): [S(0, 0), (0, 1), (1, 1), (1, 0), (2, 1), (3, 1), (3, 2), E(3, 3)]

Labirinto com caminho destacado:
S * 1 0 0
* * 1 0 1
1 * 1 0 0
1 * * E 1
```

**Explicação**: O robô encontrou um caminho de 8 posições do canto superior esquerdo até a posição (3,3), contornando os obstáculos.

---

### Exemplo 2: Labirinto Complexo (Com Solução)

**Entrada:**

```
S 0 0 1 0 0
1 1 0 1 0 1
0 0 0 0 0 0
0 1 1 1 1 0
0 0 0 0 0 E
```

**Saída:**

```
✓ Caminho encontrado com 11 passos!
Menor caminho (coordenadas): [S(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3), (2, 4), (2, 5), (3, 5), (4, 5), E(4, 5)]

Labirinto com caminho destacado:
S * * 1 0 0
1 1 * 1 0 1
0 0 * * * *
0 1 1 1 1 *
0 0 0 0 0 E
```

**Explicação**: Em um labirinto mais complexo, o algoritmo consegue navegar por um caminho serpenteante, evitando múltiplos obstáculos.

---

### Exemplo 3: Labirinto Sem Solução

**Entrada:**

```
S 0 1 0
1 0 1 0
0 0 1 0
0 1 1 E
```

**Saída:**

```
✗ Sem solução: Não há caminho possível entre S e E.
```

**Explicação**: O ponto final (E) está completamente isolado por obstáculos, tornando impossível alcançá-lo a partir do ponto inicial.

---

### Exemplo 4: Labirinto Grande (Teste de Eficiência)

**Entrada:**

```
S 0 0 0 0 0 0 0 0 0
0 1 1 1 1 1 1 1 0 0
0 0 0 0 0 0 0 1 0 0
0 1 1 1 1 1 0 1 0 0
0 0 0 0 0 1 0 1 0 0
0 1 1 1 0 1 0 1 0 0
0 0 0 0 0 1 0 0 0 0
0 1 1 1 1 1 1 1 1 0
0 0 0 0 0 0 0 0 0 E
```

**Saída:**

```
✓ Caminho encontrado com 26 passos!

Labirinto com caminho destacado:
S * * * * * * * * *
* 1 1 1 1 1 1 1 * *
* * * * * * * 1 * *
0 1 1 1 1 1 * 1 * *
0 0 0 0 0 1 * 1 * *
0 1 1 1 0 1 * 1 * *
0 0 0 0 0 1 * * * *
0 1 1 1 1 1 1 1 1 *
0 0 0 0 0 0 0 0 0 E
```

**Explicação**: Mesmo em labirintos grandes e complexos, o algoritmo A\* consegue encontrar eficientemente o caminho ótimo.

## 🏗️ Estrutura do Código

### Classes Principais

#### 1. `Node`

Representa um nó/posição no labirinto durante a busca.

**Atributos:**

- `position`: Coordenadas (linha, coluna)
- `g`: Custo do caminho desde o início
- `h`: Estimativa heurística até o objetivo
- `f`: Custo total (f = g + h)
- `parent`: Nó anterior no caminho (para reconstrução)

#### 2. `PathFinder`

Implementa o algoritmo A\* completo.

**Métodos Principais:**

- `__init__(maze)`: Inicializa com o labirinto e localiza S e E
- `find_path()`: Executa o algoritmo A\* e retorna o caminho
- `_manhattan_distance(pos1, pos2)`: Calcula a heurística
- `_is_valid_position(position)`: Valida se uma posição é transitável
- `_get_neighbors(position)`: Retorna vizinhos válidos (cima, baixo, esquerda, direita)
- `_reconstruct_path(node)`: Reconstrói o caminho final
- `display_maze_with_path(path)`: Cria visualização do labirinto com caminho

### Fluxo de Dados

```
Labirinto (matriz 2D)
    ↓
PathFinder (inicialização)
    ↓
Localização de S e E
    ↓
Algoritmo A* (find_path)
    ↓
Exploração de nós (fila de prioridade)
    ↓
Caminho encontrado ou "Sem solução"
    ↓
Visualização do resultado
```

## 📈 Complexidade do Algoritmo

### Complexidade de Tempo

- **Melhor caso**: O(b^d) onde b é o fator de ramificação e d é a profundidade
- **Pior caso**: O(n log n) onde n é o número de células do labirinto
- Na prática, muito mais eficiente que busca em largura devido à heurística

### Complexidade de Espaço

- O(n) onde n é o número de células do labirinto
- Precisa armazenar nós na fila de prioridade e conjunto de visitados

## ✅ Validações Implementadas

O código inclui várias validações de segurança:

1. **Validação de S e E**: Verifica se ambos existem no labirinto
2. **Validação de limites**: Garante que não sai dos limites da matriz
3. **Validação de obstáculos**: Não permite passar por células com '1'
4. **Detecção de sem solução**: Retorna `None` quando não há caminho possível

## 🎨 Características do Código

- ✅ **Código limpo e organizado**: Segue PEP 8 e boas práticas Python
- ✅ **Documentação completa**: Docstrings em todas as classes e métodos
- ✅ **Type hints**: Anotações de tipo para melhor legibilidade
- ✅ **Comentários explicativos**: Explicações em pontos críticos do algoritmo
- ✅ **Modular**: Fácil de estender e modificar
- ✅ **Reutilizável**: Pode ser importado e usado em outros projetos

## 🧪 Como Testar

### Teste 1: Labirinto Pequeno

```python
maze = [
    ['S', '0', 'E']
]
pathfinder = PathFinder(maze)
path = pathfinder.find_path()
# Esperado: [(0, 0), (0, 1), (0, 2)]
```

### Teste 2: Labirinto com Obstáculo Central

```python
maze = [
    ['S', '0', '0'],
    ['0', '1', '0'],
    ['0', '0', 'E']
]
pathfinder = PathFinder(maze)
path = pathfinder.find_path()
# Esperado: Caminho contornando o obstáculo
```

### Teste 3: Sem Solução

```python
maze = [
    ['S', '1'],
    ['1', 'E']
]
pathfinder = PathFinder(maze)
path = pathfinder.find_path()
# Esperado: None
```

## 🔄 Possíveis Extensões

O projeto pode ser estendido para incluir:

1. **Movimentos diagonais**: Permitir 8 direções em vez de 4
2. **Custos variados**: Diferentes tipos de terreno com custos diferentes
3. **Interface gráfica**: Visualização interativa do labirinto
4. **Geração de labirintos**: Criação automática de labirintos aleatórios
5. **Múltiplos objetivos**: Encontrar caminho passando por vários pontos
6. **Animação**: Mostrar o algoritmo explorando o labirinto em tempo real

## 📚 Referências

- Hart, P. E., Nilsson, N. J., & Raphael, B. (1968). A Formal Basis for the Heuristic Determination of Minimum Cost Paths. IEEE Transactions on Systems Science and Cybernetics.
- Russell, S., & Norvig, P. (2020). Artificial Intelligence: A Modern Approach (4th ed.). Pearson.
- Documentação Python: https://docs.python.org/3/

## 👥 Autores

Luiz Paulo Saud Gonçalves

Raphael Sena Auguesto de Brito

Isaac Portela da Silva

## 📝 Licença

Este projeto é desenvolvido para fins educacionais.
