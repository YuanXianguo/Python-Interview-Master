int MaxSubseqSum2(int A[], int N)
{
	int ThisSum, MaxSum = 0;
	int i, j;
	for ( i=0; i<N; i++ )   //i是子列左端位置 
	{
		ThisSum = 0; //A[i]到A[j]的子列和 
		for ( j=i; j<N; j++)//j是子列右端位置 
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


