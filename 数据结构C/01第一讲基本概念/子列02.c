int MaxSubseqSum2(int A[], int N)
{
	int ThisSum, MaxSum = 0;
	int i, j;
	for ( i=0; i<N; i++ )   //i���������λ�� 
	{
		ThisSum = 0; //A[i]��A[j]�����к� 
		for ( j=i; j<N; j++)//j�������Ҷ�λ�� 
		{
			ThisSum += A[j];
			if ( ThisSum > MaxSum )
			{
				MaxSum = ThisSum;
			}
		}
	} 
	return MsxSum;
} 


