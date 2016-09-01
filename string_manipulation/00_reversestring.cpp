#define REVERSESTRING
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
int ilimit,jlimit;

int mid,i,j;
if(length==0)
{
cout<<"wrong input"<<endl;
return "NULL";
}
//even
else if(length%2==0)
{
mid=length/2;
}
//odd
else
{
mid=(length/2)+1;
}
ilimit=mid-1;
jlimit=mid;
cout<<ilimit<<jlimit<<endl;
char temp;
for(i=0,j=length-1;i<=ilimit,j>=jlimit;++i,j--)
{
temp= charstr[i];
charstr[i]=charstr[j];
charstr[j]=temp;
cout<<charstr[i]<<endl;
cout<<charstr[j]<<endl;
//cout<<charstr<<endl;
}
string s=charstr;
return s;
}

#ifndef TEST_REVERSESTRING
void main()
{
string oldstr="abcde";
string newstr=reversestring(oldstr);
cout<<"New string:"<<newstr.c_str()<<endl;
}
#endif
