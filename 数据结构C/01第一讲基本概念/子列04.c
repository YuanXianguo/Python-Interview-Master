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
		else if ( ThisSum < 0 )//如果当前子列和为负 
		{   //则不可能使后面的部分和增大，抛弃之 
			ThisSum = 0;
		}
	} 
	return MsxSum;
} 


