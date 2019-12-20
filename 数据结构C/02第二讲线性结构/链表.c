typedef struct PolyNode_ {
	int coef;
	int expon;
	struct PolyNode_ *link;
} PolyNode, *Polynomial;

Polynomial P1, P2;


