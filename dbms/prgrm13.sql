declare
	str varchar(30):='&string';
	len int:=length(str);
	rev varchar(30);
begin
	for i in reverse 1..len
	loop
		rev:=rev||substr(str,i,1);
	end loop;
	dbms_output.put_line('Reversed String = '||rev);
end;
/


