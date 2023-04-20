# SoftDesk
## Créez une API sécurisée RESTful en utilisant Django Rest

### Comment ça marche :question::question::question:

:one:  Téléchargez le repo zip sur github 

:two:  On viens dézipper l'ensemble de notre repo dans un nouveau dossier que l'on appellera *_Softdesk_* 

:three:  Il va falloir activer l'environnement virtuel. A l'aide du terminal, on vient choisir notre nouveau dossier :arrow_down:

```
cd Softdesk
python -m venv env 
.//env/Scripts/activate.ps1

```

Normalement, lors de l'activation vous devriez voir (env) devant le chemin :arrow_down:

```
 (env) PS C:\Users\Arthur\desktop\Softdesk>

```

:four: Il faut ensuite télécharger les librairies nécessaires depuis *requirements.txt* :arrow_down: 

```
 pip install -r requirements.text

```

### Utilisation :question::question::question:


:one:  Si nécessaire, effectué les migrations :arrow_down: 

```
python manage.py makemigrations
python manage.py migrate

```

:two:  On lance le serveur Django :arrow_down: 

```
python manage.py runserver

```

Il est possible de naviguer dans l'API via [Postman](https://www.postman.com/) ou bien l'interface Django REST : [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
Documentation de l'API [ICI](https://documenter.getpostman.com/view/26504381/2s93Y3tfDk)
