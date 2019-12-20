#define MaxSize <´¢´æÊý¾ÝÔªËØµÄ×î´ó¸öÊý>
typedef struct DNode_ {
	ElementType Data[MaxSize];
	int Top1; 
	int Top2;
} DNode, *DStack;

DNode S;
S.Top1 = -1;      //¶ÑÕ»1¿Õ 
S.Top2 = MaxSize; //¶ÑÕ»2¿Õ 

DStack PtrS;

void Push(DStack PtrS, ElementType item, int Tag)
{
	if ( PtrS->Top2 - PtrS->Top1 == 1 )
	{
		printf("¶ÑÕ»Âú");
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
			printf("¶ÑÕ»1¿Õ");
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
			printf("¶ÑÕ»2¿Õ");
			return; 
		}
		else
		{
			return (PtrS->Data[(PtrS->Top2)--]);
		}
	}
}
