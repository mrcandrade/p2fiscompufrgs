#include <stdio.h>  // inclui stdio
#include <stdlib.h> // inclui stdlib
#include <math.h>   // inclui math pra exp e pow

const double C_val = 1.0e-2;  // capacitancia
const double q0 = 1.0;  // carga inicial
const double R_val = 3200.0;  // resistencia

double tau() {
    return R_val * C_val;  // constante de tempo
}

double q_analytic(double t) {
    double tt = t / tau();  // normaliza t
    return q0 * exp(-tt);  // q(t)
}

double i_analytic(double t) {
    return -(q0 / tau()) * exp(-t / tau());  // derivada exata dq/dt
}

double deriv_forward(double t, double dt) {
    double q1 = q_analytic(t + dt);  // q em t+dt
    double q0v = q_analytic(t);  // q em t
    return (q1 - q0v) / dt;  // forward
}

double deriv_centered(double t, double dt) {
    double q_plus = q_analytic(t + dt);  // q em t+dt
    double q_minus = q_analytic(t - dt);  // q em t-dt
    return (q_plus - q_minus) / (2.0 * dt);  // centered
}

int main() {

    const char *out_dir = ".";  // caminho relativo: pasta atual

    double dt_fixed = 1e-4;  // dt fixo
    double t_start = 0.0;  // inicio
    double t_end = 10.0;  // fim
    double t_step = 0.5;  // passo principal

    char path_a[512];  // buffer caminho
    snprintf(path_a, sizeof(path_a), "%s/questao3_a.csv", out_dir);  // monta caminho arquivo a

    FILE *fa = fopen(path_a, "w");  // abre csv a
    fprintf(fa, "t,i_exact,i_forward,err_forward,i_centered,err_centered\n");  // header

    int n_points = (int)((t_end - t_start) / t_step + 0.5) + 1;  // qtd pontos

    int k;  // indice loop
    for (k = 0; k < n_points; k++) {  // loop principal
        double t = t_start + k * t_step;  // tempo atual

        double ie = i_analytic(t);  // i exato
        double ifw = deriv_forward(t, dt_fixed);  // forward
        double icd = deriv_centered(t, dt_fixed);  // centered

        double efw = fabs(ifw - ie);  // erro forward
        double ecd = fabs(icd - ie);  // erro centered

        fprintf(fa, "%.6f,%.12e,%.12e,%.12e,%.12e,%.12e\n",
                t, ie, ifw, efw, icd, ecd);  // escreve linha csv
    }

    fclose(fa);  // fecha arquivo a

    double t_study = 5.0;  // tempo fixo para parte b
    double dts[] = {1e-1,1e-2,1e-3,1e-4,1e-5,1e-6,1e-7};  // dt variados
    int M = sizeof(dts)/sizeof(dts[0]);  // qtd dt

    char path_b[512];  // buffer caminho
    snprintf(path_b, sizeof(path_b), "%s/questao3_b.csv", out_dir);  // caminho arquivo b

    FILE *fb = fopen(path_b, "w");  // abre csv b
    fprintf(fb, "dt,err_forward,err_centered,if_forward,if_centered,i_exact\n");  // header

    int j;  // indice
    for (j = 0; j < M; j++) {  // loop dt
        double dt = dts[j];  // dt atual

        double ie = i_analytic(t_study);  // i exato
        double ifw = deriv_forward(t_study, dt);  // forward
        double icd = deriv_centered(t_study, dt);  // centered

        double efw = fabs(ifw - ie);  // erro forward
        double ecd = fabs(icd - ie);  // erro centered

        fprintf(fb, "%.12e,%.12e,%.12e,%.12e,%.12e,%.12e\n",
                dt, efw, ecd, ifw, icd, ie);  // escreve linha csv
    }

    fclose(fb);  // fecha arquivo b

    return 0;  // fim
}
