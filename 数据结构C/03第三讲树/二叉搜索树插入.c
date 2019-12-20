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
		{	//递归插入右子树 
			BST->Right = Insert(X, BST->Right);
		}
		else if ( X < BST->Data)
		{
			BST->Left = Insert(X, BST->Left);
		}
		//else X已经存在，什么都不做 
	}
	return BST;
} 


