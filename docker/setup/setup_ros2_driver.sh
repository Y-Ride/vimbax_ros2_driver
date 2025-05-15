#!/bin/bash
set -e

ARCH=${1:-$(uname -m)}  # Use argument if provided, otherwise detect automatically

# Determine the directory the script is in
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

cd "$SCRIPT_DIR"

echo "Installing VimbaX ros2 driver dependencies for architecture: $ARCH"

if [[ "$ARCH" == "arm64" || "$ARCH" == "aarch64" ]]; then
    echo "Using: ros-humble-vimbax-camera-driver-1.0.0-arm64.deb"
    apt install -y ./ros-humble-vimbax-camera-driver-1.0.0-arm64.deb
elif [[ "$ARCH" == "amd64" || "$ARCH" == "x86_64" ]]; then
    echo "Using: ros-humble-vimbax-camera-driver-1.0.0-amd64.deb"
    apt install -y ./ros-humble-vimbax-camera-driver-1.0.0-amd64.deb
else
    echo "Unsupported architecture: $ARCH"
    exit 1
fi
