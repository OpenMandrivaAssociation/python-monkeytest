# Created by pyp2rpm-3.3.3
%bcond_without tests
%global pypi_name monkeytest
%define psnme Send2Trash 

Name:           python-%{pypi_name}
Version:        20201219
Release:        1
Summary:        A disk benchmark to test your hard drive read-write speed in Python

License:        MIT
URL:            https://github.com/thodnev/MonkeyTest
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/python-%{pypi_name}-%{version}.tar.xz
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-setuptools

%if %{with tests}
BuildRequires:  python-attrs
BuildRequires:  python-pytz
%endif

Requires:	python-gobject3

%description
A simplistic script to show that such system programming
tasks are possible and convenient to be solved in Python

%{?python_provide:%python_provide python-%{pypi_name}}

%prep
%setup -n python-%{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf python-%{pypi_name}.egg-info


%install
install -d %{buildroot}%{python3_sitelib}/monkeytest.py
# mkdir -p  %{buildroot}/%{python3_sitelib}/ 
#cp monkeytest.py %{buildroot}/%{python3_sitedir}/

%files -n python-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/*
#%%{python3_sitelib}/__pycache__/*
#%%{python3_sitelib}/%{pypi_name}.py
#%%{python3_sitelib}/%{pypi_name}
#%%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

