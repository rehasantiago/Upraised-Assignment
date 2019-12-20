# Upraised-Assignment <br/>

## 1.Schema for the database table <br>
![Schema](/images/Selection_005.png)

## 2.How to run the assignment <br/>
1.Create a virtual environment: `virtualenv -p python .`<br/>
2.To start the virtual environment: `source bin/activate`<br/>
3.Installing the dependencies: `pip install -r requirements.txt`<br/>
4.Migrations: `python manage.py makemigrations`, `python manage.py migrate`<br/>
5.Create a superuser: `python manage.py createsuperuser`<br/>
6.Run server: `python manage.py runserver`<br/>

## 3.Input CSV and dumping it into the database
1.You can now open the API in your browser at `http://127.0.0.1:[port]/upload` to upload the csv file and click on upload <br/>
**Below**:*Screenshot of the view*
![View](/images/upload.png)


## 4.APIS
### 1.Job Search <br/>
1.You can now open the API in your browser at `localhost:[port]/jobs/<value>` <br/>
2.This API takes in the value of the skill or title of the required jobs <br/>
3.It returns a list in which each list item is a dictionary of job<br/>
**Below**:*Screenshot of the API*
![Job Search](/images/job.png)


### 2.Analytics
1.You can now open the API in your browser at `localhost:[port]/startdate/<date>/enddate/<date>` <br/>
2.This API takes in two values, the startdate and enddate which should be in year-month-day-hour-minute-second format<br/>
3.It returns a dictionary with *total jobs*, *jobs grouped by title*, *jobs grouped by company* and *jobs grouped by skills* <br/>
**Below**:*Screenshot of the API*
![Analytics](/images/analytics.png)
