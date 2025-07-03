#!/bin/bash
set -e

# 给启动脚本添加执行权限
chmod +x run_pocket_disease_service.sh
chmod +x run_molecule_search_service.sh
chmod +x run_gas_properties_service.sh

echo "启动所有服务..."

# 启动口袋-分子-疾病服务
echo "启动口袋-分子-疾病服务 (端口5004)..."
./run_pocket_disease_service.sh &

# 启动分子搜索服务
echo "启动分子搜索服务 (端口5005)..."
./run_molecule_search_service.sh &

# 启动气体特性预测服务
echo "启动气体特性预测服务 (端口5006)..."
./run_gas_properties_service.sh &

echo "所有服务已启动!"
echo "- 口袋-分子-疾病服务运行在 http://0.0.0.0:5001"
echo "- 分子搜索服务运行在 http://0.0.0.0:5002"
echo "- 气体特性预测服务运行在 http://0.0.0.0:5003"

echo "日志文件位于:"
echo "- /app/pocket_disease_service.log"
echo "- /app/molecule_search_service.log"
echo "- /app/gas_properties_service.log"

# 等待所有后台进程
wait 