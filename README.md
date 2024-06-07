# Multimodal-Large-Language-Model (MMLLM)

Localized MMLLM

## Host requirements
1. **Docker**: [Installation Guide](https://docs.docker.com/engine/install/)
2. **Minimum of 8 GB RAM**
3. **Adequate Disk Space** for Docker images and containers
4. **Port 8501** available for mapping to the container (else redefine port number in Dockerfile)

## Usage
1.  Clone this repository and navigate to project folder
```
git clone https://github.com/NotYuSheng/CT-Multimodal-Large-Language-Model.git
cd Multimodal-Large-Language-Model
```

2.  Build the Docker Image:
```
docker build -t multimodal_app .
```

3.  Map port 8501 from the container to port 8501 on the host machine
```
docker run -p 8501:8501 multimodal_app
```

~~3.  Interactive Run (Start Interactive shell)~~
```
docker run -it --name my_multimodal_container multimodal_app /bin/bash
```

~~3.  Detached Run (Run in background)~~
```
docker run -d --name my_multimodal_container multimodal_app

```
