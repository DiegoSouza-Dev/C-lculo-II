{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "KREtaZEnuX2a"
      },
      "source": [
        "# Integral Definida e Teorema Fundamental do Cálculo\n",
        "## Exercícios Práticos - Ciência da Computação\n",
        "\n",
        "Este notebook contém 5 exercícios práticos sobre integral definida, Soma de Riemann e Teorema Fundamental do Cálculo, contextualizados com exemplos de Ciência da Computação.\n",
        "\n",
        "**Instruções:** Execute cada célula sequencialmente e analise os resultados."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Ytojn2EBuX2d"
      },
      "source": [
        "---\n",
        "## Exercício 1: Carga em Servidor Web\n",
        "\n",
        "**Problema:**\n",
        "\n",
        "Um servidor recebe requisições a uma taxa $r(t) = 2t$ requisições por segundo, no intervalo $t \\in [0, 5]$ segundos.\n",
        "\n",
        "Estime o total de requisições:\n",
        "1. Usando Soma de Riemann pela direita com $n = 50$\n",
        "2. Comparando com o valor exato via integral definida"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Y-RhEXMpuX2e",
        "outputId": "7ce0983e-218a-461b-b464-74d6e0162aec"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Soma de Riemann (direita, n=5): 30.0000 req\n",
            "Valor exato: 25 req\n",
            "Erro absoluto: 5.0000 req\n"
          ]
        }
      ],
      "source": [
        "import numpy as np\n",
        "\n",
        "def r(t):\n",
        "    return 2 * t  # taxa de requisições (req/s)\n",
        "\n",
        "a, b = 0, 5       # intervalo de tempo em segundos\n",
        "n = 5\n",
        "dt = (b - a) / n\n",
        "\n",
        "# Soma de Riemann pela direita\n",
        "t_right = np.linspace(a + dt, b, n)\n",
        "riemann_sum = np.sum(r(t_right) * dt)\n",
        "\n",
        "# Valor exato: ∫_0^5 2t dt = [t^2]_0^5 = 25\n",
        "exact = 25\n",
        "\n",
        "print(f\"Soma de Riemann (direita, n={n}): {riemann_sum:.4f} req\")\n",
        "print(f\"Valor exato: {exact} req\")\n",
        "print(f\"Erro absoluto: {abs(riemann_sum - exact):.4f} req\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "pjhzT1ysuX2g"
      },
      "source": [
        "---\n",
        "## Exercício 2: API REST sob Carga\n",
        "\n",
        "**Problema:**\n",
        "\n",
        "A taxa de chamadas a uma API é aproximada por $f(t) = 100\\sin(t) + 200$ chamadas por minuto em $t \\in [0, \\pi]$ minutos.\n",
        "\n",
        "Implemente `riemann_sum` que suporte métodos `left`, `right`, `midpoint` e compare as aproximações com o valor de referência dado pela integral simbólica."
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def f(t):\n",
        "    return 100 * np.sin(t) + 200\n",
        "\n",
        "# funçao\n",
        "a2, b2 = 0, np.pi\n",
        "n2 = 100\n",
        "dt2 = (b2 - a2) / n2\n",
        "\n",
        "# ponto médio de cada subintervalo\n",
        "t_right = np.linspace(a2 + dt2, b2, n2)\n",
        "\n",
        "\n",
        "#cálculos das somas\n",
        "sum_right = np.sum(f(t_right) * dt2)\n",
        "\n",
        "exact2 = 200 + 200 * np.pi\n",
        "\n",
        "#cálculo do Erro Absoluto\n",
        "erro_abs = abs(sum_right - exact2)\n",
        "\n",
        "print(f\"Resultados para n = {n2}\")\n",
        "print(f\"Soma de Riemann (Direita):  {sum_right:.4f}\")\n",
        "print(f\"Valor Exato:  {exact2:.4f}\")\n",
        "print(f\"Erro Absoluto:  {erro_abs:.4f}\")\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "REmYbAbB4s1M",
        "outputId": "6b6e7f41-4f18-4fd8-cc17-565cbbaa1269"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Resultados para n = 100\n",
            "Soma de Riemann (Direita):  828.3021\n",
            "Valor Exato:  828.3185\n",
            "Erro Absoluto:  0.0164\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "tnTbFyGWuX2h"
      },
      "source": [
        "---\n",
        "## Exercício 3: Tempo de CPU Total de um Processo\n",
        "\n",
        "**Problema:**\n",
        "\n",
        "Um processo em execução tem consumo de CPU instantâneo $c(t) = 0.5t^2 + 3$ unidades de CPU por segundo em $t \\in [0, 10]$.\n",
        "\n",
        "Calcule:\n",
        "1. A integral definida com SymPy\n",
        "2. Uma aproximação numérica por Riemann (midpoint)\n",
        "3. O erro entre as duas respostas"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "import sympy as sp\n",
        "\n",
        "#calculo Simbólico com SymPy\n",
        "t_sym = sp.Symbol('t')\n",
        "c_sym = 0.5 * t_sym**2 + 3\n",
        "\n",
        "#calcula a integral de 0 a 10\n",
        "exact_integral = sp.integrate(c_sym, (t_sym, 0, 10))\n",
        "exact_val = float(exact_integral)\n",
        "\n",
        "#aproximação por Riemann\n",
        "def c_num(t):\n",
        "    return 0.5 * t**2 + 3\n",
        "\n",
        "a3, b3 = 0, 10\n",
        "n3 = 100\n",
        "dt3 = (b3 - a3) / n3\n",
        "\n",
        "# pontos médios\n",
        "t_mid = np.linspace(a3 + dt3/2, b3 - dt3/2, n3)\n",
        "midpoint_sum = np.sum(c_num(t_mid) * dt3)\n",
        "\n",
        "# 3. Cálculo do Erro\n",
        "erro_abs = abs(midpoint_sum - exact_val)\n",
        "\n",
        "print(f\" Exercício 3: Consumo de CPU \")\n",
        "print(f\"Valor Exato (SymPy):  {exact_val:.4f}\")\n",
        "print(f\"Aproximação (Midpoint): {midpoint_sum:.4f}\")\n",
        "print(f\"Erro Absoluto: {erro_abs:.4e}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EY3YsuLe9igz",
        "outputId": "e03ad1f1-d536-4284-e0f7-188e31815ea7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            " Exercício 3: Consumo de CPU \n",
            "Valor Exato (SymPy):  196.6667\n",
            "Aproximação (Midpoint): 196.6625\n",
            "Erro Absoluto: 4.1667e-03\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "MXqplcuyuX2i"
      },
      "source": [
        "---\n",
        "## Exercício 4: Custo Total de Execução de Algoritmo\n",
        "\n",
        "**Problema:**\n",
        "\n",
        "Um modelo contínuo para o \"custo instantâneo\" de um algoritmo em função do tamanho de entrada $n$ é $g(n) = 0.01n^2 + 2n$ unidades de tempo por unidade de $n$, para $n \\in [0, 1000]$.\n",
        "\n",
        "1. Use SciPy para calcular $\\int_{0}^{1000} g(n)\\,dn$ (custo total acumulado)\n",
        "2. Interprete o resultado"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "from scipy.integrate import quad\n",
        "\n",
        "#função\n",
        "def g(n):\n",
        "    return 0.01 * n**2 + 2 * n\n",
        "\n",
        "#  0 a 1000\n",
        "result, error = quad(g, 0, 1000)\n",
        "\n",
        "print(f\"Custo total acumulado: {result:.2f} unidades de tempo\")\n",
        "print(f\"Erro estimado da integração: {error}\")"
      ],
      "metadata": {
        "id": "rIV0ECD99i4C",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "8a44cdae-31f0-45bb-ebdf-b3072a75d24f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Custo total acumulado: 4333333.33 unidades de tempo\n",
            "Erro estimado da integração: 4.8109664400423454e-08\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "VzLi03_iuX2j"
      },
      "source": [
        "---\n",
        "## Exercício 5: Visualização - Área sob Curva de Uso de Memória\n",
        "\n",
        "**Problema:**\n",
        "\n",
        "O uso de memória de um serviço em execução é modelado por $m(t) = 50t + 100$ MB em $t \\in [0, 10]$ minutos.\n",
        "\n",
        "Plote a função e preencha a área correspondente à integral $\\int_0^{10} m(t)\\,dt$, mostrando o valor numérico."
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "#função: m(t) = 50t + 100\n",
        "def m(t):\n",
        "    return 50 * t + 100\n",
        "\n",
        "#parâmetros do intervalo\n",
        "t_start, t_end = 0, 10\n",
        "t = np.linspace(t_start, t_end, 500)\n",
        "y = m(t)\n",
        "\n",
        "#integral de 50t + 100 de 0 a 10: [25t^2 + 100t] de 0 a 10\n",
        "valor_integral = (25 * 10**2 + 100 * 10) - (25 * 0**2 + 100 * 0)\n",
        "\n",
        "#gráfico\n",
        "plt.figure(figsize=(10, 6))\n",
        "plt.plot(t, y, 'b', linewidth=2, label='m(t) = 50t + 100 (MB)')\n",
        "\n",
        "#preenchendo a área sob a curva\n",
        "plt.fill_between(t, y, color='skyblue', alpha=0.4, label=f'Área (Integral) = {valor_integral} MB·min')\n",
        "\n",
        "#codigo de exibiçao\n",
        "plt.title('Uso de Memória ao Longo do Tempo')\n",
        "plt.xlabel('Tempo (minutos)')\n",
        "plt.ylabel('Memória (MB)')\n",
        "plt.grid(True, linestyle='--', alpha=0.7)\n",
        "plt.legend()\n",
        "plt.ylim(0, 650)\n",
        "plt.xlim(0, 10)\n",
        "\n",
        "plt.show()\n",
        "\n",
        "print(f\"O valor numérico da área (integral) é: {valor_integral} MB-minutos\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 583
        },
        "id": "3RDb1i3UrE-H",
        "outputId": "16ce2a6b-df96-4b1e-d35c-1ce0caed06af"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1000x600 with 1 Axes>"
            ],
            "image/png": "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8884d+5cob6/R48eWLduHR599FF0794d586dw8KFCxEZGalKPnv27In27dvjtddew/nz59GgQQP8/PPP+P777/H888/bVgjvxGQy4d13383THhgYiGeeeQYffvghRowYgbZt2+Lxxx/HlStXMGfOHFStWhUTJkwo/Ivynz59+uChhx7Ciy++iNOnT6N27dr44YcfkJKSAkB9edu0adPQtWtXREVFYeTIkcjMzMTcuXNhMBjw1ltv3fE4o0ePxrx58xATE4P9+/cjLCwMK1asyHOvmLu7u93naBUeHo53330X//d//4fz58+jT58+KFOmDM6dO4dvv/0WY8aMwcSJE+95//k5d+4cevXqhS5dumDnzp344osvMHjwYNvPXIMGDTBs2DB8+umnSE1NRdu2bbFnzx4sX74cffr0Qfv27e06HiIqYZxSA5GIyE6++OIL0aJFC+Hr6ys8PT1F7dq1xeTJk1Vl1YUQ4pNPPhFt2rQR5cqVE56eniI8PFy89NJLIi0tTbXdgQMHRHR0tPDz8xM+Pj6iffv2YseOHYUay7Vr18TQoUOFv7+/MBgMYujQoeLgwYN5SkoLIcSZM2dETEyMCA0NFe7u7uKBBx4QPXr0EF9//fVdj4P/Sr/fSUGl8Q8ePCj69u1rex2qVKkiBgwYILZu3XrX7y2orHnbtm3zlNW/cuWKGDFihAgKChIeHh6iXr16eV4Da3n3adOm5dlnfqXf4+PjxaOPPioCAgKEwWAQ/fv3F5cvXxYAxJtvvnnH10NRFDFlyhRRpUoV4enpKRo1aiTWr18vhg0bJqpUqaLa9ubNm2LChAmiQoUKwt3dXdSsWVNMmzZNVTK/INZy7fn9Cw8Pt223Zs0a0ahRI+Hp6SkCAwPFE088IeLj4/PsK7/X2/r+5JSUlCQGDx4sypQpIwwGgxg+fLjYvn27ACBWr16t2vaXX34RrVq1Et7e3sLf31/07NlTHDt27K5zE0KICxcuiF69egkfHx8RFBQknnvuOfHTTz+pSr8XZY53k7v0u9U333wjWrduLXx9fYWvr6+oXbu2iI2NFSdPnrRtk19cCiFElSpVRPfu3fO05/65sr7Ox44dE/369RNlypQRZcuWFePGjVOVtBdCCJPJJCZPniyqVasm3N3dRaVKlcT//d//5fk9RESljyTEfdzVTERERMXSd999h0cffRTb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X331lYYOHRr83OHDh6tVq1ZatWqV1qxZowceeEANGjQI7mdnZyszM1PLli07qVoAABHgAABwCmbNmuWkpaUFP+7QoYMzZ86csNv88Y9/dPr27es4juPs2LHDkeS89NJLwf25c+c6kpzFixcH1yZOnOh07tw5+PGoUaOc9PR0p7y8PLj2/PPPO40aNXL8fr9z6NAhp0GDBs5rr70W3K+qqnKysrKcSZMmnbD+nJwc55FHHjnmTJKcbdu2BdfuuOMOp2HDhk5ZWVlwbeDAgc4dd9wR/LhNmzbOM888E/xYkvOHP/wh+PGhQ4ccSc57770X/Dqh3zvHcZx58+Y5oX8djx8/3snJyQm7zT/+8Q/H6/U6O3fuDK598cUXjiRn5cqVjuM4TkpKijN79uwTnttxHKdnz57Oww8//IO3AQBEDle2AAA/WXl5ubZv365bbrlFjRo1Cv559NFHj3m62tlnnx3878zMTElS9+7dw9b27dsX9jk5OTlq2LBh8OO+ffvq0KFD2rVrl7Zv367q6mr169cvuN+gQQOdd9552rRp0wlrPnLkiBITE49Zb9iwoTp06BBWT9u2bcNej3a8Gr8v9JzJyclKTU390c/5MZs2bVLr1q3VunXr4Fq3bt3UuHHj4FnHjh2rW2+9Vbm5uXr88ceP+3TBpKQkHT58+LRqAQCcPJotAMBPdujQIUnSiy++qHXr1gX/bNiwQStWrAi7behT2mpeo/T9NROjyZs1a6aDBw8esx5aS009x1v7sRp/6HM8Ho8cxwnbr66uPunaf8jDDz+sL774QldccYU+/PBDdevWTfPmzQu7zYEDB+rUUA8AqOtotgAAP1lmZqaysrL01VdfqWPHjmF/2rVrd9r3v379eh05ciT48YoVK9SoUSO1bt1aHTp0UHx8vD755JPgfnV1tVatWqVu3bqd8D579uypjRs3nnZtP0VGRobKyspUXl4eXFu3bl3YbeLj48OGcEhS165dtWvXLu3atSu4tnHjRhUXF4ed9YwzztC9996rf/zjH7r22ms1a9as4F5FRYW2b9+unj17RvhUAIATodkCAJyWCRMmaOLEiZoyZYq2bNmizz//XLNmzdLTTz992vddVVWlW265RRs3btTChQs1fvx45efny+PxKDk5WXfddZfuv/9+LVq0SBs3btRtt92mw4cP65ZbbjnhfQ4cOFDLly8/pqExoU+fPmrYsKF+//vfa/v27ZozZ05w2mCNtm3baseOHVq3bp3279+vyspK5ebmqnv37ho+fLjWrl2rlStXauTIkbrwwgvVu3dvHTlyRPn5+VqyZIm++eYbffLJJ1q1apW6du0avN8VK1YoISFBffv2NXxqAKi/aLYAAKfl1ltv1UsvvaRZs2ape/fuuvDCCzV79uyIXNm6+OKL1alTJ/Xv319Dhw7VVVddFfYGyo8//riGDBmiESNG6JxzztG2bdv0/vvvq0mTJie8z8suu0xxcXH63//939Ou71Slp6fr1Vdf1cKFC9W9e3fNnTv3mDeEHjJkiC699FINGDBAGRkZmjt3rizL0vz589WkSRP1799fubm5at++vd544w1JktfrVVFRkUaOHKkzzjhD119/vS677LKwyY1z587V8OHDw14DBwBwl+V8/8njAADUAqNHj1ZxcbHeeeediN/3tGnT9O677+r999+P+H3XRvv371fnzp21evXqiDTBAICTExftAgAAMO2OO+5QcXGxysrKlJKSEu1yXPf1119r+vTpNFoAYBhXtgAAtZKbV7YAADCBZgsAAAAAXMCADAAAAABwAc0WAAAAALiAZgsAAAAAXECzBQAAAAAuoNkCAAAAABfQbAEAAACAC2i2AAAAAMAFNFsAAAAA4AKaLQAAAABwwf8Hfeyy7HrRgb8AAAAASUVORK5CYII=\n"
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "O valor numérico da área (integral) é: 3500 MB-minutos\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "SQypmmV9uX2k"
      },
      "source": [
        "---\n",
        "## Conclusão\n",
        "\n",
        "Nestes exercícios você:\n",
        "- Calculou integrais definidas usando Soma de Riemann\n",
        "- Comparou métodos numéricos (left, right, midpoint)\n",
        "- Usou ferramentas simbólicas (SymPy) e numéricas (SciPy)\n",
        "- Visualizou a interpretação geométrica da integral\n",
        "- Aplicou conceitos em contextos de Ciência da Computação\n",
        "\n",
        "**Próximos passos:** Experimente modificar os parâmetros (intervalos, funções, valores de n) para explorar o comportamento das aproximações!"
      ]
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.8.0"
    },
    "colab": {
      "provenance": []
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}