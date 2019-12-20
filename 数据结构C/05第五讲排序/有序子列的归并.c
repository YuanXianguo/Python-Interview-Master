//L=左边起始位置，R=右边起始位置，RightEnd=右边终点位置
void Merge(ElementType A[], ElementType TmpA[], int L, int R, int RightEnd)
{	//左边终点位置，假设左右两列挨着 
	LeftEnd = R - 1;
	Tmp = L; //存放结果的数组的初始位置
	NumElements = RightEnd - L + 1;
	while ( L <= LeftEnd && R <= RightEnd )
	{
		if (A[L] <= A[R])	TmpA[Tmp++] = A[L++];
		else				TmpA[Tmp++] = A[R++];
	} 
	while ( L <= LeftEnd )
		TmpA[Tmp++] = A[L++];
	while ( R <= RightEnd )
		TmpA[Tmp++] = A[R++];
	for (i=0; i< NumElements; i++,RinghtEndj--)
	{
		A[RightEnd] = TmpA[RightEnd];
	}
} 


