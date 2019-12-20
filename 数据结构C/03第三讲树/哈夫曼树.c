typedef struct TreeNode_ {
	int Weight;
	struct TreeNode_ Left, Right;
} TreeNode, *HuffmanTree; 

HuffmanTree HuffmanJ(MinHeap H)
{	//假设H->Size个权值已经存在H->Elements[]->Weight里 
	int i;
	HuffmanTree T;
	BuildMinHeap(H); //将H->Elemnts[]按权值调整为最小堆
	for (i=1; i<H->Size; i++)
	{
		T = malloc(sizeof(TreeNode)); //建立新结点
		T->Left = DeleteMin(H); //删除最小堆中最小结点，作为新T的左子结点 
		T->Right = DeleteMin(H); 
		T->Weight = T->Left->Weight + T->Right->Weight;//计算新权值
		Insert(H, T); 
	 } 
	 T = DeleteMin(H); //调整后的最小堆的堆顶（最小值）即哈夫曼树树根 
	 return T;
}


