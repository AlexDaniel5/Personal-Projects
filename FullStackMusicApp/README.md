To Create Folders:
- django-admin startproject <name>
- cd into project
- django-admin startapp <name>

To Start Web Server:
- python .\manage.py makemigrations
- python .\manage.py migrate
- python .\manage.py runserver
- Open another terminal and go into the path folder MusicController/frontend
- Run the command npm run dev

Important Notes:
- You only have to run the server once and django will automatically make updates to the server as you edit the code
- If we get a url that is blank call the main function. To create directories in the url make the url pattern first parameter non-blank,
ex. /home. If we do admin/ then whatever directory were in going back one will direct us to that page.
- Whatever is in views and has a request parameter will return a response; whenever you have a webserver there will be an incoming request which goes to an endpoint which returns a response to the sender in a format such as html or json
