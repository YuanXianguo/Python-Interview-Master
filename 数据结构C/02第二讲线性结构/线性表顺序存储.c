typedef struct LNode_ {
	ElementType Data[MAXSIZE];
	int Last; 
} LNode�� *List;

LNode L; 
List PtrL;

�����±�Ϊi��Ԫ�أ�L.Data[i]��PtrL->Data[i];
���Ա�ĳ��ȣ�L.Last+1��PtrL->Last+1;

//��ʼ���������յ�˳��� 
List MakeEmpty()
{
	List PtrL;
	PtrL = (List)malloc(sizeof(LNode));
	PtrL->Last = -1;
	return PtrL;
}

//����
int Find(List PtrL, ElementType X)
{
	int i = 0;
	while ( i <= PtrL->Last && PtrL->Data[i] != X )
	{
		i ++;
	}
	if ( i > PtrL ) 	
	{
		printf("���ڱ���");
		return;
	}
	else
	{
		return i;
	}
} 

//���루��i(1<=i<=n+1)��λ���ϲ���һ��ֵΪX����Ԫ�أ�
void Insert(List PtrL, ElementType X, int i) 
{
	int j;
	if ( PtrL->Last == MAXSIZE-1 )
	{
		printf("����")��
		return; 
	} 
	if ( i<1 || i>PtrL->Last+1 )
	{
		printf("λ�ò��Ϸ�");
		return;
	}
	for ( j=PtrL->Last; j>=i-1; j-- )
	{
		PtrL->Data[j+1] = PtrL->Data[j];
	}
	PtrL->Data[i-1] = X;
	PtrL->Last ++; //Last��ָ�����Ԫ�� 
} 

//ɾ����ɾ����ĵ�i(1<=i<=n+1)��λ���ϵ�Ԫ�أ�
void Delete(List PtrL, int i)
{
	int j;
	if ( i<1 || i>PtrL->Last+1 )
	{
		printf("λ�ò��Ϸ�");
		return;
	}
	for ( j=i; j<=PtrL->Last; j++ )
	{
		PtrL->Data[j-1] = PtrL->Data[j];
	}
	PtrL->Last --;
	return;
}
