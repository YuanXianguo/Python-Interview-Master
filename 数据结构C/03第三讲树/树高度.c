int PostOrderGetHeight(BinTree BT)
{
	int HL, HR, MaxH;
	if ( BT )
	{
		HL = PostOrderGetHeight( BT->Left) ;
		HR = PostOrderGetHeight( BT->Right );
		MaxH = (HL > HR) ? HL : HR;
		return (MaxH + 1);
	}
	else 
	{
		return 0;//¿ÕÊ÷Éî¶ÈÎª0 
	}
} 


