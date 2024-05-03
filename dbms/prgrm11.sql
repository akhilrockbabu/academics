set serveroutput on
declare
	n int:=&numbers;
	fact int:=1;
begin
	for i in 1..n
	loop
		fact:=fact*i;
	end loop;
	dbms_output.put_line('Fcatorial of '||n ||'='||fact);
end;
/
