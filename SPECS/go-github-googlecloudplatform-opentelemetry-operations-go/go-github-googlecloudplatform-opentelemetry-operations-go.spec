# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           opentelemetry-operations-go
%define go_import_path  github.com/GoogleCloudPlatform/opentelemetry-operations-go
# Install the complete source tree, but defer its large integration test suite.
%define go_test_exclude_glob %{go_import_path}*

Name:           go-github-googlecloudplatform-opentelemetry-operations-go
Version:        0.62.0
Release:        %autorelease
Summary:        Google Cloud integrations for OpenTelemetry
License:        Apache-2.0
URL:            https://github.com/GoogleCloudPlatform/opentelemetry-operations-go
#!RemoteAsset:  sha256:a6fae3974bd416025cc469762db31ab707818b4674b9d93336f13805b03cd2e8
Source0:        https://github.com/GoogleCloudPlatform/opentelemetry-operations-go/archive/refs/tags/exporter/metric/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# GitHub includes the nested release tag in the archive directory name.
BuildOption(prep):  -n %{_name}-exporter-metric-v%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/detectors/gcp) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/e2e-test-server) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/e2e-test-server/cloudfunctions) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/e2e-test-server/endtoendserver) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/e2e-test-server/scenarios) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/example/log/slogbridge) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/example/metric/collector) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/example/metric/exponential_histogram) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/example/metric/otlpgrpc) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/example/metric/sdk) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/example/trace/http) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/example/trace/otlpgrpc) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/example/trace/otlphttp) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/collector) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/collector/googlemanagedprometheus) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/collector/integrationtest) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/collector/integrationtest/protos) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/collector/integrationtest/testcases) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/collector/internal/datapointstorage) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/collector/internal/logsutil) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/collector/internal/normalization) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/metric) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/trace) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/extension/googleclientauthextension) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/cloudmock) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/resourcemapping) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/propagator) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/tools) = %{version}

Requires:       go(cloud.google.com/go/auth)
Requires:       go(cloud.google.com/go/compute/metadata)
Requires:       go(cloud.google.com/go/logging)
Requires:       go(cloud.google.com/go/monitoring)
Requires:       go(cloud.google.com/go/pubsub/v2)
Requires:       go(cloud.google.com/go/trace)
Requires:       go(github.com/GoogleCloudPlatform/functions-framework-go)
Requires:       go(github.com/client9/misspell)
Requires:       go(github.com/cloudevents/sdk-go/v2)
Requires:       go(github.com/fsnotify/fsnotify)
Requires:       go(github.com/go-viper/mapstructure/v2)
Requires:       go(github.com/golangci/golangci-lint/v2)
Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/googleapis/gax-go/v2)
Requires:       go(github.com/itchyny/gojq)
Requires:       go(github.com/prometheus/common)
Requires:       go(github.com/prometheus/otlptranslator)
Requires:       go(github.com/stretchr/testify)
Requires:       go(github.com/tidwall/wal)
Requires:       go(github.com/wadey/gocovmerge)
Requires:       go(go.opentelemetry.io/collector/component)
Requires:       go(go.opentelemetry.io/collector/component/componenttest)
Requires:       go(go.opentelemetry.io/collector/exporter)
Requires:       go(go.opentelemetry.io/collector/extension)
Requires:       go(go.opentelemetry.io/collector/extension/extensionauth)
Requires:       go(go.opentelemetry.io/collector/featuregate)
Requires:       go(go.opentelemetry.io/collector/pdata)
Requires:       go(go.opentelemetry.io/contrib/bridges/otelslog)
Requires:       go(go.opentelemetry.io/contrib/detectors/gcp)
Requires:       go(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(go.opentelemetry.io/otel/exporters/otlp/otlplog/otlploghttp)
Requires:       go(go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetricgrpc)
Requires:       go(go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetrichttp)
Requires:       go(go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc)
Requires:       go(go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp)
Requires:       go(go.opentelemetry.io/otel/exporters/stdout/stdoutlog)
Requires:       go(go.opentelemetry.io/otel/log)
Requires:       go(go.opentelemetry.io/otel/metric)
Requires:       go(go.opentelemetry.io/otel/sdk)
Requires:       go(go.opentelemetry.io/otel/sdk/log)
Requires:       go(go.opentelemetry.io/otel/sdk/metric)
Requires:       go(go.opentelemetry.io/otel/trace)
Requires:       go(go.uber.org/atomic)
Requires:       go(go.uber.org/zap)
Requires:       go(golang.org/x/oauth2)
Requires:       go(golang.org/x/tools)
Requires:       go(golang.org/x/vuln)
Requires:       go(gonum.org/v1/gonum)
Requires:       go(google.golang.org/api)
Requires:       go(google.golang.org/genproto)
Requires:       go(google.golang.org/genproto/googleapis/api)
Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)

# Replace the former source RPMs because this repository owns their paths.
Obsoletes:      go-github-googlecloudplatform-opentelemetry-operations-go-detectors-gcp
Obsoletes:      go-github-googlecloudplatform-opentelemetry-operations-go-exporter-metric
Obsoletes:      go-github-googlecloudplatform-opentelemetry-operations-go-internal-cloudmock
Obsoletes:      go-github-googlecloudplatform-opentelemetry-operations-go-internal-resourcemapping

%description
This package provides the complete Google Cloud OpenTelemetry integration
repository, including detectors, exporters, propagators, and test support.

%prep -a
# This directory differs from its declared module path. Normalize it before
# the standard install/check macros copy the repository into GOPATH.
mv e2e-test-server/cloud_functions e2e-test-server/cloudfunctions

%check
# Remove prep's pre-normalization copy so no stale cloud_functions package
# remains. GOPATH discovery tests the normalized tree and nested modules once.
rm -rf %{_builddir}/go/src/%{go_import_path}
%buildsystem_golangmodules_check

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
