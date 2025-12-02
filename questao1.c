#include <stdio.h>  // inclui stdio
#include <stdlib.h> // inclui stdlib
#include <math.h>   // inclui math pra log e exp

int main(void) {
    const char *fname = "force.txt";  // caminho relativo agora
    FILE *fp = fopen(fname, "r");  // abre arquivo pra leitura
    double x, F;  // variaveis pra ler x e f
    int n = 0;  // contador de pontos
    double sx = 0.0, sy = 0.0, sxx = 0.0, sxy = 0.0;  // acumuladores dos logs

    while (fscanf(fp, "%lf %lf", &x, &F) == 2) {  // lendo pares x f
        if (x <= 0.0 || F <= 0.0) {  // ignora valores nao positivos
            continue;
        }
        double lx = log(x);  // log de x
        double ly = log(F);  // log de f
        sx += lx;  // acumula lx
        sy += ly;  // acumula ly
        sxx += lx * lx;  // acumula lx^2
        sxy += lx * ly;  // acumula lx*ly
        n++;  // conta ponto valido
    }
    fclose(fp);  // fecha arquivo

    if (n < 2) {  // se poucos pontos sai
        return 1;
    }

    double denom = n * sxx - sx * sx;  // denominador regressao
    if (fabs(denom) < 1e-12) {  // evita divisao ruim
        return 1;
    }

    double b = (n * sxy - sx * sy) / denom;  // inclinacao
    double a = (sy - b * sx) / n;  // intercepto
    double alpha = b;  // alpha eh b
    double k = exp(a);  // k = exp(a)
    printf("pontos lidos: %d\n", n);  // print n
    printf("alpha = %.6f\n", alpha);  // print alpha
    printf("k     = %.6f\n", k);  // print k

    return 0;  // fim
}
