void Dijkstra(Vertex s)
{	//���ܽ���и��ߵ���� 
	while (1)
	{
		V = δ��¼������dist��С��;
		if ( ������V������ )
			break; 
		collected[V] = true;
		for ( V��ÿ���ڽӵ�W )
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
 

