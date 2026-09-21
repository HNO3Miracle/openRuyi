# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname ruamel.yaml
%global pypi_name ruamel_yaml

%bcond oldlibyaml 1

Name:           python-ruamel-yaml
Version:        0.19.1
Release:        %autorelease
Summary:        YAML 1.2 loader/dumper package for Python
License:        MIT
URL:            https://sourceforge.net/projects/ruamel-yaml/
#!RemoteAsset:  sha256:53eb66cd27849eff968ebf8f0bf61f46cdac2da1d1f3576dd4ccee9b25c31993
Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l ruamel
# TODO: Unknown distribution option: 'build_zig'
BuildOption(check):  -e ruamel.yaml.clibz.*
BuildOption(check):  -e ruamel.yaml.cyaml

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pytest)

Provides:       python3-ruamel-yaml = %{version}-%{release}
%python_provide python3-ruamel-yaml

# The oldlibyaml subpackage is used to provide the libyaml C library for ruamel.yaml.
# It is only built when the bootstrap build option is not set, as it is not needed for the bootstrap build.
%if %{with oldlibyaml}
Recommends:     python-ruamel-yaml+oldlibyaml = %{version}-%{release}
%endif

%if %{with oldlibyaml}
%pyproject_extras_subpkg -n python-ruamel-yaml oldlibyaml
%endif

%description
ruamel.yaml is a YAML parser/emitter that supports roundtrip preservation of
comments, seq/map flow style, and map key order.

%generate_buildrequires
%pyproject_buildrequires %{!?with_oldlibyaml:-x oldlibyaml}

%files -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
