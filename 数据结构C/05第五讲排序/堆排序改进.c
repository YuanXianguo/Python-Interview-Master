void Heap_Sort(ElementType A[], int N)
{	//BuildHeap(A)
	for (i=N/2; i>=0; i--)
	{
		PercDown(A, i, N);
	}
	for (i=N-1; i>0; i--)
	{	//DeleteMax
		Swap(&A[0], &A[i]);
		PercDown(A, 0, i);
	}
} 


