//Georgi K Joseph
//S3-D
// 21

//source code...
#include<stdio.h>
#include<stdlib.h>

int btree[100];
const int size=100;

void setminus()
{
    int i;
    for(i=0;i<100;i++)
        btree[i]=-1;
}

int search(int data)
{
    int i;
    for(i=0;i<size;i++)
        if(btree[i]==data)
            return i;
    return -1;
}

void insertion()
{
    int data,position,cho;
    if(btree[0]==-1)
    {
        printf("Enter data: ");
        scanf("%d",&btree[0]);
    }
    else
    {
        printf("Select parent node(by data): ");
        scanf("%d",&data);
        position=search(data);
        if(position!=-1)
        {
            if(btree[(2*position)+1]!=-1 && btree[(2*position)+2]!=-1)
            {
                printf("\nBoth child nodes are occupied\n");
            }
            else
            {
                printf("\nSelect child node\n1.Left\n2.Right\nEnter Choice: ");
                scanf("%d",&cho);
                if(cho==1)
                {
                    if(btree[(2*position)+1]!=-1)
                    {
                        printf("\nNode already occupied\n");
                    }
                    else
                    {
                        printf("Enter data: ");
                        scanf("%d",&btree[(2*position)+1]);
                    }
                }
                else
                {
                    if(btree[(2*position)+2]!=-1)
                    {
                        printf("\nNode already occupied\n");
                    }
                    else
                    {
                        printf("Enter data: ");
                        scanf("%d",&btree[(2*position)+2]);
                    }
                }
            }
        }
        else
        {
            printf("\nNode not Found\n");
        }
    }
    
}
void printnode(int index)
{
    if(btree[(2*index)+1]!=-1)
    {
        printnode((2*index)+1);
    }
    if(btree[(2*index)+2]!=-1)
    {
        printnode((2*index)+2);
    }
    printf("%d ",btree[index]);
}

void display()
{
    if(btree[0]==-1)
        printf("\nTree is Empty\n");
 
    else
    {
        printnode(0);
    }
}

int deepest()
{
    int i;
    for(i=99;i>=0;i--)
        if(btree[i]!=-1)
            return i;
    return -1;
}

void deletion()
{
    int data,position,d_ele;
    if(btree[0]==-1)
        printf("\nTree is Empty");
    else
    {
        printf("\nSelect node(by data): ");
        scanf("%d",&data);
        position=search(data);
        if(position==-1)
            printf("\nNode not found\n");
        else
        {
          //to find the position of data
            d_ele=deepest();                //to find the deepest element
            btree[position]=btree[d_ele];
            btree[d_ele]=-1;
        }
    }
}

void main()
{
    int cho;
    setminus();
    do
    {
        printf("\n   MENU\n1.Insertion\n2.Deletion\n3.Display\n4.Exit\nEnter Choice: ");
        scanf("%d",&cho);
        if(cho==1)
            insertion();
        else if(cho==2)
            deletion();
        else if(cho==3)
            display();
    }while(cho==1||cho==2||cho==3);
}
