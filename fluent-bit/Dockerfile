ARG BUILD_FROM=ghcr.io/hassio-addons/debian-base:7.6.2
FROM ${BUILD_FROM}

ARG FLUENTBIT_VERSION=3.0.7

RUN apt-get update -y && \
    apt-get install curl gpg --no-install-recommends -y && \
    apt-get install curl --no-install-recommends -y

COPY fluentbit.key /fluentbit.key
RUN cat /fluentbit.key | gpg --dearmor > /usr/share/keyrings/fluentbit-keyring.gpg && \
    rm /fluentbit.key

RUN . /etc/os-release && \
    export OS=$( echo "${ID}" | tr '[:upper:]' '[:lower:]') && \
    export CODENAME=$( echo "${VERSION_CODENAME}" | tr '[:upper:]' '[:lower:]') && \
    echo "deb [signed-by=/usr/share/keyrings/fluentbit-keyring.gpg] https://packages.fluentbit.io/debian/${CODENAME} ${CODENAME} main" > /etc/apt/sources.list.d/fluentbit.list

ENV FLUENTBIT_VERSION=$FLUENTBIT_VERSION
RUN apt-get update -y && \
    apt-get install python3 python3-pip --no-install-recommends -y && \
    apt-get install fluent-bit=${FLUENTBIT_VERSION} --no-install-recommends -y

COPY run.py /run.py
CMD ["python3", "-u", "/run.py"]
