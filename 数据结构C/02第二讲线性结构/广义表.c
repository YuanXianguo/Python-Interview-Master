typedef struct GNode_ {
	int Tag; //��־��0��ʾ����ǵ�Ԫ�أ�1��ʾ����ǹ���� 
	union { //�ӱ�ָ����Sublist�뵥Ԫ��Data���ã������ô洢�ռ� 
		ElementType Data;
		GList SubList;
	} URegion;
	GList Next; //ָ���̽�� 
} GNode, *GList;



