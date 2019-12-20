Position Find(ElementType X, BinTree BST)
{
	if ( !BST )
	{
		return NULL;
	}
	else
	{
		if ( X > BST->Data )
		{	//���������м������� 
			return Find(X, BST->Right);
		}
		else if ( X < BST->Data)
		{
			return Find(X, BST->Left);
		}
		else
		{	//���ҳɹ� 
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
			{	//�����������ƶ����������� 
				BST = BST->Right;
			} 
			else if ( X < BST->Data)
			{
				BST = BST->Left;
			}
			else
			{	//���ҳɹ� 
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
		{	//�����������ƶ����������� 
			BST = BST->Right;
		} 
		else if ( X < BST->Data)
		{
			BST = BST->Left;
		}
		else
		{	//���ҳɹ� 
			return BST;
		} 
	}
	return NULL;
} 

