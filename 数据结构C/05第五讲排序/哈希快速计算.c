Index Hash(const char *Key, int TableSize)
{
	unsigned int h = 0; //散列函数值，初始化为0
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


