数组中每个元素的类型描述为：
typedef struct {
	ElementType Data;
	int Parent;
} SetType; 

SetType S[]

int Find(SetType S[], ElementType X)
{//在数组S中查找值为X的元素所属集合，MaxSize是全局变量，为数组S的最大长度
	int i;
	for (i=0; i<MaxSize && S[i].Data!=X; i++)
	{
		if (i>=MaxSize)
		{
			return -1; //未找到 
		}
		else
		{
			for ( ; S[i].Parent>=0; i=S[i].Parent);
		}
		return i;//找到X所属集合，返回树根结点在数组S中的下标 
	 } 	
}

//元素少的集合并到元素多的集合树上 
void Union(SetType S[], ElementType X1, ElementType X2)
{
	int Root1, Root2;
	Root1 = Find(S, X1);
	Root2 = Find(S, X2);
	if (Root1 != Root2)
	{	//Parent小的绝对值大，元素多 
		if (S[Root1].Parent < S[Root2].Parent)
		{
			S[Root2].Parent = Root1;
		}
		else
		{
			S[Root1].Parent = Root2;
		}
	}
 } 
 


