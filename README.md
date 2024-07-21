# Multimodal-Large-Language-Model (MLLM)
*Localized multimodal large language model for text and image processing tasks.*

<!-- [[🤗Space DEMO](https://huggingface.co/spaces/NotYuSheng/MMLLM)] -->

## Host requirement(s)
- **Docker**: [[Installation Guide](https://docs.docker.com/engine/install/)]
- **Docker Compose**: [[Installation Guide](https://docs.docker.com/compose/install/)]
- **NVIDIA Container Toolkit** [[Installation Guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)]
- Built with Docker on a **Linux** host, issues may occur when containers are built with Windows or macOS
- Ensure port 5000, 8501, and 11434 is not already in use
- Hardware Specification are dependant largely on the model used, LLaVA requires around 6 to 8 GB RAM to run
- Project can be ran on either CPU or GPU

## Tested Model(s)
| Model Name | Size | Link |
| --- | --- | --- |
| llava:7b | 4.7GB | [Link](https://www.ollama.com/library/llava:7b) |

Other models from [Ollama](https://www.ollama.com/library) can be added into [ollama/ollama-build.sh](ollama/ollama-build.sh)

## Usage
Project will run on GPU by default, to run on CPU, remove the following lines from the [docker-compose.yml](docker-compose.yml).

>     deploy:
>       resources:
>         reservations:
>           devices:
>             - driver: nvidia
>               count: all
>               capabilities: [gpu]

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

API calls to Ollama server can be made to
```
<host-ip>:5000
```

API calls to Ollama server made to 11434 will not be logged
```
<host-ip>:11434
```
