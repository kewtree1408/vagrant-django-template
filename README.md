django-admin.py startproject --template https://github.com/kewtree1408/vagrant-django-template/master --name=Vagrantfile myproject
cd myproject
vagrant up
vagrant ssh
  (then, within the SSH session:)
./manage.py runserver 0.0.0.0:8001

This will make the app accessible on the host machine as http://localhost:8111/ .
