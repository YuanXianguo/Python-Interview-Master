#include <stdio.h>
#include <time.h>
 
clock_t start, stop;//clock_tʱclock()�������صı�������
double duration; //��¼���⺯������ʱ�䣬����λ��λ 

int main()
{   //���ڲ��Է�Χ�ڵ�׼������д��clock()����֮ǰ 
	start = clock(); //��ʼ��ʱ
	MyFunction();   //���⺯�� 
	stop = clock();//ֹͣ��ʱ 
	duration = ((double)(stop - start))/CLK_TCK;
	//�������ڲ��Է�Χ�Ĵ���д�ں��� 
	
	return 0;
}


