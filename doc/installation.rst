Installation
=====

.. note::

   Project will run on GPU by default. To run on CPU, use the `docker-compose.cpu.yml` instead.

.. important::
   
   If running on Windows with GPU, run commands from the WSL terminal.

1. Clone this repository and navigate to the project folder:

   .. code-block:: bash

       git clone https://github.com/NotYuSheng/Multimodal-Large-Language-Model.git
       cd Multimodal-Large-Language-Model

2. Build the Docker images:

   .. code-block:: bash

       docker-compose build

3. Run the images:

   .. code-block:: bash

       docker-compose up -d

4. Access the Streamlit webpage from the host:

   .. code-block:: text

       <host-ip>:8501

   API calls to Ollama server can be made to:

   .. code-block:: text

       <host-ip>:11434
