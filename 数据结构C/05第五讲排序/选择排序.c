void Selection_Sort(ElementType A[], int N)
{
	for (i=0; i<N; i++)
	{	//��A[i]��A[N-1]������СԪ��������λ�ø���MinPosition
		MinPosition = ScanForMin(A, i, N-1);
		//��δ���򲿷ֵ���СԪ�������򲿷ֵ����λ�� 
		Swap(A[i], A[MinPosition]);
	}
}


