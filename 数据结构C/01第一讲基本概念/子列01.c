int MaxSubseqSum1(int A[], int N)
{
	int ThisSum, MaxSum = 0;
	int i, j, k;
	for ( i=0; i<N; i++ )   //i���������λ�� 
	{
		for ( j=i; j<N; j++)//j�������Ҷ�λ�� 
		{
			ThisSum = 0; //A[i]��A[j]�����к� 
			for ( k=i; k<=j; k++)
			{
				ThisSum += A[k];
			}
			if ( ThisSum > MaxSum )
			{
				MaxSum = ThisSum;
			}
		}
	} 
	return MsxSum;
} 


