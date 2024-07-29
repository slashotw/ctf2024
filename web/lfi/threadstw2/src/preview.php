<?php
// PHP 代碼保持不變
// 設定上傳目錄
$uploadDirectory = 'upload/';

// 檢查是否有上傳檔案
if (isset($_FILES['file'])) {
    $file = $_FILES['file'];

    // 檢查是否有錯誤碼
    if ($file['error'] === UPLOAD_ERR_OK) {
        // 檢查檔案大小是否大於500KB
        $maxFileSize = 500 * 1024; // 500KB
        if ($file['size'] > $maxFileSize) {
            die('Error: 檔案大小不能超過 500KB.');
        }

        // 檢查是否僅允許單一檔案
        if (count($_FILES) > 1) {
            die('Error: 一次僅允許上傳單一檔案.');
        }

        // 取得檔案名稱及副檔名
        $originalFileName = $file['name'];
        $fileExtension = pathinfo($originalFileName, PATHINFO_EXTENSION);
        
        // 產生8位隨機數字
        $randomNumber = bin2hex(random_bytes(4));

        // 新的檔案名稱
        $newFileName = $randomNumber . '_' . $file['name'];

        // 移動檔案到上傳目錄
        if (@move_uploaded_file($file['tmp_name'], $uploadDirectory . $newFileName)) {
            $uploadMessage = 'SUCCESS~檔案上傳成功！';
        } else {
            $uploadMessage = 'Error: 檔案上傳失敗.';
        }
    } else {
        $uploadMessage = 'Error: 檔案上傳錯誤.';
    }
} else {
    $uploadMessage = 'Error: 沒有選擇檔案上傳.';
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Process</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">
    <style>
        body {
            background-color: #121212;
            color: #e0e0e0;
        }
        .card {
            background-color: #1e1e1e;
            border-radius: 1rem;
            transition: box-shadow 0.3s ease;
            overflow: hidden;
        }
        .card:hover {
            box-shadow: 0 0 20px rgba(0, 100, 255, 0.5);
        }
        .text-black {
            color: #e0e0e0 !important;
        }
        .text-black-50 {
            color: #a0a0a0 !important;
        }
    </style>
</head>
<body>
    <section class="vh-100 d-flex align-items-center">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-12 col-xl-10">
                    <div class="card">
                        <div class="row g-0">
                            <div class="col-md-5 d-none d-md-block">
                                <img src="<?php echo "upload/".$newFileName; ?>" alt="user avatar" class="img-fluid h-100" style="object-fit: cover; object-position: center;">
                            </div>
                            <div class="col-md-7">
                                <div class="card-body p-5">
                                    <h2 class="text-center mb-4">Processes2.0</h2>
                                    
                                    <div class="mb-4">
                                        <h3 class="fw-bold">@<?php 
                                        if ($_SERVER["REQUEST_METHOD"] == "POST") {
                                            if (isset($_POST["username"]) && isset($_POST["password"])) {
                                                echo htmlspecialchars($_POST["username"]);
                                            } else {
                                                echo "Username or password is empty";
                                            }
                                        }
                                        ?></h3>
                                    </div>
                                    
                                    <h5 class="fw-normal mb-4 text-black-50">Screenshot to share with your friend!</h5>
                                    
                                    <?php if (isset($uploadMessage)): ?>
                                        <div class="alert <?php echo strpos($uploadMessage, 'SUCCESS') !== false ? 'alert-success' : 'alert-danger'; ?>">
                                            <?php echo $uploadMessage; ?>
                                        </div>
                                    <?php endif; ?>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-/bQdsTh/da6pkI1MST/rWKFNjaCP5gBSY4sEBT38Q/9RBh9AH40zEOg7Hlq2THRZ" crossorigin="anonymous"></script>
</body>
</html>