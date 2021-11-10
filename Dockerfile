
# syntax=docker/dockerfile:1

FROM fairnle/nle-focal:v0.7.2
# just copies from our folder to the one in container.
COPY . .
RUN pip install tensorflow
