void SelectionSort(int List[], int N)
{	//将N个整数List[0]...List[N-1]进行非递减排序
	for ( i=0; i<N; i++ )
	{
		MinPosition = ScanForMin(List, i, N-1);
		//从List[i]到List[N-1]中找最小元，并将其位置赋给MinPosition
		Swap(List[i], List[MinPositon]);
		//将未排序部分的最小元换到有序部分的最后位置
	}
}


