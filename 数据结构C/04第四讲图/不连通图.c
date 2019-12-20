void ListComponents(Graph G)
{
	for ( each V in G )
	{
		if ( !visited[V] )
		{
			DFS(V); //or BFS(V)
		}
	}
}


