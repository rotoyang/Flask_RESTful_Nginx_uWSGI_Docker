Requirement: Docker & Docker-Compose

# Running Docker in Local
1. Clone Repo in directory named app
2. Add app/.mysql & app/.env files
  <pre><code>  .mysql:
    MYSQL_HOST=mysql
    MYSQL_PORT=3306
    MYSQL_DATABASE=DB_NAME_YOU_LIKE
    MYSQL_USER=DB_USER_YOU_WANT
    MYSQL_PASSWORD=USER_PASSWORD_YOU_DEFINE
    MYSQL_ROOT_PASSWORD=ROOT_PASSWORD_YOU_MAKE
  </code></pre>
  <pre><code>  .env:  # This is for local develop environment.
    MYSQL_HOST=0.0.0.0
    MYSQL_PORT=3306
    MYSQL_DATABASESAME_AS_.mysql_IS_REQUIRED
    MYSQL_USER=SAME_AS_.mysql_IS_REQUIRED
    MYSQL_PASSWORD=SAME_AS_.mysql_IS_REQUIRED
    MYSQL_ROOT_PASSWORD=SAME_AS_.mysql_IS_REQUIRED
    FLASK_APP=task.app
  </code></pre>
3. cd app 
4. Run: docker-compose -f dev.yml up --build -d
5. Stop: docker-compose -f dev.yml down

# Init CertBot in Prod Environment
1. Before exec below process, revise email and domain in the file first.
2. chmod + x init-letsencrypt.sh
3. sudo ./init-letsencrypt.sh
