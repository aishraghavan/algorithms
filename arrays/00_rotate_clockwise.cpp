//key idea
//i,j
//col,i
//row,col
//j,row

#define ROTATION
#include<iostream>
#include<conio.h>

using namespace std;

#ifndef TEST_ROTATION
void main()
{
int a[4][4]={{1,2,3,4},
	{5,6,7,8},
	{9,10,11,12},
	{13,14,15,16}};
int n=4;
for(int i=0;i<n/2;++i)
{
for(int j=i;j<n-1-i;++j)
{
int row=n-1-i;
int col=n-1-j;
int temp=a[i][j];
a[i][j]=a[col][i];
a[col][i]=a[row][col];
a[row][col]=a[j][row];
a[j][row]=temp;
}
}
for(int ii=0;ii<4;ii++)
{
for(int jj=0;jj<4;jj++)
{
cout<<a[ii][jj]<<"\t";
}
cout<<endl;
}
}
#endif

