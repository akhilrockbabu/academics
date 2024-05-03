set serveroutput on
create or replace function addnum(x in number,y in number)
return number is
z number;
begin
z:=x+y;
return(z);
end addnum;
/
select addnum(6,4) from dual;

/*
declare
a number:=&first_number;
b number:=&second_number;
c number;
begin
c:=a+b;
dbms_output.put_line('Sum = '||c);
end;
/
*/
