%global debug_package %{nil}

%define libdir /lib

Name:           darwinx-System.Common
Version:        2.0.0
Release:        1%{?dist}
Summary:        System Common libraries

Group:          Development/Languages
License:        MIT
URL:            https://github.com/dotnet
Prefix:		/usr
BuildArch:	noarch

%description
System Common libraries

%prep
%setup -c %{name}-%{version} -T
nuget install NLog -Version 5.0.1

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{darwinx_prefix}%{libdir}
find */lib/netstandard2.0/ -iname "*.dll" -exec install -m 644 {} $RPM_BUILD_ROOT%{darwinx_prefix}%{libdir}/ \;

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{darwinx_prefix}%{libdir}/*.dll

%changelog
* Thu Aug 26 2021 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.0.0
- Initial version
