#define MaxSize <储存数据元素的最大个数>
typedef struct SNode_ {
	ElementType Data[MaxSize];
	int Top; 
} SNode, *Stack;

Stack PtrS;

//入栈 
void Push(Stack PtrS, ElementType item)
{
	if ( PtrS->Top == MaxSize-1)
	{
		printf("堆栈满");
		return;
	}
	else
	{
		PtrS->Data[++(PtrS->Top)] = item;
		return;
	}
} 

//出栈
ElementType Pop(Stack PtrS)
{
	if ( PtrS->Top == -1 )
	{
		printf("堆栈空");
		return;
	}
	else
	{
		return (PtrS->Data[(PtrS->Top)--]);
	}
} 
 

