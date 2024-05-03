<?php
$man=$_POST['man'];
$id=$_POST['id'];
$con=new mysqli("localhost","root","","MCA");
$update="update product set manufacturer='$man' where id=$id";
if($con->query($update)==TRUE)
{
	echo "sucess";
}
?>
