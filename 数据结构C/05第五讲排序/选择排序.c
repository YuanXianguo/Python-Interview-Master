void Selection_Sort(ElementType A[], int N)
{
	for (i=0; i<N; i++)
	{	//从A[i]到A[N-1]中找最小元，并将其位置赋给MinPosition
		MinPosition = ScanForMin(A, i, N-1);
		//将未排序部分的最小元换到有序部分的最后位置 
		Swap(A[i], A[MinPosition]);
	}
}


