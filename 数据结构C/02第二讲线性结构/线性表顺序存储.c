typedef struct LNode_ {
	ElementType Data[MAXSIZE];
	int Last; 
} LNode， *List;

LNode L; 
List PtrL;

访问下标为i的元素：L.Data[i]或PtrL->Data[i];
线性表的长度：L.Last+1或PtrL->Last+1;

//初始化（建立空的顺序表） 
List MakeEmpty()
{
	List PtrL;
	PtrL = (List)malloc(sizeof(LNode));
	PtrL->Last = -1;
	return PtrL;
}

//查找
int Find(List PtrL, ElementType X)
{
	int i = 0;
	while ( i <= PtrL->Last && PtrL->Data[i] != X )
	{
		i ++;
	}
	if ( i > PtrL ) 	
	{
		printf("不在表中");
		return;
	}
	else
	{
		return i;
	}
} 

//插入（第i(1<=i<=n+1)个位置上插入一个值为X的新元素）
void Insert(List PtrL, ElementType X, int i) 
{
	int j;
	if ( PtrL->Last == MAXSIZE-1 )
	{
		printf("表满")；
		return; 
	} 
	if ( i<1 || i>PtrL->Last+1 )
	{
		printf("位置不合法");
		return;
	}
	for ( j=PtrL->Last; j>=i-1; j-- )
	{
		PtrL->Data[j+1] = PtrL->Data[j];
	}
	PtrL->Data[i-1] = X;
	PtrL->Last ++; //Last仍指向最后元素 
} 

//删除（删除表的第i(1<=i<=n+1)个位置上的元素）
void Delete(List PtrL, int i)
{
	int j;
	if ( i<1 || i>PtrL->Last+1 )
	{
		printf("位置不合法");
		return;
	}
	for ( j=i; j<=PtrL->Last; j++ )
	{
		PtrL->Data[j-1] = PtrL->Data[j];
	}
	PtrL->Last --;
	return;
}
