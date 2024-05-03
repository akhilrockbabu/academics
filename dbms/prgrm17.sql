set serveroutput on
create or replace procedure findmin(x in number,y in number,z out number)is
begin
if x<y
then
z:=x;
else
z:=y;
end if;
end;
/

declare
a number:=&a;
b number:=&b;
c number;
begin
findmin(a,b,c);
dbms_output.put_line('Minimum = '||c);
end;
/

