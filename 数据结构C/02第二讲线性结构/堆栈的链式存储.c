typedef struct SNode_ {
	ElementType Data;
	struct SNode *Next; 
} SNode, *Stack;

Stack S;

//堆栈初始化
Stack CreateStack()
{	//构建一个堆栈的头结点，返回指针 
	Stack S;
	S = (Stack)malloc(sizeof(SNode));
	S->Next = NULL;
	return S; 
} 

//判断堆栈S是否为空
int IsEmpty(Stack S)
{	//若为空返回1，否则0 
	return ( S->Next == NULL );
} 

//入栈
void Push(Stack S, ElementType item)
{
	struct SNode *TmpCell;
	TmpCell = (Stack)malloc(sizeof(SNode));
	TmpCell->Data = item;
	TmpCell->Next = S->Next;
	S->Next = TmpCell;
} 

//出栈
ElementType Pop(Stack S)
{
	struct SNode *FirstCell;
	ElementType TopItem;
	if ( IsEmpty(S) )
	{
		printf("堆栈空");
		return NULL;
	}
	else
	{
		FirstCell = S->Next;
		S->Next = FirstCell->Next;
		TopItem = FirstCell->Data;
		free(FirstCell); 
		return TopItem;
	} 	
} 
