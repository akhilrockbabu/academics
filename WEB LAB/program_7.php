<?php

$con=new mysqli("localhost","root","","MCA");

if($con->connect_error)
	echo "connection failed";
else
	echo "successfull";
	
$product="CREATE TABLE product(id INT(2) PRIMARY KEY AUTO_INCREMENT,name varchar(30) NOT NULL,qty INT(2) NOT NULL,unitp INT(2) NOT NULL,manu date NOT NULL,exp date NOT NULL)";

if($con->query($product)==TRUE)
	echo "product created successfully";
else
	echo "table creation failed";
$con->close();
?>
