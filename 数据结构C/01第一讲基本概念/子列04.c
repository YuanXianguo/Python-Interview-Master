int MaxSubseqSum4(int A[], int N)
{
	int ThisSum, MaxSum;
	int i;
	ThisSum = MaxSum = 0; 
	for ( i=0; i<N; i++ )
	{
		ThisSum += A[i];
		if ( ThisSum > MaxSum )
		{
			MaxSum = ThisSum;
		}
		else if ( ThisSum < 0 )//�����ǰ���к�Ϊ�� 
		{   //�򲻿���ʹ����Ĳ��ֺ���������֮ 
			ThisSum = 0;
		}
	} 
	return MsxSum;
} 


