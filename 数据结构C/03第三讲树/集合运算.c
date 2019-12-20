������ÿ��Ԫ�ص���������Ϊ��
typedef struct {
	ElementType Data;
	int Parent;
} SetType; 

SetType S[]

int Find(SetType S[], ElementType X)
{//������S�в���ֵΪX��Ԫ���������ϣ�MaxSize��ȫ�ֱ�����Ϊ����S����󳤶�
	int i;
	for (i=0; i<MaxSize && S[i].Data!=X; i++)
	{
		if (i>=MaxSize)
		{
			return -1; //δ�ҵ� 
		}
		else
		{
			for ( ; S[i].Parent>=0; i=S[i].Parent);
		}
		return i;//�ҵ�X�������ϣ������������������S�е��±� 
	 } 	
}

//Ԫ���ٵļ��ϲ���Ԫ�ض�ļ������� 
void Union(SetType S[], ElementType X1, ElementType X2)
{
	int Root1, Root2;
	Root1 = Find(S, X1);
	Root2 = Find(S, X2);
	if (Root1 != Root2)
	{	//ParentС�ľ���ֵ��Ԫ�ض� 
		if (S[Root1].Parent < S[Root2].Parent)
		{
			S[Root2].Parent = Root1;
		}
		else
		{
			S[Root1].Parent = Root2;
		}
	}
 } 
 


