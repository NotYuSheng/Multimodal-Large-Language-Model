Installation
=====

1. Clone this repository and navigate to the project folder:

   .. code-block:: bash

       git clone https://github.com/NotYuSheng/ChannelGPT-Tool.git
       cd ChannelGPT-Tool

2. Build the Docker images:

   .. code-block:: bash

       docker-compose build

3. Run the images:

   .. code-block:: bash

       docker-compose up -d

4. Access the Open-WebUI webpage from the host:

   .. code-block:: text

       <host-ip>:8080

   Access the FastAPI docs page from:

   .. code-block:: text

       <host-ip>:8000/docs

5. Import the Model and Tool in Open-WebUI:  
   After accessing the Open-WebUI interface, navigate to the `Workspace` tab. Use the following JSON files to import the model and tool:

   - **Model:** `open-webui_json/channelgpt_model.json`  
   - **Tool:** `open-webui_json/tool-youtube.json`
