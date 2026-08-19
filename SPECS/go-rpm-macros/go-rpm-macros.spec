# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _commit 89f3871e1654a6c534fd9d12dfed6184c5122926

Name:           go-rpm-macros
Version:        0.1+git20260720.89f3871
Release:        %autorelease
Summary:        Go macros for openRuyi packaging
License:        MIT AND GPL-3.0-or-later
URL:            https://github.com/openRuyi-Project/go-rpm-macros
#!RemoteAsset:  sha256:92a2a1bb2bb7aa68ebbe81388e27393989cb103556b4c32e5cee0f07f4480f9f
Source0:        https://github.com/openRuyi-Project/go-rpm-macros/archive/%{_commit}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch

%description
This package provides RPM macros for packaging Go software in openRuyi.

%prep
%autosetup -n %{name}-%{_commit}

# No build needed
%build

%install
install -D -m644 macros.golang %{buildroot}%{_rpmmacrodir}/macros.golang
install -D -m644 macros.buildsystem.golang %{buildroot}%{_rpmmacrodir}/macros.buildsystem.golang
install -D -m644 macros.buildsystem.golangmodules %{buildroot}%{_rpmmacrodir}/macros.buildsystem.golangmodules
install -D -m644 go.attr %{buildroot}%{_fileattrsdir}/go.attr
install -D -m755 go-rpm-integration %{buildroot}%{_rpmconfigdir}/go-rpm-integration

%check
bash -n go-rpm-integration

%files
%license LICENSE LICENSE.GPL-3.0-or-later
%doc LICENSES.md
%{_rpmmacrodir}/macros.golang
%{_rpmmacrodir}/macros.buildsystem.golang
%{_rpmmacrodir}/macros.buildsystem.golangmodules
%{_fileattrsdir}/go.attr
%{_rpmconfigdir}/go-rpm-integration

%changelog
%autochangelog
