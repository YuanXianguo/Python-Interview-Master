void Kruskal(Graph G)
{
	MST = { };
	while ( MST中不到|V|-1条边 && E中还有边 )
	{
		从E中取一条权重最小的边E(v,w);//最小堆
		将E(v,w)从E中删除;
		if ( E(v,w)不在MST中构成回路 )//并查集
		{
			将E(v,w)加入MST; 
		}
		else 
		{
			彻底无视E(v,w); 
		} 
	}
	if ( MST中不到|V|-1条边 )
	{
		Error ("生成树不存在，图不连通");
	} 
}



