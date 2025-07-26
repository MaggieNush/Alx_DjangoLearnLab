Permissions Setup:
- Book model has custom permissions: can_create, can_edit, can_delete
- These are enforced in views using @permission_required decorator.
- Users are assigned to groups (Editors, Creators, Deleters) in Django Admin.
- Only users in correct groups can access certain views.

How to Test:
1. Create users.
2. Assign them to groups with relevant permissions.
3. Try to access views: create, edit, delete.
4. Unauthorized users will get a 403 Forbidden.
