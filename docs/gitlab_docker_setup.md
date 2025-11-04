# GitLab Docker Repository Setup on Vonnegut

This document outlines how to set up and use a private GitLab Docker container registry on Vonnegut for building and storing Docker images.

## Prerequisites

- Access to GitLab instance on Vonnegut
- Repository created in GitLab with appropriate permissions
- GitLab CI/CD runners configured with Docker support

## 1. Create GitLab Repository

### Via GitLab Web UI

1. Navigate to GitLab on Vonnegut
2. Click **New project** → **Create blank project**
3. Set project name (e.g., `beast-unifi-integration`)
4. Set visibility level to **Private**
5. Click **Create project**

### Via GitLab CLI (if available)

```bash
glab repo create beast-unifi-integration --private
```

## 2. Configure GitLab Remote

```bash
# Add GitLab remote (replace with your GitLab URL and namespace)
git remote add gitlab https://vonnegut/gitlab/your-namespace/beast-unifi-integration.git

# Or if using SSH
git remote add gitlab git@vonnegut:your-namespace/beast-unifi-integration.git

# Verify remotes
git remote -v
```

## 3. Push Code to GitLab

```bash
# Push main branch to GitLab
git push gitlab main

# Or push all branches
git push gitlab --all
```

## 4. GitLab Container Registry

GitLab automatically provides a container registry for each project. The registry URL format is:

```
{vonnegut-gitlab-url}/container_registry
```

Or directly:
```
{vonnegut-gitlab-url}/registry/group/project
```

### Access Registry URL

1. In your GitLab project, navigate to **Packages & Registries** → **Container Registry**
2. The registry URL will be displayed (e.g., `vonnegut/gitlab/your-namespace/beast-unifi-integration/container_registry`)

## 5. CI/CD Pipeline Configuration

The `.gitlab-ci.yml` file in the repository root is configured to:

- Build Docker images from the Dockerfile
- Push images to GitLab Container Registry
- Tag images with branch/commit information
- Tag `main` branch images as `latest`

### Pipeline Variables (Optional)

You can set build variables in GitLab under **Settings** → **CI/CD** → **Variables**:

- `MID_INSTALLATION_URL` - ServiceNow MID installer URL (defaults to configured URL)
- `MID_SIGNATURE_VERIFICATION` - Enable/disable signature verification (default: `TRUE`)
- `MID_USERNAME` - MID server username (default: `mid`)
- `GROUP_ID` - Container group ID (default: `1001`)
- `USER_ID` - Container user ID (default: `1001`)

## 6. Using Docker Images from Registry

### Login to Registry

```bash
# Login to GitLab container registry
docker login vonnegut

# Or with full URL
docker login vonnegut/gitlab
```

You can use:
- **Personal Access Token**: Create under **User Settings** → **Access Tokens** with `read_registry` scope
- **Deploy Token**: Create under **Project Settings** → **Repository** → **Deploy tokens** with `read_registry` scope
- **CI/CD Job Token**: Automatically available in CI/CD jobs

### Pull Docker Image

```bash
# Pull latest image
docker pull vonnegut/gitlab/your-namespace/beast-unifi-integration:latest

# Pull specific branch image
docker pull vonnegut/gitlab/your-namespace/beast-unifi-integration:main

# Pull tagged image
docker pull vonnegut/gitlab/your-namespace/beast-unifi-integration:v1.0.0
```

### Run Container

```bash
docker run -d \
  --name mid-server \
  -e MID_INSTANCE_URL="https://your-instance.service-now.com" \
  -e MID_INSTANCE_USERNAME="mid_username" \
  -e MID_INSTANCE_PASSWORD="mid_password" \
  -e MID_SERVER_NAME="mid-server-name" \
  vonnegut/gitlab/your-namespace/beast-unifi-integration:latest
```

## 7. Configure Runner (if needed)

If you need to set up a GitLab Runner with Docker support:

### Install GitLab Runner

```bash
# Download runner binary (adjust for your OS/arch)
curl -L "https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.rpm.sh" | bash

# Install GitLab Runner
yum install gitlab-runner
```

### Register Runner

```bash
sudo gitlab-runner register \
  --url https://vonnegut \
  --registration-token YOUR_REGISTRATION_TOKEN \
  --executor docker \
  --docker-image docker:24-dind \
  --docker-privileged \
  --description "Docker Runner"
```

The registration token can be found in **Settings** → **CI/CD** → **Runners**.

## 8. Manual Build and Push (Alternative)

If you prefer to build and push manually:

```bash
# Login to registry
docker login vonnegut

# Build image
cd src/beast_unifi_servicenow/mid_server/docker
docker build \
  --build-arg MID_INSTALLATION_URL="https://..." \
  -t vonnegut/gitlab/your-namespace/beast-unifi-integration:latest \
  .

# Push image
docker push vonnegut/gitlab/your-namespace/beast-unifi-integration:latest
```

## 9. Access Control

### Make Registry Private

1. Navigate to **Settings** → **General** → **Visibility, project features, permissions**
2. Ensure **Container Registry** is enabled
3. Set project visibility to **Private** to restrict access

### Manage Access

- **Project Members**: Automatically have access based on project role
- **Deploy Tokens**: Create for automated access without user credentials
- **Personal Access Tokens**: User-specific tokens for registry access

## Troubleshooting

### Docker Login Fails

- Verify GitLab URL is correct
- Check that you have proper credentials (PAT or deploy token)
- Ensure registry is enabled for the project

### CI/CD Pipeline Fails

- Verify runner has Docker support
- Check runner tags match `.gitlab-ci.yml` requirements
- Ensure runner has sufficient resources

### Permission Denied

- Verify you have Developer or Maintainer role in the project
- Check that registry is enabled
- Verify deploy token has `read_registry` or `write_registry` scopes

## Additional Resources

- [GitLab Container Registry Documentation](https://docs.gitlab.com/ee/user/packages/container_registry/)
- [GitLab CI/CD Documentation](https://docs.gitlab.com/ee/ci/)
- [Docker Build Best Practices](https://docs.docker.com/build/building/best-practices/)

