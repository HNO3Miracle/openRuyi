# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pyyaml_ft
%global pypi_name pyyaml-ft

Name:           python-%{pypi_name}
Version:        8.0.0
Release:        %autorelease
Summary:        YAML parser and emitter for Python with free-threading support
License:        MIT
URL:            https://github.com/Quansight-Labs/pyyaml-ft
#!RemoteAsset:  sha256:0c947dce03954c7b5d38869ed4878b2e6ff1d44b08a0d84dc83fdad205ae39ab
Source0:        https://files.pythonhosted.org/packages/5e/eb/5a0d575de784f9a1f94e2b1288c6886f13f34185e13117ed530f32b6f8a8/pyyaml_ft-%{version}.tar.gz

BuildRequires:  pyproject-rpm-macros
BuildRequires:  gcc
BuildRequires:  pkgconfig(yaml-0.1)
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(cython) >= 3.1
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{pypi_name}
Provides:       python3-%{pypi_name} = %{version}-%{release}

%description
PyYAML-ft provides a YAML parser and emitter for Python with support for
free-threaded Python 3.13 runtimes.

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
# The upstream build only enables the libyaml-backed extension when this
# environment variable is set; the declarative BuildOption(build) path in
# openRuyi cannot express that env-var-only switch correctly here.
PYYAML_FORCE_LIBYAML=1 %pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l yaml_ft _yaml_ft

%check
%pyproject_check_import yaml_ft

%files -f %{pyproject_files}
%doc README.md CHANGES
%license LICENSE

%changelog
%autochangelog
