Position Find(ElementType X, BinTree BST)
{
	if ( !BST )
	{
		return NULL;
	}
	else
	{
		if ( X > BST->Data )
		{	//在右子树中继续查找 
			return Find(X, BST->Right);
		}
		else if ( X < BST->Data)
		{
			return Find(X, BST->Left);
		}
		else
		{	//查找成功 
			return BST;
		}
	}
} 

Position IterFind(ElementType X, BinTree BST)
{
	if ( !BST )
	{
		return NULL;		
	}
	else
	{
		while ( BST )
		{
			if ( X > BST->Data )
			{	//向右子树中移动，继续查找 
				BST = BST->Right;
			} 
			else if ( X < BST->Data)
			{
				BST = BST->Left;
			}
			else
			{	//查找成功 
				return BST;
			} 
		}
	}
	
} 

Position IterFind(ElementType X, BinTree BST)
{
	while ( !BST )
	{
		if ( X > BST->Data )
		{	//向右子树中移动，继续查找 
			BST = BST->Right;
		} 
		else if ( X < BST->Data)
		{
			BST = BST->Left;
		}
		else
		{	//查找成功 
			return BST;
		} 
	}
	return NULL;
} 

