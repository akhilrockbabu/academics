declare
	n int:=&numbers;
begin
	if(mod(n,2)=0)
	then
		dbms_output.put_line(n||' is even');
	else
		dbms_output.put_line(n||' is odd');
	end if;
end;
/
