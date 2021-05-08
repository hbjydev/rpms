FROM centos:8
LABEL maintainer="hi@hbjy.dev"

RUN dnf install gcc rpm-build rpm-devel rpmlint make python38 \
  bash diffutils patch rpmdevtools sudo -y && \
  dnf clean all -y

RUN useradd builder -u 1000 -m -G users,wheel && \
  echo "builder ALL=(ALL:ALL) NOPASSWD:ALL" >> /etc/sudoers && \
  mkdir /home/builder/rpmbuild && chown -R builder /home/builder
USER builder

WORKDIR /home/builder/rpmbuild
COPY . .

ENV FLAVOR=rpmbuild OS=centos DIST=el8
