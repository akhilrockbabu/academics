<html>
<body>
<?php
//creating connection
$con=new mysqli("localhost","root","","MCA");
$q="select * from Student";
$r=$con->query($q);
if($r->num_rows>0)
{
	?>
	<table border="1">
	<tr>
	<td colspan="2" STUDENT DETAILS></td>
	</tr>
	<tr>
	<td>ID</td>
	<td>NAME</td>
	</tr>
	<?php
	while($row=$r->fetch_assoc())
	{
		$id=$row['id'];
		$name=$row['name'];
		?>
		<tr>
		<td><?php echo $id;?></td>
		<td><?php echo $name;?></td>
		</tr>
		<?php
	}
}
else
	echo "please enter some details";
$con->close();
?>
</table>
</body>
</html>

	
	

