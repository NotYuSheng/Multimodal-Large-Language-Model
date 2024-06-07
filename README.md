# CT-Multimodal-Large-Language-Model

## Host requirements
1. **Docker**: [Installation Guide](https://docs.docker.com/engine/install/)
2. **Minimum of 8 GB RAM**
3. **Adequate Disk Space** for Docker images and containers
4. **Port 8501** available for mapping to the container (else redefine port number in Dockerfile)

## Usage
1.  Clone this repository and navigate to LLaVA folder
```
git clone https://github.com/NotYuSheng/CT-Multimodal-Large-Language-Model.git
cd Multimodal-Large-Language-Model
```

2.  Build the Docker Image:
```
docker build -t multimodal_app .
```

4.  Run Docker container
```
docker-compose up -d
```
5.  Access the web page on
```
http://localhost:8501
```
6.  Stopping Docker container
```
docker-compose down
```
