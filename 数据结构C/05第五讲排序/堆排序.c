void Heap_Sort(ElementType A[], int N)
{
	BuildHeap(A); //O(N)
	for (i=0; i<N; i++)
	{
		TmpA[i] = DeleteMin(A) //O(logN) 
	}
	for (i=0; i<N; i++)
	{
		A[i] = TmpA[i];
	}
} 


