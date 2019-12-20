void Unweight(Vertex S)
{
	Enqueue(S, Q);
	while ( !IsEmpty(Q) )
	{
		V = Dequeue(Q);
		for ( V的每个邻接点W )
		{	//dist[W]=S到W的最短距离，dist[S]=0 
			if ( dist[W]==-1 )
			{
				dist[W] = dist[V] + 1;
				//path[W]=S到W的路上经过的某顶点 
				path[W] = V;
				Enqueue(W, Q);
			}
		} 
	}
}


