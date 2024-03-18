from django.db import models
from django.core.validators import RegexValidator,MinLengthValidator, MaxLengthValidator,MinValueValidator,MaxValueValidator




class BooksModel(models.Model):
    title_regex = RegexValidator(regex=r'^(?=.{3,12}$)(?![_.])(?!.*[_.]{2})[a-zA-Z]+(?<![_.])$',
                                     message="title"
                                             "must string and should not be less than 3 and greater than 12")
    author_regex = RegexValidator(regex=r'^(?=.{3,12}$)(?![_.])(?!.*[_.]{2})[a-zA-Z]+(?<![_.])$',
                                    message="lastname "
                                            "must string and should not be less than 3 and greater than 12")
    date_regex = RegexValidator(regex=r'^\d{4}-\d{2}-\d{2}$',message="Date must be in the format YYYY-MM-DD")
    Title = models.CharField(validators=[title_regex], max_length=30)
    Author = models.CharField(validators=[author_regex], max_length=30)
    Date_Field = models.DateField(validators=[date_regex])    
    objects = models.Manager

    class Meta:
        db_table = "Books_Table"


class ReviewModel(models.Model):
    Review_Text = models.TextField(validators=[
        MinLengthValidator(50, message='Review must be at least 50 characters long.'),
        MaxLengthValidator(1000, message='Review cannot exceed 1000 characters.')
    ])
    Rating = models.IntegerField(
        validators=[
            MinValueValidator(0, message='Integer must be greater than or equal to 0.'),
            MaxValueValidator(100, message='Integer must be less than or equal to 100.')
        ]
    )
    BookId = models.ForeignKey(BooksModel, related_name="BookId", on_delete=models.CASCADE)
    objects = models.Manager
    class Meta:
        db_table = "Review_Table"


