# Permissions and Groups Setup

## Custom Permissions
Defined in `Book` model (`models.py`):
- `can_view`: Can view book entries
- `can_create`: Can create new books
- `can_edit`: Can edit books
- `can_delete`: Can delete books

## Groups
- **Viewers** → can_view
- **Editors** → can_view, can_create, can_edit
- **Admins** → all permissions

## Enforced in Views
- `book_list` → requires `can_view`
- `add_book` → requires `can_create`
- `edit_book` → requires `can_edit`
- `delete_book` → requires `can_delete`

Users must be assigned to a group with the right permissions.
