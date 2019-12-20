void Prim()
{
	MST = {s};
	while (1)
	{	//dist为顶点到这棵树的距离 
		V = 未收录顶点中dist最小者;
		if ( 这样的V不存在 )
			break;
		将V收录进MSF:dist[V] = 0;
		for ( V的每个邻接点W )
		{
			if ( dist[W] != 0 )
			{
				if ( E(v,w) < dist[W] )
				{
					dist[W] = E(v,w);
					parent[W] = V;
				}
			}
		 } 
	}
	if ( MSF中收的顶点不到|V|个 )
	{
		Error ( "生成树不存在,图不连通" );
	}
}

 
