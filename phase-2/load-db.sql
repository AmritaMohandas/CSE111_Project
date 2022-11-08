-- SQLite

.mode "csv"
.separator ","
.headers off
.import 'data/books.csv' books
.import 'data/authors.csv' authors
.import 'data/booksauthors.csv' booksauthors
.import 'data/genres.csv' genres
.import 'data/booksgenres.csv' booksgenres