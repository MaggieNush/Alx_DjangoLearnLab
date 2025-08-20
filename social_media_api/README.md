Project Title: Social Media API

Setup: Instructions on how to set up the project (pip install, migrate, runserver).

API Endpoints: For each endpoint, provide the following details:

Endpoint URL: e.g., /api/posts/

Methods: GET, POST, PUT, DELETE

Functionality: What the endpoint does (e.g., "List all posts or create a new post.").

Permissions: What level of access is required (e.g., "Requires Token Authentication for POST, PUT, DELETE.").

Query Parameters: Document pagination (?page=<number>) and filtering (?title=<str>, ?content=<str>).

Example Request: A curl command or a JSON body example.

Example Response: A JSON response body.

Follow/Unfollow Endpoint:

URL: /api/accounts/follow/<int:user_id>/

Method: POST

Description: Toggles the follow status for a user.

Permissions: IsAuthenticated

Example: Provide a curl example or a Postman request screenshot.

Feed Endpoint:

URL: /api/posts/feed/

Method: GET

Description: Returns an aggregated, chronological feed of posts from all users the authenticated user is following.

Permissions: IsAuthenticated

Example: Provide an example of the JSON response.

Like/Unlike Endpoint:

URL: /api/posts/<int:pk>/like/

Method: POST

Description: Toggles the "like" status on a post for the authenticated user. If a like exists, it is removed; otherwise, a new like is created.

Permissions: IsAuthenticated

Example: Provide a curl example for the POST request.

Notifications Endpoint:

URL: /api/notifications/

Method: GET

Description: Retrieves a list of all notifications for the authenticated user, ordered chronologically.

Permissions: IsAuthenticated

Example: Provide an example of the JSON response body showing a liked notification.