Deploy guide
============

To deploy:

- Checkout source code to /srv/{{cookiecutter.repo_name}}
- Create virtualenv 'venv' and install production requirements
{%- if cookiecutter.is_react_project == 'y' %}
- Make sure you have node>=0.12.0 (see: https://nodesource.com/blog/nodejs-v012-iojs-and-the-nodesource-linux-repositories)
{%- else %}
- Install yuglify, if you plan to use js/css compression ('npm -g install yuglify' to install globally){% endif %}

- Create {{cookiecutter.repo_name}}/media/ dir and ensure it's writable by server process (usually this means www-data user)
- Create database and user
- Add local settings
- syncdb, migrate, collectstatic
{%- if cookiecutter.is_react_project == 'y' %}
- npm run build{% endif %}

- Copy gunicorn.conf to /etc/init/gunicorn-{{cookiecutter.repo_name}}.conf
- Copy nginx.conf to /etc/nginx/sites-enabled/{{cookiecutter.repo_name}}.conf
- start the service and reload nginx


Files in this directory:

- gunicorn.conf - upstart script to start the gunicorn server process.
- nginx.conf - Nginx site configuration
