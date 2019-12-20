typedef struct LNode_ {
	ElementType Element[MAXSIZE];
	int Length;
} LNode, *List;;

List Tbl;

int BinarySearch(List Tbl, ElementType K)
{
	int left, right, mid;
	
	left = 1;
	right = Tbl->Length;
	while ( left <= right )
	{
		mid = (left+righr) / 2;
		if ( K < Tbl->Element[mid] )
		{
			right = mid - 1;
		}
		else if ( K > Tbl->Element[mid] )
		{
			left = mid + 1;
		}
		else 
		{
			return mid;
		}
	 } 
	 return -1;
} 
