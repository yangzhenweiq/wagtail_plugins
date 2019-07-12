import os
from glob import glob

HERE = os.path.abspath(os.path.dirname(__file__))

config = { 
    "add": {
        "MYSQL_PASSWORD": "{{ 8|random_string }}",
    },  
    "defaults": {
        "HOST": "wagtail.{{ LMS_HOST }}",
        "DOCKER_REGISTRY": "yangzhenweiq",
        "DOCKER_IMAGE_SERVER": "yangzhenweiq/wagtailtest001:latest",
        "MYSQL_DATABASE": "wagtail",
        "MYSQL_USERNAME": "saladbar",
    },
}

templates = os.path.join(HERE, "templates")

hooks = {
    "init": ["mysql-client", "wagtail"],
    "build-image": {"wagtail": "{{ WAGTAIL_DOCKER_IMAGE_SERVER }}"} ,
    "remote-image": {"wagtail": "{{ WAGTAIL_DOCKER_IMAGE_SERVER }}"}
}

def patches():
    all_patches = {}
    for path in glob(os.path.join(HERE, "patches", "*")):
        with open(path) as patch_file:
            name = os.path.basename(path)
            content = patch_file.read()
            all_patches[name] = content
    return all_patches
