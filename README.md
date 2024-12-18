# PST_LLM

# Docker
Pour faire fonctionner le projet nous utilisons le logiciel ollama (que vous pouvez retrouver sur https://ollama.com/), qui nous permet d'appeler différents LLM opensource.

Pour faciliter l'intégration à une application nous utilisons un ollama sur conteneur docker, pour cela il faut une installation de docker, les procédures sur linux dépendent du système d'exploitation, vous pouvez retrouver les tutoriels en focntion de votre OS ici https://docs.docker.com/engine/install/
Pour windows il faut cliquer sur https://docs.docker.com/engine/install/binaries/   et aller voir la partie sur windows ou installer docker desktop, ou faire l'installation en utilisant Windows Subsytem for Linux.

# Setup
Pour une utilisation de l'application présente sur ce github, vous pouvez simplement executer le fichier windows_setup.bat pour windows et linux_setup.sh pour linux.

les fichiers setup font:
une installation du conteneur ollama le rendant utilisable pour les gpus, pour cela il faut avoir les nvidia tool kit installer compatible avec votre OS
sinon vous pouver remplacer "docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama"  par  "docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama" pour faire une utilisation sur cpu.
sinon vous pouvez remplacer par "docker run -d --device /dev/kfd --device /dev/dri -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama:rocm" qui permet une utilisation sur gpu amd

Ensuite le fichier de setup install le modèle que nous allons utiliser sur le conteneur
Fais un network docker pour permettre à des conteneurs de communiquer.
ajouter le conteneur ollama dans le network
utilise le dockerfile présent dans le dossier pour mettre notre application dans un conteneur sur le port 5000
et allume ce dernier de conteneur.

pour plus d'informations sur l'installation du conteneur ollama voir https://hub.docker.com/r/ollama/ollama

# Utilisation

Une fois que le setup est réaliser vous pouvez simplement utiliser l'application en envoyant le cas résumé et le nom du modèle sur le port 5000 en local.
Vous pouvez voir un exemple de cela dans le fichier t.py

l'application crée par le setup accepte 2 routes en poste, la première "/summarize_2ex" et la seconde "/summarize_1ex", les 2 font la même chose mais dans l'une on passe 2 exemples de ce que l'on attend au llama, dans l'autre 1 seul. La différences de résultats n'est pas flagrante.

pour utilise l'application il faut simplement envoyer sur le port 5000 un json de ce type :

data = {
    "message": """message que l'on veut résumé ici
""",
"model_name": "llama3.1:8b"  #ou nom du modèle que l'on veut utiliser
}
