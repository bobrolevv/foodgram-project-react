# praktikum_new_diplom

django-admin startproject mysite

pip freeze > requirements.txt
pip install -r requirements.txt
pip freeze > requirements.txt
активировать:

    venv\Scripts\activate.bat - для Windows;
    source venv/bin/activate - для Linux и MacOS.

docker build -t backend-img .


docker run --rm -it -p 8000:8000 img
--rm удалить контейнер после отсановки
-it интрактивный терминал

To delete all containers including its volumes use,
docker rm -vf $(docker ps -aq)
To delete all the images,
docker rmi -f $(docker images -aq)

docker stop $(docker ps -qa) && docker rm $(docker ps -qa) && docker rmi -f $(docker images -qa ) && docker volume rm $(docker volume ls -q) && docker network rm $(docker network ls -q)