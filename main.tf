# Defines the local server infrastructure.

provider "local" {}

resource "local_file" "nginx_config" {
  filename = "nginx.conf"
  content  = <<EOT
server {
    listen 80;
    
    location / {
        proxy_pass http://localhost:8000;
    }
}
EOT
}

resource "null_resource" "start_containers" {
  provisioner "local-exec" {
    command = "docker-compose up -d"
  }
}
