void LevelOrderTraversal(BinTree BT)
{
	Queue Q;
	BinTree T;
	if ( !BT ) return;
	Q = CreatQueue;
	Add(Q, BT);
	while ( !IsEmpty(Q) )
	{
		T = Delete(Q);
		printf("%d\t", T->Data); 
		if ( T->Left )
		{
			Add(Q, T->Left);
		}
		if ( T->Right )
		{
			Add(Q, T->Right);
		} 
	}
} 


