 <?php
   
$con=new mysqli("localhost","root","","personal");
if($con->connect_error)
{
	die(" connection failed".$con->connect_error);
	}

$result=$con->query("SELECT * FROM student");

echo "<table style='align=center;'>";
echo "<tr><th>name</th><th>age</th><th>adress</th><th>email</th><th>qualification</th><th>pan_no</th></tr>";

while($row=$result->fetch_assoc())
{
echo "<tr>";
echo "<td>".$row['name']."</td>";
echo "<td>".$row['age']."</td>";
echo "<td>".$row['adress']."</td>";
echo "<td>".$row['email']."</td>";
echo "<td>".$row['qualification']."</td>";
echo "<td>".$row['pan_no']."</td>";
echo "</tr>";
}
echo "</table>";
$con->close();
?>


