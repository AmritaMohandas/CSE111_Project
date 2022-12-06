-- SQLite

.mode "csv"
.separator ","
.headers off
.import 'data/books.csv' books
.import 'data/authors.csv' authors
.import 'data/booksauthors.csv' booksauthors
.import 'data/genres.csv' genres
.import 'data/booksgenres.csv' booksgenres
.import 'data/publishers.csv' publishers
.import 'data/bookspublishers.csv' bookspublishers
.import 'data/format.csv' format
.import 'data/users.csv' users
.import 'data/readingstatus.csv' readingstatus
.import 'data/ratings.csv' ratings