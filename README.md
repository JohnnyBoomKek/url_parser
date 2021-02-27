URL parser


The service is designed to parse any given web-page for all of its links.
The initial idea also included getting domain info about every given link using api.domainsdb.info asynchronously. 
Unfortunately due to the API not giving expected results it's just a url parser. 

To give the app a shot on your local machine you are going to have to:

- Make sure you have python3 installed

- clone this repo

- create a virtual environment with:
```
    python -m venv venvname 
    (venv being the name of your env.) 
```
- on UNIX based systems you are going to need to activate your venv: 

```
*source venvname/bin/activate*
```

 - locate to the url_parser folder 
 ```
  cd url_parser/
 ``` 
- start the app
```
  python manage.py runserver
 ``` 
  
 
