#!/bin/sh

set -ex

SOURCE=favicon.svg

inkscape -z -e favicon-16x16.png -w 16 -h 16 ${SOURCE}
inkscape -z -e favicon-32x32.png -w 32 -h 32 ${SOURCE}
inkscape -z -e android-chrome-192x192.png -w 192 -h 192 ${SOURCE}
inkscape -z -e android-chrome-512x512.png -w 512 -h 512 ${SOURCE}
inkscape -z -e apple-touch-icon.png -w 160 -h 160 ${SOURCE}
convert android-chrome-512x512.png -define icon:auto-resize=64,48,32,16 favicon.ico
