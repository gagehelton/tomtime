sudo rm -r /etc/nginx/sites-enabled/default
sudo cp tomtime.live /etc/nginx/sites-enabled/
sudo cp tomtime.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl restart nginx
sudo systemctl enable tomtime
sudo systemctl start tomtime
