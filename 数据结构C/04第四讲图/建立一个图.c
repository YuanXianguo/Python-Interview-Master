typedef struct GNode_ {
	int Nv; //������
	int Ne; //����
	WeightType G[MaxVertexNum][MaxVertexNum];
	DataType Data[MaxVertexNum]; //�涥������� 
} GNode, *MGraph;

MGraph Graph; //���ڽӾ���洢��ͼ����

//MGraph��ʼ�� 
typedef int Vertex; //�ö����±��ʾ���㣬Ϊ���� 
MGraph CreateGraph(int VertexNum)
{
	Vertex V, W;
	MGraph Graph;
	Graph = (MGraph)malloc(sizeof(GNode));
	Graph->Nv = VertexNum;
	Graph->Ne = 0;
	for (V=0; V<Graph->Nv; V++)
		for (W=0; W<Graph->Nv; W++)
			Graph->G[V][W] = 0; //��INFINITY
	return Graph; 
}

//��MGraph�в����
typedef struct ENode_ {
	Vertex V1, V2; //�����<v1,v2>
	WeightType Weight;//Ȩ�� 
} ENode, *Edge; 

void InsertEdge(MGraph Graph, Edge E)
{	//�����<v1,v2> 
	Graph->G[E->V1][E->V2] = E->Weight;
	//��������ͼ����Ҫ�����<v2,v1>
	Graph->G[E->V2][E->V1] = E->Weight; 
}

//�����ؽ���һ��MGraph
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
	//������������ݶ����������
	for (V=0; V<Graph->Nv; V++)
	{
		scanf("%c", &(Graph->Data[V]));
	} 
	return Grpah; 
} 
