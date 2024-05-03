/*create table square(num INT,square INT);*/

set serveroutput on
create or replace function pow(x in number)
return number is
y number;
begin
y:=power(x,2);
return y;
end pow;
/

declare
a number:=&first_number;
b number:=&second_number;
i number;
y number;
begin
for i in a..b
loop
y:=pow(i);
insert into square values(i,y);
end loop;
end;
/


