<!DOCTYPE html>
<html>
<head>
    <title>Rezultat</title>
</head>
<body>
    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $numar1 = $_POST["numar1"];
        $numar2 = $_POST["numar2"];
        $suma = $numar1 + $numar2;
        echo "Suma celor doua numere este: " . $suma;
    }
    ?>
</body>
</html>
