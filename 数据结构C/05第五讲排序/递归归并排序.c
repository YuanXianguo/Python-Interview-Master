void MSort(ElementType A[], ElementType TmpA[], int L, int RightEnd)
{
	int Center;
	if ( L < RightEnd )
	{
		Center = (L + RightEnd) / 2;
		MSort(A, TmpA, L, Center);
		MSort(A, TmpA, Center+1, RightEnd);
		Merge(A, TmpA, L, Center+1, RightEnd);
	}
}

void Merge_Sort(ElementType A[], int N)
{
	ElementType *TmpA;
	TmpA = malloc(N * sizeof(ElementType));
	if ( TmpA != NULL )
	{
		MSort(A, TmpA, 0, N-1);
		free(TmpA);
	}
	else Error("¿Õ¼ä²»×ã");
} 
