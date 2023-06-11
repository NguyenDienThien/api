<?php
$ip = $_GET['ip'];
$port = $_GET['port'];
$time = $_GET['time'];
$method = $_GET['method'];

// Kiểm tra các tham số
if (empty($ip) || empty($port) || empty($time) || empty($method)) {
    die("Missing parameters");
}

// Chạy script Python với các tham số
$command = "python bypassaz.py " . escapeshellarg($ip) . " " . escapeshellarg($port) . " " . escapeshellarg($time);
$output = shell_exec($command);

// Xử lý kết quả
if ($output !== null) {
    echo nl2br($output);
} else {
    echo "An error occurred while executing the script.";
}
?>
