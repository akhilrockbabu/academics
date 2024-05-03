set serveroutput on

create or replace procedure squarenum(x in out number)is
begin
x:=x*x;
end;
/

declare
a number:=&a;
begin
squarenum(a);
dbms_output.put_line('Square of Number is '||a);
end;
/
