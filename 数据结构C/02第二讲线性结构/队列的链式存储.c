typedef struct QNode_ {
	ElementType Data;
	struct QNode_  *Next; 	
} QNode, *Queue; 

typedef struct QueueNode_ { //�����нṹ 
	QNode *rear; //ָ���β���
	QNode *front;//ָ���ͷ��� 
} QueueNode;

Queue PtrQ;

//����ͷ������ʽ������Ӳ���
void Add(Queue PtrQ, ElementType item)
{
	struct Node *TmpCell, *FrontCell;
	FrontCell = (Queue)malloc(sizeof(QNode));
	FrontCell->Data = item;
	TmpCell = PtrQ->front;
	FrontCell->Next = TmpCell->Next;
	PtrQ->front = FrontCell;
}

//����ͷ������ʽ���г��Ӳ���
ElementType Delete(Queue PtrQ)
{
	struct Node *FrontCell;
	ElementType FrontItem;
	if ( PtrQ->front == NULL )
	{
		printf("���п�");
		return ERROR; 
	}
	FrontCell = PtrQ->front;
	if ( PtrQ->front == PtrQ->rear )
	{	//��ֻ��һ��Ԫ��,ɾ���������Ϊ�� 
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
