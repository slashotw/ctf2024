
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Processes2.0</title>
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
        .form-control {
            background-color: #2a2a2a;
            border: 1px solid #444;
            color: #e0e0e0;
        }
        .form-control:focus {
            background-color: #333;
            border-color: #0066cc;
            box-shadow: 0 0 0 0.25rem rgba(0, 102, 204, 0.25);
            color: #fff;
        }
        .btn-primary {
            background-color: #0066cc;
            border-color: #0066cc;
        }
        .btn-primary:hover {
            background-color: #0052a3;
            border-color: #0052a3;
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
                                <img src="a.jpg" alt="login form" class="img-fluid h-100" style="object-fit: cover; object-position: left;">
                            </div>
                            <div class="col-md-7">
                                <div class="card-body p-5">
                                    <h2 class="text-center mb-5">脆 (活網版threads)</h2>
                                    <h5 class="text-center mb-4 text-danger">開放註冊中</h5>
                                    
                                    <form method="POST" action="preview.php" enctype="multipart/form-data">
                                        <div class="mb-4">
                                            <label for="username" class="form-label">Account Name</label>
                                            <input type="text" name="username" id="username" class="form-control form-control-lg" required>
                                        </div>
                                        
                                        <div class="mb-4">
                                            <label for="password" class="form-label">Password</label>
                                            <input type="password" name="password" id="password" class="form-control form-control-lg" required>
                                        </div>
                                        
                                        <div class="mb-4">
                                            <label for="formFile" class="form-label">Avatar</label>
                                            <input class="form-control form-control-lg" name="file" type="file" id="formFile">
                                        </div>
                                        
                                        <div class="d-grid">
                                            <button type="submit" class="btn btn-primary btn-lg">Register</button>
                                        </div>
                                    </form>
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