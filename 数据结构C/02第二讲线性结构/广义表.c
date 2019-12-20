typedef struct GNode_ {
	int Tag; //标志域：0表示结点是单元素，1表示结点是广义表 
	union { //子表指针域Sublist与单元素Data复用，即共用存储空间 
		ElementType Data;
		GList SubList;
	} URegion;
	GList Next; //指向后继结点 
} GNode, *GList;



