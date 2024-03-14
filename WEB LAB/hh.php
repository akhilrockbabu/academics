<?php
function factorial(&$c)
{
if($c==1)
{
	return 1;
}
else
{
	return $c*factorial($c-1);
}
}
$i=5;
echo factorial($i);
echo $i;

?>
