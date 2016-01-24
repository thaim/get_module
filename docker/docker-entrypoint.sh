#!/bin/bash

set -e

if [ "$GET_MODULE_PROXY_HOST" -a "$GET_MODULE_PROXY_PORT" ]; then
    mkdir -p "$HOME/.subversion"
    cat > "$HOME/.subversion/servers" <<EOF
[global]
http-proxy-host = $GET_MODULE_PROXY_HOST
http-proxy-port = $GET_MODULE_PROXY_PORT
EOF

    if [ "$GET_MODULE_NO_PROXY" ]; then
        cat >> "$HOME/.subversion/servers" <<EOF
http-proxy-exception = $GET_MODULE_NO_PROXY
EOF

        export NO_PROXY=$GET_MODULE_NO_PROXY
    fi

    export HTTP_PROXY=$GET_MODULE_PROXY_HOST:$GET_MODULE_PROXY_PORT
    export HTTPS_PROXY=$GET_MODULE_PROXY_HOST:$GET_MODULE_PROXY_PORT
fi

set -- get_module.py "$@"

exec "$@"
