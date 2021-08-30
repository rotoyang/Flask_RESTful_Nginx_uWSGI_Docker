Requirement: Docker & Docker-Compose

# Running Docker in Local
1. Clone Repo, renamed directory to app
2. Add app/.env file
  <pre><code>  .env:
    # Flask
    FLASK_APP=task.app
    # MySQL
    MYSQL_HOST=mysql
    MYSQL_PORT=3306
    MYSQL_DATABASE=DB_NAME_YOU_LIKE
    MYSQL_USER=DB_USER_YOU_WANT
    MYSQL_PASSWORD=USER_PASSWORD_YOU_DEFINE
    MYSQL_ROOT_PASSWORD=ROOT_PASSWORD_YOU_MAKE
  </code></pre>
3. cd app 
4. Run: docker-compose -f dev.yml up --build -d
5. Stop: docker-compose -f dev.yml down
6. Migrate: docker-compose -f dev.yml exec -T flask flask db migrate -m "COMMENT_MESSAGE"


# Running Docker in Server
1. Same as Local step 1~2.
2. Edit prod.yml, change nginx args 
    - CERTBOT_EMAIL=YOUR_EMAIL
    - DOMAIN_LIST=YOUR_DOMAIN
4. cd app
5. Run: docker-compose -f prod.yml up --build -d
6. Stop: docker-compose -f prod.yml down


# Grant User Permission to Docker in Server Side
1. sudo gpasswd -a ${USER} docker
2. sudo su
3. su ubuntu
