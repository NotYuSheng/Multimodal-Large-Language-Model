# Multimodal-Large-Language-Model (MMLLM)

## Tested Models
| Model Name | Size | Link |
| --- | --- | --- |
| llava:7b | 4.7GB | [Link](https://www.ollama.com/library/llava:7b) |

## Host requirements
**Docker**: [Installation Guide](https://docs.docker.com/engine/install/)

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

3.  Run image in detached and foreground mode
```
docker run -d -t multimodal_app
```

4.  Wait for model to pull (Wait for "All services startup completed")
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
