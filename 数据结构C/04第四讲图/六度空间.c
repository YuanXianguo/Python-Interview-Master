void SDS()
{
	for ( each V in G )
	{
		count = BFS(V);
		Output(count/N);
	}
} 

int BFS(Vertex V)
{
	visited[V] = true;
	int count = 1;
	int level = 0;
	int last = V;
	Enqueue(V, Q);
	while ( !IsEmpty(Q) )
	{
		V = Dequeue(Q);
		for ( V的每个邻接点W )
		{
			if ( !visited[W])
			{
				visited[W] = true;
				Enqueue(W, Q);
				count ++;
				int tail = W;
			}
		} 
		if ( V== last )
		{
			level ++;
			last = tail;
		}
		if ( level == 6 )  break;
	}
	return count;
}

