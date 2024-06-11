# Multimodal-Large-Language-Model (MMLLM)

## Host requirements
1. **Docker**: [Installation Guide](https://docs.docker.com/engine/install/)
2. **Minimum of 8 GB RAM**
3. **Port 8501** available for mapping to the container (else redefine port number in Dockerfile and run command)
4. **Disk Space** Dependant on model size

| Model Name | Size | Link |
| --- | --- | --- |
| llava:7b | 4.7GB | [Link](https://www.ollama.com/library/llava:7b) |

## Usage
1.  Clone this repository and navigate to project folder
```
git clone https://github.com/NotYuSheng/Multimodal-Large-Language-Model.git
cd Multimodal-Large-Language-Model
```

2.  Build the Docker Image:
```
docker build -t multimodal_app .
```

3.  Map port 8501 from the container to port 8501 on the host machine
```
docker run -d -p 8501:8501 multimodal_app
```

3.  Or run start with interactive shell
```
docker run -d -it -p 8501:8501 multimodal_app /bin/bash
```

4.  Subsequent interactive shell (Optional)
```
docker exec -it <container-id> /bin/bash
```
