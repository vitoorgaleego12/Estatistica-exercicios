{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPCcDy6WLzjlTq70hCZOcLL",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/vitoorgaleego12/Estatistica-exercicios/blob/main/investimentos.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "cJddHhaUtnRz"
      },
      "outputs": [],
      "source": [
        "pip install pandas numpy matplotlib seaborn"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "def calcular_investimento(valor_investido, taxa_juros, anos):\n",
        "    \"\"\"Calcula o valor futuro de um investimento com juros compostos.\"\"\"\n",
        "    return valor_investido * (1 + taxa_juros) ** anos\n",
        "\n",
        "def simular_investimentos(valor_investido, taxa_juros, anos):\n",
        "    \"\"\"Simula o crescimento do investimento ao longo dos anos.\"\"\"\n",
        "    anos_lista = list(range(anos + 1))\n",
        "    valores_futuros = [calcular_investimento(valor_investido, taxa_juros, ano) for ano in anos_lista]\n",
        "    return anos_lista, valores_futuros\n",
        "\n",
        "def plotar_grafico(anos, valores_futuros, taxa_juros):\n",
        "    \"\"\"Plota o gráfico do crescimento do investimento.\"\"\"\n",
        "    plt.figure(figsize=(10, 6))\n",
        "    plt.plot(anos, valores_futuros, marker='o')\n",
        "    plt.title(f'Crescimento do Investimento com Taxa de {taxa_juros*100:.2f}% ao Ano')\n",
        "    plt.xlabel('Anos')\n",
        "    plt.ylabel('Valor Futuro (R$)')\n",
        "    plt.grid()\n",
        "    plt.show()\n",
        "\n",
        "def main():\n",
        "    print(\"Bem-vindo ao simulador de investimentos!\")\n",
        "\n",
        "    # Entrada de dados do usuário\n",
        "    valor_investido = float(input(\"Digite o valor do investimento inicial (R$): \"))\n",
        "    taxa_juros_percentual = float(input(\"Digite a taxa de juros anual (%): \"))\n",
        "    taxa_juros = taxa_juros_percentual / 100  # Converte para decimal\n",
        "    anos = int(input(\"Digite o número de anos para o investimento: \"))\n",
        "\n",
        "    # Simulação\n",
        "    anos_lista, valores_futuros = simular_investimentos(valor_investido, taxa_juros, anos)\n",
        "\n",
        "    # Exibir resultados\n",
        "    print(\"\\nResultado da simulação:\")\n",
        "    for ano, valor in zip(anos_lista, valores_futuros):\n",
        "        print(f\"Ano {ano}: R$ {valor:.2f}\")\n",
        "\n",
        "    # Plotar gráfico\n",
        "    plotar_grafico(anos_lista, valores_futuros, taxa_juros)\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    main()"
      ],
      "metadata": {
        "id": "pGxqrIN4tn8U"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}