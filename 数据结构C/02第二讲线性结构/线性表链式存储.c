typedef struct LNode_ {
	ElementType Data;
	int Next; 
} LNode， *List;

List PtrL;

//求表长
int Length(List PtrL)
{
	List p = PtrL; //p指向表的第一个结点
	int i = 0;
	while ( p )
	{
		p = p->Next;
		i ++;
	} 
	return i; //当前p指向的是第i个结点 
} 

//按序号查找
List FindKth(List PtrL, int K)
{
	List p = PtrL; 
	int i = 1;
	while ( p && i < K)
	{
		p = p->Next;
		i ++;
	} 
	if ( !p )
	{
		printf("不在表中");
		return;
	}
	else
	{
		return p;
	}
} 

//按值查找
int Find(List PtrL, ElementType X)
{
	List p = PtrL;
	int i = 1;
	while ( p && p->Data != X )
	{
		p = p->Next;
		i ++;
	}
	if ( !p )
	{
		printf("不在表中");
		return;
	}
	else
	{
		return i;
	}
} 

//插入（第i-1(1<=i<=n+1)个结点后插入一个值为X的新结点）
List Insert(List PtrL, ElementType X, int i) 
{
	List p, s;
	p = FindKth(PtrL, i-1);
	if ( i == 1)
	{
		s = (List)malloc(sizeof(LNode));
		s->Data = X;
		s->Next = PtrL;
		return s;
	}
	if ( !p )
	{
		printf("参数i错误");
		return;
	}
	else 
	{
		s = (List)malloc(sizeof(LNode));
		s->Data = X;
		s->Next = p->Next;
		p->Next = s;
		return PtrL;
	}
} 

//删除（删除表的第i(1<=i<=n+1)个结点的元素）
List Delete(List PtrL, int i)
{
	List p, s;
	for ( s=NULL,p=PtrL; p; s=p,p=p->Next )
	{
		if ( p == FindKth(PtrL, i) )
		{
			if ( s )
			{
				s->Next = p->Next;
			}
			else
			{
				Ptrl = p->Next;
			}
			free(p);
			break;
		}
	}
	printf("不在表中");
	return PtrL;
}
