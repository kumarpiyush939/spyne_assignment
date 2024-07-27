from django.urls import path
from .views import (
    DiscussionCreateView,
    DiscussionUpdateView,
    DiscussionDeleteView,
    DiscussionListByTagsView,
    DiscussionSearchByTextView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
    LikeCreateView,
    LikeDeleteView,
)


urlpatterns = [
    path(
        "",
        DiscussionListByTagsView.as_view(),
        name="discussion-list-by-tags",
    ),
    path(
        "create/", DiscussionCreateView.as_view(), name="discussion-create"
    ),
    path(
        "<int:pk>/update/",
        DiscussionUpdateView.as_view(),
        name="discussion-update",
    ),
    path(
        "<int:pk>/delete/",
        DiscussionDeleteView.as_view(),
        name="discussion-delete",
    ),
    path(
        "search/",
        DiscussionSearchByTextView.as_view(),
        name="discussion-search-by-text",
    ),
]


# COMMENT urls

urlpatterns += [
    path("comments/create/", CommentCreateView.as_view(), name="comment-create"),
    path(
        "comments/<int:pk>/update/", CommentUpdateView.as_view(), name="comment-update"
    ),
    path(
        "comments/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"
    ),
]


#  LIKE urls


urlpatterns += [
    path("likes/create/", LikeCreateView.as_view(), name="like-create"),
    path("likes/<int:pk>/delete/", LikeDeleteView.as_view(), name="like-delete"),
]
