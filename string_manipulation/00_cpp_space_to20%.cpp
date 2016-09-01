"""
Carrercup book
"""
#define SPACETOSOMECHAR
#include<iostream>
#include<conio.h>
#include<string.h>

using namespace std;

string insertvalue(string str,int length)
{
char *p=(char*)str.c_str();
char *q=new char('\0');
static int j=0;
for(int i=0;i<length;i++)
{
if(p[i]==' ')
{
q[j]='2';
q[j+1]='0';
q[j+2]='%';
j+=2;
}
else
{
q[j]=p[i];
}
j++;
}
q[j]='\0';
string temp=q;
return q;
}

#ifndef TEST_SPACETOSOMECHAR
void main()
{
string val="hi how ";
int length=7;
string g;
g=insertvalue(val,length);
cout<<g.c_str()<<endl;
}
#endif

