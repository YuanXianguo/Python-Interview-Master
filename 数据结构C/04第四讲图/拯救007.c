int DFS(Vertex V)
{
	visited[V] = true;
	if ( IsSaf(V)) answer = YES;
	else
	{
		for ( each W in G )
		{
			if ( !visited[W] && Jump(V, W ))
			{
				answer = DFS(W);
				if (answer==YES) break;
			}
		}
	}
	return answer;
}

void Save007(Graph G)
{
	for ( each V in G )
	{
		if ( !visited[V] && Firstjump[V] )
		{
			answer = DFS(V);
			if (answer==YES) break;
		}
	}
	if (answer==YES) output("Yes");
	else output("No");
 } 
