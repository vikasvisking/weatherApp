
# WeatherApp
It is a simple Django Rest Framework project where user can fetch data from a particular url, save it to the designed models. Also u can view the data saved in json format.

# Installation

(these steps are for ubuntu)

1)Install Python3 or cheak ur python version by :-  $ python3 --version.
2)Install pip or upgrade it to latest version by :- ~$ python3 -m pip3 install --upgrade pip
3)install virtual enviroment  : ~$ sudo pip install virtualenv
4)Create virtual enviroment by:- ~$ virtualenv myprojectenv
5)Activate the virtual enviroment:- ~$ source myprojectenv/bin/activate
6)clone the respository by command:- git clone https://github.com/vikasvisking/weatherApp.git
7)move inside the cloned folder i.e weatherApp by:- cd weatherApp
8)install requirements:- pip3 install -r requirements.txt
9)create migration by running the following command: ~$ python3 manage.py makemigrations
10)run : ~$ python3 manage.py migrate
11)un development server : ~$ python manage.py runserver

the application has been successfully deployed on the local.

# Use

* TO store data in database
1) run :-  ~$ python manage.py storedata

* To implement Http Get request,
1)the get request accepts 4 parameters i.e startDate, lastDate, metric, location.
  so the format of the url request should be like this:

  http://localhost:8000?startDate=1910-02&lastDate=2000-02&metric=Rainfall&location=England

2) startDate and endDate should be in the following format: 1910-02 (no need to provide date)
3)Value of location should be one out of these:  'UK', 'England', 'Scotland', 'Wales'
4)Value of metric should be one out of these: 'Tmax' , 'Tmin', 'Rainfall' 

