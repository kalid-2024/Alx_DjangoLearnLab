# Advanced API Project

## Book API Endpoints
- **GET /api/books/** → List all books
- **GET /api/books/<id>/** → Retrieve a book by ID
- **POST /api/books/create/** → Create a new book (requires authentication)
- **PUT /api/books/update/<id>/** → Update a book (requires authentication)
- **DELETE /api/books/delete/<id>/** → Delete a book (requires authentication)

### Permissions
- Public: List & Retrieve
- Authenticated Users: Create, Update, Delete