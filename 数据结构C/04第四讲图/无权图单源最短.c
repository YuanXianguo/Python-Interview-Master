void Unweight(Vertex S)
{
	Enqueue(S, Q);
	while ( !IsEmpty(Q) )
	{
		V = Dequeue(Q);
		for ( V��ÿ���ڽӵ�W )
		{	//dist[W]=S��W����̾��룬dist[S]=0 
			if ( dist[W]==-1 )
			{
				dist[W] = dist[V] + 1;
				//path[W]=S��W��·�Ͼ�����ĳ���� 
				path[W] = V;
				Enqueue(W, Q);
			}
		} 
	}
}


