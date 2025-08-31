FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-opencv \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY src/requirements.txt /app/
RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["/bin/bash"]
