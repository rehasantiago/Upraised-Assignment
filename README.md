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
**Below**:*Screenshot of the API*

### 2.Analytics
1.You can now open the API in your browser at `localhost:[port]/startdate/<date>/enddate/<date>` <br/>
2.This API takes in two values, the startdate and enddate which should be in year-month-day-hour-minute-second format<br/>
**Below**:*Screenshot of the API*
