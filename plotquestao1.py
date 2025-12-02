import math  # importando math pra usar log e exp
import matplotlib.pyplot as plt  # importando matplotlib pra plot
import os  # adicionado para montar caminho relativo

def ler_dados(arquivo="force.txt"):  # alterado para nome simples relativo
    x_vals = []  # lista pra x
    f_vals = []  # lista pra f
    with open(arquivo, "r") as f:  # abrindo arquivo
        for linha in f:  # lendo linha
            linha = linha.strip()  # tirando espacos
            if not linha:  # se vazio pula
                continue
            partes = linha.split()  # separando
            if len(partes) < 2:  # se nao tem 2 valores pula
                continue
            try:
                x = float(partes[0])  # lendo x
                F = float(partes[1])  # lendo f
            except ValueError:
                continue  # se falhar pula
            if x > 0 and F > 0:  # só aceita valores positivos
                x_vals.append(x)  # adiciona x
                f_vals.append(F)  # adiciona f
    return x_vals, f_vals  # retorna listas

def ajuste_potencia(x_vals, f_vals):
    n = len(x_vals)  # qtd pontos
    soma_lx = 0.0  # soma log x
    soma_ly = 0.0  # soma log f
    soma_lx2 = 0.0  # soma log x ao quadrado
    soma_lxly = 0.0  # soma produto
    for i in range(n):  # loop pontos
        lx = math.log(x_vals[i])  # log x
        ly = math.log(f_vals[i])  # log f
        soma_lx += lx  # acumulando
        soma_ly += ly
        soma_lx2 += lx * lx
        soma_lxly += lx * ly
    denom = n * soma_lx2 - soma_lx * soma_lx  # denominador regressao
    alpha = (n * soma_lxly - soma_lx * soma_ly) / denom  # inclinacao
    a = (soma_ly - alpha * soma_lx) / n  # intercepto
    k = math.exp(a)  # voltando da forma log
    return k, alpha  # retorna ajuste

def plot_simples(x_vals, f_vals, k, alpha, saida='output/questao1.png'):
    x_min = min(x_vals)  # menor x
    x_max = max(x_vals)  # maior x
    x_fit = [x_min + i * (x_max - x_min) / 300.0 for i in range(301)]  # gerando x pra curva
    f_fit = [k * (xx ** alpha) for xx in x_fit]  # aplicando funcao ajustada

    fig, axs = plt.subplots(1, 2, figsize=(12, 5))  # criando duas figuras lado a lado

    axs[0].scatter(x_vals, f_vals, color='blue', label='dados')  # scatter simples
    axs[0].plot(x_fit, f_fit, color='red', label=f'ajuste: F={k:.3g} x^{alpha:.3g}')  # curva
    axs[0].set_xlabel('x (m)')  # nome eixo
    axs[0].set_ylabel('F (N)')
    axs[0].set_title('dados e ajuste linear')  # titulo rapido
    axs[0].grid(True)
    axs[0].legend()

    axs[1].scatter(x_vals, f_vals, color='blue', label='dados')  # scatter log
    axs[1].plot(x_fit, f_fit, color='red', label='ajuste')  # linha ajuste
    axs[1].set_xscale('log')  # eixo log
    axs[1].set_yscale('log')
    axs[1].set_xlabel('x (m) [log]')
    axs[1].set_ylabel('F (N) [log]')
    axs[1].set_title('graffico log-log')
    axs[1].grid(True, which='both', ls='--')
    axs[1].legend()

    fig.tight_layout()  # organizar layout
    fig.savefig(saida, dpi=150)  # salvar png
    plt.show()  # mostrar

def main():
    base = os.path.dirname(__file__)  # novo: pega pasta do script
    arquivo = os.path.join(base, "force.txt")  # novo: monta caminho relativo

    x_vals, f_vals = ler_dados(arquivo)  # lendo dados

    k, alpha = ajuste_potencia(x_vals, f_vals)  # ajustando
    print('pontos lidosno total', len(x_vals))  # print quantidade
    print(f'alpha = {alpha:.6f}')  # print alpha
    print(f'k     = {k:.6f}')  # print k

    plot_simples(x_vals, f_vals, k, alpha)  # plotando

if __name__ == '__main__':  # se rodar direto
    main()  # executa
