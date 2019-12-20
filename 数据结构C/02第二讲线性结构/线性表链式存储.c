typedef struct LNode_ {
	ElementType Data;
	int Next; 
} LNode�� *List;

List PtrL;

//���
int Length(List PtrL)
{
	List p = PtrL; //pָ���ĵ�һ�����
	int i = 0;
	while ( p )
	{
		p = p->Next;
		i ++;
	} 
	return i; //��ǰpָ����ǵ�i����� 
} 

//����Ų���
List FindKth(List PtrL, int K)
{
	List p = PtrL; 
	int i = 1;
	while ( p && i < K)
	{
		p = p->Next;
		i ++;
	} 
	if ( !p )
	{
		printf("���ڱ���");
		return;
	}
	else
	{
		return p;
	}
} 

//��ֵ����
int Find(List PtrL, ElementType X)
{
	List p = PtrL;
	int i = 1;
	while ( p && p->Data != X )
	{
		p = p->Next;
		i ++;
	}
	if ( !p )
	{
		printf("���ڱ���");
		return;
	}
	else
	{
		return i;
	}
} 

//���루��i-1(1<=i<=n+1)���������һ��ֵΪX���½�㣩
List Insert(List PtrL, ElementType X, int i) 
{
	List p, s;
	p = FindKth(PtrL, i-1);
	if ( i == 1)
	{
		s = (List)malloc(sizeof(LNode));
		s->Data = X;
		s->Next = PtrL;
		return s;
	}
	if ( !p )
	{
		printf("����i����");
		return;
	}
	else 
	{
		s = (List)malloc(sizeof(LNode));
		s->Data = X;
		s->Next = p->Next;
		p->Next = s;
		return PtrL;
	}
} 

//ɾ����ɾ����ĵ�i(1<=i<=n+1)������Ԫ�أ�
List Delete(List PtrL, int i)
{
	List p, s;
	for ( s=NULL,p=PtrL; p; s=p,p=p->Next )
	{
		if ( p == FindKth(PtrL, i) )
		{
			if ( s )
			{
				s->Next = p->Next;
			}
			else
			{
				Ptrl = p->Next;
			}
			free(p);
			break;
		}
	}
	printf("���ڱ���");
	return PtrL;
}
