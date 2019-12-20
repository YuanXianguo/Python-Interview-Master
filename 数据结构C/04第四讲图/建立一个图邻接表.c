typedef struct AdjVNode_ {
	Vertex AdjV; //邻接点下标
	WeightType Weight; //边权重
	struct AdjVNode_ *Next;  
} AdjVNode, *PtrToAdjVNode;

typedef struct Vnode_ {
	PtrToAdjVNode FirstEdge;
	DataType Data[MaxVertexNum]; //存顶点的数据 
} AdjList[MaxVertexNum]; //邻接表类型 

typedef struct GNode_ {
	int Nv; //顶点数
	int Ne; //边数
	AdjList G; //邻接表 
} GNode, *LGraph;

LGraph Graph; //以邻接表存储的图类型

//LGraph初始化 
typedef int Vertex; //用顶点下标表示顶点，为整型 
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

//插入边
void InsertEdge(LGraph Graph, Edge E)
{
	PtrToAdjVNode NewNode;
	//插入边<v1,v2>
	//为v2建立新的邻接点 
	NewNode = (PtrToAdjVNode)malloc(sizeof(AdjVNode));
	NewNode->AdjV = E->V2;
	NewNode->Weight = E->Weight;
	//将v2插入v1的表头
	NewNode->Next = Graph->G[E->V1].FirstEdge;
	Graph->G[E->V1].FirstEdge = NewNode;
	
	//若是无向图，还要插入边<v2,v1> 
	//为v1建立新的邻接点 
	NewNode = (PtrToAdjVNode)malloc(sizeof(AdjVNode));
	NewNode->AdjV = E->V1;
	NewNode->Weight = E->Weight;
	//将v1插入v2的表头
	NewNode->Next = Graph->G[E->V2].FirstEdge;
	Graph->G[E->V2].FirstEdge = NewNode;
} 

//完整地建立一个LGraph 
