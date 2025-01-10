import requests
import json
import base64
# Your GitHub API key token
api_key = 'sjhfjhsjfhjhj_hh346GBkjshjhsdh'
# The username
username = 'username'
file_path = 'list_types.java'
# repository name
repo = 'repo_name'
# GitHub API URL of file to get data 
file_path = 'file path'
url = f'https://api.github.com/repos/{username}/{repo}/contents/{file_path}'
# Headers for the request
headers = { 
    'Authorization': f'token {api_key}',
    'Accept': 'application/vnd.github.v3+json'
}
response = requests.get(url, headers=headers)    # Make the GET request
if response.status_code == 200:                  # Check if the request was successful
    file_content = response.json()
    #  file text data 
    decoded_content = base64.b64decode(file_content['content']).decode('utf-8')
    print(f"File Content:\n{decoded_content}")
else:
    print(f"Failed to retrieve repositories: {response.status_code}")
