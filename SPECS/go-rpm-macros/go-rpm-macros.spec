# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _commit 864d62d7384090449a2b88aaef0ded86bcc7f0ae

Name:           go-rpm-macros
Version:        0.1+git20260821.864d62d
Release:        %autorelease
Summary:        Go macros for openRuyi packaging
License:        MIT AND GPL-3.0-or-later
URL:            https://github.com/openRuyi-Project/go-rpm-macros
#!RemoteAsset:  sha256:a844471e7c276869e1c3434b2278908dba2824a77df81595dc2319bc3b2bef4c
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
