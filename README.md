# CT-Multimodal-Large-Language-Model

## Operating System Details
The app was created and hosted on:
- **Distributor ID:** Kali
- **Description:** Kali GNU/Linux Rolling
- **Release:** 2023.2
- **Codename:** kali-rolling

## Host requirements
1. **Docker**: [Installation Guide](https://docs.docker.com/engine/install/)
2. **Docker Compose**: [Installation Guide](https://docs.docker.com/compose/install/)
3. **Minimum of 4 GB RAM**
4. **Adequate Disk Space** for Docker images and containers
5. **Port 8501** available for mapping to the container (else redefine port number in Dockerfile)
6. **Internet Access**

## Usage
1.  Build the Docker Image:
```zsh
docker-compose build
```

2.  Run Docker container
```zsh
docker-compose up -d
```
3.  Access the web page on
```zsh
http://localhost:8501
```
4.  Stopping Docker container
```zsh
docker-compose down
```
