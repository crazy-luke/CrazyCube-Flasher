#!/usr/bin/env bash
# rm -fr build dist
VERSION=1.0.0
NAME="CrazyCube Flasher"
DIST_NAME="CrazyCube-Flasher"

pyinstaller --log-level=DEBUG \
            --noconfirm \
            --windowed \
            build-on-mac.spec

# https://github.com/sindresorhus/create-dmg
create-dmg "dist/$NAME.app"
mv "$NAME $VERSION.dmg" "dist/$DIST_NAME.dmg"
