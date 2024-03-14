<html>
<head>
<style>

table{
border:1px solid black;
width:500px;
}
tr:nth-child(even){
background-color:lightblue;
}
th,td{
padding:10px;
border:1px solid black;
text-align:center;
}
body{
font-family:sans-serif;
}
a{
color:hotpink;
/* padding:10px;
display:inline-block;*/
}
a:hover {
color:green;
}
</style>
<title>BILL</title>
<body align="center">
	<h1 align="center">Rockiey's Supermart</h1>
	<form action="" method="POST">
		<table border="3" align="center" style="color:black" bordercolor="redorange" width="20%" height="20%">
		<tr>
		<th colspan="3">BILL DETAILS</th>
		</tr>
		<tr>
		<td align="center">ITEM</td>
		<td align="center">QUANTITY</td>
		<td align="center">UNIT PRICE</td>
		</tr>
		<tr>
		<td align="center"><input type="text" name="i1"></td>
		<td align="center"><input type="text" name="q1"></td>
		<td align="center"><input type="text" name="u1"></td>
		</tr>
		<tr>
		<td align="center"><input type="text" name="i2"></td>
		<td align="center"><input type="text" name="q2"></td>
		<td align="center"><input type="text" name="u2"></td>
		</tr>
		<tr>
		<td align="center"><input type="text" name="i3"></td>
		<td align="center"><input type="text" name="q3"></td>
		<td align="center"><input type="text" name="u3"></td>
		</tr>
		</table><br><br>
		<input type="submit" name="next" value="SUBMIT">
		<input type="reset" name="s1" value="CLEAR">
	</form>
</body>
</head>
</html>
<?php
if(isset($_POST['next']))
{
	$i1=$_POST["i1"];
	$i2=$_POST["i2"];
	$i3=$_POST["i3"];
	$q1=$_POST["q1"];
	$q2=$_POST["q2"];
	$q3=$_POST["q3"];
	$u1=$_POST["u1"];
	$u2=$_POST["u2"];
	$u3=$_POST["u3"];
	$t1=$q1*$u1;
	$t2=$q2*$u2;
	$t3=$q3*$u3;
	$t=$t1+$t2+$t3;
?>
<html>
	<h1 align="center">PAYMENT SLIP</h1>
	<form>
		<table border="3" align="center" style="color:black" bordercolor="redorange" width="20%" height="20%">
		<tr>
		<th colspan="5">BILL DETAILS</th>
		</tr>
		<tr>
		<td align="center">S.NO</td>
		<td align="center">ITEM</td>
		<td align="center">QUANTITY</td>
		<td align="center">UNIT PRICE</td>
		<td align="center">TOTAL PRICE</td>
		</tr>
		<tr>
		<td align="center">1</td>
		<td align="center"><?php echo $i1;?></td>
		<td align="center"><?php echo $q1;?></td>
		<td align="center"><?php echo $u1;?></td>
		<td align="center"><?php echo $t1;?></td>
		</tr>
		<tr>
		<td align="center">2</td>
		<td align="center"><?php echo $i2;?></td>
		<td align="center"><?php echo $q2;?></td>
		<td align="center"><?php echo $u2;?></td>
		<td align="center"><?php echo $t2;?></td>
		</tr>
		<tr>
		<td align="center">3</td>
		<td align="center"><?php echo $i3;?></td>
		<td align="center"><?php echo $q3;?></td>
		<td align="center"><?php echo $u3;?></td>
		<td align="center"><?php echo $t3;?></td>
		</tr>
		<tr>
		<td align="center" colspan="4">GRAND TOTAL</td>
		<td align="center"><?php echo $t;?></td>
		</table><br><br>
		<input type="submit" name="clear" value="CLEAR">
	</form>
</body>
</head>
</html>
<?php
}
if(isset($_POST["clear"]))
{
	header(Refresh);
}
?>
	
