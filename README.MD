# 建立映像檔
docker build -t bloomTest .

# 執行映像檔
docker run bloomTest --name=bloomTest

# 除錯用，直接進入容器互動介面並跳過啟動命令
docker run -it bloomTest /bin/bash --name=bloomTest