[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/Hotel-booking-with-chat-bot-support-django
ExecStart=/home/ubuntu/Hotel-booking-with-chat-bot-support-django/hotelenv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          HotelProject.wsgi:application

[Install]
WantedBy=multi-user.target

server {
    listen 80;
    server_name 54.234.27.213;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static {
            autoindex on;
            alias /home/ubuntu/Hotel-booking-with-chat-bot-support-django/static;
       }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
ssh -i "hotelsite.pem" ubuntu@ec2-54-226-122-15.compute-1.amazonaws.com

My AWS Credentials are : 
Email:- siddesh.edu@gmail.com
Username :- Siddesh 
Pass:- Siddesh@199530thnov