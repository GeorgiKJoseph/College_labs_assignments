//Georgi K Joseph
//S3-D
//21

//source code...
#include<stdio.h>

void main()
{
    int arr[20],f,l,mid,i,size,ele,j,count=0;
    printf("enter the size of array: ");
    scanf("%d",&size);
    printf("Enter elements: ");
    for(i=0;i<size;i++)
    {
        scanf("%d",&arr[i]);
    }
    printf("enter element to be searched: ");
    scanf("%d",&ele);
    f=0;
    l=size-1;
    for(i=0;i<size;i++)
    {
        for(j=i;j<size;j++)
        {
            if(arr[i]>arr[j])
            {
                arr[i]=arr[i]+arr[j];
                arr[j]=arr[i]-arr[j];
                arr[i]=arr[i]-arr[j];
            }
        }
    }
    for(i=0;i<size;i++)
    {
        printf("%d ",arr[i]);
    }

    while(l>=f)
    {
        mid=(int)((f+l)/2);
        //printf("%d",mid);
        if(arr[mid]==ele)
        {
            printf("\nelement found\n");
            count+=1;
            break;
        }
        else if(arr[mid]>ele)
        {
            l=mid-1;
        }
        else if(arr[mid]<ele)
        {
            f=mid+1;
        }
    }
    if(count==0)
    {
        printf("\nelement not found\n");
    }

}
