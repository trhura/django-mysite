Steps to setup the project :

    0) fork the repository for your use. 

    1) make sure pip (python module) is installed globally (http://www.pip-installer.org/en/latest/installing.html#installing-globally)
    
    2) Install virtualenv (python module, see https://pypi.python.org/pypi/virtualenv) - 
      $> pip install virtualenv

    3) install the project repository
      $> cd path/to/some_folder
      $> git clone <forked_path>
    
    4) install the inkbulb dependencies (these steps will download all thirdparty modules needed, may take 5-10 mins)
      $> cd path/to/some_folder/
      $> virtualenv mysite_env
      $> source mysite_env/bin/activate
      (mysite_env)$> cd inkbulb/
      (mysite_env)$> pip install -r requirements.txt
    
    5) To start the local webserver, this should start the application on 8000 port
      (mysite_env)$> manage.py runserver
    
    6) Goto localhost:8000, to see the application
    
    go to admin (username = admin / password = admin):
    http://127.0.0.1:8000/admin/
    
    to see list of problems
    http://127.0.0.1:8000/problems/