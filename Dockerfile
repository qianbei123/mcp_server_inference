FROM python:3.10.18-slim-bookworm

# Sync the project into a new environment, asserting the lockfile is up to date
WORKDIR /app

# 同步市区时间
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo "Asia/Shanghai" > /etc/timezone

# 将当前目录下的所有文件复制到容器的/app目录中
COPY . /app
RUN chmod +x /app/run.sh
RUN chmod +x /app/run_gas_properties_service.sh
RUN chmod +x /app/run_molecule_search_service.sh
RUN chmod +x /app/run_pocket_disease_service.sh
RUN pip install uv -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple
RUN uv sync --locked
RUN . .venv/bin/activate

EXPOSE 5003 5004 5005 5006

# # 容器启动时执行的命令，首先同步时间，然后运行应用程序
# CMD ["./run.sh"]
