typedef struct LNode_ {
	ElementType Element[MAXSIZE];
	int Length;
} LNode, *List;;

List Tbl;

int SequentialSearch(List Tbl, ElementType K);
{
	int i;
	Tbl->Element[0] = K; //�����ڱ�
	for (i=Tbl->Length; Tbl->Element[i]!=K; i--);
	return i; //���ҳɹ��������ڵ�Ԫ�±ꣻ���ɹ�����0 
}


