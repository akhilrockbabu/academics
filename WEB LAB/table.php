<?php

$con=new mysqli("localhost","root","","personal");
if($con->connect_error)
{
	die(" connection failed".$con->connect_error);
	}

	
$tb="CREATE TABLE student(id INT(2) PRIMARY KEY,name VARCHAR(30),age INT(3),adress VARCHAR(30),email VARCHAR(30),qualification VARCHAR(30),pan_no INT(20))";


if($con->query($tb)==TRUE)
	echo "Student created successfully";
else
	echo "table creation failed".$con->connect_error;
$con->close();
?>
