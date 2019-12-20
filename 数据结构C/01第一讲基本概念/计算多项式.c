#include <stdio.h>
#include <time.h>
#include <math.h>
#define MAXN 100 //多项式最大项数，即阶数+1 
#define MAXK 1e7 //被测函数最大重复调用次数 
clock_t start, stop;
double duration;
double f1(int n, double a[], double x);
double f2(int n, double a[], double x);
void ftest(double(*pf)(int n, double a[], double x), int n, double a[], double x);

int main()
{   
	int i;
	double a[MAXN];
	for ( i=0; i<MAXN; i++ )
	{
		a[i] = (double)i;//初始化系数 
	}
	
	double (*pf)(int n, double a[], double x) = f1;
	ftest(pf, MAXN-1, a, 1.1);
	pf = f2;
	ftest(pf, MAXN-1, a, 1.1);

	return 0;
}

void ftest(double(*pf)(int n, double a[], double x), int n, double a[], double x)
{
	int i;
	start = clock(); 
	for ( i=0; i<MAXK; i++ ) //重复调用函数以获得充分多的时钟打点数 
	{
		(*pf)(n, a, x); 
	}
	stop = clock();
	duration = ((double)(stop - start))/CLK_TCK/MAXK;
	printf("ticks=%f\n", (double)(stop-start));
	printf("duration=%6.2e\n", duration);
}

double f1(int n, double a[], double x)
{
	int i;
	double p = a[0];
	for ( i=1; i<=n; i++ )
	{
		p += (a[i] * pow(x, i));
	}
	return p;
}

double f2(int n, double a[], double x)
{
	int i;
	double p = a[n];
	for ( i=n; i>0; i-- )
	{
		p = a[i-1] + x*p;
	}
	return p;
}
