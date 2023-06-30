<?php 

    session_start(); 

    if ((!isset($_POST['login'])) || (!isset($_POST['haslo'])))
    {
        header('Location: index.php');
        exit();
    }

    require_once "connect.php"; 
    
    $polaczenie = @new mysqli($host, $db_user, $db_password, $db_name); 


    if ($polaczenie -> connect_errno!=0)
    {
        echo "Error:".$polaczenie->connect_errno; 
    }
    else
    {
        $login = $_POST['login'];
        $haslo = $_POST['haslo'];

        if (($login == null) && ($haslo == null))
        {
            header('Location: index.php');
            exit();
        }
        if (($login != $wiersz['login']) or ($haslo != $wiersz['password']))
        {
            header('Location: index.php');
        }
       
        $login = htmlentities($login, ENT_QUOTES, "UTF-8");
        $haslo = htmlentities($haslo, ENT_QUOTES, "UTF-8");

        if ($rezultat = @$polaczenie -> query(sprintf("SELECT * FROM users WHERE login = '%s' AND password = '%s'", 
        mysqli_real_escape_string($polaczenie,$login),
        mysqli_real_escape_string($polaczenie,$haslo)))) 
        {
           $ile_login = $rezultat -> num_rows;
           if($ile_login>0)
           {    
                $_SESSION['zalogowany'] = true; 
                

                $wiersz = $rezultat -> fetch_assoc(); 
                $_SESSUIN['id'] = $wiersz['id']; 
                $login = $wiersz['login']; 
                $_SESSION['login'] = $wiersz['login'];
                $_SESSION['haslo'] = $wiersz['password'];
                $_SESSION['id'] = $wiersz['id'];
                $_SESSION['name'] = $wiersz['name'];
                $_SESSION['lastname'] = $wiersz['lastname'];
                $_SESSION['email'] = $wiersz['email'];

                unset($_SESSION['blad']);
                $rezultat -> free_result(); 
                header('Location: webside.php'); 
            } 
            else 
            {
                $_SESSION['blad'] = '<span style="color:red">Nieprawidłowy login lub hasło!</span>'; 
                header('Lacation: index.php');
            } 
        }
        $polaczenie->close();
    }
?>