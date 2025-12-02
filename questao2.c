#include <stdio.h>  // inclui stdio
#include <stdlib.h> // inclui stdlib
#include <math.h>   // inclui math pra pow e exp

const double k = 1.114327;  // constante k
const double alpha = 2.941676;  // constante alpha

double F(double x) {
    return k * pow(x, alpha);  // f(x) = k * x^alpha
}

double exact_work(double a, double b) {
    return k / (alpha + 1.0) * (pow(b, alpha + 1.0) - pow(a, alpha + 1.0));  // integral analitica
}

double trapezoid(double a, double b, int N) {
    double h = (b - a) / N;  // tamanho do passo
    double s = 0.5 * (F(a) + F(b));  // extremos
    int i;  // indice
    double x;  // ponto x
    for (i = 1; i < N; i++) {  // loop interno
        x = a + i * h;  // calcula x
        s += F(x);  // soma f(x)
    }
    return s * h;  // retorna integral
}

double simpson(double a, double b, int N) {
    if (N % 2 == 1) N += 1;  // ajusta n pra ser par
    double h = (b - a) / N;  // passo
    double s = F(a) + F(b);  // extremos
    int i;  // indice
    double x;  // ponto
    int coef;  // coef variavel
    for (i = 1; i < N; i++) {  // loop interno
        x = a + i * h;  // calcula ponto
        coef = (i % 2 == 1) ? 4 : 2;  // coef de simpson
        s += coef * F(x);  // soma ponderada
    }
    return s * h / 3.0;  // retorno
}

int main() {

    double a = 0.0;  // limite inferior
    double b = 5.0;  // limite superior
    int N = 1000;  // n inicial

    double W_exact = exact_work(a, b);  // integral exata
    double W_trap = trapezoid(a, b, N);  // trapezio
    double W_simp = simpson(a, b, N);  // simpson

    printf("k = %.6f, alpha = %.6f\n", k, alpha);  // printa params
    printf("W (exato) = %.12f\n", W_exact);  // resultado exato
    printf("W (trapezio, N=%d) = %.12f, erro = %.6e\n", N, W_trap, fabs(W_trap - W_exact));  // trapezio
    printf("W (simpson, N=%d) = %.12f, erro = %.6e\n", N, W_simp, fabs(W_simp - W_exact));  // simpson

    int Ns[] = {10,20,40,80,160,320,640,1280,2560};  // lista varios n
    int M = sizeof(Ns)/sizeof(Ns[0]);  // qtd elementos

    const char *out_file = "errors.csv";  // caminho relativo agora

    FILE *fp = fopen(out_file, "w");  // abre csv pra escrever
    fprintf(fp, "N,err_trap,err_simp\n");  // header csv

    int i;  // indice
    for (i = 0; i < M; i++) {  // loop sobre ns
        int n = Ns[i];  // n atual
        double wt = trapezoid(a, b, n);  // integral trap
        double ws = simpson(a, b, n);  // integral simp
        fprintf(fp, "%d,%.12e,%.12e\n", n, fabs(wt - W_exact), fabs(ws - W_exact));  // escreve linha
    }

    fclose(fp);  // fecha csv

    return 0;  // fim
}
