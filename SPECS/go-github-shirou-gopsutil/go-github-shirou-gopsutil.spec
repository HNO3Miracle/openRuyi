# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gopsutil
%define go_import_path  github.com/shirou/gopsutil
# It seems that need sensors to pass it - Julian
# Tests fail in container with cpu limit on riscv64 - Julian
# Builder has swap disabled, ignore it - Julian
# Process tests depend on host PID namespace behavior.
# The release archive also contains the independently packaged /v3 module.
%define go_test_exclude %{shrink:
    github.com/shirou/gopsutil/sensors
    github.com/shirou/gopsutil/cpu
    github.com/shirou/gopsutil/mem
    github.com/shirou/gopsutil/process
}
%define go_test_exclude_glob %{go_import_path}/v3*

Name:           go-github-shirou-gopsutil
Version:        3.21.11
Release:        %autorelease
Summary:        psutil for golang
License:        BSD-3-Clause
URL:            https://github.com/shirou/gopsutil
#!RemoteAsset:  sha256:cb6fcdf8faece3e584604d6293a4b7e09fd5259a806174eded2fb90a3042c227
Source0:        https://github.com/shirou/gopsutil/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/tklauser/go-sysconf)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/shirou/gopsutil) = %{version}
Provides:       go(github.com/shirou/gopsutil/process) = %{version}

Requires:       go(github.com/tklauser/go-sysconf)
Requires:       go(golang.org/x/sys)

%description
gopsutil: psutil for Go

This is a port of psutil (https://github.com/giampaolo/psutil).

The challenge is porting all psutil functions on some architectures.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}
%exclude %{go_sys_gopath}/%{go_import_path}/v3

%changelog
%autochangelog
