#define MaxSize <��������Ԫ�ص�������>
typedef struct DNode_ {
	ElementType Data[MaxSize];
	int Top1; 
	int Top2;
} DNode, *DStack;

DNode S;
S.Top1 = -1;      //��ջ1�� 
S.Top2 = MaxSize; //��ջ2�� 

DStack PtrS;

void Push(DStack PtrS, ElementType item, int Tag)
{
	if ( PtrS->Top2 - PtrS->Top1 == 1 )
	{
		printf("��ջ��");
		return;
	}
	if ( Tag == 1 )
	{
		PtrS->Data[++(PtrS->Top1)] == item;
	}
	else
	{
		PtrS->Data[--(PtrS->Top2)] == item;
	}
}

ElementType Pop(DStack PtrS, int Tag)
{
	if ( Tag == 1 )
	{
		if ( PtrS->Top1 == -1 )
		{
			printf("��ջ1��");
			return; 
		}
		else
		{
			return (PtrS->Data[(PtrS->Top1)--]);
		}
	}
	else
	{
		if ( PtrS->Top2 == MaxSize )
		{
			printf("��ջ2��");
			return; 
		}
		else
		{
			return (PtrS->Data[(PtrS->Top2)--]);
		}
	}
}
