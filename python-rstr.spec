# Created by pyp2rpm-3.3.5
%global pypi_name rstr

Name:           python-%{pypi_name}
Version:        2.1.0
Release:        1%{?dist}
Summary:        Generate random strings in Python

License:        None
URL:            http://bitbucket.org/leapfrogdevelopment/rstr/overview
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
rstr is a helper module for easily generating random strings of various types.
It could be useful for fuzz testing, generating dummy data, or other
applications. It has no dependencies outside the standard library, and should
be compatible with Python 3.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
rstr is a helper module for easily generating random strings of various types.
It could be useful for fuzz testing, generating dummy data, or other
applications. It has no dependencies outside the standard library, and should
be compatible with Python 3.


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Jan 05 2021 Frédéric Pierret (fepitre) <frederic.pierret@qubes-os.org> - 2.1.0-1
- Initial package.
