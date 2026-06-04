<?php
if (!file_exists("/tmp/news.json")) {
    $file = fopen("/tmp/news.json", "w");
    fwrite($file, json_encode([
        [
            "title" => "Welcome",
            "content" => "This is the first news item. You can add more news items using the admin panel.",
            "date" => date("Y-m-d H:i:s"),
            "image" => "https://placehold.co/300x200"
        ]
    ]));
    fclose($file);
}

if (!file_exists("/tmp/admin_pass.txt")) {
    $file = fopen("/tmp/admin_pass.txt", "w");
    $random = bin2hex(random_bytes(16));
    fwrite($file, $random);
    fclose($file);

    $stdout = fopen('php://stdout', 'w');
    fwrite($stdout, "Admin password: $random\n");
    fclose($stdout);
}
?>
