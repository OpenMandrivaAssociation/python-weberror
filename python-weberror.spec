%define tarname	WebError

Summary:	Web error handling and exception catching for Python
Name:		python-weberror
Version:	0.10.3
Release:	3
Source0:	http://pypi.python.org/packages/source/W/%{tarname}/%{tarname}-%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		http://pypi.python.org/pypi/WebError/
BuildArch:	noarch
Requires:	python-tempita
Requires:	python-webob
Requires:	python-pygments
Requires:	python-paste >= 1.7.1
BuildRequires:	python-setuptools

%description 
This package provides Python libraries for web error handling and
exception catching.

%prep
%setup -q -n %{tarname}-%{version}

%install
find . -type f -exec chmod 644 {} \;
find . -type d -exec chmod 755 {} \;
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
sed -i 's/.*egg-info$//' FILE_LIST

%files -f FILE_LIST
%doc CHANGELOG LICENSE



%changelog
* Thu Mar 31 2011 Lev Givon <lev@mandriva.org> 0.10.3-1mdv2011.0
+ Revision: 649467
- import python-weberror


