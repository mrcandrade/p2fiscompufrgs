import csv  
import matplotlib.pyplot as plt  
import os  # adicionado para caminho relativo

def plot_errors(csv_path='output/errors.csv', out='output/questao2.png'):
    Ns = []  # abrindo lista de n subintervalos
    trap_err = []  # lista pra erros do trapezio
    simp_err = []  # lista pra erros do simpson

    base = os.path.dirname(__file__)  # pega pasta do script
    csv_path = os.path.join(base, csv_path)  # monta caminho relativo para entrada
    out = os.path.join(base, out)  # monta caminho relativo para saida

    with open(csv_path, 'r', newline='') as f:  # abrindo o csv
        reader = csv.reader(f)  # criando leitor do csv
        header = next(reader, None)  # pulando header
        for row in reader:  # loop nas linhas
            if not row:  # se linha vazia pula
                continue
            N = int(row[0])  # pegando n
            et = float(row[1])  # erro trapezio
            es = float(row[2])  # erro simpson
            Ns.append(N)  # guardando n na lista
            trap_err.append(et)  # guardando erro trap
            simp_err.append(es)  # guardando erro simp

    plt.figure(figsize=(7,5))  # criando figura
    plt.loglog(Ns, trap_err, 'o-', label='trapezio')  # plotando curva trap
    plt.loglog(Ns, simp_err, 's-', label='simpson')  # plotando curva simp

    ref2 = [trap_err[0] * (Ns[0]/n)**2 for n in Ns]  # referencia ordem 2
    ref4 = [simp_err[0] * (Ns[0]/n)**4 for n in Ns]  # referencia ordem 4
    plt.loglog(Ns, ref2, '--', color='gray', label='~N^-2')  # plot ref2
    plt.loglog(Ns, ref4, ':', color='gray', label='~N^-4')  # plot ref4

    plt.xlabel('N n subintervalos')  # nome eixo x
    plt.ylabel('erro absoluto')  # nome eixo y
    plt.title('xonvergencia: erro vs N (trapezio e simpson)')  # titulo rapido
    plt.grid(True, which='both', ls='--')  # ativando grid
    plt.legend()  # legenda
    plt.tight_layout()  # arrumando layout
    plt.savefig(out, dpi=150)  # salvando imagem
    print(f'salvo em {out}')  # print rapido

if __name__ == '__main__':  # se rodar direto
    plot_errors()  # chama a funcao
