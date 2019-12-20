#define MaxSize <储存数据元素的最大个数> 
typedef struct QNode_ {
	ElementType Data[MaxSize];
	int rear;
	int front;
} QNode, *Queue;

Queue PtrQ;

//入队列
void Add(Queue PtrQ, ElementType item)
{
	if ( (PtrQ->rear+1)%MaxSize == PtrQ->front )
	{
		printf("队列满");
		return;
	}
	PtrQ->rear = (PtrQ->rear+1) % MaxSize;
	PtrQ->Data[PtrQ->rear] = item;
} 

//出队列
ElementType Delete(Queue PtrQ)
{
	if ( PtrQ->front == PtrQ->rear )
	{
		printf("队列空");
		return ERROR;
	}
	else
	{
		PtrQ->front = (PtrQ->front+1) % MaxSize;
		return PtrQ->Data[PtrQ->front];
	}
}

 
