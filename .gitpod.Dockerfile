# .gitpod.Dockerfile
FROM gitpod/workspace-full

# Install Python dependencies
RUN apt-get update && apt-get install -y python3-pip
