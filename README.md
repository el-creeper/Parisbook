# Parisbook 

Ceci est un vieux projet (2020), ce site permetait de rechercher la disponibilité de livre sur Paris.

## Compte rendu du projet de fin d’année de 1e NSI

### Formation du projet et construction du plan

Pendant la recherche de notre projet plusieurs idées nous sont venues à l’esprit, mais aucune ne convenait, elles étaient soit inutiles, soit peu originales, trop difficiles à mettre en œuvre ou trop simples. Rocco a finalement eu l’idée de ce projet. Le but était de trouver dans Paris le livre que l’on souhaite acheter. Et nous retourner plusieurs informations à son sujet, comme le prix, le nom de la librairie, la position etc...
Comme nous n’avions plus beaucoup de temps pour rédiger le cahier des charges, Elliot s’est chargé de le réaliser. La forme devait être un programme, avec une barre de recherche et une carte où serait affiché les différents points représentant la localisation des librairies. Elliot devait se charger des requêtes au serveur web, et avec Rocco du traitement de l’information. Rocco devait en plus de cela faire l’affichage et l’intégration de l’application avec Timoteo. Et enfin le visuel devait être effectué par Timoteo.

### Début du projet 

Durant les deux semaines de vacances, le groupe n’a pas beaucoup avancé car les différentes actions qu’effectuaient le programme était liées entre elles. Comme Elliot n’avait pas beaucoup de connexion et que c’était lui qui devait faire la première partie du projet, il fût très compliqué pour les autres d’avancer. 
Malgré tout nous nous sommes tout de suite rendu compte qu’un site internet, irai mieux avec le projet souhaité. Rocco décida donc de créer la page html et le css. Il n’a pas beaucoup changé depuis. Le site est minimaliste, avec le nom du projet « Paribook », ainsi qu’une barre de recherche et une carte interactive venant de google map, centrée à Paris.  Elliot commença à coder la partie permettant de récupérer les différentes informations. Il décida d’utiliser un navigateur programmable du nom de sélénium, qui figure parmi les plus connu et qui a donc une grosse documentation. Le seul problème avec les navigateurs programmables est qu’il faut télécharger l’extension correspondant au navigateur souhaité. 
Le premier site qui devait pouvoir fournir des informations devaient être la Fnac. Le code commence donc en définissant le lien grâce aux noms du livre fournit. On ouvre ensuite la session de sélénium qui permet d’accéder au site. La première épreuve à surmonter était d’accepter les cookies (on les accepte parce que les cookies c’est bon). Il fût très compliqué de trouver la solution à ce problème car Elliot et sa connexion ne lui permettait pas de faire assez de recherches sur la documentation, de plus le démarrage du programme était très lent puisqu’il fallait à chaque fois recharger la page. 
La méthode utilisée pour appuyer sur le bouton est la suivante : rechercher le bouton grâce à son id et dire au navigateur d’appuyer dessus. Théoriquement cela est très facile, mais pour des raisons mystérieuses, l’id n’est pas reconnu sur la page. Mais à force de tâtonnement et de test, Elliot trouva qu’en ne mettant qu’une seule partie de l’id cela fonctionnait. Après avoir appuyé sur ce bouton il fallait, appuyer sur le premier livre qui apparaissait. Malheureusement, le même problème survenu, le nom de la classe de l’élément n’est pas reconnu. Pour ce problème contrairement au précédent, il n’était pas possible de mettre d’espace dans le class Name. Enfin un troisième bouton devait être cliqué, celui de la recherche des boutiques disponibles. Cette implémentation fût plus simple que les deux premières mais nécessita tout de même plusieurs heures de travail. 
Nous avions donc maintenant un pop-up pour mettre la ville dans laquelle nous voulions rechercher le livre. Le seul problème est qu’il est impossible d’interagir avec le pop-up en utilisant seulement des id html. Le pop-up étant géré par du javascript, il est très difficile d’obtenir les informations la concernant. Nous avons donc rendu ce projet comme il était en cherchant pour les semaines à venir des solutions. 

### Changement de site

De retour à Paris, Elliot eût enfin une bonne connexion, ce qui lui permit de se rendre compte que la Fnac détectait désormais son navigateur programmable et le bloquait. Malgré quelque ajout de ligne permettant de changer des paramètres à chaque requête, rien ne lui permit de contourner ce blocage. Il demanda donc à sa mère si elle connaissait un site répertoriant de nombreuses librairies et cela lui permit de trouver un site plus petit : parislibrairies. Il possédait moins de protection anti bot que la Fnac, ce qui était parfait. Mais il fallut recoder tout le programme en s’adaptant au nouveau site. Heureusement, en regardant la documentation, de sélénium en profondeur il se rendit compte qu’il y avait une méthode pour faire les requêtes qui s’appelait XPATH. Il s’agit d’un chemin d’accès sur la page html et en plus en inspectant l’élément il était possible de copier directement le chemin (exemple de chemin XPATH : //*[@id="liste_livres"]/li[1]/div[2]/div[2]/div/div/div[1]/span[2]/a). Cela permit facilement de récupérer toutes les informations requises sur la première librairie. On créa ensuite un tableau de tableau de dictionnaire avec dans celui-ci les informations concernant le prix, le stock, le nom de la librairie et l’adresse de celle-ci. Le code python était donc en grande partie finit, il « suffisait » seulement de faire le cgi, et envoyer la map. C’est cette version que nous avons rendu lors du second rendu. 

###  Mise en place du site web

Il était convenu qu’Elliot mettait en place le serveur afin que celui-ci puisse interagir avec la page web. Malheureusement, ce choix fît perdre environ une semaine au groupe. Effectivement, deux bugs, ont empêché d’avancer. Le constat de ce problème était simple effectivement, il n’y avait aucune interaction entre le site web et le serveur, seulement l’exécution du program.cgi et non les données associées aux recherches.
Le premier problème était le suivant, Elliot utilisait le navigateur Opera pour accéder aux pages web (il permet de limiter la RAM utilisée ce qui est très pratique). Malheureusement, Opera pour une raison dont nous ignorons la cause, ne permet pas d’exécuter un script cgi. Se rendre compte de cela à été très long, car ce n’est pas un bug auquel on pourrait s’attendre, et de plus il n’y aucun moyen de se rendre compte que ce bug survient à cause du navigateur. Heureusement, la solution était simple : utiliser Chrome ou Edge.  
Une seconde erreur nous a fait perdre beaucoup de temps, effectivement nous utilisons serveur-web-post.py pour mettre en ligne la page web. Et qui aurait l’idée d’aller regarder dans le programme la limite de out, parce que la page web html ne s’affiche pas ? Le problème venait donc de là, il est configuré par défaut à 5 secondes, or le serveur prend plus que ça pour renvoyer la réponse. Nous l’avons donc modifié à 20 au cas où. Ainsi Elliot put donner le code à Rocco pour qu’il puisse traiter les données.
Le premier problème qu’a pu rencontrer Rocco est qu’on ne peut pas placer des points sur une carte avec une adresse, est qu’il faut obligatoirement des coordonnées. Nous ne voulions pas utiliser l’api de google pour faire la requête, car il fallait rentrer une carte de crédit pour pouvoir y accéder. Rocco a donc décidé de rechercher dans la liste de toutes les bibliothèques les coordonnés et de les rentrer dans un fichier texte, (il y a 200 bibliothèques donc c’était un peu long). Il a donc par la suite remplacé dans le dictionnaire, l’adresse par les coordonnées avec une boucle. 
Finalement Timoteo, a fait le reste du cgi, créant le contenu de la page renvoyée. Mais surtout, en envoyant la map au site web. En réalité il est presque impossible d’envoyer une map sans l’api google map. Nous avons donc fini par créer un compte sur google cloud plateforme et donc de renseigner une carte de crédit (celle de Elliot). Heureusement, google-nous offre gracieusement 300€ de requête, et par la suite rien ne sera débité sur la carte sans confirmation. Il ne faut donc pas trop faire de requête sur la page html sinon elle ne marchera plus. Afficher la carte à donc été assez compliqué, car il faut l’afficher en javascript, mais la documentation n’est pas très claire concernant l’api de google. Nous avons ajouté un titre au point, ainsi que le prix du livre. 
Nous avons donc pu finir la première version fonctionnelle du site. Malgré tout, le site ne correspond pas à la finalité que nous voulions avoir sur le cahier des charges. 

### Les bugs persistants

1.	Quand on écrit « true&fkej=rkeke », dans la barre de recherche le serveur crash
2.	Quelquefois le serveur crash pour une raison inconnu
3.	Si on recherche un livre inexistant aucune page web ne peux s’afficher

### Quelque photo

![image](https://github.com/el-creeper/Parisbook/assets/162908742/da3b7729-9c3c-4111-a6fc-1614f09dfe45)
![image](https://github.com/el-creeper/Parisbook/assets/162908742/46e6ee5b-71a1-426d-ad2d-801b58e81a30)
![image](https://github.com/el-creeper/Parisbook/assets/162908742/41cb2895-b2ca-4230-a40f-927959ceb19d)


