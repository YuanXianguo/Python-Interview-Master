void DFS(Vertex V)
{
	visited[V] = true;
	for ( V的每个邻接点W )
	{
		if ( !visited[W])
		{
			DFS(W);
		}
	} 
}

void BFS(Vertex V)
{
	visited[V] = true;
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
			}
		} 
	}
}

