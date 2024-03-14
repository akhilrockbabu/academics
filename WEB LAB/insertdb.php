<?php
   $con=new mysqli("localhost","root","","personal");
if($con->connect_error)
{
	die(" connection failed".$con->connect_error);
	}
	
	if(isset($_POST['insert']))
	{
	$name=$_POST['name'];
	$age=$_POST['age'];
	$adress=$_POST['adress'];
	$email=$_POST['email'];
	$qualification=$_POST['qualification'];
	$pan_no=$_POST['pan_no'];
	
	$ins="insert into student(name,age,adress,email,qualification,pan_no)VALUES('$name','$age','$adress','$email','$qualification','$pan_no')";
	
	if($con->query($ins)===TRUE))
	echo "value inserted successfully";
	
else

	echo "insertion failed".$con->connect_error;

}

$con->close();
?>
