<?php
session_start();
include 'generate.php';
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sandbox</title>
</head>
<body>
    <nav>
        <a href="index.php">Home</a>
        <a href="login.php">Login</a>
        <a href="admin.php">Admin</a>
    </nav>
    <h1>News feed:</h1>
    <main>
<?php
$file = fopen("/tmp/news.json", "r");
$news = json_decode(fread($file, filesize("/tmp/news.json")), true);
fclose($file);

foreach ($news as $item) {
    echo "<article>";
    echo "<h2>" . $item["title"] . "</h2>";
    echo "<p>" . $item["content"] . "</p>";
    echo "<p><em>Published on: " . $item["date"] . "</em></p>";
    echo "<img src='/image.php?url=" . $item["image"] . "' alt='News image' style='max-width: 100%; height: auto;'/>";
    echo "</article>";
}
?>
    </main>
</body>
</html>
