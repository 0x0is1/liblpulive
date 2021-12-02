import requests
import config

API_URL = "https://lpulive.lpu.in/fugu-api/api"

class urls:
    conversation = "/conversation"
    chat = "/chat"
    user = "/user"
    notification = "/notification"

headers = {
    "authority": "lpulive.lpu.in",
    "domain": "lpu.in",
    "device_type": "WEB",
    "app_version": "1.0.0"
}

def get_message(channel_id, en_user_id, page_start=1):
    url = f"{API_URL}{urls.conversation}/getMessages?channel_id={channel_id}&en_user_id={en_user_id}&page_start={page_start}"
    resp = requests.get(url, headers=headers)
    return resp.json()

def get_starred_message(channel_id, en_user_id, page_start=1):
    url = f"{API_URL}{urls.conversation}/getStarredMessages?channel_id={channel_id}&en_user_id={en_user_id}&page_start={page_start}"
    resp = requests.get(url, headers=headers)
    return resp.json()

def get_group_info(channel_id, en_user_id, user_count=50):
    url = f"{API_URL}{urls.chat}/getGroupInfo?channel_id={channel_id}&en_user_id={en_user_id}&get_data_type=MEMBERS&user_page_start={user_count}"
    resp = requests.get(url, headers=headers)
    return resp.json()

def get_user_info(fuid, wsid, access_token):
    url = f"{API_URL}{urls.user}/getUserInfo?fugu_user_id={fuid}&workspace_id={wsid}"
    headers["access_token"] = access_token
    resp = requests.get(url, headers=headers)
    return resp.json()

def login_via_access_token(lpu_access_token, access_token):
    url = "{API_URL}{urls.user}/v1/loginViaAccessToken"
    headers["content-type"] = "application/json"
    headers["access_token"] = access_token
    data = '{"lpu_access_token":"'+lpu_access_token+'","time_zone":330}'
    resp = requests.post(url, headers=headers, data=data)
    return resp.json()

def login(username, password):
    url = "{API_URL}{urls.user}/v1/userLogin"
    headers["content-type"] = "application/json"
    data = '{"password":"'+password+'","username":"' + \
        username+'","domain":"lpu.in","time_zone":330}'
    resp = requests.post(url, headers=headers, data=data)
    return resp.json()

def get_notifications(en_user_id, page_start=1):
    url = f"{API_URL}{urls.notification}/getNotifications?en_user_id={en_user_id}&page_start={page_start}"
    resp = requests.get(url, headers=headers)
    return resp.json()

def getWorkspaceDetails():
    url = f"{API_URL}/workspace/getWorkspaceDetails?workspace=spaces"
    resp = requests.get(url, headers=headers)
    return resp.json()

def get_conversations(en_user_id, page_start=1):
    url = f"{API_URL}{urls.conversation}/getConversations?en_user_id={en_user_id}&page_start={page_start}"
    resp = requests.get(url, headers=headers)
    return resp.json()
