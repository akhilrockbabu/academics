<html>
<head>
</head>
<script>
function verify()
{
if(document.forms.f1.n1.value=="")
{
window.alert("enter name");
document.forms.f1.n1.focus();
}
else if(document.forms.f1.n2.value=="")
{
window.alert("enter age");
document.forms.f1.n1.focus();
}
else if(document.forms.f1.n3.value=="")
{
window.alert("enter adress");
document.forms.f1.n3.focus();
}
if(document.forms.f1.n4.value=="")
{
window.alert("enter email");
document.forms.f1.n4.focus();
}
if(document.forms.f1.n5.value=="")
{
window.alert("enter qualification");
document.forms.f1.n5.focus();
}
if(document.forms.f1.n6.value=="")
{
window.alert("enter pan_no");
document.forms.f1.n6.focus();
}
}
</script>

<title>personal data</title>

<h1 style="align=center;">personal data</h1>
<form method="post" action="insertdb.php" id="f1" onsubmit="return verify()">
<table border="3" align="center" style="color:black" bordercolor="redorange" width="20%" height="20%">
<tr>
<td>
<label for="name">name</label>
</td>
<td>
<input type"text" name="name" id="n1" required><br>
</tr></td>
<tr>
<td>
<label for"age">age</label>
</td>
<td>
<input type="text" name="age" id="n2"><br>
</td>
</tr>
<tr><td>
<label for="adress">adress</label>
</td>
<td>
<input type="text" name="adress" id="n3"><br>
</tr>
</td>
<tr>
<td>
<label for="email">email</label>
</td>
<td>
<input type="text" name="email"  pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$"  id="n4">
</tr>
</td>
<tr>
<td>
<label for="qualification">qualification</label>
</td>
<td>
<input type="text" name="qualification" id="n6"><br>
</tr></td>
<tr><td>
<label for="pan no">pan_no</label>
</td>
<td>
<input type="password" name="pan_no" id="n6"><br>
</tr>
<tr>

<td colspan="2" align=center><input type="submit" name="insert" value="insert" onClick="ver()"></td>
</tr>

 
 </table>
    
   </form>
   </html>
   
  


	
	
	
	
	
	
	
	
	




