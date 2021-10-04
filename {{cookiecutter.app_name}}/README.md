# What is this?
This project is a boilerplate for a new Python/FastApi project. It has a single router, and a single endpoint for getting books.
# First steps
## Setup
- You first need to create an .env file, and add your database credentials in it.
```bash
cp .env.example .env
```
- Create a new virtual python environment, and install the dependencies.
```bash
pip install -r requirements.txt
```
## Running
- Run project by `uvicorn {{cookiecutter.app_name}}_service.main:app --reload --host=0.0.0.0`
- Check the documentation at http://0.0.0.0:8000/v1/{{cookiecutter.app_name}}/docs

# What is next?
## Routes and API wise
- You probably want to change the directory at `{{cookiecutter.app_name}}_service/api/v1/book_service` to something more meaningful.
- For creating a new service, you can use `{{cookiecutter.app_name}}_service/api/v1/book_service` as a base.
- After creating a new service, include its router inside the `main.py` file
- Your new routers need to inherit from `GenericRouter` class.
- Don't forget to add your database models in `{{cookiecutter.app_name}}_service/models/`. Feel free to remove `book.py`

## Continious integration
- Enter your NPM key at the dockerfile. It is required for creating and deploying the SDK. Search for _NPM_KEY in the file.
- Go add a build trigger at GCP Build dashboard.
- `cloudbuild.yaml` is responsible for build definitions. You can change the pairs under `substitions` as you wish.
  
## Deployment
### Backend side
- Add these lines to your `docker-compose.yml` file which holds your backend services
```yaml
  {{cookiecutter.app_name}}_service:
    image: eu.gcr.io/YOUR_GCP_PROJECT]]/{{cookiecutter.app_name}}:latest
    ports:
      - AN_AVAILABLE_PORT:80
    environment:
      POSTGRE_USER: postgres
      POSTGRE_PASSWORD: password
      POSTGRE_URL: postgre
      POSTGRE_PORT: 5432
      POSTGRE_DBNAME: postgre
      PORT: 80
      BUILD: PROD
      MODULE_NAME: {{cookiecutter.app_name}}_service.main
    restart: always

```
- Run `docker-compose up {{cookiecutter.app_name}}_service -d`

### Nginx configuration
- Add these lines to your `nginx.conf.template` file, inside the `server {` block:
```nginx
# This needs to go to the top
set ${{cookiecutter.app_name}} "${{{cookiecutter.app_name}}_API}";

# This needs to go to the bottom, just above your generic handler.
location ~ /v1/{{cookiecutter.app_name}} {
    proxy_pass ${{cookiecutter.app_name}}$request_uri;
}
```
- Add following environment variable to your nginx's `docker-compose.yml` file:
```yaml
    environment:
        - {{cookiecutter.app_name}}_API=http://ADDRESS_OF_YOUR_BACKEND:THE_AVAILABLE_PORT_YOU_HAVE_SET_IN_DOCKER_COMPOSE
```
- Run `docker-compose up nginx -d`

## Getting the SDK
- If you have done every previous step correctly, you should be able to access your SDK at https://www.npmjs.com/package/@paraboly/{{cookiecutter.app_name}}_sdk. You can remove the `@paraboly` part. For that, edit `publish.sh` and `Dockerfile`.
- You can also install the SDK by running `npm install @paraboly/{{cookiecutter.app_name}}_sdk`