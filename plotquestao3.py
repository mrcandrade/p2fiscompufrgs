import csv  
import matplotlib.pyplot as plt  
import os  # adicionado para caminhos relativos

def plot_part_a(csv_path='output/questao3_a.csv', out='output/questao3_a.png'):
    base = os.path.dirname(__file__)  # pega pasta onde esta o script
    csv_path = os.path.join(base, csv_path)  # caminho relativo arquivo csv
    out = os.path.join(base, out)  # caminho relativo saida png

    t = []  # lista tempo
    ie = []  # lista corrente exata
    ifw = []  # lista derivada forward
    icd = []  # lista derivada centrada
    with open(csv_path, 'r') as f:  # abrindo csv
        reader = csv.reader(f)  # criando leitor
        next(reader)  # pulando header
        for row in reader:  # lendo linhas
            if not row: continue  # pula linha vazia
            t.append(float(row[0]))  # tempo
            ie.append(float(row[1]))  # i exata
            ifw.append(float(row[2]))  # forward
            icd.append(float(row[4]))  # centrada

    plt.figure(figsize=(8,5))  # criando figura
    plt.plot(t, ie, 'k-', label='i exato')  # curva exata
    plt.plot(t, ifw, 'ro', label='derivada a direita')  # forward
    plt.plot(t, icd, 'bs', label='derivada centrada')  # centrada
    plt.xlabel('t s')  # nome eixo x
    plt.ylabel('i a')  # nome eixo y
    plt.title('parte a: it — exato vs numerico dt=1e-4')  # titulo
    plt.legend()  # legenda
    plt.grid(True)  # grid
    plt.tight_layout()  # arrumar layout
    plt.savefig(out, dpi=150)  # salvar figura
    print('salvo em', out)  # mensagem salva

def plot_part_b(csv_path='output/questao3_b.csv', out='output/questao3_b.png'):
    base = os.path.dirname(__file__)  # pasta do script
    csv_path = os.path.join(base, csv_path)  # caminho relativo csv
    out = os.path.join(base, out)  # caminho relativo saida

    dts = []  # lista dt
    err_fw = []  # lista erros forward
    err_cd = []  # lista erros centered
    with open(csv_path, 'r') as f:  # abrindo csv
        reader = csv.reader(f)  # leitor
        next(reader)  # pular header
        for row in reader:  # lendo linhas
            if not row: continue  # pula vazias
            dts.append(float(row[0]))  # dt
            err_fw.append(float(row[1]))  # erro forward
            err_cd.append(float(row[2]))  # erro centrado

    plt.figure(figsize=(7,5))  # nova figura
    plt.loglog(dts, err_fw, 'o-', label='erro forward')  # grafico forward
    plt.loglog(dts, err_cd, 's-', label='erro centered')  # grafico centered
    plt.xlabel('dt s')  # eixo x
    plt.ylabel('erro absoluto a')  # eixo y
    plt.title('parteb: erro em t=5.0 s vs dt escala log-log')  # titulo
    plt.grid(True, which='both', ls='--')  # grid log
    plt.legend()  # legenda
    plt.tight_layout()  # layout
    plt.savefig(out, dpi=150)  # salvar png
    print('salvo em', out)  # aviso

if __name__ == '__main__':  # se rodado direto
    plot_part_a()  # plota parte a
    plot_part_b()  # plota parte b
