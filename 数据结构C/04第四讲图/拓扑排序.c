void TopSort()
{
	for ( cnt = 0; cnt < �������; cnt ++ )
	{
		V = δ��������Ϊ0�Ķ���; 
		if ( ������V������ )
		{
			Error ("ͼ���л�·");
			break;
		}
		���V�����߼�¼V��������;
		for ( V��ÿ���ڽӵ�W )
		{
			Indegree[W]--;
		} 
	}
} 


