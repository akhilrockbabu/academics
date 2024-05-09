set serveroutput on
create or replace trigger display_salary_changes 
before delete or insert or update on customers 
for each row 
          when (new.id > 0) 
declare 
   sal_diff number; 
begin 
   sal_diff := :new.salary  - :old.salary; 
   dbms_output.put_line('old salary: ' || :old.salary); 
   dbms_output.put_line('new salary: ' || :new.salary); 
   dbms_output.put_line('salary difference: ' || sal_diff); 
end; 
/ 
