typedef struct TreeNode_ {
	int Weight;
	struct TreeNode_ Left, Right;
} TreeNode, *HuffmanTree; 

HuffmanTree HuffmanJ(MinHeap H)
{	//����H->Size��Ȩֵ�Ѿ�����H->Elements[]->Weight�� 
	int i;
	HuffmanTree T;
	BuildMinHeap(H); //��H->Elemnts[]��Ȩֵ����Ϊ��С��
	for (i=1; i<H->Size; i++)
	{
		T = malloc(sizeof(TreeNode)); //�����½��
		T->Left = DeleteMin(H); //ɾ����С������С��㣬��Ϊ��T�����ӽ�� 
		T->Right = DeleteMin(H); 
		T->Weight = T->Left->Weight + T->Right->Weight;//������Ȩֵ
		Insert(H, T); 
	 } 
	 T = DeleteMin(H); //���������С�ѵĶѶ�����Сֵ���������������� 
	 return T;
}


