docker run -p 5008:5008 --rm \
  --mount type=bind,src=/Users/arnorhs/projects/kittentts/vol,dst=/app/vol \
  ktts

#  -v $HOME/.cache/pip-docker/:/root/.cache/pip