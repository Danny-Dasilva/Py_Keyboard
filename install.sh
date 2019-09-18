echo "dtoverlay=dwc2" | sudo tee -a /boot/config.txt
echo "dwc2" | sudo tee -a /etc/modules
sudo echo "libcomposite" | sudo tee -a /etc/modules
sudo touch /usr/bin/isticktoit_usb
sudo chmod +x /usr/bin/isticktoit_usb
line="@reboot sudo /usr/bin/isticktoit_usb"
    (crontab -u "pi" -l; echo "$line" ) | crontab -u "pi" -

sudo cp usb.sh /usr/bin/isticktoit_usb