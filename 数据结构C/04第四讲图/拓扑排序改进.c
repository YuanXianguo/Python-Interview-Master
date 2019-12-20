void TopSort()
{
	for ( 图中每个顶点V )
	{
		if ( Indegree[V]==0 )
		{
			Enqueue(V, Q);
		} 
	}
	while ( !IsEmpty(Q) )
	{
		V = Dequeue(Q);
		输出V，或者记录V的输出序号;
		cnt ++;
		for ( V的每个邻接点W )
		{
			if ( --Indegree[W] == 0 );
			Enqueue(W, Q);
		} 
	}  
	if ( cnt != 顶点个数 )
	{
		Error ("图中有回路");
	}
} 


