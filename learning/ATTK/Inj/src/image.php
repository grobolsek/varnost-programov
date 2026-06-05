<?php
session_start();

if (!isset($_GET['url'])) {
    http_response_code(400);
    echo "Missing url parameter";
    exit();
}

$url = $_GET['url'];
$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
$imageData = curl_exec($ch);
$contentType = curl_getinfo($ch, CURLINFO_CONTENT_TYPE);

if ($imageData === false) {
    http_response_code(500);
    echo "Failed to fetch image";
    exit();
}

header("Content-Type: " . $contentType);
echo $imageData;
?>
