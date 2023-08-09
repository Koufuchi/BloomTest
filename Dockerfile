# 使用 ubuntu 作為基礎映像檔
FROM ubuntu:22.04

# 更新套件庫
RUN apt update

# 安裝 Python 和相關套件，這個 OS 版本預設裝 3.10
RUN apt install python3 python3-pip -y
RUN pip3 install --upgrade pip

# 安裝 transformers 和 torch 套件，後者可在 https://pytorch.org/get-started/locally/ 選擇適用語法替換
RUN pip3 install transformers
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# 複製專案目錄到容器中
COPY . /app

# 設定工作目錄
WORKDIR /app

# 設定啟動命令
CMD ["python3", "bloom.py"]
