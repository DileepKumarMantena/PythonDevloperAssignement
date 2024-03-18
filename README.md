
---

# Django REST Framework CRUD APIs with Swagger Documentation

I'm pleased to introduce a robust set of CRUD APIs developed using Django REST Framework, facilitating seamless management of entities pertaining to Books and Reviews. Within this system, each entity boasts a suite of four fundamental APIs, encompassing Create, Retrieve, Update, and Delete operations.

For seamless access to these APIs, authentication is imperative. By creating a superuser account, you can effortlessly authenticate your access. Execute the following command to initiate the process:

```
python3 manage.py createsuperuser
```

Upon execution, this command prompts the creation of a unique username and password, thereby granting authorized access to the APIs.

Furthermore, to enhance user experience and streamline the API interaction process, Swagger integration has been meticulously implemented. This integration not only furnishes comprehensive documentation but also augments the visual presentation of the APIs, ensuring a user-friendly and intuitive browsing experience.

---

```
Books Crud Api's
```
1.createBookRecord(): This API function is utilized to insert a new book record into the database.
2.removeBookRecord(): This API function is employed to delete a specific book record from the database.
3.retrieveBooks(): This API function is employed to fetch either a single book record or all book records from the database.
4.updateBookRecord(): This API function is employed to modify the data within an existing book record in the database.

```
Review Crud Api's 
```
1.createReviewRecord(): This API function is utilized to insert a new review record into the database.
2.removeReviewRecord(): This API function is employed to delete a specific review record from the database.
3.retrieveReviews(): This API function is employed to fetch either a single review record or all review records from the database.
4.updateReviewRecord(): This API function is employed to modify the data within an existing review record in the database.

Certainly, here's a more professional version:

To execute the APIs:

1. Navigate to the project directory.
2. Execute the following commands for database migrations:

```
python3 manage.py makemigrations
```

```
python3 manage.py migrate
```

These commands will generate the necessary database tables.

3. After migration, initiate the application by running:

```
python3 manage.py runserver
```

This command will start the application, allowing the APIs to be accessed.