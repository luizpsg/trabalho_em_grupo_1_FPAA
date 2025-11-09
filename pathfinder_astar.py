"""
PathFinder - Algoritmo A* para Resolução de Labirintos 2D
Autor: Implementação para trabalho acadêmico
Descrição: Resolve labirintos 2D usando o algoritmo A* com heurística de Manhattan
"""

import heapq
from typing import List, Tuple, Optional, Set


class Node:
    """
    Representa um nó no labirinto para o algoritmo A*.
    
    Atributos:
        position: Tupla (linha, coluna) da posição do nó
        g: Custo do caminho desde o início até este nó
        h: Heurística - estimativa do custo até o objetivo
        f: Custo total (f = g + h)
        parent: Nó anterior no caminho
    """
    def __init__(self, position: Tuple[int, int], g: int = 0, h: int = 0, parent=None):
        self.position = position
        self.g = g
        self.h = h
        self.f = g + h
        self.parent = parent
    
    def __lt__(self, other):
        """Comparação para a fila de prioridade"""
        return self.f < other.f
    
    def __eq__(self, other):
        """Igualdade baseada na posição"""
        return self.position == other.position
    
    def __hash__(self):
        """Hash baseado na posição para usar em sets"""
        return hash(self.position)


class PathFinder:
    """
    Implementa o algoritmo A* para encontrar o menor caminho em um labirinto.
    """
    
    def __init__(self, maze: List[List[str]]):
        """
        Inicializa o PathFinder com um labirinto.
        
        Args:
            maze: Matriz 2D representando o labirinto
                  'S' = início, 'E' = fim, '0' = livre, '1' = obstáculo
        """
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0]) if maze else 0
        self.start = None
        self.end = None
        
        # Encontra as posições de início (S) e fim (E)
        self._find_start_end()
    
    def _find_start_end(self):
        """Localiza as posições de início (S) e fim (E) no labirinto."""
        for i in range(self.rows):
            for j in range(self.cols):
                if self.maze[i][j] == 'S':
                    self.start = (i, j)
                elif self.maze[i][j] == 'E':
                    self.end = (i, j)
        
        if self.start is None:
            raise ValueError("Posição inicial 'S' não encontrada no labirinto!")
        if self.end is None:
            raise ValueError("Posição final 'E' não encontrada no labirinto!")
    
    def _manhattan_distance(self, pos1: Tuple[int, int], pos2: Tuple[int, int]) -> int:
        """
        Calcula a distância de Manhattan entre duas posições.
        
        Heurística: h(n) = |x_atual - x_final| + |y_atual - y_final|
        
        Args:
            pos1: Primeira posição (linha, coluna)
            pos2: Segunda posição (linha, coluna)
            
        Returns:
            Distância de Manhattan entre as posições
        """
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
    
    def _is_valid_position(self, position: Tuple[int, int]) -> bool:
        """
        Verifica se uma posição é válida no labirinto.
        
        Args:
            position: Posição (linha, coluna) a verificar
            
        Returns:
            True se a posição é válida, False caso contrário
        """
        row, col = position
        
        # Verifica se está dentro dos limites
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return False
        
        # Verifica se não é um obstáculo
        if self.maze[row][col] == '1':
            return False
        
        return True
    
    def _get_neighbors(self, position: Tuple[int, int]) -> List[Tuple[int, int]]:
        """
        Retorna as posições vizinhas válidas (cima, baixo, esquerda, direita).
        
        Args:
            position: Posição atual (linha, coluna)
            
        Returns:
            Lista de posições vizinhas válidas
        """
        row, col = position
        neighbors = []
        
        # Movimentos possíveis: cima, baixo, esquerda, direita
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for dr, dc in directions:
            new_position = (row + dr, col + dc)
            if self._is_valid_position(new_position):
                neighbors.append(new_position)
        
        return neighbors
    
    def _reconstruct_path(self, node: Node) -> List[Tuple[int, int]]:
        """
        Reconstrói o caminho do início ao fim seguindo os nós pais.
        
        Args:
            node: Nó final do caminho
            
        Returns:
            Lista de posições do início ao fim
        """
        path = []
        current = node
        
        while current is not None:
            path.append(current.position)
            current = current.parent
        
        return path[::-1]  # Inverte para começar do início
    
    def find_path(self) -> Optional[List[Tuple[int, int]]]:
        """
        Executa o algoritmo A* para encontrar o menor caminho.
        
        O algoritmo funciona da seguinte forma:
        1. Começa com o nó inicial na fila de prioridade
        2. A cada iteração, remove o nó com menor f (custo total)
        3. Se for o objetivo, reconstrói e retorna o caminho
        4. Caso contrário, explora os vizinhos:
           - Calcula g (custo do início até o vizinho)
           - Calcula h (heurística do vizinho até o fim)
           - Adiciona o vizinho à fila se for um caminho melhor
        
        Returns:
            Lista de posições do caminho encontrado, ou None se não houver solução
        """
        # Fila de prioridade (heap) para nós a explorar
        open_list = []
        # Conjunto de posições já visitadas
        closed_set: Set[Tuple[int, int]] = set()
        # Dicionário para rastrear o melhor custo g para cada posição
        g_costs = {self.start: 0}
        
        # Cria o nó inicial
        start_node = Node(
            position=self.start,
            g=0,
            h=self._manhattan_distance(self.start, self.end),
            parent=None
        )
        
        heapq.heappush(open_list, start_node)
        
        # Loop principal do A*
        while open_list:
            # Remove o nó com menor f da fila
            current_node = heapq.heappop(open_list)
            current_pos = current_node.position
            
            # Se já visitamos esta posição, pula
            if current_pos in closed_set:
                continue
            
            # Marca como visitada
            closed_set.add(current_pos)
            
            # Se chegamos ao objetivo, reconstrói o caminho
            if current_pos == self.end:
                return self._reconstruct_path(current_node)
            
            # Explora os vizinhos
            for neighbor_pos in self._get_neighbors(current_pos):
                # Se já visitamos, pula
                if neighbor_pos in closed_set:
                    continue
                
                # Calcula o novo custo g (custo atual + 1)
                new_g = current_node.g + 1
                
                # Se encontramos um caminho melhor ou é a primeira vez visitando
                if neighbor_pos not in g_costs or new_g < g_costs[neighbor_pos]:
                    g_costs[neighbor_pos] = new_g
                    
                    # Cria o nó vizinho
                    neighbor_node = Node(
                        position=neighbor_pos,
                        g=new_g,
                        h=self._manhattan_distance(neighbor_pos, self.end),
                        parent=current_node
                    )
                    
                    heapq.heappush(open_list, neighbor_node)
        
        # Se a fila está vazia e não chegamos ao objetivo, não há solução
        return None
    
    def display_maze_with_path(self, path: List[Tuple[int, int]]) -> str:
        """
        Cria uma representação visual do labirinto com o caminho destacado.
        
        Args:
            path: Lista de posições do caminho encontrado
            
        Returns:
            String com o labirinto e caminho destacado
        """
        # Cria uma cópia do labirinto para não modificar o original
        display = [row[:] for row in self.maze]
        
        # Marca o caminho com '*' (exceto início e fim)
        for pos in path:
            if pos != self.start and pos != self.end:
                display[pos[0]][pos[1]] = '*'
        
        # Converte para string
        result = []
        for row in display:
            result.append(' '.join(row))
        
        return '\n'.join(result)


def format_path(path: List[Tuple[int, int]], maze: List[List[str]]) -> str:
    """
    Formata o caminho para exibição, mostrando 'S' e 'E' no início e fim.
    
    Args:
        path: Lista de posições do caminho
        maze: Matriz do labirinto
        
    Returns:
        String formatada do caminho
    """
    if not path:
        return "[]"
    
    formatted = []
    for i, pos in enumerate(path):
        if i == 0:
            formatted.append(f"S{pos}")
        elif i == len(path) - 1:
            formatted.append(f"E{pos}")
        else:
            formatted.append(str(pos))
    
    return "[" + ", ".join(formatted) + "]"


def main():
    """
    Função principal para demonstrar o uso do PathFinder.
    """
    print("=" * 60)
    print("PathFinder - Resolvendo Labirintos com Algoritmo A*")
    print("=" * 60)
    print()
    
    # Exemplo 1: Labirinto do enunciado
    print("EXEMPLO 1: Labirinto do Enunciado")
    print("-" * 60)
    maze1 = [
        ['S', '0', '1', '0', '0'],
        ['0', '0', '1', '0', '1'],
        ['1', '0', '1', '0', '0'],
        ['1', '0', '0', 'E', '1']
    ]
    
    print("Labirinto original:")
    for row in maze1:
        print(' '.join(row))
    print()
    
    pathfinder1 = PathFinder(maze1)
    path1 = pathfinder1.find_path()
    
    if path1:
        print(f"✓ Caminho encontrado com {len(path1)} passos!")
        print(f"Menor caminho (coordenadas): {format_path(path1, maze1)}")
        print()
        print("Labirinto com caminho destacado:")
        print(pathfinder1.display_maze_with_path(path1))
    else:
        print("✗ Sem solução: Não há caminho possível entre S e E.")
    
    print()
    print("=" * 60)
    print()
    
    # Exemplo 2: Labirinto mais complexo
    print("EXEMPLO 2: Labirinto Complexo")
    print("-" * 60)
    maze2 = [
        ['S', '0', '0', '1', '0', '0'],
        ['1', '1', '0', '1', '0', '1'],
        ['0', '0', '0', '0', '0', '0'],
        ['0', '1', '1', '1', '1', '0'],
        ['0', '0', '0', '0', '0', 'E']
    ]
    
    print("Labirinto original:")
    for row in maze2:
        print(' '.join(row))
    print()
    
    pathfinder2 = PathFinder(maze2)
    path2 = pathfinder2.find_path()
    
    if path2:
        print(f"✓ Caminho encontrado com {len(path2)} passos!")
        print(f"Menor caminho (coordenadas): {format_path(path2, maze2)}")
        print()
        print("Labirinto com caminho destacado:")
        print(pathfinder2.display_maze_with_path(path2))
    else:
        print("✗ Sem solução: Não há caminho possível entre S e E.")
    
    print()
    print("=" * 60)
    print()
    
    # Exemplo 3: Labirinto sem solução
    print("EXEMPLO 3: Labirinto Sem Solução")
    print("-" * 60)
    maze3 = [
        ['S', '0', '1', '0'],
        ['1', '0', '1', '0'],
        ['0', '0', '1', '0'],
        ['0', '1', '1', 'E']
    ]
    
    print("Labirinto original:")
    for row in maze3:
        print(' '.join(row))
    print()
    
    pathfinder3 = PathFinder(maze3)
    path3 = pathfinder3.find_path()
    
    if path3:
        print(f"✓ Caminho encontrado com {len(path3)} passos!")
        print(f"Menor caminho (coordenadas): {format_path(path3, maze3)}")
        print()
        print("Labirinto com caminho destacado:")
        print(pathfinder3.display_maze_with_path(path3))
    else:
        print("✗ Sem solução: Não há caminho possível entre S e E.")
    
    print()
    print("=" * 60)


if __name__ == "__main__":
    main()
