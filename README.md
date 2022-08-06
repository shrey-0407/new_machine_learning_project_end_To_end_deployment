# new_machine_learning_project_end_To_end_deployment

Software and account Requirement.
Github Account
Heroku Account
VS Code IDE
GIT cli
GIT Documentation

Creating conda environment
```
conda create -p venv python==3.7 -y
```
```
conda activate venv/
```
OR 
```
conda activate venv
```
```
pip install -r requirements.txt
```


To Add files to git
```
git add .
```

OR
```
git add <file_name>
```

> Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status 
```
git status
```
To check all version maintained by git
```
git log
```

To create version/commit all changes by git
```
git commit -m "message"
```

To send version/changes to github
```
git push origin main
```

To check remote url 
```
git remote -v
```


To setup CI/CD pipeline in heroku we need 3 information
1. HEROKU_EMAIL = shreyash966977@gmail.com
2. HEROKU_API_KEY = c195a9c4-e1d0-4a87-acdb-7918963cb76f
3. HEROKU_APP_NAME = ml-regressor-app01


BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```
> Note: Image name for docker must be lowercase


To list docker image
```
docker images
```

Run docker image
```
docker run -p 5000:5000 -e PORT=5000 f8c749e73678
```

To check running container in docker
```
docker ps
```

Tos stop docker conatiner
```
docker stop <container_id>
```
