Position FindMin(BinTree BST)
{
	if ( !BST )
	{
		return NULL;
	}
	else if ( !BST->Left )
	{
		return BST;
	}
	else 
	{
		return FindMin(BST->Left);
	}
}

Position FindMax(BinTree BST)
{
	if ( !BST )
	{
		return NULL;
	}
	else
	{
		while ( BST->Right )
		{
			BST = BST->Right;
		}
		return BST;
	}	
}
