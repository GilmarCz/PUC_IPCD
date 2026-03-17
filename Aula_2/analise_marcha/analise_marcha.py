"""
=========================================================
ANÁLISE COMPUTACIONAL DE MARCHA HUMANA
Footprints (Center of Pressure - CoP)

Disciplina: Introdução à Programação e Ciência de Dados

Autor: Gilmar Czeika

Descrição:
Este programa realiza a análise de dados de marcha humana
utilizando footprints (trajetória do centro de pressão).

Funcionalidades:

1. Leitura automática de múltiplos arquivos Excel
2. Limpeza e preparação dos dados
3. Visualização da trajetória da marcha
4. Separação entre pé esquerdo e direito
5. Cálculo de parâmetros espaciais e temporais
6. Classificação simples da marcha
7. Exportação dos resultados para Excel
8. Geração de gráficos

=========================================================
"""

# IMPORTAÇÃO DAS BIBLIOTECAS

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# FUNÇÃO PARA CARREGAR DADOS

def carregar_dados(arquivo):
    """
    Lê um arquivo Excel contendo dados da marcha
    e realiza a limpeza básica dos dados.
    """

    print(f"\nCarregando arquivo: {arquivo}")

    df = pd.read_excel(arquivo)

    # remover dados inválidos
    if "Obj" in df.columns:
        df = df[df["Obj"] != 998]

    return df


# FUNÇÃO PARA CALCULAR PARÂMETROS DA MARCHA

def calcular_parametros(df):
    """
    Calcula parâmetros espaciais e temporais da marcha.
    """

    resultados = {}
    
    # STEP LENGTH - distância média entre passos
    distancias = np.sqrt(np.diff(df["X"])**2 + np.diff(df["Y"])**2)
    step_length = np.mean(distancias)
    
    # STRIDE LENGTH  
    stride_length = step_length * 2
    
    # STEP WIDTH
    step_width = np.std(df["Y"])

    # STRIDE WIDTH
    stride_width = step_width * 2
    
    # FOOT LENGTH
    foot_length = df["X"].max() - df["X"].min()
    
    # STEP TIME
    step_time = np.mean(np.diff(df["Time"]))
    
    # STRIDE TIME
    stride_time = step_time * 2
    
    # VELOCIDADE
    tempo_total = df["Time"].max() - df["Time"].min()

    distancia_total = np.sqrt(
        (df["X"].iloc[-1] - df["X"].iloc[0])**2 +
        (df["Y"].iloc[-1] - df["Y"].iloc[0])**2
    )

    velocity = distancia_total / tempo_total

    resultados["Step Length"] = step_length
    resultados["Stride Length"] = stride_length
    resultados["Step Width"] = step_width
    resultados["Stride Width"] = stride_width
    resultados["Foot Length"] = foot_length
    resultados["Step Time"] = step_time
    resultados["Stride Time"] = stride_time
    resultados["Velocity"] = velocity

    return resultados

# FUNÇÃO PARA CLASSIFICAR MARCHA
def classificar_marcha(velocity, step_width):
    """
    Classificação simples da marcha baseada
    em heurísticas biomecânicas básicas.
    """
    if velocity < 0.5 or step_width > 10:
        return "Possível marcha anormal"

    return "Marcha normal"

# FUNÇÃO PARA GERAR GRÁFICOS
def gerar_graficos(df, nome_arquivo):
    # gráfico da trajetória completa
    plt.figure()
    plt.scatter(df["X"], df["Y"])
    plt.title(f"Footprints da Marcha - {nome_arquivo}")
    plt.xlabel("Coordenada X")
    plt.ylabel("Coordenada Y")
    plt.grid(True)
    plt.savefig(f"resultados/footprints_{nome_arquivo}.png")
    plt.close()

    # separar pés
    pe_esquerdo = df[df["L/R"] == 0]
    pe_direito = df[df["L/R"] == 1]

    plt.figure()
    plt.scatter(pe_esquerdo["X"], pe_esquerdo["Y"], label="Pé esquerdo")
    plt.scatter(pe_direito["X"], pe_direito["Y"], label="Pé direito")
    plt.title(f"Footprints Separados - {nome_arquivo}")
    plt.xlabel("Coordenada X")
    plt.ylabel("Coordenada Y")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"resultados/feet_{nome_arquivo}.png")
    plt.close()

# FUNÇÃO PRINCIPAL
def main():

    pasta_dados = "dados"
    resultados_gerais = []

    for arquivo in os.listdir(pasta_dados):
        if arquivo.endswith(".xlsx"):
            caminho = os.path.join(pasta_dados, arquivo)
            df = carregar_dados(caminho)
            gerar_graficos(df, arquivo)
            parametros = calcular_parametros(df)
            classificacao = classificar_marcha(
                parametros["Velocity"],
                parametros["Step Width"]
            )

            parametros["Arquivo"] = arquivo
            parametros["Classificação"] = classificacao
            resultados_gerais.append(parametros)

    tabela_final = pd.DataFrame(resultados_gerais)

    print("\nResultados finais:")
    print(tabela_final)
    tabela_final.to_excel("resultados/analise_marcha_resultados.xlsx", index=False)
    print("\nResultados salvos em: resultados/analise_marcha_resultados.xlsx")

# EXECUÇÃO DO PROGRAMA
if __name__ == "__main__":
    main()