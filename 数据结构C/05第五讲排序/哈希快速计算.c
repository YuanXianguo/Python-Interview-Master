Index Hash(const char *Key, int TableSize)
{
	unsigned int h = 0; //ɢ�к���ֵ����ʼ��Ϊ0
	while ( *Key != '\0' )
	{
		h = (h << 5) + *Key++;
	} 
	return h % TableSize;
} 

struct HashTbl{
	int TableSize;
	List TheLists;
} *H;


