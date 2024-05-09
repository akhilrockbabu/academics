set serveroutput on
create or replace trigger t2 after insert or update on xy
begin
if inserting
then insert into test values('inserted',CURRENT_TIMESTAMP);
else
insert into test values('updated',CURRENT_TIMESTAMP);
end if;
end;
/

