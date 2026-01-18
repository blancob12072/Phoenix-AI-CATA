FROM runpod/pytorch:2.2.1-py3.10-cuda12.1.1-devel-ubuntu22.04

# Install Phoenix AI CATA core tools
RUN apt-get update && apt-get install -y \
    ngspice gnuplot openfoam \
    && rm -rf /var/lib/apt/lists/*

# Install Python libraries for simulation
RUN pip install --no-cache-dir skidl pyspice schemdraw

WORKDIR /workspace
