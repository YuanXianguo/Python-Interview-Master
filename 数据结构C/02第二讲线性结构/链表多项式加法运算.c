typedef struct PolyNode_ {
	int coef;
	int expon;
	struct PolyNode_ *link;
} PolyNode, *Polynomial;

Polynomial P1, P2;

void Attach(int coef_, int expon_, Polynomial *pRear)
{
	Polynomial P;
	P = (Polynomial)malloc(sizeof(PolyNode));
	P->coef = coef_;
	P->expon = expon_;
	P->link = NULL;
	(*pRear)->link = P;
	*pRear = P;
}

Polynomial PolyAdd(Polynomial P1, Polynomial P2)
{
	Polynomial front, rear, temp;
	int sum;
	rear = (Polynomial)malloc(sizeof(PolyNode));
	front = rear; //��¼�������ʽ����ͷ��� 
	while ( P1 && P2 )
	{
		switch ( Compare(P1->expon, P2->expon) )
		{	//P1�󷵻�1��P2�󷵻�-1����ȷ���0 
			case 1:
				Attach(P1->coef, P2->expon, &rear);
				P1 = P1->link;
				break;
			case -1:
				Attach(P2->coef, P2->expon, &rear);
				P2 = P2->link;
				break;
			case 0:
				sum = P1->coef + P2->coef;
				if ( sum )
				{
					Attach(sum, P1->expon, &rear);
					P1 = P1->link;
					P2 = P2->link;
					break;
				} 
		}
	}
	//��δ���������һ������ʽ�����н�㸴�Ƶ��������ʽ��ȥ
	for ( ; P1; P1 = P1->link )
	{
		Attach(P1->coef, P1->expon, &rear);
	} 
	for ( ; P2; P2 = P2->link )
	{
		Attach(P2->coef, P2->expon, &rear);
	} 
	rear->link = NULL;
	temp = front;
	front = front->link; //��frontָ��������ʽ��һ�������� 
	free(temp);
	return front;
}
