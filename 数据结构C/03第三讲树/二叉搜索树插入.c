Position Insert(ElementType X, BinTree BST)
{
	if ( !BST )
	{
		BST = malloc(sizeof(TreeNode));
		BST->Data = X;
		BST->Left = BST->Right = NULL;
	}
	else
	{
		if ( X > BST->Data )
		{	//�ݹ���������� 
			BST->Right = Insert(X, BST->Right);
		}
		else if ( X < BST->Data)
		{
			BST->Left = Insert(X, BST->Left);
		}
		//else X�Ѿ����ڣ�ʲô������ 
	}
	return BST;
} 


