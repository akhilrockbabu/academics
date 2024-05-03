set serveroutput on
declare
	area float;
	radius float:=&radius;
begin
	area:=radius*radius*3.14;
	dbms_output.put_line('Area ='||area);
end;
/
