//L=�����ʼλ�ã�R=�ұ���ʼλ�ã�RightEnd=�ұ��յ�λ��
void Merge(ElementType A[], ElementType TmpA[], int L, int R, int RightEnd)
{	//����յ�λ�ã������������а��� 
	LeftEnd = R - 1;
	Tmp = L; //��Ž��������ĳ�ʼλ��
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


