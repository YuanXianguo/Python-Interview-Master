#define MaxSize <��������Ԫ�ص�������>
typedef struct SNode_ {
	ElementType Data[MaxSize];
	int Top; 
} SNode, *Stack;

Stack PtrS;

//��ջ 
void Push(Stack PtrS, ElementType item)
{
	if ( PtrS->Top == MaxSize-1)
	{
		printf("��ջ��");
		return;
	}
	else
	{
		PtrS->Data[++(PtrS->Top)] = item;
		return;
	}
} 

//��ջ
ElementType Pop(Stack PtrS)
{
	if ( PtrS->Top == -1 )
	{
		printf("��ջ��");
		return;
	}
	else
	{
		return (PtrS->Data[(PtrS->Top)--]);
	}
} 
 

