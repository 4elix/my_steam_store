from django import template
from pages.models import CommentLike


register = template.Library()


@register.simple_tag()
def count_like_dislike(user, comment_id):
    return CommentLike.objects.filter(user=user, comment_id=comment_id)
