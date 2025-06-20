
FROM jupyterhub/jupyterhub:4.0.2

USER root

# 安装依赖
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        postgresql-client \
        build-essential \
        python3-dev && \
    rm -rf /var/lib/apt/lists/*

# 复制requirements并安装Python包
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# 复制配置文件
COPY config/ /srv/jupyterhub/config/

# 创建用户和设置权限
RUN useradd -m -s /bin/bash jovyan && \
    mkdir -p /srv/content && \
    chown -R jovyan:jovyan /srv/content

# 设置工作目录
WORKDIR /srv/jupyterhub

# 启动命令
CMD ["jupyterhub", "-f", "/srv/jupyterhub/config/jupyterhub_config.py"]
