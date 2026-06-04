<?php
session_start();

if (!isset($_GET['title'])) {
    http_response_code(400);
    echo "Missing title parameter";
    exit();
}

$file = fopen("/tmp/news.json", "r");
$news = json_decode(fread($file, filesize("/tmp/news.json")), true);
fclose($file);

$post = null;
foreach ($news as $item) {
    if ($item['title'] === $_GET['title']) {
        $post = $item;
        break;
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php echo $_GET['title']; ?></title>
</head>
<body>
    <nav>
        <a href="index.php">Home</a>
        <a href="login.php">Login</a>
        <a href="admin.php">Admin</a>
    </nav>
<?php
if ($post === null) {
    echo "<p>Post not found</p>";
} else {
    echo "<article>";
    echo "<h2>" . $post["title"] . "</h2>";
    echo "<p>" . $post["content"] . "</p>";
    echo "<p><em>Published on: " . $post["date"] . "</em></p>";
    echo "<img src='/image.php?url=" . $post["image"] . "' alt='News image' style='max-width: 100%; height: auto;'/>";
    echo "</article>";
}
?>
</body>
</html>
