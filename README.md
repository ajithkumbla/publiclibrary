# publiclibrary
django public library
Install virtualenv

virtualenv is a virtual environment where you can install software and Python packages in a contained development space, which isolates the installed software and packages from the rest of your machine’s global environment. This convenient isolation prevents conflicting packages or software from interacting with each other.

To install virtualenv, we will use the pip3 command, as shown below:

pip3 install virtualenv

Once it is installed, run a version check to verify that the installation has completed successfully:

virtualenv --version

While in the server’s home directory, we have to create the directory that will contain our Django application. Run the following command to create a directory called django-apps, or another name of your choice. Then navigate to the directory.

mkdir django-apps

cd django-apps 

While inside the django-apps directory, create your virtual environment. Let’s call it env.

virtualenv env
Now, activate the virtual environment with the following command:

. env/bin/activate

creating a django project

 django-admin startproject projectname

cd projectname

creating app

 python3 manage.py startapp appname

development server

 python3 manage.py runserver

# ABOUT PUBLIC LIBRARY

admins can login to the system by entering username and password and can add new libraries by providing name,address and the location of the library.they also can publish the reviews provided by the user by approving it.

user can login to the if user name and password is taken else can register as new user by providing neccessary details.They can view the libraries those are added by the admin and can send reviews of the library

guest user can check list of libraries and also reviews.

# creating superuser in django

python3 manage.py createsuperuser


