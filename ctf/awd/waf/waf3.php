<?php
error_reporting(E_ALL^E_NOTICE^E_WARNING);

function StopAttack($StrFiltKey,$StrFiltValue,$ArrFiltReq){  

	if(is_array($StrFiltValue))
	{
    $StrFiltValue=implode($StrFiltValue);
	}  
	if (preg_match("/".$ArrFiltReq."/is",$StrFiltValue)==1){   
		//slog("<br><br>����IP: ".$_SERVER["REMOTE_ADDR"]."<br>����ʱ��: ".strftime("%Y-%m-%d %H:%M:%S")."<br>����ҳ��:".$_SERVER["PHP_SELF"]."<br>�ύ��ʽ: ".$_SERVER["REQUEST_METHOD"]."<br>�ύ����: ".$StrFiltKey."<br>�ύ����: ".$StrFiltValue);
		global $logfilename, $logstr,$data;
		file_put_contents($logfilename.".txt", "***".$logstr."\r\n", FILE_APPEND);
		file_put_contents($logfilename."-post.txt", "***".$logstr."|".$data."\r\n", FILE_APPEND);
		header("HTTP/1.1 500 Internal Server Error");
       die("HTTP/1.1 500 Internal Server Error");
	}
}


$logfilename='/var/tmp/'.substr(date('Hi',time()),0,3).'log';

$getfilter="\=|flag|passwd|O:4:|array_map|z0|\#|\;|-|\&|\||\'|\"|and|like|script|EXEC|UNION|SELECT|UPDATE|INSERT|INTO|VALUES|SELECT|DELETE|FROM|CREATE|ALTER|DROP|TRUNCATE|TABLE|DATABASE|\(|\)|php|eval|assert\?";
$postfilter="<\\?|\\'|\'|\"|flag|O:4:|array_map|z0|\\b(and|or)\\b.{1,6}?(=|>|<|\\bin\\b|\\blike\\b)|\\/\\*.+?\\*\\/|<\\s*script\\b|\\bEXEC\\b|UNION.+?SELECT|UPDATE.+?SET|INSERT\\s+INTO.+?VALUES|(SELECT|DELETE).+?FROM|(CREATE|ALTER|DROP|TRUNCATE)\\s+(TABLE|DATABASE)|define|eval|curl|wget|file_get_contents|include|require|require_once|shell_exec|phpinfo|system|passthru|preg_\w+|execute|echo|print|print_r|var_dump|fpopen|open|alert|showmodaldialog";
$datafilter="<\\?|script|flag|O:4:|array_map|z0|\\b(and|or)\\b.{1,6}?(=|>|<|\\bin\\b|\\blike\\b)|\\/\\*.+?\\*\\/|<\\s*script\\b|\\bEXEC\\b|UNION.+?SELECT|UPDATE.+?SET|INSERT\\s+INTO.+?VALUES|(SELECT|DELETE).+?FROM|(CREATE|ALTER|DROP|TRUNCATE)\\s+(TABLE|DATABASE)|define|eval|curl|wget|file_get_contents|include|require|require_once|shell_exec|phpinfo|system|passthru|preg_\w+|execute|echo|print|print_r|var_dump|fpopen|open|alert|showmodaldialog";
$cookiefilter="<\\?|O:4:|array_map|z0|\\b(and|or)\\b.{1,6}?(=|>|<|\\bin\\b|\\blike\\b)|\\/\\*.+?\\*\\/|<\\s*script\\b|\\bEXEC\\b|UNION.+?SELECT|UPDATE.+?SET|INSERT\\s+INTO.+?VALUES|(SELECT|DELETE).+?FROM|(CREATE|ALTER|DROP|TRUNCATE)\\s+(TABLE|DATABASE)";
$cookiefilter=$postfilter;
$URLFilter="\\/(up|attachments|upimg|images|css|uploadfiles|html|uploads|templets|static|template|data|inc|forumdata|upload|includes|cache|avatar)\\/.*ph.*";
///(up|attachments|upimg|images|css|uploadfiles|html|uploads|templets|static|template|data|inc|forumdata|upload|includes|cache|avatar)/(\\w+).(php|jsp)

$ip4=$_SERVER['REMOTE_ADDR'];
$pattern = '/^(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9])\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)/';
preg_match($pattern, $ip4, $matches, PREG_OFFSET_CAPTURE);
$ip3=$matches[0][0];
$pattern = '/^(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9])\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)/';
preg_match($pattern, $ip4, $matches, PREG_OFFSET_CAPTURE);
$ip3=$matches[0][0];
$ip2=$matches[0][0];
//print $ip2;

$data = file_get_contents('php://input'); 

while (list($key, $val) = each($_FILES))
  {
  //print_r($val);
  //$handle = fopen($val['tmp_name'], 'r');
   // while(!feof($handle)){
     //   echo fgetss($handle, 1024, '<br>');
    //}
    //fclose($handle);
   $a = file($val['tmp_name']);
    foreach($a as $line => $content){
        //echo 'line '.($line + 1).':'.$content;
		$phpstr=strpos($content,'?php');
       $scriptstr=strpos($content,'script');
		if (( $phpstr !== false) or ( $scriptstr !== false) ){
			header("HTTP/1.1 500 Internal Server Error");
          die("HTTP/1.1 500 Internal Server Error");
       }
    }
  }
$logstr="";
$logstr=date('y-m-d_h:i:s',time())."|".$_SERVER['REMOTE_ADDR']."|".$_SERVER['REQUEST_METHOD']."|".'http://'.$_SERVER['HTTP_HOST'].$_SERVER['REQUEST_URI']."|".$_SERVER['HTTP_USER_AGENT'];

//$httpmethod=arrry("GET","POST");
//if (in_array($_SERVER['REQUEST_METHOD'],httpmethod)){
//}
//else{
//	die("<!DOCTYPE HTML PUBLIC '-//IETF//DTD HTML 2.0//EN'><html><head><title>404 Not Found</title></head><body><h1>Not Found</h1><p>The requested URL was not found on this server.</p></body></html>");
//}



$httpmethod=array("GET","POST");
if (!in_array($_SERVER['REQUEST_METHOD'],$httpmethod)){
	header("HTTP/1.1 500 Internal Server Error");
          die("HTTP/1.1 500 Internal Server Error");
}

$ipallow=array("10.10.1.47");//allow ips
$ipdeny=array("10.10.1.1"); //deny ips
//$ipdeny=array("172.10.101.1","172.10.101.2");



if (in_array($ip2,$ipdeny) or in_array($ip3,$ipdeny) or in_array($ip4,$ipdeny)){
	header("HTTP/1.1 500 Internal Server Error");
       die("HTTP/1.1 500 Internal Server Error");
}

if(in_array($ip2,$ipallow) or in_array($ip3,$ipallow) or in_array($ip4,$ipallow)){

}
else
{
  if (1==1){  //������\E5\83?  	
  	
  	
  	
  	StopAttack("UrlFilter",$_SERVER['REQUEST_URI'],$URLFilter);
  	
		foreach($_GET as $key=>$value){
			if (strlen($value)>10){
				//header("HTTP/1.1 500 Internal Server Error");
       //die("HTTP/1.1 500 Internal Server Error");
			}
			else{
			}
			StopAttack($key,$value,$getfilter);
		}

		foreach($_POST as $key=>$value){ 
			if (strlen($value)>15){
				//header("HTTP/1.1 500 Internal Server Error");
       //die("HTTP/1.1 500 Internal Server Error");
			}
			else{
			}
			StopAttack($key,$value,$postfilter);
		}
		
		foreach($_COOKIE as $key=>$value){ 
	    StopAttack($key,$value,$cookiefilter);
		}
		
		if ($data<>""){
			StopAttack("PostDataFilter",$data,$datafilter);
		}
	}
}

file_put_contents($logfilename.".txt", $logstr."\r\n", FILE_APPEND);
file_put_contents($logfilename."-post.txt", $logstr."|".$data."\r\n", FILE_APPEND);

?>