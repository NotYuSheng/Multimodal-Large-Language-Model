Usage
=====

> **NOTE**  
> Project will run on GPU by default. To run on CPU, remove the following lines from the `docker-compose.yml <docker-compose.yml>`.

>     deploy:
>       resources:
>         reservations:
>           devices:
>             - driver: nvidia
>               count: all
>               capabilities: [gpu]

> **IMPORTANT**  
> If running on Windows with GPU, run commands from WSL terminal

1.  Clone this repository and navigate to the project folder:
    ```bash
    git clone https://github.com/NotYuSheng/Multimodal-Large-Language-Model.git
    cd Multimodal-Large-Language-Model
    ```

2.  Build the Docker images:
    ```bash
    docker-compose build
    ```

3.  Run images:
    ```bash
    docker-compose up -d
    ```

4.  Access the Streamlit webpage from the host:
    ```text
    <host-ip>:8501
    ```

   API calls to Ollama server can be made to:
    ```text
    <host-ip>:11434
    ```
