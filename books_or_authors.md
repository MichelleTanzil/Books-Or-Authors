Query: Create 5 books with the following names: C Sharp, Java, Python, PHP, Ruby
Book.objects.create(title="C Sharp", desc="A book about C Sharp")
Book.objects.create(title="Java", desc="A book about Java")
Book.objects.create(title="Python", desc="A book about Python")
Book.objects.create(title="PHP", desc="A book about PHP")
Book.objects.create(title="Ruby", desc="A book about Ruby")

Query: Create 5 different authors: Jane Austen, Emily Dickinson, Fyodor Dostoevksy, William Shakespeare, Lau Tzu
Author.objects.create(first_name="Jane", last_name="Austen")
Author.objects.create(first_name="Emily", last_name="Dickinson")
Author.objects.create(first_name="Fyodor", last_name="Dostoevksy")
Author.objects.create(first_name="William", last_name="Shakespeare")
Author.objects.create(first_name="Lau", last_name="Tzu")

Add a new text field in the authors table called 'notes'.
notes = models.TextField()
option 1
"notes_abt_this_book"

Create and run the migration files to update the table in your database.

Query: Change the name of the C Sharp book to C#
C = Book.objects.get(id=1)
C.title = "C#"
C.save()

Query: Change the first name of the 4th author to Bill
Bill = Author.objects.get(id=4)
Bill.first_name = "Bill"
Bill.save()

Query: Assign the first author to the first 2 books
jane = Author.objects.get(id=1)
book1 = Book.objects.get(id=1)
book2 = Book.objects.get(id=2)
<!-- Solution 1 -->
jane.books.add(book1)
jane.books.add(book2)

<!-- Solution 2 -->
book1.authors.add(jane)
book2.authors.add(jane)

Query: Assign the second author to the first 3 books
emily = Author.objects.get(id=2)
book3 = Book.objects.get(id=3)

<!-- Solution 1 -->
emily.books.add(book1)
emily.books.add(book2)
emily.books.add(book3)

<!-- Solution 2 -->
book1.authors.add(emily)
book2.authors.add(emily)
book3.authors.add(emily)

Query: Assign the third author to the first 4 books
fyodor = Author.objects.get(id=3)
book4 = Book.objects.get(id=4)
<!-- Solution 1 -->
fyodor.books.add(book1)
fyodor.books.add(book2)
fyodor.books.add(book3)
fyodor.books.add(book4)

<!-- Solution 2 -->
book1.authors.add(fyodor)
book2.authors.add(fyodor)
book3.authors.add(fyodor)
book4.authors.add(fyodor)

Query: Assign the fourth author to the first 5 books (or in other words, all the books)
bill = Author.objects.get(id=4)
book5 = Book.objects.get(id=5)

<!-- Solution 1 -->
bill.books.add(book1)
bill.books.add(book2)
bill.books.add(book3)
bill.books.add(book4)
bill.books.add(book5)

<!-- Solution 2 -->
book1.authors.add(bill)
book2.authors.add(bill)
book3.authors.add(bill)
book4.authors.add(bill)
book5.authors.add(bill)

Query: Retrieve all the authors for the 3rd book
book3.authors.all()

Query: Remove the first author of the 3rd book
book3.authors.remove(emily)

Query: Add the 5th author as one of the authors of the 2nd book
lau = Author.objects.get(id=5)

<!-- Solution 1 -->
lau.books.add(book2)

<!-- Solution 2 -->
book2.authors.add(lau)

Query: Find all the books that the 3rd author is part of
fyodor.books.all()

Query: Find all the authors that contributed to the 5th book
book5.authors.all()