typedef struct GNode_ {
	int Nv; //顶点数
	int Ne; //边数
	WeightType G[MaxVertexNum][MaxVertexNum];
	DataType Data[MaxVertexNum]; //存顶点的数据 
} GNode, *MGraph;

MGraph Graph; //以邻接矩阵存储的图类型

//MGraph初始化 
typedef int Vertex; //用顶点下标表示顶点，为整型 
MGraph CreateGraph(int VertexNum)
{
	Vertex V, W;
	MGraph Graph;
	Graph = (MGraph)malloc(sizeof(GNode));
	Graph->Nv = VertexNum;
	Graph->Ne = 0;
	for (V=0; V<Graph->Nv; V++)
		for (W=0; W<Graph->Nv; W++)
			Graph->G[V][W] = 0; //或INFINITY
	return Graph; 
}

//向MGraph中插入边
typedef struct ENode_ {
	Vertex V1, V2; //有向边<v1,v2>
	WeightType Weight;//权重 
} ENode, *Edge; 

void InsertEdge(MGraph Graph, Edge E)
{	//插入边<v1,v2> 
	Graph->G[E->V1][E->V2] = E->Weight;
	//若是无向图，还要插入边<v2,v1>
	Graph->G[E->V2][E->V1] = E->Weight; 
}

//完整地建立一个MGraph
MGraph BuildGraph()
{
	MGraph Graph;
	Edge E;
	Vertex V;
	int Nv, i;
	scanf("%d", &Nv);
	Graph = CreateGraph(Nv);
	scanf("%d", &(Graph->Ne));
	if (Graph->Ne != 0)
	{
		E = (Edge)malloc(sizeof(ENode));
		for (i=0; i<Graph->Ne; i++)
		{
			scanf("%d %d %d", &E->V1, &E->V2, &E->Weight);
			InsertEdge(Graph, E);
		}
	}
	//如果顶点有数据额话，读入数据
	for (V=0; V<Graph->Nv; V++)
	{
		scanf("%c", &(Graph->Data[V]));
	} 
	return Grpah; 
} 
