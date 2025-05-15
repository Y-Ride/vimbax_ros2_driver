#!/bin/bash
set -e

ARCH=${1:-$(uname -m)}  # Use argument if provided, otherwise detect automatically

# Determine the directory the script is in
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Extract location (can be changed if needed)
INSTALL_DIR="/opt"

echo "Installing VimbaX for architecture: $ARCH"
cd "$INSTALL_DIR"

if [[ "$ARCH" == "arm64" || "$ARCH" == "aarch64" ]]; then
    echo "Using: VimbaX_Setup-2025-1-Linux_ARM64.tar.gz"
    tar -xvzf "$SCRIPT_DIR/VimbaX_Setup-2025-1-Linux_ARM64.tar.gz"
elif [[ "$ARCH" == "amd64" || "$ARCH" == "x86_64" ]]; then
    echo "Using: VimbaX_Setup-2025-1-Linux64.tar.gz"
    tar -xvzf "$SCRIPT_DIR/VimbaX_Setup-2025-1-Linux64.tar.gz"
else
    echo "Unsupported architecture: $ARCH"
    exit 1
fi
