void Quicksort(ElementType A[], int N)
{
	if ( N < 2 )	return;
	pivot = ��A[]��ѡһ����Ԫ;
	��S = {A[] ��pivot֮��}�ֳ�2�������Ӽ�;
		A1={a��S | a��pivot}��
		A2={a��S | a��pivot};
	A[] = Quicksort(A1,N1)��{pivot}��Quicksort(A2,N2); 
} 

ElementType Median3(ElementType A[], int Left, int Right)
{	//A[Left] <= A[Center] <= A[Right] 
	int Center = (Left + Right) / 2;
	if (A[Left] > A[Center])
		Swap(&A[Left], &A[Center]);
	if (A[Left] > A[Right])
		Swap(&A[Left], &A[Right]);
	if (A[Center] > A[Right])
		Swap(&A[Center], &A[Right]);
	//��pivot�ص��ұ� 
	Swap(&A[Center], &A[Right-1]);
	//ֻ��Ҫ����A[Left+1]...A[Right-2] 
	return A[Right-1]; //����pivot 
}

void Quicksort(ElementType A[], int Left, int Right)
{
	if ( Cutoff <= Right-Left )
	{
		Pivot = Median3(A, Left, Right);
		i = Left; j = Right - 1;
		for ( ; ; )
		{
			while (A[++i] < Pivot) { }
			while (A[--j] > Pivot) { }
			if ( i < j )
			{
				Swap(&A[i], &A[j]);
			}
			else break;
		}
		Swap(&A[i], &A[Right-1]);
		Quicksort(A, Left, i-1);
		Quicksort(A, i+1, Right);
	}
	else
		Insertion_Sort(A+Left, Right-Left+1);
}

void Quick_Sort(ElementType A[], int N)
{
	Quicksort(A, 0, N-1);
}
