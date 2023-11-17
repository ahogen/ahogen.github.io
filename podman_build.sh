#!/usr/bin/bash

# # If ssh-agent not started, start it
# if ps -p $SSH_AGENT_PID > /dev/null
# then
#    echo "ssh-agent is already running"
# else
#     echo "Starting ssh-agent"
#     eval $(ssh-agent -s)
# fi


# --mount=type=bind,source=${SSH_AUTH_SOCK},destination=/ssh-agent \

# Build with Podman
podman run -v $PWD:/antora:Z \
    --env NODE_TLS_REJECT_UNAUTHORIZED=0 \
    --rm -it \
    docker.io/antora/antora --git-credentials-path=./.git-credentials  antora-playbook.yml
