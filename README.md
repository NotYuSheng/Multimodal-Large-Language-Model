# Multimodal-Large-Language-Model (MLLM)
*Localized multimodal large language model for interactive text and image processing tasks.*

[[🤗Space DEMO](https://huggingface.co/spaces/NotYuSheng/MMLLM)] Currently unavailable

## Host requirement(s)
- **Docker**: [[Installation Guide](https://docs.docker.com/engine/install/)]
- **Docker Compose**: [[InstallationGuide](https://docs.docker.com/compose/install/)]
- Built with Docker on a **Linux** host, issues may occur when containers are built with Windows or macOS
- Ensure port 8501 and 11434 is not already in use
- Hardware Specification are dependant largely on the model used, LLaVA requires around 6 to 8 GB RAM to run
- Project has only been configured to run and tested on NVIDIA GPU
- Project will run on GPU by default, to run on CPU, remove the following lines from the [docker-compose.yml](docker-compose.yml).

>     deploy:
>       resources:
>         reservations:
>           devices:
>             - driver: nvidia
>               count: all
>               capabilities: [gpu]

## Tested Model(s)
| Model Name | Size | Link |
| --- | --- | --- |
| llava:7b | 4.7GB | [Link](https://www.ollama.com/library/llava:7b) |

Other models from [Ollama](https://www.ollama.com/library) can be added into [ollama/ollama-service.sh](ollama/ollama-service.sh)

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

4.  Access Streamlit webpage from host
```
<host-ip>:8501
```

API calls to Ollama server can be made on 
```
<host-ip>:11434
```

## Useful Docker commands
List Docker containers
```
docker ps -a
```

Check container(s) log(s)
```
docker-compose logs
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
