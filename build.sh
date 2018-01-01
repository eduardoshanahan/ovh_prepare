IMAGE_VERSION=$(cat version.json | grep version | head -1 | awk -F: '{ print $2 }' | sed 's/[\",]//g' | tr -d '[[:space:]]')
docker build . -t eduardoshanahan/ovh_prepare:$IMAGE_VERSION
docker build . -t eduardoshanahan/ovh_prepare:latest