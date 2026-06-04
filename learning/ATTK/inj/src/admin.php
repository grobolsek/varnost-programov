<?php
session_start();
if (!isset($_SESSION['username'])) {
    header("Location: login.php");
    exit();
}

if (isset($_POST['title']) && isset($_POST['content'])) {
    $newsItem = [
        "title" => $_POST['title'],
        "content" => $_POST['content'],
        "date" => date("Y-m-d H:i:s"),
        "image" => $_POST['image'] ?? ""
    ];

    $file = fopen("/tmp/news.json", "r");
    $news = json_decode(fread($file, filesize("/tmp/news.json")), true);
    fclose($file);

    array_unshift($news, $newsItem);

    $file = fopen("/tmp/news.json", "w");
    fwrite($file, json_encode($news));
    fclose($file);

    header("Location: index.php");
    exit();
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin</title>
</head>
<body>
    <nav>
        <a href="index.php">Home</a>
        <a href="login.php">Login</a>
        <a href="admin.php">Admin</a>
    </nav>
    <h1>Add news feed</h1>
    <main>
        <form action="admin.php" method="post">
            <label for="title">Title:</label><br>
            <input type="text" id="title" name="title" required><br>
            <label for="content">Content:</label><br>
            <textarea id="content" name="content" required></textarea><br>
            <label for="image">Image URL:</label><br>
            <input type="text" id="image" name="image"><br>
            <input type="submit" value="Add News">
        </form>
    </main>
</body>
</html>
