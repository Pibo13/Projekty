<?php
    session_start();
    if (!isset($_SESSION['zalogowany']))
    {
        header('Location: index.php');
        exit();
    }
?>




<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style_webside.css"/>
    <title>POLPIOTECH: Konto użytkownika</title>
</head>




<br><br>
<body>
<header>
    <nav class="menu">
                    
        <div class="dropdown">
            <a href="webside.php">Strona główna</a>
        </div>

        <div class="dropdown">
            <a href="#">Profil</a>
                <ul>
                    <li><a href="webuserprofil.php">Konto użytkownika</a></li>
                    <li><a href="websideset.php">Ustawienia</a></li>
                </ul>
        </div>

        <div class="dropdown">
            <a href="#">Chmura</a>
                <ul>
                    <li><a href="#">Google Drive</a></li>
                    <li><a href="#">Microsoft OneDrive</a></li>
                </ul>
        </div>

        <div class="dropdown">
            <a href="#">Projekty</a>
                <ul>
                    <li><a href="#">BATCH</a></li>
                    <li><a href="#">VBA</a></li>
                    <li><a href="#">HTML/CSS/JS/PHP/MySQL</a></li>
                    <li><a href="#">C++</a></li>
                    <li><a href="#">Python</a></li>
                </ul>
        </div>

        <div class="dropdown">
            <a href="#">Książki</a>
                <ul>
                    <li><a href="#">Projekty IT w praktyce</a></li>
                    <li><a href="#">Certyfikowany Tester ISTQB</a></li>
                    <li><a href="#">Python dla testera</a></li>
                    <li><a href="#">Algorytmy w pythonie</a></li>
                    <li><a href="#">Kali Linux i testy penetracyjne</a></li>
                    <li><a href="#">HTML i CSS</a></li>
                    <li><a href="#">JavaScript i JQUERY</a></li>
                    <li><a href="#">PHP i SQL</a></li>
                </ul>
        </div>

        <div class="logout">
            <p><a href="logout.php">Wyloguj</a></p>
        </div>

        <div class="userinfo">    
            <?php
                echo "<p><b>Użytkownik: </b>".$_SESSION['login'];
            ?>
        </div>

    </nav>
</header>


    <div class="textInfo">
 
        <div class="text_side">
            <div img_front>
                <img class="imagesInFront" src="grom.jpeg">
            </div>
        <p><h2>Konto:</h2></p>


        </div>

        <div class="userinfo">    
            <?php
                echo "<p><b>|| Użytkownik: </b>".$_SESSION['login' ], " |";
                echo "<p><b>| ID-Profil: </b>".$_SESSION['id'], " |";
                echo "<p><b>| Imię: </b>".$_SESSION['name'], " |";
                echo "<p><b>| Nazwisko: </b>".$_SESSION['lastname'], " |";
                echo "<p><b>| E-Mail: </b>".$_SESSION['email'], " ||";
            ?>
        </div>
        


        </div>
    </div>

    </body>
    </html>