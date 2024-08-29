Project Features
================

Features
------------

- Upon deployment, Ollama can be accessed via an API call to the server IP: ``<server-ip>:11434``. 
- Any device on the network can query the host server.

.. important::
   
   The project has been fully Dockerized. The Ollama server can be run standalone without deploying the Streamlit web app. 
   To do this, simply remove the ``streamlit`` folder and the ``streamlit_app`` service from the ``docker-compose.yml``.

.. image:: doc/images/network-diagram.png
   :alt: Network diagram
