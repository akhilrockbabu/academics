set serveroutput on

create or replace function findmax(x in number,y in number)
return number is
z number;
begin
if x>y
then
z:=x;
else
z:=y;
end if;
return z;
end findmax;
/

declare
a number:=&number1;
b number:=&number2;
c number;
begin
c:=findmax(a,b);
dbms_output.put_line('Max Number('||a||','||b||') is : '||c);
end;
/
