# Multimodal-Large-Language-Model (MLLM)

## Tested Model(s)
| Model Name | Size | Link |
| --- | --- | --- |
| llava:7b | 4.7GB | [Link](https://www.ollama.com/library/llava:7b) |

## Host requirement(s)
- **Docker**: [Installation Guide](https://docs.docker.com/engine/install/)

- Ensure port 8501 and 11434 is not in use.

## Usage
1.  Clone this repository and navigate to project folder
```
git clone https://github.com/NotYuSheng/Multimodal-Large-Language-Model.git
cd Multimodal-Large-Language-Model
```

2.  Build the Docker images:
```
docker-compose build
```

3.  Run images
```
docker-compose up -d
```

~~4.  Wait for model to pull (Wait for Streamlit app to start)~~
```  
docker logs -f <container-id>
```

5.  Access Streamlit webpage from host
```
localhost:8501
```

API calls to Ollama server can be made on 
```
localhost:11434
```

## Useful Docker commands
List Docker containers
```
docker ps -a
```

Check container build status
```
docker logs <container-id>
```

Get interactive shell after container has started
```
docker exec -it <container-id> /bin/bash
```

Start docker container after host restart
```
docker container start <container-id>
```

Delete all containers including its volumes use
```
docker rm -vf $(docker ps -aq)
```

Delete all images
```
docker rmi -f $(docker images -aq)
```

## Common Issue(s):
### Error: 
> docker: Got permission denied while trying to connect to the Docker daemon socket at ...

### Solution:
1. Add current user to docker group
```
sudo usermod -aG docker $USER
```
2. Verify docker can be ran
```
docker ps -a
```
3. Reboot if error persist
```
sudo reboot
```
