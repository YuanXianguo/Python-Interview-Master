void TopSort()
{
	for ( ͼ��ÿ������V )
	{
		if ( Indegree[V]==0 )
		{
			Enqueue(V, Q);
		} 
	}
	while ( !IsEmpty(Q) )
	{
		V = Dequeue(Q);
		���V�����߼�¼V��������;
		cnt ++;
		for ( V��ÿ���ڽӵ�W )
		{
			if ( --Indegree[W] == 0 );
			Enqueue(W, Q);
		} 
	}  
	if ( cnt != ������� )
	{
		Error ("ͼ���л�·");
	}
} 


