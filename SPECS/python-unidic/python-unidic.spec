# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname unidic

Name:           python-%{srcname}
Version:        1.1.0
Release:        %autorelease
Summary:        Python wrapper for downloading and locating UniDic
License:        MIT
URL:            https://github.com/polm/unidic-py
#!RemoteAsset:  sha256:0ab91c05de342c84d2a6314901fd3afb9061ecd7534dd4a0431dccbb87d921b7
Source0:        https://files.pythonhosted.org/packages/source/u/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
unidic provides Python helpers for downloading and locating the UniDic
dictionary files used by MeCab-based tokenizers.

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
%pyproject_check_import %{srcname}

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
