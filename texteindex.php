
<div id="body_index">
<div id="inscription_steam">
<?php
header( 'content-type: text/html; charset=utf-8' );
   //include("login_steam.php");
   require 'steamauth/steamauth.php' ;
require 'scripts.php';
$api_key = "5BB69AE39C3B27011CE4CCDA8606F427";



if(!isset($_SESSION['steamid'])) {
 
  steamlogin(); //login button

}  else {
  
  include ('steamauth/userInfo.php'); //To access the $steamprofile array
  //Protected content
  logoutbutton(); //Logout Button
  $locale='en_US.UTF-8';
  setlocale(LC_ALL,$locale);
  putenv('LC_ALL='.$locale);
  //echo exec('locale charmap');
  echo '<form action="texteindex.php?gp=1" method="post"><input value="Petite communauté" type="submit" /> </form>';
  echo '<form action="texteindex.php?gp=2" method="post"><input value="Moyenne communauté" type="submit" /> </form>';
  echo '<form action="texteindex.php?gp=3" method="post"><input value="Grande communauté" type="submit" /> </form>';
  echo '<form action="texteindex.php?gp=f" method="post"><input value="Mes amis" type="submit" /> </form>';

  
}

if (isset ($_GET['gp'])) {
  $gp = htmlspecialchars($_GET['gp']);
  if ($gp == '1' or $gp == '2' or $gp == '3') {
    best_community($steamprofile['steamid'], $gp);
  }
  elseif ($gp == 'f') {
    best_friends($steamprofile['steamid']);
  }
}


?>
</div>

   <div id="texte_index">
   <h1> Viens découvrir tes meilleurs teammates ! </h1>
   
   Bienvenue sur ce site de rencontre pour gamers. 
   Si tu cherches des compagnons de jeu ayant les mêmes goûts que toi, tu es au bon endroit ! 
   Nous t'aiderons à trouver des joueurs qui semblent aimer les mêmes jeux que toi :)
   

   </div>

</div>
