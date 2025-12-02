README – Como Rodar os Programas em C e Python

Estrutura 

projeto/
 ├── questao1.c
 ├── questao1_plot.py
 ├── questao2.c
 ├── questao2_plot.py
 ├── questao3.c
 ├── questao3_plot.py
 ├── force.txt
 ├── output/
        ├── errors.csv        
        ├── questao3_a.csv    
        ├── questao3_b.csv    
        ├── questao1.png
        ├── questao2.png
        ├── questao3.png
 └── README.txt

--------------------------------------------

QUESTÃO 1

Parte em C

1. Compilar:

Windows (MinGW):
gcc questao1.c -o questao1.exe -lm

Linux/Mac:
gcc questao1.c -o questao1 -lm

2. Executar:
./questao1

Requisitos:
- O arquivo force.txt deve estar na mesma pasta.

Saída:
- Imprime o valor de k e alpha.

Parte em Python

Executar:
python questao1_plot.py

Requisitos:
pip install matplotlib

Saída:
- Gera questao1.png.

--------------------------------------------

QUESTÃO 2

Parte em C

1. Compilar:
gcc questao2.c -o questao2 -lm

2. Executar:
./questao2

Saída:
- Gera o arquivo errors.csv.

Parte em Python

Executar:
python questao2_plot.py

Saída:
- Gera questao2.png.

--------------------------------------------

QUESTÃO 3

Parte em C

1. Compilar:
gcc questao3.c -o questao3 -lm

2. Executar:
./questao3

Saída:
- Gera questao3_a.csv e questao3_b.csv.

Parte em Python

Executar:
python questao3_plot.py

Saída:
- Gera questao3_a.png e questao3_b.png.

--------------------------------------------

Resumo geral

Para qualquer arquivo C:
gcc arquivo.c -o programa -lm
./programa

Para qualquer script Python:
python arquivo.py

Arquivos necessários:
- force.txt (questão 1)
- errors.csv (questão 2)
- questao3_a.csv e questao3_b.csv (questão 3)
