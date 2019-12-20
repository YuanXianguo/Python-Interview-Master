BinTree Delete(ElementType X, BinTree BST)
{
	Position Tmp;
	if ( !BST )
	{
		printf("未找到");
	}
	else if ( X < BST->Data)
	{
		BST->Left = Delete(X, BST->Left);
	} 
	else if ( X > BST->Data)
	{
		BST->Right = Delete(X, BST->Right);
	} 
	else
	{	//被删除结点有左右两个子结点 
		if ( BST->Left && BST->Right )
		{	//在右子树中找最小的元素填充删除元素结点 
			Tmp = FindMin(BST->Right);
			BST->Data = Tmp->Data;
			//在删除结点的右子树中删除最小元素 
			BST->Right = Delete(BST->Data, BST->Right); 
		}
		else
		{	//被删除结点有一个或无结点 
			Tmp = BST;
			if ( !BST->Left )
			{
				BST = BST->Right;
			}
			else if ( !BST->Right )
			{
				BST = BST->Left;
			}
			free(Tmp);
		}
	}
	return BST;
}


