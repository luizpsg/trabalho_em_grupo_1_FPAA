"""
Exemplos Personalizáveis - PathFinder A*
Use este arquivo para testar seus próprios labirintos!
"""

from pathfinder_astar import PathFinder, format_path


def test_custom_maze():
    """
    Função para testar um labirinto personalizado.
    Modifique a matriz 'my_maze' abaixo para criar seu próprio labirinto!
    """
    print("=" * 60)
    print("TESTE PERSONALIZADO - Crie seu próprio labirinto!")
    print("=" * 60)
    print()
    
    # 🎯 MODIFIQUE ESTE LABIRINTO AQUI!
    # Regras:
    # - 'S' = Início (deve ter exatamente 1)
    # - 'E' = Fim (deve ter exatamente 1)
    # - '0' = Caminho livre
    # - '1' = Obstáculo
    
    my_maze = [
        ['S', '0', '0', '0', '0'],
        ['1', '1', '0', '1', '0'],
        ['0', '0', '0', '1', '0'],
        ['0', '1', '1', '1', '0'],
        ['0', '0', '0', '0', 'E']
    ]
    
    print("Seu labirinto:")
    for row in my_maze:
        print(' '.join(row))
    print()
    
    try:
        pathfinder = PathFinder(my_maze)
        path = pathfinder.find_path()
        
        if path:
            print(f"✓ Caminho encontrado com {len(path)} passos!")
            print(f"Menor caminho: {format_path(path, my_maze)}")
            print()
            print("Labirinto com caminho destacado:")
            print(pathfinder.display_maze_with_path(path))
            print()
            print(f"📊 Estatísticas:")
            print(f"   - Distância total: {len(path) - 1} movimentos")
            print(f"   - Posição inicial: {path[0]}")
            print(f"   - Posição final: {path[-1]}")
        else:
            print("✗ Sem solução: Não há caminho possível entre S e E.")
            print("💡 Dica: Verifique se o E está acessível a partir do S!")
    
    except ValueError as e:
        print(f"❌ Erro: {e}")
        print("💡 Dica: Certifique-se de que há exatamente um 'S' e um 'E' no labirinto.")
    
    print("=" * 60)


def test_maze_variations():
    """
    Testa diferentes variações de labirintos para demonstrar o algoritmo.
    """
    print("\n" + "=" * 60)
    print("TESTES DE VARIAÇÕES DE LABIRINTOS")
    print("=" * 60)
    print()
    
    # Teste 1: Labirinto linear (caminho direto)
    print("TESTE 1: Caminho Direto")
    print("-" * 40)
    maze1 = [
        ['S', '0', '0', '0', 'E']
    ]
    run_test(maze1)
    
    # Teste 2: Labirinto em L
    print("\nTESTE 2: Caminho em L")
    print("-" * 40)
    maze2 = [
        ['S', '0', '0'],
        ['1', '1', '0'],
        ['E', '0', '0']
    ]
    run_test(maze2)
    
    # Teste 3: Múltiplos caminhos possíveis (A* escolhe o mais curto)
    print("\nTESTE 3: Múltiplos Caminhos (A* escolhe o melhor)")
    print("-" * 40)
    maze3 = [
        ['S', '0', '0', '0', '0'],
        ['0', '1', '1', '1', '0'],
        ['0', '0', '0', '0', '0'],
        ['0', '1', '1', '1', '0'],
        ['0', '0', '0', '0', 'E']
    ]
    run_test(maze3)
    
    # Teste 4: Labirinto espiralado
    print("\nTESTE 4: Labirinto Espiralado")
    print("-" * 40)
    maze4 = [
        ['S', '0', '0', '0', '0', '0', '0'],
        ['1', '1', '1', '1', '1', '1', '0'],
        ['0', '0', '0', '0', '0', '0', '0'],
        ['0', '1', '1', '1', '1', '1', '1'],
        ['0', '0', '0', '0', '0', '0', 'E']
    ]
    run_test(maze4)


def run_test(maze):
    """Executa um teste individual em um labirinto."""
    print("Labirinto:")
    for row in maze:
        print(' '.join(row))
    print()
    
    try:
        pathfinder = PathFinder(maze)
        path = pathfinder.find_path()
        
        if path:
            print(f"✓ Solução encontrada! Passos: {len(path)}")
            print(pathfinder.display_maze_with_path(path))
        else:
            print("✗ Sem solução")
    except Exception as e:
        print(f"❌ Erro: {e}")
    print()


def compare_maze_sizes():
    """
    Compara o desempenho do algoritmo em labirintos de diferentes tamanhos.
    """
    import time
    
    print("\n" + "=" * 60)
    print("COMPARAÇÃO DE DESEMPENHO POR TAMANHO")
    print("=" * 60)
    print()
    
    # Labirinto pequeno (5x5)
    small_maze = [
        ['S', '0', '0', '0', '0'],
        ['0', '1', '1', '1', '0'],
        ['0', '0', '0', '0', '0'],
        ['0', '1', '1', '1', '0'],
        ['0', '0', '0', '0', 'E']
    ]
    
    # Labirinto médio (10x10)
    medium_maze = [
        ['S', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '1', '1', '1', '1', '1', '1', '1', '1', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '1', '1', '1', '1', '1', '1', '1', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '1', '0', '0'],
        ['0', '1', '1', '1', '1', '1', '0', '1', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '1', '0', '0'],
        ['0', '1', '1', '1', '1', '1', '1', '1', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', 'E']
    ]
    
    # Labirinto grande (15x15)
    large_maze = [
        ['S'] + ['0'] * 14,
        ['0'] + ['1'] * 13 + ['0'],
        ['0'] + ['0'] * 13 + ['0'],
        ['0'] + ['1'] * 13 + ['0'],
        ['0'] + ['0'] * 13 + ['0'],
        ['0'] + ['1'] * 13 + ['0'],
        ['0'] + ['0'] * 13 + ['0'],
        ['0'] + ['1'] * 13 + ['0'],
        ['0'] + ['0'] * 13 + ['0'],
        ['0'] + ['1'] * 13 + ['0'],
        ['0'] + ['0'] * 13 + ['0'],
        ['0'] + ['1'] * 13 + ['0'],
        ['0'] + ['0'] * 13 + ['0'],
        ['0'] + ['1'] * 13 + ['0'],
        ['0'] * 14 + ['E']
    ]
    
    mazes = [
        ("Pequeno (5x5)", small_maze),
        ("Médio (10x10)", medium_maze),
        ("Grande (15x15)", large_maze)
    ]
    
    for name, maze in mazes:
        print(f"Testando labirinto {name}...")
        
        start_time = time.time()
        pathfinder = PathFinder(maze)
        path = pathfinder.find_path()
        end_time = time.time()
        
        elapsed = (end_time - start_time) * 1000  # em milissegundos
        
        if path:
            print(f"  ✓ Caminho encontrado: {len(path)} passos")
            print(f"  ⏱️  Tempo de execução: {elapsed:.2f} ms")
        else:
            print(f"  ✗ Sem solução")
            print(f"  ⏱️  Tempo de execução: {elapsed:.2f} ms")
        print()


def interactive_maze_builder():
    """
    Modo interativo para construir um labirinto passo a passo.
    """
    print("\n" + "=" * 60)
    print("CONSTRUTOR INTERATIVO DE LABIRINTOS")
    print("=" * 60)
    print()
    print("Este modo permite criar um labirinto personalizado.")
    print("Instruções:")
    print("  - Digite as dimensões do labirinto (linhas e colunas)")
    print("  - Para cada célula, escolha: S (início), E (fim), 0 (livre), 1 (obstáculo)")
    print()
    
    try:
        rows = int(input("Número de linhas: "))
        cols = int(input("Número de colunas: "))
        
        if rows < 1 or cols < 1:
            print("❌ Dimensões inválidas!")
            return
        
        print(f"\nCriando labirinto {rows}x{cols}")
        print("Para cada posição, digite: S, E, 0, ou 1")
        print()
        
        maze = []
        for i in range(rows):
            row = []
            for j in range(cols):
                while True:
                    cell = input(f"Célula [{i}][{j}]: ").strip().upper()
                    if cell in ['S', 'E', '0', '1']:
                        row.append(cell)
                        break
                    else:
                        print("  ❌ Entrada inválida! Use: S, E, 0, ou 1")
            maze.append(row)
        
        print("\nSeu labirinto criado:")
        for row in maze:
            print(' '.join(row))
        print()
        
        pathfinder = PathFinder(maze)
        path = pathfinder.find_path()
        
        if path:
            print(f"✓ Caminho encontrado com {len(path)} passos!")
            print(pathfinder.display_maze_with_path(path))
        else:
            print("✗ Sem solução para este labirinto.")
    
    except ValueError as e:
        print(f"❌ Erro: {e}")
    except KeyboardInterrupt:
        print("\n\nOperação cancelada pelo usuário.")


def main():
    """Menu principal com todas as opções de teste."""
    while True:
        print("\n" + "=" * 60)
        print("MENU PRINCIPAL - PathFinder A*")
        print("=" * 60)
        print()
        print("Escolha uma opção:")
        print("  1. Testar labirinto personalizado (edite o código)")
        print("  2. Testar variações de labirintos")
        print("  3. Comparar desempenho por tamanho")
        print("  4. Construtor interativo de labirintos")
        print("  5. Sair")
        print()
        
        choice = input("Digite sua escolha (1-5): ").strip()
        
        if choice == '1':
            test_custom_maze()
        elif choice == '2':
            test_maze_variations()
        elif choice == '3':
            compare_maze_sizes()
        elif choice == '4':
            interactive_maze_builder()
        elif choice == '5':
            print("\n👋 Até logo!")
            break
        else:
            print("\n❌ Opção inválida! Tente novamente.")
        
        input("\nPressione ENTER para continuar...")


if __name__ == "__main__":
    main()
