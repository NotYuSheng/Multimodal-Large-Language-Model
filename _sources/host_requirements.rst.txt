Host Requirements
=================

- **Docker**: `Installation Guide <https://docs.docker.com/engine/install/>`_
- **Docker Compose**: `Installation Guide <https://docs.docker.com/compose/install/>`_
- Compatible with Linux and Windows Host
- Ensure port 8501 and 11434 are not already in use
- At least 8 GB of RAM available to run the 7B models, 16 GB to run the 13B models, and 32 GB to run the 33B models. `Source <https://github.com/ollama/ollama>`_
- Project can be run on either CPU or GPU

Running on GPU
--------------
- **NVIDIA Container Toolkit** (Linux) `Installation Guide <https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html>`_
- **NVIDIA CUDA Toolkit** (Windows) `Installation <https://developer.nvidia.com/cuda-downloads>`_
- **WSL** (Windows) `Installation <https://docs.docker.com/desktop/gpu/>`_

Tested Model(s)
---------------
.. list-table::
   :widths: 20 10 20
   :header-rows: 1

   * - Model Name
     - Size
     - Link
   * - llava:7b
     - 4.7GB
     - `Link <https://www.ollama.com/library/llava:7b>`_
   * - llava:34b
     - 20GB
     - `Link <https://www.ollama.com/library/llava:34b>`_

Llava is pulled and loaded by default, other models from `Ollama <https://www.ollama.com/library>`_ can be added into ``ollama/ollama-build.sh``.
