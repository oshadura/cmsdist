### RPM external py2-cmstest 0.6.1
## IMPORT build-with-pip

%define pip_name mccabe
%define source0 usercommand://%{pip_name}?package_dependency=py2-pip,git&command=pip%%20download%%20--no-deps%%20--no-binary%%3D:all:%%20--disable-pip-version-check%%20-d%%20.%%20%{pip_name}==%{realversion};/bin/ls%%20|grep%%20-v%%20files.list>%%20files.list&output=/source.tar.gz