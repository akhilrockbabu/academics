<html>
<body>
<form action="" method="POST">
	<table>
		<tr>
		<td>
			ENTER THE NUMBER:
		</td>
		<td>
			<input type="text" placeholder="enter the number to find cube" name="t1">
		</td>
	</table>
	<input type="submit" value="SUBMIT" name="sub">
</form>
<?php
if(isset($_POST['sub']))
{
	$v1=$_POST['t1'];
	echo "entered value is: ",$v1,"<br>";
	echo "cube is: ",cube($v1);
	inc($v1);
	echo "<br>";
	echo "incremented value is: ",$v1;
	square($v1);
}
function cube($a)
{
	return $a*$a*$a;
}
function square($b)
{
	echo "<br> Now square is: ",$b*$b;
}
function inc(&$c)
{
	return $c++;
}
?>
</body>
</html>
