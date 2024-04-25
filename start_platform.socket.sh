#!/bin/bash

# start the platform.socket 
systemctl restart platform.socket
echo "$(date '+%Y-%m-%d %H:%M:%S')  - platform.socket  restarted"   >> /var/www/Angizeh_2/log_start_platform_socket.log



