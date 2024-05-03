<?php
$list=array(array("id"=>1,"name"=>"akhil","MFC"=>49,"ASE"=>47,"DFCA"=>48,"ADS"=>49),
	array("id"=>2,"name"=>"albert","MFC"=>37,"ASE"=>27,"DFCA"=>28,"ADS"=>39),
	array("id"=>3,"name"=>"frestin","MFC"=>29,"ASE"=>17,"DFCA"=>28,"ADS"=>19));
?>
<html>
<head>
	<title>INTERNAL MARKS</title>
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
padding:10px;
display:inline-block;
}
a:hover {
color:green;
}
</style>
<body>
	<h1 align="center">MAR ATHNASIUS COLLEGE OF ENGINEERING</h1><br>
	<h1 align="center">SESSIONAL EXAM 1</h1><br>
	<form method="POST" action="" align="center">
		<table align="center" border="1">
			<tr>
				<td colspan="2">STUDENT DETAILS</td>
			</tr>
			<tr>
				<td>Name</td>
				<td><input type="text" name="n" placeholder="enter the name"></td>
			</tr>
			<tr>
				<td>ROLLNO</td>
				<td><input type="number" name="i" placeholder="enter the ID"></td>
			</tr>
		</table><br><br>
	<input type="submit" name="next" value="SUBMIT">
</form>
<?php
if(isset($_POST['next']))
{
	$total=50;
	$fail=0;
	$totalmarks=0;
	foreach($list as $l)
	{
		if($l["id"]==$_POST['i'] && $l['name']==strtolower($_POST['n']))
		{
			?>
			<h3 align="center">NAME :<?php echo strtoupper($_POST['n']);?></h3>
			<h3 align="center">ROLL NO:<?php echo $_POST['i'];?></h3>
			<table align="center" border="1">
			<tr>
			<td>SUBJECT</td>
			<td>MARKS</td>
			<td>PASS/FAIL</td>
			</tr>
			<?php
			foreach($l as $key=>$value)
			{
				if($key!="name" && $key!="id")
				{
				$totalmarks=$totalmarks+$value;
				?>
					<tr>
						<td><?php echo $key;?></td>
						<td><?php echo $value;?></td>
						<?php
						if($value>=$total*0.5)
						{
						?>
						<td>PASS</td>
						<?php
						}
						else
						{
						?>
						<td>FAIL</td>
						<?php
						$fail=1;
						}
						?>
						
					</tr>
				<?php
				}

			}?>
			<tr>
			<td>TOTAL</td>
			<td><?php echo $totalmarks;?></td>
			<?php
			if($fail==1)
			{
			?>
			<td>FAIL</td>
			<?php
			}
			else
			{
			?>
			<td>PASS</td>
			<?php
			}
			?>
			</tr>
			</table>
			<?php
		}

	}
}
?>
</body>
</head>
</html>
