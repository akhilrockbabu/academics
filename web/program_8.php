<html>
<head>
<body>
<h2 align="center">PRODUCT DEATAILS</H2>
  <br>
  <form method="post" action="" align="center">
   <table align="center" width="25%" height="30%">
      <tr>
        <td> Product Name:</td>
        <td> <input type="text" placeholder="enterproduct name" name="n1" required></td>
      </tr>
      <tr>
        <td>Quantity:</td>
        <td><input type="number" placeholder="enter quantity" name="n2" required></td>
      </tr>
        <br><br>
      <tr>
        <td>Unit Price:</td>
        <td><input type="number" placeholder="enter unit price" name="n3" required></td>
      </tr>
 
      <tr>
        <td>Manufacturer Date:</td>
        <td><input type="date" placeholder="enter manu-date" name="n4" required></td>
      </tr>
 
      <tr>
        <td>Expired Date:</td>
        <td><input type="date" placeholder="enter exp-date" name="n5" required></td>
      </tr>
 
    </table>
    <input type="submit" value="submit" name="s">
   </form>

<?php
//creating connection
$con=new mysqli("localhost","root","","MCA");

if(isset($_POST['s']))
{
$name=$_POST['n1'];
$qty=$_POST['n2'];
$price=$_POST['n3'];
$manu=$_POST['n4'];
$exp=$_POST['n5'];

//table insertion 
$table="insert into product(name,qty,unitp,manu,exp)values('$name',$qty,$price,'$manu','$exp')";

if($con->query($table))
	echo "inserted successfully";
else
	echo "not inserted";
}
$con->close();
?>

<form action="program_9.php" method="post">
<br>
<input type="submit" value="show details">
</form>
</head>

</html> 

	
