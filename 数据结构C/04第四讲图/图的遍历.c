void DFS(Vertex V)
{
	visited[V] = true;
	for ( V��ÿ���ڽӵ�W )
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
		for ( V��ÿ���ڽӵ�W )
		{
			if ( !visited[W])
			{
				visited[W] = true;
				Enqueue(W, Q);
			}
		} 
	}
}

