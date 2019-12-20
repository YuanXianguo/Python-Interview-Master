#include <stdio.h>
#include <time.h>
 
clock_t start, stop;//clock_t时clock()函数返回的变量类型
double duration; //记录被测函数运行时间，以秒位单位 

int main()
{   //不在测试范围内的准备工作写在clock()调用之前 
	start = clock(); //开始计时
	MyFunction();   //被测函数 
	stop = clock();//停止计时 
	duration = ((double)(stop - start))/CLK_TCK;
	//其他不在测试范围的处理写在后面 
	
	return 0;
}


