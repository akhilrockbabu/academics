set serveroutput on
declare
	n int:=&range;
	area float;
begin
	if(n>0)
	then
		for i in 1..n
		loop
			area:=3.14*i*i;
			dbms_output.put_line('area of circle with radius '||i||' = '||area);
		end loop;
	else
			dbms_output.put_line('enter valid range');
	end if;
end;
/
