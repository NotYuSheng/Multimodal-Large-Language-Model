# Multimodal-Large-Language-Model (MMLLM)

## Host requirements
1.  **Docker**: [Installation Guide](https://docs.docker.com/engine/install/)

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
docker run -d -p 8501:8501 -p 11434:11434 multimodal_app
```

4.  Wait for model to pull (could take awhile)
```  
tail | docker logs -f <container-id>
```

5.  Access Streamlit webpage from host
```
<container-ip>:8501
```

## Docker usage commands
List running Docker containers
```
docker ps
```

Check container build status
```
docker logs <container-id>
```

Get interactive shell after container has started
```
docker exec -it <container-id> /bin/bash
```

## Sample
