void Dijkstra(Vertex s)
{	//不能解决有负边的情况 
	while (1)
	{
		V = 未收录顶点中dist最小者;
		if ( 这样的V不存在 )
			break; 
		collected[V] = true;
		for ( V的每个邻接点W )
		{
			if ( collectec[W] == false )
			{
				if ( dist[V]+E<v,w> < dist[W] )
				{
					dist[W] = dist[V] + E<v,w>;
					path[W] = V;
				}
			}
		}			 
	}
} 
 

