  <?php
	  $home=dirname(__FILE__);
	require_once("$home/../../discript.php");
	$file=fopen("in.disp","w");
	$dx=2.46;
	$dy=$dx*1.7321;
	$dz=6.70;
	$pac=$dz/$dx;
	if(!$usinglat){
$latx=floor($xlen/$dx);
$laty=floor($ylen/$dy);
$latz=floor($thick/$dz);
	}
	fprintf($file,
"3
$dx
$pac
6
6
y
$latx $laty $latz 
1
3
C
0
graphite.xyz
structure
map.in
");
	  $home=dirname(__FILE__);	
	shell_exec("$home/../../latgen <in.disp");
?>