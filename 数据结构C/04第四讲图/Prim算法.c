void Prim()
{
	MST = {s};
	while (1)
	{	//distΪ���㵽������ľ��� 
		V = δ��¼������dist��С��;
		if ( ������V������ )
			break;
		��V��¼��MSF:dist[V] = 0;
		for ( V��ÿ���ڽӵ�W )
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
	if ( MSF���յĶ��㲻��|V|�� )
	{
		Error ( "������������,ͼ����ͨ" );
	}
}

 
