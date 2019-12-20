BinTree Delete(ElementType X, BinTree BST)
{
	Position Tmp;
	if ( !BST )
	{
		printf("δ�ҵ�");
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
	{	//��ɾ����������������ӽ�� 
		if ( BST->Left && BST->Right )
		{	//��������������С��Ԫ�����ɾ��Ԫ�ؽ�� 
			Tmp = FindMin(BST->Right);
			BST->Data = Tmp->Data;
			//��ɾ��������������ɾ����СԪ�� 
			BST->Right = Delete(BST->Data, BST->Right); 
		}
		else
		{	//��ɾ�������һ�����޽�� 
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


