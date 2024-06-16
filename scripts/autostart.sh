#!/bin/bash

# Ejecuta la configuracion de Picom
picom --config $HOME/.config/qtile/picom/picom.conf &

polychromatic-cli -e JErickDev &

