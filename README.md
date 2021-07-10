#courseapi

This project contains many api end points to access course

First you need to login to access endpoint:

127.0.0.1:8000/rest-api/login

To get all the course added by user:

GET 127.0.0.1:8000/courselist:

TO add course :
POST 127.0.0.1:8000/courselist "name":"xyz", "author":"xyz","date":"YYYY-MM-DD","price":"1000"

To get course by its id:

GET 127.0.0.1:8000/coursedetail/id

To Edit the course:

PUT 127.0.0.1:8000/coursedetail/id "name":"xyz", "author":"xyz","date":"YYYY-MM-DD","price":"1000"

To delete the course:

DELETE 127.0.0.1:8000/coursedetail/id

To Get Wishlist:
GET 127.0.0.1:8000/wishlist

To add wishlist:
POST 127.0.0.1:8000/wishlist "course":" "name":"xyz", "author":"xyz","date":"YYYY-MM-DD","price":"1000" "

These all are the endpoints of api.
