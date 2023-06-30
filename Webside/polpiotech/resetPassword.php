<?php
    session_start();
    
    if (isset($_SESSION['zalogowany']) && ($_SESSION['zalogowany']==true))
    {
        header('Location: webside.php'); 
        exit(); 
    }

?>
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css"/>
    <title>POLPIOTECH: Panel logowania</title>
</head>
<body>

<div class="tytul">
        <div class="firma">
            <span>Polish Peter Technology Sp. z o.o.</span>
        </div>
        <div class="marka">
            <h1><b>POLPIOTECH®</b></h1>
        </div>
    </div>

<div class="inBody">
        <div class="glownyNaglowek">
            <h1>Panel przywracania hasła</h1> <br/><br/>
        </div>
        <div class="belka"></div>
        <div class="panelLogowania">
            <span><b>Wprowadź dane, aby rozpocząć procedurę przywrócenia dostępu do konta.</b></span> <br/><br/>
            <form action="logon.php" method="post"> 
                Login: <input type="text" name="login" /> <br><br/> 
                E-Mail: <input type="text" name="email" /> <br/><br/>
</br>
                <input type="submit" value="Reset hasła"/>
                <input type="submit" value="Anuluj"/>
            </form>
        </div>

 <!--       <?php
            if(isset($_SESSION['blad']))    echo $_SESSION['blad'];
        ?> -->
    </div>
</body>
</html>