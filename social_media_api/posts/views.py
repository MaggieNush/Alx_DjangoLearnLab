from rest_framework import permissions, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework import generics

class PostViewSet(viewsets.ModelViewSet):
    # Defines the set of objects the viewset can operate on
    queryset = Post.objects.all()

    # The serializer to use for converting data
    serializer_class = PostSerializer

    # IsAuthenticatedOrReadOnly: Allows any user to view, but only authenticated users to write.
    # IsOwnerOrReadOnly: Ensures that a user can only edit/delete their own posts.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    # The filter backend to use for filtering the queryset
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'author', 'content']

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


class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated] # Only authenticated users can see their feed

    def get_queryset(self):
        # We get the list of users the current user is following.
        following_users = self.request.user.following.all()
        
        # We filter posts to include only those where the author is in the list of followed users.
        # We order them by creation date, from newest to oldest.
        queryset = Post.objects.filter(author__in=following_users).order_by('-created_at')
        
        return queryset