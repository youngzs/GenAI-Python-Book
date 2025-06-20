
# JupyterHub配置文件
import os

# 基础配置
c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.port = 8000

# 数据库配置
c.JupyterHub.db_url = 'postgresql://jupyterhub:educationhub123@postgres:5432/jupyterhub'

# 认证配置 - 使用本地用户认证
c.JupyterHub.authenticator_class = 'jupyterhub.auth.DummyAuthenticator'
c.DummyAuthenticator.password = "python123"

# 管理员用户
c.Authenticator.admin_users = {'admin', 'teacher'}

# Spawner配置
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.image = 'jupyter/datascience-notebook:latest'
c.DockerSpawner.remove = True
c.DockerSpawner.network_name = 'python-edu-network'

# 容器配置
c.DockerSpawner.volumes = {
    '/srv/content': '/home/jovyan/course-content',
    '/data/hub/{username}': '/home/jovyan/work'
}

# nbgrader配置
c.JupyterHub.services = [
    {
        'name': 'nbgrader-formgrader',
        'url': 'http://127.0.0.1:9999',
        'command': [
            'python', '-m', 'nbgrader', 'formgrader',
            '--port=9999',
            '--no-browser'
        ],
        'environment': {
            'NBGRADER_CONFIG_FILE': '/srv/jupyterhub/config/nbgrader_config.py'
        }
    }
]

# 日志配置
c.JupyterHub.log_level = 'INFO'
