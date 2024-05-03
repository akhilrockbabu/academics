#include<stdio.h>
#include<stdlib.h>
int s[10],visited[10],i,j,n,adj[20][20],v,top=0,item,f,k;
void push(int v);
int pop();
void push(int v)
{
	top++;
	s[top]=v;
}
int pop()
{
	v=s[top];
	top--;
	return v;
}
int main()
{
	printf("enter the number of vertices\n");
	scanf("%d",&n);
	for(i=1;i<=n;++i)
	{
		visited[i]=0;
	}
	printf("enter the adjacency matrix:\n");
	for(i=1;i<=n;++i)
	{
		for(j=1;j<=n;++j)
		{
			printf("adj[%d][%d]:",i,j);
			scanf("%d",&adj[i][j]);
			printf("\n");
		}
	}
	printf("The Spanning tree edges are\n");
	push(1);
	i=1;
	while(top!=0 && i<n)
	{
	    item=s[top];
	    visited[item]=1;
	    for(j=1;j<=n;++j)
	    {
	        if(adj[item][j]==1 && visited[j]==0)
	        {
	            printf("%d->%d\n",item,j);
	            push(j);
	            f=1;
	            break;
	        }
	    }
	    if(f==0)
	        k=pop();
	    else
	        i++;
	}
	return 0;
}

/*enter the number of vertices
5
enter the adjacency matrix:
adj[1][1]:0
adj[1][2]:1
adj[1][3]:1
adj[1][4]:0
adj[1][5]:0
adj[2][1]:1
adj[2][2]:0
adj[2][3]:0
adj[2][4]:1
adj[2][5]:1
adj[3][1]:1
adj[3][2]:0
adj[3][3]:0
adj[3][4]:1
adj[3][5]:0
adj[4][1]:0
adj[4][2]:1
adj[4][3]:1
adj[4][4]:0
adj[4][5]:0
adj[5][1]:0
adj[5][2]:1
adj[5][3]:0
adj[5][4]:0
adj[5][5]:0
Spanning tree edges are:
edge(1,2)
edge(1,3)
edge(3,4)
edge(2,5)
*/
			
	
