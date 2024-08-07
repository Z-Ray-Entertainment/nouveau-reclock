#!/usr/bin/bash
flatpak-builder --force-clean --sandbox --user --install --install-deps-from=flathub --ccache --mirror-screenshots-url=https://dl.flathub.org/media/ --repo=repo builddir ../de.z_ray.Nvreclock.json
rm -rf ./repo ./builddir ./.flatpak-builder