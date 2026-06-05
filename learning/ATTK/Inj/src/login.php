<?php
session_start();

if (isset($_SESSION['username'])) {
    header("Location: index.php");
    exit();
}

if (isset($_POST['username']) && isset($_POST['password'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];

    $adminPassFile = "/tmp/admin_pass.txt";
    $adminPassword = trim(file_get_contents($adminPassFile));

    if ($username === "admin" && $password === $adminPassword) {
        $_SESSION['username'] = $username;
        header("Location: index.php");
        exit();
    } else {
        $error = "Invalid username or password";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>
    <nav>
        <a href="index.php">Home</a>
        <a href="login.php">Login</a>
        <a href="admin.php">Admin</a>
    </nav>
    <h1>Login</h1>
    <main>
        <?php if (isset($error)) { echo "<p style='color: red;'>$error</p>"; } ?>
        <form action="login.php" method="post">
            <label for="username">Username:</label><br>
            <input type="text" id="username" name="username" required><br>
            <label for="password">Password:</label><br>
            <input type="password" id="password" name="password" required><br>
            <input type="submit" value="Login">
        </form>
    </main>
</body>

