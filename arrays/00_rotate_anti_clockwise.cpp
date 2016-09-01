

#define COLTRANSFORM
#include<iostream>
#include<conio.h>

using namespace std;

#ifndef TEST_COLTRANSFORM
void main()
{
  int mat[4][4]={{1,2,3,4},
                 {5,6,7,8},
                 {9,10,11,12},
                 {13,14,15,16}};
  int n=4;
  for(int ii=0;ii<4;ii++)
  {
  for(int jj=0;jj<4;jj++)
  {  
    cout<< mat[ii][jj]<<"\t";
  }
  cout<<"\n";
  }
  cout<<endl<<endl;

  int i,j,row,col,temp;
  int N=4;
  for(i=0;i<N/2;++i)
  {
  for(j=i;j<N-1-i;++j)
  {
  row=N-1-i;
  col=N-1-j;
  temp=mat[i][j];
  mat[i][j]=mat[col][i]; //left=bottom
  mat[col][i]=mat[row][col];//bottom=right
  mat[row][col]=mat[j][row];//right=top
  mat[j][row]=temp;//top=left
  }
  }
  for(int ii=0;ii<4;ii++)
  {
  for(int jj=0;jj<4;jj++)
  {  
    cout<< mat[ii][jj]<<"\t";
  }
  cout<<"\n";
  }
  cout<<endl<<endl;

  int mat1[4][4]={{1,2,3,4},
                 {5,6,7,8},
                 {9,10,11,12},
                 {13,14,15,16}};
  for(i=0;i<N/2;++i)
  {
  for(j=i;j<N-1-i;++j)
  {
  row=N-1-i;
  col=N-1-j;

  /*
  temp=b;
  b=l;
  l=t;
  t=r;
  r=b;
  bottom-mat1[col][i];
  left-mat1[i][j];
  top-mat1[j][row];
  right-mat1[row][col];
  */
  /*temp=mat[i][j];
  mat[i][j]=mat[j][col];
  mat[j][col]=mat1[row][col];
  mat1[row][col]=mat1[col][i];
  mat1[col][i]=temp;*/

  temp=mat1[i][j];
  mat1[i][j]=mat1[j][row];
  mat1[j][row]=mat1[row][col];
  mat1[row][col]=mat1[col][i];
  mat1[col][i]=temp;
  }
  }

  for(int ii=0;ii<4;ii++)
  {
  for(int jj=0;jj<4;jj++)
  {  
    cout<< mat1[ii][jj]<<"\t";
  }
  cout<<"\n";
  }
}
#endif

