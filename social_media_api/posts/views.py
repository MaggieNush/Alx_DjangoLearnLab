from rest_framework import permissions, viewsets
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    # Defines the set of objects the viewset can operate on
    queryset = Post.objects.all()

    # The serializer to use for converting data
    serializer_class = PostSerializer

    # IsAuthenticatedOrReadOnly: Allows any user to view, but only authenticated users to write.
    # IsOwnerOrReadOnly: Ensures that a user can only edit/delete their own posts.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    # The method is called when a new object is created
    # Sets the author of the post to the currently authenticated user
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    # Defines the set of objects the viewset can operate on
    queryset = Comment.objects.all()

    # The serializer to use for converting data
    serializer_class = CommentSerializer

    # IsAuthenticatedOrReadOnly: Allows any user to view, but only authenticated users to write.
    # IsOwnerOrReadOnly: Ensures that a user can only edit/delete their own comments.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    # The method is called when a new object is created
    # Sets the author of the comment to the currently authenticated user
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)