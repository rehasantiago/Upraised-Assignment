# Upraised-Assignment <br/>

## 1.Schema for the database table <br>
![Schema](https://lh3.googleusercontent.com/SO3mb-jdBf0IBy-jZ3Z__VdX4AJkwiOfuUG4bX2oaEIMi6Bwcv0qXuTLCWrYujgFP-XZY_E-SZ6CZ3cgCdMHY4ygDpN2dWnuEZic0qiz3iuA86WV-bFjIIVZVyI85gOzlQGhAgtixbjcbFQaLN4Z5pBCAh9cW9nWR2PWs3zQdVxNpV1P9ySTHhnREW8EhgDELfHFMsbAZzNNOP7yhL7SP_jM-jX5AMQGp-M8X5TT6gpLlYKCw5NCvPTaQ9BiGI--WT22u8UpHAMdxFHo5kZDI2r9oqP3KY2zGpUkarksp-MIsIDMjYxsrv0n7_Sr66vYYUjoP16VihuTtVfgqlp-_kKqOIwNonif8ZRQFfkoQjj5jpDjG1AeRE9Nlml3DC6tbKah1crLOU0ywYTRao8v1UN2NnWj3kAFNFf9h5QeZi0kizcBofCAwm_dBuor7bXLnUAlgmpf5O4BJVh4b7fjzSnch3tfG3fYESnwp-45ON2-SbferWKxN7d7r9KV3zDFFUZ5lI9-IaLKsVQSBl7UWSSwGmffu_vcMlMyUxdBFp3QrNXScc7AR2nnwiOBDCY3I_ih9il0TRVkCy6HXPm5PmsoDfYUOo-B541WkQeMvJ9XoNKOy4QOJasGxlP1wAAOSBW7z__ps4RTmhqW14cYXX1EwpVrq6mIvV9uwYdh3_qXH8BCum_jZzc=w487-h188-no)

## 2.How to run the assignment <br/>
1.Create a virtual environment: `virtualenv p python .`<br/>
2.To start the virtual environment: `source bin/activate`<br/>
3.Installing the dependencies: `pip install -r requirements.txt`<br/>
4.Migrations: `python manage.py makemigrations`, `python manage.py migrate`<br/>
5.Create a superuser: `python manage.py createsuperuser`<br/>
6.Run server: `python manage.py runserver`<br/>

## 3.Input CSV and dumping it into the database
1.You can now open the API in your browser at `http://127.0.0.1:[port]/upload` to upload the csv file and click on upload <br/>
**Below**:*Screenshot of the view*
![View](https://lh3.googleusercontent.com/2ncmFvB7-dmD17S3OjZoiTo-gsyZ28rHGZSVfwXgfyv0ehZOG_qe6s1YodC7XzmDWwhU2yUC0Cbb0QuQm97Gn-39rUPdQk8B3SFjUDOwoJU48VVO8FR5HR-dczJfVB1pW-cEmT4kCbmoH3Cs0Na9KQjZ9uWYtvTjDJGrVQA9DRfM1ZhOVvljsvCMWcnZ-kIBYhRFGRKJb8ydKkN39uGIVg1vlmTajimTPoWW3rHkLh4vCGvDGw5TG5yoz69E7xHMZHxdanSvgY3dIVHtpi5H1c66323kDpUYrfVVMTDEFFisjQzABOcI_sPUI36xL6Li1loFl1_4f3UFYVN-wEPByRvgay5uqxj7KHlMax4Kqi9C10XnO3T2j2N37RLcJPciTgBROpmDmMFS_gOxPW1r-QYBrBqUeI8nxRMk_6ejZnXKWw8ffYwIFKR8Q24QCq_zoBfm9GDgXDobhPoOJk0b8nBLZXCpxv6Aj0unhwiEKoyn_NR4E51wnNcSDXjNn4zdMFPciAVoTkJNPgi_nNuRMdHesR7cze0pLmxfL11kwdl82cMpX-X4hb7CG4hLii7VOqnWw-w0QAvAvKBw_KmKQ-sACaVtdhFTgYEelDWtAzU2tb4rfCzMqvCy1g-eUtWCL6G6SNlipDdvB0wfdKC0o47dAG7x4JHu8OwDoUgfh-V2fnK083OAPYE=w725-h377-no)


## 4.APIS
### 1.Job Search <br/>
1.You can now open the API in your browser at `localhost:[port]/jobs/<value>` <br/>
2.This API takes in the value of the skill or title of the required jobs <br/>
3.It returns a list in which each list item is a dictionary of job<br/>
**Below**:*Screenshot of the API*
![Job Search](https://lh3.googleusercontent.com/wVfDB_-axCCO_PEFv5yxx2viKe87v9DgMvCOdq5s21N1k-kAzP2fdMTCGScSHaPJK0GuALXD-jBm9xDUTsPvHxedkaxbCy8FT8jXYa6xE3Z-eawz935yPw8unROwle62MTqj6PNksbYNdQEWYjMb-304kTnzSfqb3213ndNY0DK3JmXQaRktmT-z1jL9zSJvhfCMllMRCyjb9eFSnKjjST0R6WGL5JBYWVz67noWiyKJ2Azgr_2TMftjqWPIXDf2XH3JZi4neguF9oGmzL1fS9ntqS9LQ5QsvHdxD0YUKQmHuzyYGs6L20R4XpZJ9EkMY55h8NtZYXeb3SpQAxEPLI-EDdNhBQWdmx4638iqeybBFS9BBZsbmrpIZ_BhRIr5lmR3pkt2YHN4NRMezznzXcmLBlnpZ0s-dFeAhHEi5H5f8uSw4vHJXaD4whRjSBgIQWQmgXZJon_JzYhwHJfreYTPRTw2sdgVBkY4y391dEyVkrRxejFCyXmpUzbxIiFoBENspUsuEL5Q8iOpkUdayVNtG3PK94xocSb1lW62w5Kc-flart5yKq_wAPBd_uWdc2m4NNOtqpjQibhTKTJPICbGGe-pDa7eTL0qct8sXgdIHM2427T2PCJh0-QaIfGLBY9OGfE3waMJjpzQb78tjSY6ZzrOMYIOVU9r6rpOxY-2UDQ8dg_BhVg=w874-h467-no)


### 2.Analytics
1.You can now open the API in your browser at `localhost:[port]/startdate/<date>/enddate/<date>` <br/>
2.This API takes in two values, the startdate and enddate which should be in year-month-day-hour-minute-second format<br/>
3.It returns a dictionary with *total jobs*, *jobs grouped by title*, *jobs grouped by company* and *jobs grouped by skills* <br/>
**Below**:*Screenshot of the API*
![Analytics](https://lh3.googleusercontent.com/RT2XjlJauCZ9p1fJgim5kGOdAt6uLeUM1ybbR6Mpp38P4sSHizrk9VhgDHjSLCYYA8aI6oYEtgSlSOuBL2ghnuy82gWs4YQrFi6kOlzmkqBUggh46FbTM80KNWxnHkD6oPcOn0QmmAjiKxls2bFik-RcRP9dh_RNJMxKl9C9TTc4Jhswva1naUX9TmfO0K4JYVtJE5F8a0fXp4YUE5B14DEu4o5vz2D62JQF_XYioi9tf9wMGUmhr2wBc6YnPN03co_QvVAi-KDY_NA83NUXTpQF55ROrGF61MIn0cB3PkrP1nTjSrgyz65bFTtTMm-VKH_BJfLt4hCKsPqdixWLCrloYCMuueo5TRF1UZtCyl_pjkDqenMPhiq9XjG3A9qbVXY-3QPG91bg973xaNwyNpqRL_c0QQR-S9gRmIxYmmdZsoaavFK1hlZ1rFGTIvVK9fLqxRyNBMgTxiTbJbDB-WkRNSSWGrl-x9Qp0PNswTfU5nSBV25sdk51cNuIxH9gzJj5Gx4qemuQ_0gEYIYEVMHFMpqEgDeqbr3a-R4oNdTYteb2pfGSWcOz_9S4yn3HjpirY5EHjz2Lr7AQgt91Do8fJZr61wt7KmPnDGtHD6stBRsYWnVcFvO59GPcXgAXA61mhEfHTe1MOQMOfx4-CrLoo8azkthZBLuJ-yDAmAlWhyTCbz2Cetk=w824-h271-no)
