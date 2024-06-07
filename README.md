# CT-Multimodal-Large-Language-Model

## Operating System Details
The app was created and hosted on:
- **Distributor ID:** Kali
- **Description:** Kali GNU/Linux Rolling
- **Release:** 2023.2
- **Codename:** kali-rolling

## Host requirements
1. **Docker**: [Installation Guide](https://docs.docker.com/engine/install/)
~~2. **Docker Compose**: [Installation Guide](https://docs.docker.com/compose/install/)~~
3. **Minimum of 8 GB RAM**
4. **Adequate Disk Space** for Docker images and containers
5. **Port 8501** available for mapping to the container (else redefine port number in Dockerfile)
6. **Internet Access**

## Usage
1.  Clone this repository and navigate to LLaVA folder
```
git clone https://github.com/NotYuSheng/CT-Multimodal-Large-Language-Model.git
cd CT-Multimodal-Large-Language-Model
```

~~2.  Build the Docker Image:~~
```
docker build -t multimodal_app .
```

3.  Build the Docker compose:
```
docker-compose build
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
