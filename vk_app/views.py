from django.shortcuts import render
import pdb
import requests
import json


def home(request):
    return render(request, 'index.html', {})


def settings(request):
    token = request.user.userprofile.token
    vk_id = request.user.userprofile.vk_id
    friends = requests.get('https://api.vk.com/method/friends.get?user_ids={}&count=5&order=random&fields=nickname,photo_50&access_token={}&v=6'.format(vk_id, token))
    friends = json.loads(friends.text)
    friends = friends['response']['items']
    return render(request, 'profile.html', {'friends': friends})