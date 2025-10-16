FROM ghcr.io/hassio-addons/debian-base:8.1.4

RUN apt-get update -y && \
    apt-get install curl gpg --no-install-recommends -y

COPY fluentbit.key /fluentbit.key
RUN cat /fluentbit.key | gpg --dearmor > /usr/share/keyrings/fluentbit-keyring.gpg && \
    rm /fluentbit.key

RUN . /etc/os-release && \
    export OS=$( echo "${ID}" | tr '[:upper:]' '[:lower:]') && \
    export CODENAME=$( echo "${VERSION_CODENAME}" | tr '[:upper:]' '[:lower:]') && \
    echo "deb [signed-by=/usr/share/keyrings/fluentbit-keyring.gpg] https://packages.fluentbit.io/debian/${CODENAME} ${CODENAME} main" > /etc/apt/sources.list.d/fluentbit.list

# renovate: release=bookworm depName=fluent-bit
ENV FLUENTBIT_VERSION="3.2.10"

# log out the version of fluent-bit that will be installed
RUN echo "Fluent Bit version: ${FLUENTBIT_VERSION}"

RUN apt-get update -y && \
    apt-get install python3 python3-pip --no-install-recommends -y && \
    apt-get install fluent-bit=${FLUENTBIT_VERSION} --no-install-recommends -y

COPY run.py /run.py
CMD ["python3", "-u", "/run.py"]