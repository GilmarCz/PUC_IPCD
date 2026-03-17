# ============================================================
# Introdução à Programação e à Ciência de Dados
# Soluções dos Exercícios - Aula 01
# ============================================================

# Importação das bibliotecas necessárias:
# - math: funções matemáticas como pi e fatorial
# - numpy: operações com vetores e arrays numéricos
# - matplotlib.pyplot: criação de gráficos
import math
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# Exercício 1 - Exibição de Texto Simples
# ============================================================
# print() exibe uma mensagem de texto no console.
# O operador * repete o caractere "=" 60 vezes, formando um separador visual.
print("=" * 60)
print("EXERCÍCIO 1 - Exibição de Texto Simples")
print("=" * 60)

# Exibe a mensagem de boas-vindas diretamente como string
print("Bem-vindo ao curso de Python!")

# ============================================================
# Exercício 2 - Operações Matemáticas
# ============================================================
print("\n" + "=" * 60)
print("EXERCÍCIO 2 - Números e Operações Matemáticas")
print("=" * 60)

# Declara duas variáveis inteiras e imprime a soma entre elas.
# A f-string permite embutir as variáveis diretamente no texto,
# incluindo a expressão a + b calculada em tempo real.
a, b = 15, 30
print(f"{a} + {b} = {a + b}")

# ============================================================
# Exercício 3 - Uso de Variáveis na Impressão
# ============================================================
print("\n" + "=" * 60)
print("EXERCÍCIO 3 - Uso de Variáveis na Impressão")
print("=" * 60)

# Armazena o nome (string) e a idade (inteiro) em variáveis.
# A f-string insere os valores das variáveis dentro da mensagem formatada.
nome = "Carlos"
idade = 25
print(f"{nome} tem {idade} anos.")

# ============================================================
# Exercício 4 - Formatação de Números Decimais
# ============================================================
print("\n" + "=" * 60)
print("EXERCÍCIO 4 - Formatação de Números Decimais")
print("=" * 60)

# math.pi retorna o valor de π com alta precisão (~3.14159265...).
# O especificador :.2f na f-string limita a exibição a 2 casas decimais.
pi = math.pi
print(f"O valor de π é aproximadamente {pi:.2f}")

# ============================================================
# Exercício 5 - Quebra de Linha e Tabulação
# ============================================================
print("\n" + "=" * 60)
print("EXERCÍCIO 5 - Quebra de Linha e Tabulação")
print("=" * 60)

# \n dentro de uma string insere uma quebra de linha.
# \t insere um caractere de tabulação (recuo), simulando indentação visual.
print("Lista de Compras:\n\t- Maçã\n\t- Pão\n\t- Leite")

# ============================================================
# Exercício 6a - Impressão com f-strings (simples)
# ============================================================
print("\n" + "=" * 60)
print("EXERCÍCIO 6a - Impressão com f-strings")
print("=" * 60)

# As variáveis aluno e nota são inseridas diretamente na mensagem
# usando f-strings, que permitem interpolação de variáveis com {}.
aluno = "Ana"
nota = 9.5
print(f"A aluna {aluno} obteve a nota {nota} na prova.")

# ============================================================
# Exercício 6b - Tabela de alunos com médias
# ============================================================
print("\n" + "=" * 60)
print("EXERCÍCIO 6b - Tabela de Alunos com Médias")
print("=" * 60)

# Lista com os nomes dos alunos e lista de listas com suas notas.
# Cada sublista contém as 4 notas de um aluno na mesma ordem da lista de nomes.
alunos = ["Lucas", "Ana", "Pedro", "Mariana", "João"]
notas = [
    [8.5, 7.0, 9.2, 6.8],  # Notas de Lucas
    [6.0, 8.5, 7.4, 9.1],  # Notas de Ana
    [7.5, 9.0, 8.8, 6.5],  # Notas de Pedro
    [9.2, 8.3, 7.7, 8.9],  # Notas de Mariana
    [5.5, 6.8, 7.0, 6.2],  # Notas de João
]

# sep define a linha separadora da tabela com caracteres + e -.
sep = "+------------+------+------+------+------+-------+"

# Imprime o cabeçalho da tabela.
# :<10 alinha o texto à esquerda em 10 caracteres; :>4 alinha à direita em 4.
print(sep)
print(f"| {'Aluno':<10} | {'N1':>4} | {'N2':>4} | {'N3':>4} | {'N4':>4} | {'Média':>5} |")
print(sep)

# zip() combina as duas listas percorrendo nome e notas juntos a cada iteração.
# sum(ns) soma as 4 notas e len(ns) retorna 4, calculando assim a média.
# :>5.2f formata a média com 2 casas decimais alinhada à direita em 5 caracteres.
for nome_aluno, ns in zip(alunos, notas):
    media = sum(ns) / len(ns)
    print(f"| {nome_aluno:<10} | {ns[0]:>4} | {ns[1]:>4} | {ns[2]:>4} | {ns[3]:>4} | {media:>5.2f} |")
print(sep)

# ============================================================
# Exercício 7 - Sequência do Somatório (exibição)
# ============================================================
print("\n" + "=" * 60)
print("EXERCÍCIO 7 - Sequência do Somatório (N termos)")
print("=" * 60)

# Gera a sequência de texto do somatório sem calcular o valor numérico.
# Para cada k de 1 até N, monta a string "k/(N-k+1)!" representando cada termo.
# List comprehension cria a lista de termos em uma única linha.
# join() une os termos da lista separando-os por " + ".
N = 5
termos = [f"{k}/{N - k + 1}!" for k in range(1, N + 1)]
print(f"Para N = {N}:")
print(" + ".join(termos))

# ============================================================
# Exercício 8 - Somatório com resultado
# ============================================================
print("\n" + "=" * 60)
print("EXERCÍCIO 8 - Somatório com Resultado")
print("=" * 60)

# input() lê o valor digitado pelo usuário como string;
# int() converte esse valor para inteiro.
N = int(input("Digite o valor de N para o somatório: "))

# Para cada termo k, calcula o expoente do fatorial no denominador (N-k+1),
# divide k pelo fatorial desse expoente e acumula na variável soma.
# math.factorial() calcula o fatorial de um número inteiro.
termos_str = []
soma = 0.0
for k in range(1, N + 1):
    exp_fat = N - k + 1                  # expoente decrescente do fatorial
    valor = k / math.factorial(exp_fat)  # valor numérico do termo k
    soma += valor                        # acumula a soma total
    termos_str.append(f"{k}/{exp_fat}!") # guarda a representação textual

# :.6f exibe o resultado com 6 casas decimais
print(f"\nSequência: {' + '.join(termos_str)}")
print(f"Resultado: S = {soma:.6f}")

# ============================================================
# Exercício 9 - Lista e Função de Presença
# ============================================================
print("\n" + "=" * 60)
print("EXERCÍCIO 9 - Uso de Lista e Função")
print("=" * 60)

# Lista predefinida com 10 valores inteiros
valores = [10, 25, 30, 45, 50, 65, 70, 85, 90, 100]

def verificar_presenca(lista, valor):
    """
    Verifica se um valor está presente em uma lista.
    Parâmetros:
        lista: a lista onde a busca será feita
        valor: o número a ser procurado
    Retorna:
        True  → se o valor for encontrado na lista
        False → se o valor não estiver na lista
    O operador 'in' percorre a lista e retorna True assim que encontra o valor.
    """
    return valor in lista

# Exibe a lista e lê o número digitado pelo usuário
print(f"Lista: {valores}")
numero = int(input("Digite um número para buscar: "))

# Chama a função e exibe a mensagem conforme o resultado (True ou False)
if verificar_presenca(valores, numero):
    print(f"O número {numero} está na lista!")
else:
    print(f"O número {numero} NÃO está na lista.")

# ============================================================
# Exercício 10 - Método dos Trapézios + Gráfico
# ============================================================
print("\n" + "=" * 60)
print("EXERCÍCIO 10 - Área sob a Curva (Método dos Trapézios)")
print("=" * 60)

def f(x):
    """
    Define a função matemática a ser integrada: f(x) = x² + 2x + 1.
    Parâmetro:
        x: valor numérico ou array numpy
    Retorna:
        o valor de f(x) para cada x fornecido
    Ao receber um array numpy, opera elemento a elemento automaticamente.
    """
    return x**2 + 2*x + 1

def metodo_trapezios(f, a, b, n=1000):
    """
    Calcula a integral aproximada de f no intervalo [a, b]
    utilizando o Método dos Trapézios.
    Parâmetros:
        f: função a ser integrada
        a: limite inferior do intervalo
        b: limite superior do intervalo
        n: número de subintervalos (quanto maior, mais preciso)
    Retorna:
        área aproximada sob a curva (valor numérico)

    O método divide o intervalo [a,b] em n partes iguais de largura h = (b-a)/n.
    Em cada subintervalo, aproxima a área por um trapézio formado pelos
    valores f(x_i) e f(x_{i+1}), somando (h/2) * (f(x_i) + f(x_{i+1})).
    """
    h = (b - a) / n      # largura de cada subintervalo
    soma = 0.0
    for i in range(n):
        # soma a área do trapézio entre x_i e x_{i+1}
        soma += f(a + i * h) + f(a + (i + 1) * h)
    return (h / 2) * soma  # multiplica pela meia largura ao final

# Lê os limites de integração e o número de subintervalos fornecidos pelo usuário
a_val = float(input("Limite inferior de integração (a): "))
b_val = float(input("Limite superior de integração (b): "))
n_val = int(input("Número de subintervalos (n, ex: 1000): "))

# Chama a função de integração e exibe o resultado
area = metodo_trapezios(f, a_val, b_val, n_val)
print(f"\nÁrea aproximada sob f(x) = x² + 2x + 1")
print(f"Intervalo: [{a_val}, {b_val}] com {n_val} subintervalos")
print(f"Resultado: A ≈ {area:.6f}")

# --- Gráfico ---
# np.linspace gera 500 pontos igualmente espaçados para traçar a curva suavemente.
# x_plot: intervalo um pouco maior que [a,b] para mostrar contexto da curva.
# x_fill: intervalo exato [a,b] para colorir a área integrada.
x_plot = np.linspace(a_val - 0.5, b_val + 0.5, 500)
x_fill = np.linspace(a_val, b_val, 500)

fig, ax = plt.subplots(figsize=(9, 5))

# Plota a curva da função em azul
ax.plot(x_plot, f(x_plot), 'b-', linewidth=2, label='f(x) = x² + 2x + 1')

# Preenche a área sob a curva no intervalo [a,b] com azul semitransparente
ax.fill_between(x_fill, f(x_fill), alpha=0.25, color='blue', label=f'Área ≈ {area:.4f}')

# Linha horizontal no eixo y=0 (referência)
ax.axhline(0, color='k', linewidth=0.8)

# Linhas verticais tracejadas indicando os limites a e b
ax.axvline(a_val, color='green', linestyle='--', linewidth=1.2, label=f'a = {a_val}')
ax.axvline(b_val, color='red',   linestyle='--', linewidth=1.2, label=f'b = {b_val}')

# Rótulos dos eixos, título, legenda e grade
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.set_title(f"Método dos Trapézios — f(x) = x² + 2x + 1\nIntervalo [{a_val}, {b_val}], n = {n_val}")
ax.legend()
ax.grid(True, alpha=0.4)
plt.tight_layout()

# Salva o gráfico na pasta atual (compatível com Google Colab)
# No Colab o arquivo aparece no painel de arquivos (ícone de pasta à esquerda)
plt.savefig("exercicio10_grafico.png", dpi=150)
plt.show()
print("\nGráfico salvo como 'exercicio10_grafico.png' na pasta atual.")