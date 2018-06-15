from .models import UserProfile


def save_profile(backend, user, response, *args, **kwargs):
    access_token = response['access_token']
    vk_id = response['user_id']


    if not UserProfile.objects.filter(user_id=user.id):
        UserProfile.objects.create(user_id=user.id, token=access_token, vk_id=vk_id)

    else:
        user = UserProfile.objects.get(user_id=user.id)
        if user.token != access_token:
            user.token = access_token
            user.save()
