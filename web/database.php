<?php

$con=new mysqli("localhost","root","");

if($con->connect_error)
	die("connection failed".$con->connect_error);
else
	echo "connection successfull";

$db="CREATE DATABASE personal";

if($con->query($db)==TRUE)
	echo "personal database created successfully";
else
	echo "database failed";
	
$con->close();
	
?>
