#define REVERSESTRING2
#include<iostream>
#include<conio.h>
#include<String.h>

using namespace std;

string reversestring(string str)
{
char *charstr=(char*)str.c_str();
cout<<charstr<<endl;
int length=str.length();
cout<<length<<endl;
int i,j;
if(length==0)
{
cout<<"wrong input"<<endl;
return "NULL";
}
char temp;
for(i=0,j=length-1;i<length,j>0;++i,j--)
{
temp= charstr[i];
charstr[i]=charstr[j];
charstr[j]=temp;
}
string s=charstr;
return s;
}

#ifndef TEST_REVERSESTRING2
void main()
{
string oldstr="abcde";
string newstr=reversestring(oldstr);
cout<<"New string:"<<newstr.c_str()<<endl;
}
#endif

