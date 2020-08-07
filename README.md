# django-task
In this project , i have created REST APIs based on Django with PostgreSQL database. 
It contains following things :-

Three user levels : 1. Super-admin, 2. Teacher, 3. Student.

http://127.0.0.1:8000/admin/login/?next=/admin/


![dj-1](https://user-images.githubusercontent.com/47775251/89604819-ae067780-d889-11ea-9ce3-d0ed385cda31.png)

![dj-2](https://user-images.githubusercontent.com/47775251/89604955-fc1b7b00-d889-11ea-8191-18b7f15c49f8.png)



Teacher can able to list all the students. Here is the permission given to the teacher by super user 'admin'.

![dj-3](https://user-images.githubusercontent.com/47775251/89605141-751ad280-d88a-11ea-8e9a-f3d82dd65779.png)



Admin can be able to list every user in the database. Admin can add as many user. Admin can make new groups. 

![dj-4](https://user-images.githubusercontent.com/47775251/89605340-e8bcdf80-d88a-11ea-9e38-4c85c10c9766.png)




 I have used JWT authentication in this project.
 JSON Web Token is an open standard for securely transferring data within parties using a JSON object. 
 JWT is used for stateless authentication mechanisms for users and providers, this means maintaining session is on the client-side instead of storing sessions on the server.
 we need to authenticate and obtain the token.
 
 Student Login using JWT Authentication : http://127.0.0.1:8000/api-auth/login/?next=/student/
 
 Teacher Login using JWT Authentication : http://127.0.0.1:8000/api-auth/login/?next=/teacher/
 
 
 
 I have used the user name for JWT Authentication as 'admin' and password- 'nishi123'.
 
 ![dj-5](https://user-images.githubusercontent.com/47775251/89607065-405d4a00-d88f-11ea-8ad4-460658bb2caa.png)
 
 
Student List :- Using Restful api in django.

Restful api for teacher using django - http://127.0.0.1:8000/student/



![dj-7](https://user-images.githubusercontent.com/47775251/89607766-ea89a180-d890-11ea-8c74-e4401c61dbfc.png)



 
 
 
 
 
 Teacher List :- Using Restful api in django.
 
 Restful api for teacher using django - http://127.0.0.1:8000/teacher/
 
 ![dj-6](https://user-images.githubusercontent.com/47775251/89607273-b8c40b00-d88f-11ea-8533-d110fde7a923.png)
 
 
 
 
 
 
