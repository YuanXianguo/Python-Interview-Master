typedef struct TreeNode_ {
	ElementType Data;
	struct TreeNode_ Left;
	struct TreeNode_ Right;
} TreeNode, *BinTree;

void InOrderTraversal(BinTree BT)
{
	BinTree T = BT;
	Stack S = CreatStack(MaxSize);
	while ( T || !IsEmpty(S) ) 
	{	//T���գ���ջ���� 
		while ( T )
		{
			Push(S, T);
			T = T->Left;
		}
		if ( !IsEmpty(S) )
		{
			T = Pop(S);
			printf("%d", T->Data);
			T = T->Right;
		}
	}
}


