from rest_framework import generics
from .models import Discussion, Comment, Like
from .serializers import DiscussionSerializer, CommentSerializer, LikeSerializer
from django.utils import timezone

#  DISSCUSSION views

class DiscussionCreateView(generics.CreateAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer
    
    # def perform_create(self, serializer):
    #     """
    #     Save the user and current time when creating a new Discussion.
    #     """
    #     request = self.request
    #     if request.user and request.user.is_authenticated:
    #         serializer.save(user=request.user, created_on=timezone.now())
    #     else:
    #         # Handle the case where the user is not authenticated, if needed
    #         serializer.save(created_on=timezone.now())


class DiscussionUpdateView(generics.UpdateAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer
    


class DiscussionDeleteView(generics.DestroyAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer
    lookup_field = 'pk'


class DiscussionListByTagsView(generics.ListAPIView):
    serializer_class = DiscussionSerializer

    def get_queryset(self):
        tags = self.request.query_params.get("tags", None)
        if tags:
            return Discussion.objects.filter(hashtags__contains=tags)
        return Discussion.objects.all()


class DiscussionSearchByTextView(generics.ListAPIView):
    serializer_class = DiscussionSerializer

    def get_queryset(self):
        # text = self.kwargs.get("text", None)
        text = self.request.query_params.get("text", None)
        # hashtags = self.request.query_params.get("hashtags", "test_hashtags")
        # hashtags = self.kwargs.get("hashtags", None)    
        print(text)
        if text:
            print(str(Discussion.objects.filter(text__icontains=text).query))
            return Discussion.objects.filter(text__icontains=text)
        # TODO Add search by hashtags
        # elif hashtags:
        #     hashtags_list = [tag.strip() for tag in hashtags.split(',')]
        #     print(hashtags_list)
        #     # print(str(Discussion.objects.filter(hashtags__icontains=hashtags_list).query))
        #     return Discussion.objects.filter(hashtags__icontains=hashtags_list)
        return Discussion.objects.none()


# COMMENT views

class CommentCreateView(generics.CreateAPIView):
    
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentUpdateView(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDeleteView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


#  LIKE views

class LikeCreateView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class LikeDeleteView(generics.DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
