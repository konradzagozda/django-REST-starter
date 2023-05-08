# Use the official Debian Bullseye image as the base image
FROM mcr.microsoft.com/devcontainers/base:bullseye

# Install Python 3.10 and required dependencies
RUN apt-get update && \
    apt-get install -y \
        software-properties-common \
        build-essential \
        libpq-dev \
        libssl-dev \
        zlib1g-dev \
        libbz2-dev \
        libreadline-dev \
        libsqlite3-dev \
        wget \
        curl \
        llvm \
        libncursesw5-dev \
        xz-utils \
        tk-dev \
        libxml2-dev \
        libxmlsec1-dev \
        libffi-dev \
        liblzma-dev

# Install Python 3.10 from source
RUN curl -O https://www.python.org/ftp/python/3.10.0/Python-3.10.0.tgz && \
    tar xvf Python-3.10.0.tgz && \
    cd Python-3.10.0 && \
    ./configure --enable-optimizations && \
    make altinstall && \
    cd .. && \
    rm -rf Python-3.10.0 && \
    rm Python-3.10.0.tgz

# Install pip for Python 3.10
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python3.10 get-pip.py && \
    rm get-pip.py

# Remove Python 3.9
RUN apt-get remove -y python3.9 python3.9-minimal python3.9-dev && \
    apt-get autoremove -y && \
    apt-get clean

# Set the default Python version to 3.10
RUN update-alternatives --install /usr/bin/python python /usr/local/bin/python3.10 1 && \
    update-alternatives --set python /usr/local/bin/python3.10


# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3.10 -

# Add Poetry's installed binaries to the PATH
ENV PATH "/root/.local/bin:$PATH"
