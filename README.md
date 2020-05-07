Le projet vous est donné avec un environnement virtuel. Cependant, utilisant 2 OS différents au sein de l'équipe (MAC et Windows) nous avons dû nous adapter. 
En effet, afin d'accéder à cet environnement virtuel sur Windows vous n'avez rien à faire si ce n'est ouvrir un nouveau terminal pour vous en assurer. 
Sur MAC, nous avons dû créer un autre environnement virtuel car le fichier settings.json (dans le folder .vscode) exécute un fichier (python.exe) se trouvant dans le dossier "Scripts" qui est inexistant pour les utilisateurs de cet OS.
Ainsi, afin d'utiliser cet autre environnement virtuel, il faut le faire manuellement via le terminal bash ou zsh, suivant ce que vous avez. 
Vérifiez d'être placé au bon endroit (regarder le chemin dans le terminal) et écrivez la commande suivante : source virtual_environment_MAC/bin/activate.

Pour Vincent : discard le change sur le settings.json avant de commit avec -> git checkout .vscode/settings.json 
