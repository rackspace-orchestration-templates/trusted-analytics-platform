from fabric.api import env, task
from envassert import detect
from hot.utils.test import get_artifacts

@task
def artifacts():
    env.platform_family = detect.detect()
    get_artifacts()
