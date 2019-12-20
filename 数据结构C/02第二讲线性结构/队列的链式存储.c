typedef struct QNode_ {
	ElementType Data;
	struct QNode_  *Next; 	
} QNode, *Queue; 

typedef struct QueueNode_ { //链队列结构 
	QNode *rear; //指向队尾结点
	QNode *front;//指向队头结点 
} QueueNode;

Queue PtrQ;

//不带头结点的链式队列入队操作
void Add(Queue PtrQ, ElementType item)
{
	struct Node *TmpCell, *FrontCell;
	FrontCell = (Queue)malloc(sizeof(QNode));
	FrontCell->Data = item;
	TmpCell = PtrQ->front;
	FrontCell->Next = TmpCell->Next;
	PtrQ->front = FrontCell;
}

//不带头结点的链式队列出队操作
ElementType Delete(Queue PtrQ)
{
	struct Node *FrontCell;
	ElementType FrontItem;
	if ( PtrQ->front == NULL )
	{
		printf("队列空");
		return ERROR; 
	}
	FrontCell = PtrQ->front;
	if ( PtrQ->front == PtrQ->rear )
	{	//若只有一个元素,删除后队列置为空 
		PtrQ->front = PtrQ->rear == NULL;
	}
	else
	{
		PtrQ->front = FrontCell->Next;
	}
	FrontItem = FrontCell->Data;
	free(FrontCell);
	return FrontItem;
} 
