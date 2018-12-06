# Run tests in check section
%bcond_without check

%global goipath         github.com/facebookgo/atomicfile
%global commit          2de1f203e7d5e386a6833233882782932729f27e

%global common_description %{expand:
Package atomicfile provides an atomically written/replaced file.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Provides an atomically written/replaced file
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license license
%doc readme.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git2de1f20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 12 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.1.20180517git2de1f20
- First package for Fedora

