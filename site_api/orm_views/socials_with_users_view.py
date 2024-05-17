from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from django.http import JsonResponse
from site_api.domain.user_may_to_many import UserSocialMedia

class SocialsWithUsersView(ViewSet):
    def get(self, request):
        socials = UserSocialMedia.objects.select_related('user').values(
            'id',
            'user__name',
            'user__username',
            'social__name',
            'social__username',
            'social__link'
        )

        socials_array = []
        for social in socials:
            socials_array.append({
                'user': social['user__name'],
                'user_username': social['user__username'],
                'social_name': social['social__name'],
                'social_username': social['social__username'],
                'link': social['social__link']
            })

        return JsonResponse({
            'socials': socials_array,
            'total_medias': len(socials_array)
        })

    @action(methods=['get'], detail=False, url_name='get_by_username')
    def get_by_username(self, request, username):
        print(request)
        print(username)

        return Response({'socials': username})