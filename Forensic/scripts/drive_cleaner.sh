#!/bin/bash
# This script will wipe the desired drive. But make sure you know what you are doing
# The script is using dd, so if you fuck up, you fuck up!

# Check if the user has provided the device path as an argument
if [ $# -ne 1 ]; then
  echo "Usage: $0 <device_path>"
  exit 1
fi

device_path="$1"

# Check if the device exists
if [ ! -e "$device_path" ]; then
  echo "Device $device_path does not exist."
  exit 1
fi

# Check if the device is mounted and unmount it if needed
if grep -qs "$device_path" /proc/mounts; then
  echo "Unmounting $device_path..."
  sudo umount "$device_path"
fi

# Perform the wipe with dd and display a progress bar
echo "Wiping $device_path..."
sudo dd if=/dev/zero of="$device_path" bs=4M status=progress
echo "Wipe completed."
