typedef struct LNode_ {
	ElementType Element[MAXSIZE];
	int Length;
} LNode, *List;;

List Tbl;

int SequentialSearch(List Tbl, ElementType K);
{
	int i;
	Tbl->Element[0] = K; //建立哨兵
	for (i=Tbl->Length; Tbl->Element[i]!=K; i--);
	return i; //查找成功返回所在单元下标；不成功返回0 
}


