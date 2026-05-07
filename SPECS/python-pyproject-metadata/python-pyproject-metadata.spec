# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pyproject-metadata

Name:           python-%{srcname}
Version:        0.11.0
Release:        %autorelease
Summary:        PEP 621 metadata parsing
License:        MIT
URL:            https://github.com/FFY00/python-pyproject-metadata
#!RemoteAsset:  sha256:c72fa49418bb7c5a10f25e050c418009898d1c051721d19f98a6fb6da59a66cf
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/pyproject_metadata-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l pyproject_metadata  +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Dataclass for PEP 621 metadata with support for core metadata generation

This project does not implement the parsing of `pyproject.toml`
containing PEP 621 metadata.

Instead, given a Python data structure representing PEP 621 metadata (already
parsed), it will validate this input and generate a PEP 643-compliant metadata
file (e.g. `PKG-INFO`).

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README*

%changelog
%autochangelog
