# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname libcst

Name:           python-%{srcname}
Version:        1.8.6
Release:        %autorelease
Summary:        Concrete syntax tree with AST-like properties for Python
License:        MIT
URL:            https://github.com/Instagram/LibCST
#!RemoteAsset:  sha256:f729c37c9317126da9475bdd06a7208eb52fcbd180a6341648b45a56b4ba708b
Source0:        https://files.pythonhosted.org/packages/de/cd/337df968b38d94c5aabd3e1b10630f047a2b345f6e1d4456bd9fe7417537/libcst-%{version}.tar.gz
Source1:        %{srcname}-%{version}-vendor.tar.zst
BuildSystem:    pyproject

BuildOption(prep):  -a1
BuildOption(install):  -l %{srcname}

BuildRequires:  cargo
BuildRequires:  gcc
BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pyyaml-ft) >= 8
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-rust)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(wheel)
BuildRequires:  rust

Provides:       python3-%{srcname}
Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
LibCST provides a concrete syntax tree for Python source code with AST-like
properties and codemod tooling.

%prep
%autosetup -a1 -n %{srcname}-%{version}
# Build against the vendored crates tarball instead of reaching crates.io
# during the OBS build.
mkdir -p .cargo
cat > .cargo/config.toml <<'EOF'
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%generate_buildrequires
%pyproject_buildrequires

%check
# The packaged test modules pull in optional test-only dependencies such as
# hypothesis. Keep import checks focused on the runtime modules.
%pyproject_check_import -e "libcst.tests*" -e "libcst.codemod.tests*" %{srcname}

%files -f %{pyproject_files}
%doc README.rst CHANGELOG.md CODE_OF_CONDUCT.md
%license LICENSE

%changelog
%autochangelog
