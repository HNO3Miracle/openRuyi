# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname wasabi

Name:           python-%{srcname}
Version:        0.10.1
Release:        %autorelease
Summary:        Lightweight console printing and formatting toolkit
License:        MIT
URL:            https://github.com/explosion/wasabi
#!RemoteAsset:  sha256:c8e372781be19272942382b14d99314d175518d7822057cb7a97010c4259d249
Source0:        https://files.pythonhosted.org/packages/source/w/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
wasabi provides lightweight console printing and formatting helpers for Python.

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
# The wheel includes upstream tests; keep this as a runtime import smoke test.
%pyproject_check_import -e wasabi.tests* %{srcname}

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
