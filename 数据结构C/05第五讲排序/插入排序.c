void Insertion_Sort(ElementType A[], int N)
{
	for ( P=1, P<N; P++ )
	{
		Tmp = A[P];//����һ����
		for ( i=P; i>=0 && A[i-1]>Tmp; i-- )
		{
			A[i] = A[i-1];//�Ƴ���λ 
		} 
		A[i] = Tmp;//������λ 
	}
}


