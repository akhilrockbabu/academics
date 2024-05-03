/*create table deposit(ac_no INT,balance INT);
insert into deposit values(&ac_no,&balance);*/

set serveroutput on
create or replace procedure bank_deposit(id in number,amt in number)is
begin
update deposit set balance=balance+amt where ac_no=id;
end;
/

declare
a number:=&account_number;
b number:=&amount;
begin
bank_deposit(a,b);
commit;
end;
/
