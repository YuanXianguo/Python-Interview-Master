void Merge_pass(ElementType A[], ElementType TmpA[], int N, int length)
{	//length=��ǰ�������еĳ��� 
	for (i=0; i<=N-2*length; i+=2*length)
	{	//��A��Ԫ�ع鲢��TmpA 
		Merge1(A, TmpA, i, i+length, i+2*length-1);
	} 
	if ( i+length < N )
	{	//�鲢���2������ 
		Merge1(A, TmpA, i, i+length, N-1);
	}
	else//���ֻʣ1������ 
	{
		for (j=i; j<N; j++)	  TmpA[j] = A[j];
	}
}

void Merge_Sort(ElementType A[], int N)
{
	int length = 1;//��ʼ�������г��� 
	ElementType *TmpA;
	TmpA = malloc(N * sizeof(ElementType));
	if ( TmpA != NULL )
	{
		while ( length < N )
		{
			Merge_pass(A, TmpA, N, length);
			length *= 2;
			Merge_pass(TmpA, A, N, length);
			length *= 2;
		}
		free(TmpA);
	}
	else Error("�ռ䲻��");
} 


