void TopSort()
{
	for ( cnt = 0; cnt < 顶点个数; cnt ++ )
	{
		V = 未输出的入度为0的顶点; 
		if ( 这样的V不存在 )
		{
			Error ("图中有回路");
			break;
		}
		输出V，或者记录V的输出序号;
		for ( V的每个邻接点W )
		{
			Indegree[W]--;
		} 
	}
} 


