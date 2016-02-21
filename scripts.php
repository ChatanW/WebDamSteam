
<?php
header( 'content-type: text/html; charset=utf-8' );
function best_community($user_id, $nb_file) {
  $api_key = "5BB69AE39C3B27011CE4CCDA8606F427";
  //echo exec('locale charmap');
  exec ("python scriptPython/script.py ".$user_id." ".$nb_file, $my_results);
  $init = 0;
  $phrase_change = "##CHANGEMENT123321##";
  for ($i = 0; $i < count($my_results); ++$i) {
    if ($my_results[$i]==$phrase_change) {
      $init = 0;
      echo '</ul> '.nl2br("\r\n");
    }
    elseif ($init == 0) {
      $id_teamate = $my_results[$i];
      $url = file_get_contents("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=".$api_key."&steamids=".$id_teamate); 
      $content = json_decode($url, true);
      $url_profile = $content['response']['players'][0]['profileurl'];
      $name_teamate = $content['response']['players'][0]['personaname'];
      $avatar = $content['response']['players'][0]['avatarmedium'];
      echo '<a href="'.$url_profile.'"> <img src="'.$avatar.'"/> '.$name_teamate.' </a>';
      $init = $init + 1;
    }
    elseif ($init==1) {
      $score = $my_results[$i];
      echo 'Teammate potentiel : '.$name_teamate.' (score : '.$score.'). Jeux en commun : ';
      //echo '   Tu as un score de '.$score.' en ce qui concerne la correspondance entre toi et '.$name_teamate.' et voici les jeux auxquels vous pouvez jouer ensemble : <ul>'. nl2br("\r\n");
      $init = $init + 1;
    }
    elseif ($init==2) {
    $game = $my_results[$i];
    echo '<li> '.$game; 
    $init = $init + 1;
    }
    elseif ($init==3) {
      $my_time = $my_results[$i] / 60;
      echo ' Ton temps de jeu : '.$my_time.' heures. ';
      //echo ', tu y as joué '.$my_time.' minutes ';
      $init = $init + 1;
    }
    elseif ($init==4) {
      $his_time = $my_results[$i] / 60;
      echo 'Son temps de jeu : '.$his_time.' heures. '.' </li> '.nl2br("\r\n");
      //echo 'et lui '.$his_time.' minutes. '.' </li> '.nl2br("\r\n");
      $init = 2;
    }
  }
}


function best_friends($user_id) {
  $api_key = "5BB69AE39C3B27011CE4CCDA8606F427";
  exec ("python scriptPython/script_friends.py ".$user_id, $my_results);
  $init = 0;
  $phrase_change = "##CHANGEMENT123321##";
  for ($i = 0; $i < count($my_results); ++$i) {
    if ($my_results[$i]==$phrase_change) {
      $init = 0;
      echo '</ul> '.nl2br("\r\n");
    }
    elseif ($init == 0) {
      $id_teamate = $my_results[$i];
      $url = file_get_contents("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=".$api_key."&steamids=".$id_teamate); 
      $content = json_decode($url, true);
      $url_profile = $content['response']['players'][0]['profileurl'];
      $name_teamate = $content['response']['players'][0]['personaname'];
      $avatar = $content['response']['players'][0]['avatarmedium'];
      echo '<a href="'.$url_profile.'"> <img src="'.$avatar.'"/> '.$name_teamate.' </a>';
      $init = $init + 1;
    }
    elseif ($init==1) {
      $score = $my_results[$i];
      echo 'Teammate potentiel : '.$name_teamate.' (score : '.$score.'). Jeux en commun : ';
      //echo '   Tu as un score de '.$score.' en ce qui concerne la correspondance entre toi et '.$name_teamate.' et voici les jeux auxquels vous pouvez jouer ensemble : <ul>'. nl2br("\r\n");
      $init = $init + 1;
    }
    elseif ($init==2) {
    $game = $my_results[$i];
    echo '<li> '.$game; 
    $init = $init + 1;
    }
    elseif ($init==3) {
      $my_time = $my_results[$i] / 60;
      echo ' Ton temps de jeu : '.$my_time.' heures. ';
      //echo ', tu y as joué '.$my_time.' minutes ';
      $init = $init + 1;
    }
    elseif ($init==4) {
      $his_time = $my_results[$i] / 60;
      echo 'Son temps de jeu : '.$his_time.' heures. '.' </li> '.nl2br("\r\n");
      //echo 'et lui '.$his_time.' minutes. '.' </li> '.nl2br("\r\n");
      $init = 2;
    }
  }
}



?>