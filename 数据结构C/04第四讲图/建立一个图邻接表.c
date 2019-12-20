typedef struct AdjVNode_ {
	Vertex AdjV; //�ڽӵ��±�
	WeightType Weight; //��Ȩ��
	struct AdjVNode_ *Next;  
} AdjVNode, *PtrToAdjVNode;

typedef struct Vnode_ {
	PtrToAdjVNode FirstEdge;
	DataType Data[MaxVertexNum]; //�涥������� 
} AdjList[MaxVertexNum]; //�ڽӱ����� 

typedef struct GNode_ {
	int Nv; //������
	int Ne; //����
	AdjList G; //�ڽӱ� 
} GNode, *LGraph;

LGraph Graph; //���ڽӱ�洢��ͼ����

//LGraph��ʼ�� 
typedef int Vertex; //�ö����±��ʾ���㣬Ϊ���� 
LGraph CreateGraph(int VertexNum)
{
	Vertex V, W;
	LGraph Graph;
	Graph = (MGraph)malloc(sizeof(GNode));
	Graph->Nv = VertexNum;
	Graph->Ne = 0;
	for (V=0; V<Graph->Nv; V++)
		Graph->G[V].FirstEdge = NULL;
	return Graph; 
}

//�����
void InsertEdge(LGraph Graph, Edge E)
{
	PtrToAdjVNode NewNode;
	//�����<v1,v2>
	//Ϊv2�����µ��ڽӵ� 
	NewNode = (PtrToAdjVNode)malloc(sizeof(AdjVNode));
	NewNode->AdjV = E->V2;
	NewNode->Weight = E->Weight;
	//��v2����v1�ı�ͷ
	NewNode->Next = Graph->G[E->V1].FirstEdge;
	Graph->G[E->V1].FirstEdge = NewNode;
	
	//��������ͼ����Ҫ�����<v2,v1> 
	//Ϊv1�����µ��ڽӵ� 
	NewNode = (PtrToAdjVNode)malloc(sizeof(AdjVNode));
	NewNode->AdjV = E->V1;
	NewNode->Weight = E->Weight;
	//��v1����v2�ı�ͷ
	NewNode->Next = Graph->G[E->V2].FirstEdge;
	Graph->G[E->V2].FirstEdge = NewNode;
} 

//�����ؽ���һ��LGraph 
