void Shell_Sort(ElementType A[], int N)
{	//希尔增量序列 
	for ( D=N/2; D>0; D/=2 )
	{	//插入排序 
		for ( P=D, P<N; P++ )
		{
			Tmp = A[P];
			for ( i=P; i>=D && A[i-D]>Tmp; i-=D )
			{
				A[i] = A[i-D];
			} 
			A[i] = Tmp;
		}
	}
}


